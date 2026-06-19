#!/usr/bin/env python3
"""Within-volume bio↔roster linking driver for the new (Infinity-2) OCR.

  python3 volume_link.py --year 1921
  python3 volume_link.py --year 1888 --doc col
  python3 volume_link.py --years 1888,1921,1960

Reads one edition's result.json, extracts bbox-grounded services-section
biographies and by-colony roster records, links them within the volume, and
writes JSONL + a markdown report under data/volume/<doc><year>/.

Deterministic end-to-end (no network/LLM). The Qwen LLM tier (GPU box, tomorrow)
re-parses the entries/blocks flagged here — see col_match/volume/llm.py and the
worklists this writes (bios_unparsed.jsonl, roster_blocks.jsonl).
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from col_match.config import Config
from col_match.volume import bios as bios_mod
from col_match.volume import match as match_mod
from col_match.volume import reader, roster


def _dump(path: Path, rows) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        for r in rows:
            fh.write(json.dumps(r.to_json() if hasattr(r, "to_json") else r, ensure_ascii=False) + "\n")


def run_year(year: int, doc: str, cfg: Config, out_root: Path) -> dict:
    blocks = reader.load_volume(year, doc)
    bios, bstats = bios_mod.extract_bios(blocks, cfg.data_dir)
    sec = bios_mod.find_services_section(blocks)
    records, rstats = roster.extract_records(blocks, stop_at=sec[0] if sec else None)
    links, mstats = match_mod.link_volume(bios, records, cfg.data_dir)

    out = out_root / f"{doc}{year}"
    _dump(out / "bios.jsonl", bios)
    _dump(out / "records.jsonl", records)
    _dump(out / "links.jsonl", links)
    # Qwen worklists for tomorrow (GPU box)
    _dump(out / "bios_unparsed.jsonl", [b for b in bios if b.parser == "unparsed"])
    _dump(out / "roster_blocks.jsonl",
          roster.collect_roster_blocks(blocks, stop_at=sec[0] if sec else None))

    link_rate = mstats["bios_linked"] / bstats["n_bios"] if bstats["n_bios"] else 0.0
    summary = {
        "year": year, "doc": doc, "pages": max((b.page for b in blocks), default=-1) + 1,
        "bios": bstats, "roster": rstats, "match": mstats,
        "bio_link_rate": round(link_rate, 4),
    }
    _write_report(out / "report.md", summary, links, records)
    (out / "summary.json").write_text(json.dumps(summary, indent=2, default=int))
    return summary


def _write_report(path: Path, s: dict, links, records) -> None:
    m, b, r = s["match"], s["bios"], s["roster"]
    lines = [
        f"# Within-volume linking — {s['doc']}{s['year']}",
        "",
        f"- pages: {s['pages']}",
        f"- **bios**: {b['n_bios']} ({b['rules_ok']} rules-parsed, {b['unparsed']} unparsed→Qwen)",
        f"- **roster records**: {r['n_records']} across {r['colonies']} colonies "
        f"({r['roster_blocks']} roster blocks)",
        f"- **links**: {m['links']}  |  bios linked: {m['bios_linked']} "
        f"(**{s['bio_link_rate']*100:.1f}%** of bios)",
        f"- ambiguous dropped: {m['ambiguous_dropped']}",
        f"- by strength: {m['by_strength']}",
        f"- by surname match: {m['by_surname_match']}",
        "",
        "## Sample links (verify against raw OCR bbox)",
        "",
    ]
    for ln in links[:30]:
        lines.append(
            f"- **{ln.bio_surname}, {ln.bio_given or ''}** → *{ln.colony}* "
            f"[{ln.strength}, pos~{ln.position_sim}] "
            f"rec: {ln.rec_given or ''} {ln.rec_surname} ({ln.rec_position or '?'}) "
            f"| bio p{ln.bio_prov.get('page')} · rec p{ln.rec_prov.get('page')}"
        )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--year", type=int)
    ap.add_argument("--years", help="comma-separated list")
    ap.add_argument("--doc", default="col", choices=["col", "dol", "cro"])
    ap.add_argument("--out", default="data/volume")
    args = ap.parse_args()

    cfg = Config.from_env()
    out_root = Path(args.out)
    years = ([int(y) for y in args.years.split(",")] if args.years
             else [args.year] if args.year else [])
    if not years:
        ap.error("give --year or --years")
    for y in years:
        s = run_year(y, args.doc, cfg, out_root)
        m = s["match"]
        print(f"{args.doc}{y}: bios {s['bios']['n_bios']} | records {s['roster']['n_records']} "
              f"| links {m['links']} | bios linked {m['bios_linked']} "
              f"({s['bio_link_rate']*100:.1f}%) | ambig {m['ambiguous_dropped']}")


if __name__ == "__main__":
    main()
