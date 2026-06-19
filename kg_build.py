#!/usr/bin/env python3
"""Driver for the biography knowledge-graph pipeline (col_match/kg).

Stages (run in order; each writes under data/kg/):
  persons   : extract bios across all editions, cluster to distinct persons,
              select the richest pre-1940 canonical entry. -> persons.jsonl
  dump      : print canonical entries for the in-session LLM to structure
              (--n, --seed). The LLM writes objects to llm_struct.jsonl.
  validate  : review llm_struct.jsonl against source text -> struct_valid.jsonl
  ground    : ground distinct event places to Wikidata QIDs via the MCP
              (this command only PREPARES the worklist; grounding runs in-session
              through the MCP, see col_match/kg/ground.py). -> places_grounding.jsonl
  colony    : resolve grounded places to historical colony QIDs (empire KG)
  emit      : assemble the KG node/edge JSONL tables

Examples:
  python3 kg_build.py persons
  python3 kg_build.py dump --n 30 --seed 0
  python3 kg_build.py validate
  python3 kg_build.py emit
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from col_match.config import Config
from col_match.kg import persons as P

OUT = Path("data/kg")


def _dump_jsonl(path: Path, rows) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        for r in rows:
            fh.write(json.dumps(r.to_json() if hasattr(r, "to_json") else r, ensure_ascii=False) + "\n")


def cmd_persons(args, cfg) -> None:
    bios = P.load_all_bios(tuple(args.docs.split(",")), cfg.data_dir, refresh=args.refresh)
    people = P.build_persons(bios)
    _dump_jsonl(OUT / "persons.jsonl", people)
    multi = sum(1 for p in people if len(p.attestations) > 1)
    print(f"raw bios {len(bios)} -> persons {len(people)} ({multi} multi-edition); "
          f"wrote {OUT/'persons.jsonl'}")


def cmd_dump(args, cfg) -> None:
    from col_match.kg.extract import dump_batch
    dump_batch(OUT / "persons.jsonl", OUT, args.n, args.seed)


def cmd_validate(args, cfg) -> None:
    from col_match.kg.validate import validate_struct
    sdir = OUT / "struct_in"
    structs = [json.loads(l) for f in sorted(sdir.glob("*.jsonl"))
               for l in f.open(encoding="utf-8")]
    bios = {b["bio_id"]: b for f in Path("data/kg/bios").glob("*.jsonl")
            for b in (json.loads(l) for l in f.open(encoding="utf-8"))}
    pid2canon = {p["person_id"]: p["canonical_bio_id"]
                 for p in (json.loads(l) for l in (OUT / "persons.jsonl").open(encoding="utf-8"))}
    out = []
    n_flags = 0
    for s in structs:
        src = bios[pid2canon[s["person_id"]]]["raw_text"]
        v = validate_struct(s, src)
        n_flags += len(v.get("flags", []))
        out.append(v)
    with (OUT / "struct_valid.jsonl").open("w", encoding="utf-8") as fh:
        for v in out:
            fh.write(json.dumps(v, ensure_ascii=False) + "\n")
    print(f"validated {len(out)} structs; {n_flags} facts dropped/flagged -> {OUT/'struct_valid.jsonl'}")


def cmd_ground(args, cfg) -> None:
    """Print the place-grounding worklist (the MCP loop is agent-driven)."""
    from col_match.kg.ground import distinct_places, query_for
    wl = distinct_places(OUT / "struct_valid.jsonl")
    print(f"# {len(wl)} distinct ungrounded places")
    for place, n in wl:
        print(json.dumps({"place": place, "count": n, "query": query_for(place)}, ensure_ascii=False))


def cmd_emit(args, cfg) -> None:
    from col_match.kg.emit import build_kg
    stats = build_kg(OUT)
    print("KG tables written to data/kg/graph/:")
    print(json.dumps(stats, indent=2))


def main() -> None:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("persons"); p.add_argument("--docs", default="col,dol")
    p.add_argument("--refresh", action="store_true")
    d = sub.add_parser("dump"); d.add_argument("--n", type=int, default=30); d.add_argument("--seed", type=int, default=0)
    sub.add_parser("validate")
    sub.add_parser("ground")
    sub.add_parser("emit")
    args = ap.parse_args()
    cfg = Config.from_env()
    {"persons": cmd_persons, "dump": cmd_dump, "validate": cmd_validate,
     "ground": cmd_ground, "emit": cmd_emit}[args.cmd](args, cfg)


if __name__ == "__main__":
    main()
