#!/usr/bin/env python3
"""In-session LLM-parse harness for the within-volume pilot.

The rules tier drops a whole entry on any single year-bearing clause it cannot
account for, so ~1/3 of bios reach the matcher with zero events. This harness
lets a strong LLM (Opus in-session now; local Qwen on the GPU box later) fill
those in, then re-runs the matcher to measure the link lift.

Workflow (resumable — both the Opus and Qwen tiers append to the same file):
  1. python3 volume_llm_parse.py --year 1921 --dump 40 --seed 0
        → prints bio_id + raw_text for unparsed bios NOT yet in the parse file.
  2. (the LLM emits one JSON object per bio and they are written to
        data/volume/col1921/llm_parsed.jsonl — schema below.)
  3. python3 volume_llm_parse.py --year 1921 --rematch
        → overlays the LLM parses onto bios.jsonl, re-runs link_volume, reports
          the new link rate and how many LLM-parsed bios newly linked.

LLM parse object (one per line):
  {"bio_id": str, "given_names": str|null, "birth_year": int|null,
   "honours": [{"award": str, "year": int|null}],
   "events": [{"position": str|null, "place": str|null,
               "year_start": int|null, "year_end": int|null}]}
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from col_match.config import Config
from col_match.volume import match as match_mod
from col_match.volume import status as status_mod
from col_match.volume.bios import VolumeBio


def _load_jsonl(path: Path) -> list[dict]:
    return [json.loads(l) for l in path.open(encoding="utf-8")] if path.exists() else []


def _parsed_ids(parse_path: Path) -> set[str]:
    return {r["bio_id"] for r in _load_jsonl(parse_path)}


def cmd_dump(out: Path, n: int, seed: int) -> None:
    import random
    unparsed = _load_jsonl(out / "bios_unparsed.jsonl")
    done = _parsed_ids(out / "llm_parsed.jsonl")
    todo = [b for b in unparsed if b["bio_id"] not in done]
    random.Random(seed).shuffle(todo)
    batch = todo[:n]
    print(f"# {len(todo)} unparsed bios remain ({len(done)} already parsed); dumping {len(batch)}")
    for b in batch:
        print(json.dumps({"bio_id": b["bio_id"], "raw_text": b["raw_text"]}, ensure_ascii=False))


def _overlay(bios: list[dict], parses: list[dict]) -> list[VolumeBio]:
    by_id = {p["bio_id"]: p for p in parses}
    out: list[VolumeBio] = []
    for b in bios:
        p = by_id.get(b["bio_id"])
        if p is not None:
            b = dict(b)
            b["given_names"] = p.get("given_names", b.get("given_names"))
            b["birth_year"] = p.get("birth_year", b.get("birth_year"))
            b["honours"] = p.get("honours", b.get("honours")) or []
            b["events"] = p.get("events", []) or []
            b["parser"] = "llm"
        out.append(VolumeBio(**{k: b.get(k) for k in VolumeBio.__dataclass_fields__}))
    return out


def cmd_rematch(out: Path, cfg: Config, year: int) -> None:
    bios_raw = _load_jsonl(out / "bios.jsonl")
    parses = _load_jsonl(out / "llm_parsed.jsonl")
    records = [_rec(r) for r in _load_jsonl(out / "records.jsonl")]
    bios = _overlay(bios_raw, parses)

    links, stats = match_mod.link_volume(bios, records, cfg.data_dir)
    linked_ids = {l.bio_id for l in links}
    llm_ids = {p["bio_id"] for p in parses}
    llm_linked = len(llm_ids & linked_ids)

    # denominator refinement via status
    active = sum(1 for b in bios
                 if status_mod.classify_status(b.raw_text, b.events, year)["expect_record"])

    base_links = len(_load_jsonl(out / "links.jsonl"))
    print(f"=== re-match {out.name} (LLM overlay: {len(parses)} bios) ===")
    print(f"links: {base_links} (deterministic) -> {stats['links']} (+{stats['links']-base_links})")
    print(f"bios linked: {stats['bios_linked']}  | by strength {stats['by_strength']}")
    print(f"LLM-parsed bios: {len(llm_ids)}  newly contributing links: {llm_linked} "
          f"({llm_linked/len(llm_ids)*100:.1f}% link rate)" if llm_ids else "no LLM parses yet")
    print(f"active (record-expected) bios: {active}  -> link rate among active: "
          f"{stats['bios_linked']/active*100:.1f}%")
    # persist the improved links for inspection
    with (out / "links_llm.jsonl").open("w", encoding="utf-8") as fh:
        for l in links:
            fh.write(json.dumps(l.to_json(), ensure_ascii=False) + "\n")


def _rec(r: dict):
    from col_match.volume.roster import VolumeRecord
    return VolumeRecord(**{k: r.get(k) for k in VolumeRecord.__dataclass_fields__})


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--year", type=int, required=True)
    ap.add_argument("--doc", default="col")
    ap.add_argument("--dump", type=int)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--rematch", action="store_true")
    ap.add_argument("--root", default="data/volume")
    args = ap.parse_args()
    out = Path(args.root) / f"{args.doc}{args.year}"
    cfg = Config.from_env()
    if args.dump:
        cmd_dump(out, args.dump, args.seed)
    elif args.rematch:
        cmd_rematch(out, cfg, args.year)
    else:
        ap.error("give --dump N or --rematch")


if __name__ == "__main__":
    main()
