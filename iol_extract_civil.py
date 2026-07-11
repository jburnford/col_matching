#!/usr/bin/env python3
"""Extract the IOL civil lists (establishment rosters) across all annual
editions, 1896-1947 — the first tranche of the wider IOL knowledge graph
(docs/IOL_VS_COL.md §2; the office—holder grammar only).

Writes data/iol/civil/civil_<tag>.jsonl (one file per edition) and a
coverage report data/iol/civil/CIVIL_EXTRACTION.md. Pre-1896 semiannual
volumes (iacsl/il main volumes) use an untested earlier layout and are
skipped; the gradation lists, honours rolls and context lists are separate
layers.

  python3 iol_extract_civil.py [--from-year 1896]
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

from col_match.volume import iol_civil, iol_reader

OUT = Path("data/iol/civil")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--from-year", type=int, default=1896)
    args = ap.parse_args()

    OUT.mkdir(parents=True, exist_ok=True)
    editions, _ = iol_reader.available_editions()
    editions = [e for e in editions if e.year >= args.from_year]

    rows = []
    for ek in editions:
        recs = iol_civil.extract_civil(ek)
        path = OUT / f"civil_{ek.tag}.jsonl"
        with open(path, "w", encoding="utf-8") as fh:
            for r in recs:
                fh.write(json.dumps(r.to_json(), ensure_ascii=False) + "\n")
        govs = Counter(r.government for r in recs)
        hon = sum(1 for r in recs if r.honours)
        svc = sum(1 for r in recs if r.service)
        act = sum(1 for r in recs if r.acting)
        rows.append({"edition": ek.dirpath.name, "tag": ek.tag,
                     "year": ek.year, "records": len(recs),
                     "governments": len(govs),
                     "pct_honours": round(100 * hon / len(recs), 1) if recs else 0,
                     "pct_service": round(100 * svc / len(recs), 1) if recs else 0,
                     "pct_acting": round(100 * act / len(recs), 1) if recs else 0})
        print(f"{ek.dirpath.name}: {len(recs):5d} records, "
              f"{len(govs):2d} governments")

    total = sum(r["records"] for r in rows)
    lines = [
        "# IOL civil-list extraction (office—holder rosters, 1896-1947)",
        "",
        f"{len(rows)} editions, **{total:,} records** "
        f"(col_match/volume/iol_civil.py).",
        "",
        "| edition | records | governments | honours% | service% | acting% |",
        "|---|---|---|---|---|---|",
    ]
    for r in rows:
        lines.append(f"| {r['edition']} | {r['records']:,} "
                     f"| {r['governments']} | {r['pct_honours']} "
                     f"| {r['pct_service']} | {r['pct_acting']} |")
    lines += [
        "",
        "Record schema: government / department / branch / office / name /",
        "honours / service / prefix / acting / flags (tenure dates, suffixes)",
        "/ raw_line / char_offset / page_est.",
        "",
        "Known limits: bare-province sub-groupings inside all-India service",
        "lists can inherit a stale government label; gradation and",
        "commission NAME LISTS are not parsed (separate layer); pre-1896",
        "semiannual volumes skipped.",
    ]
    (OUT / "CIVIL_EXTRACTION.md").write_text("\n".join(lines) + "\n",
                                             encoding="utf-8")
    print(f"\n{total:,} records across {len(rows)} editions -> {OUT}/")


if __name__ == "__main__":
    main()
