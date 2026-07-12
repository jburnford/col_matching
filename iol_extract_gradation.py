#!/usr/bin/env python3
"""Extract the gradation lists (civil-service and army seniority rosters)
across all IOL editions (col_match/volume/iol_gradation.py).

Each entry = (person, grade/class, seniority year, corps or current
appointment) — two attestations per year back to 1861, twenty-five years
before the biographical record begins.

Writes data/iol/gradation/gradation_<tag>.jsonl + GRADATION_EXTRACTION.md.
"""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

from col_match.volume import iol_gradation, iol_reader

OUT = Path("data/iol/gradation")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    editions, _ = iol_reader.available_editions()

    rows = []
    for ek in editions:
        recs = iol_gradation.extract_gradation(ek)
        with open(OUT / f"gradation_{ek.tag}.jsonl", "w",
                  encoding="utf-8") as fh:
            for r in recs:
                fh.write(json.dumps(r.to_json(), ensure_ascii=False) + "\n")
        c = Counter(r.list_type for r in recs)
        rows.append({"edition": ek.dirpath.name, "tag": ek.tag,
                     "records": len(recs), "civil": c.get("civil", 0),
                     "army": c.get("army", 0)})
        if recs:
            print(f"{ek.dirpath.name}: {len(recs):5d} "
                  f"(civil {c.get('civil', 0)}, army {c.get('army', 0)})")

    total = sum(r["records"] for r in rows)
    nonzero = [r for r in rows if r["records"]]
    lines = [
        "# IOL gradation-list extraction (seniority rosters)",
        "",
        f"{len(nonzero)} editions, **{total:,} entries**.",
        "",
        "| edition | entries | civil | army |",
        "|---|---|---|---|",
    ]
    for r in nonzero:
        lines.append(f"| {r['edition']} | {r['records']:,} | {r['civil']:,} "
                     f"| {r['army']:,} |")
    lines += [
        "",
        "Civil schema: establishment / class / entry (covenant) year /",
        "surname / given / honours / current appointment / on_furlough.",
        "Army schema: rank / promotion year+day / first-commission year /",
        "surname / initials / honours / corps code.",
        "Known limits: some 1860s two-column army tables are partially",
        "captured; year-group headers inside table cells can be missed",
        "(group_year null); marker glyphs (* † ‡ = Bath grades in early",
        "volumes) are stripped, not decoded.",
    ]
    (OUT / "GRADATION_EXTRACTION.md").write_text("\n".join(lines) + "\n",
                                                 encoding="utf-8")
    print(f"\n{total:,} entries -> {OUT}/")


if __name__ == "__main__":
    main()
