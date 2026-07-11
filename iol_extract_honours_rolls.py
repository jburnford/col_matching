#!/usr/bin/env python3
"""Extract the Indian-order honours rolls (Star of India, Indian Empire,
Crown of India) across all IOL editions — the external award-date anchor
for the A1/A6 identity screens (docs/IOL_VS_COL.md; only 56% of bio honour
mentions carry a year, the rolls print exact appointment dates from ~1890).

Writes data/iol/honours_rolls/rolls_<tag>.jsonl per edition and a coverage
report ROLLS_EXTRACTION.md.

  python3 iol_extract_honours_rolls.py
"""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

from col_match.volume import iol_honours_rolls, iol_reader

OUT = Path("data/iol/honours_rolls")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    editions, _ = iol_reader.available_editions()

    rows = []
    for ek in editions:
        recs = iol_honours_rolls.extract_rolls(ek)
        path = OUT / f"rolls_{ek.tag}.jsonl"
        with open(path, "w", encoding="utf-8") as fh:
            for r in recs:
                fh.write(json.dumps(r.to_json(), ensure_ascii=False) + "\n")
        grades = Counter(r.grade for r in recs)
        dated = sum(1 for r in recs if r.appt_year)
        rows.append({"edition": ek.dirpath.name, "tag": ek.tag,
                     "year": ek.year, "entries": len(recs),
                     "dated_pct": round(100 * dated / len(recs), 1)
                     if recs else 0,
                     "grades": dict(sorted(grades.items()))})
        if recs:
            print(f"{ek.dirpath.name}: {len(recs):5d} entries "
                  f"({dated / len(recs):.0%} dated)")

    total = sum(r["entries"] for r in rows)
    nonzero = [r for r in rows if r["entries"]]
    lines = [
        "# IOL honours-roll extraction (Star of India / Indian Empire / "
        "Crown of India)",
        "",
        f"{len(nonzero)} editions with rolls, **{total:,} entries** "
        "(col_match/volume/iol_honours_rolls.py).",
        "",
        "| edition | entries | dated% | grades |",
        "|---|---|---|---|",
    ]
    for r in nonzero:
        g = ", ".join(f"{k}:{v}" for k, v in r["grades"].items())
        lines.append(f"| {r['edition']} | {r['entries']:,} "
                     f"| {r['dated_pct']} | {g} |")
    lines += [
        "",
        "Known limits: pre-1890 rolls are largely undated (dates begin",
        "~1880s); the 1930s Crown of India roll prints as a table and is",
        "missed; Kaisar-i-Hind / O.B.I. / I.O.M. and the C.M.G./R.V.O.",
        "Indian-services lists reset the parser and await their own layer.",
    ]
    (OUT / "ROLLS_EXTRACTION.md").write_text("\n".join(lines) + "\n",
                                             encoding="utf-8")
    print(f"\n{total:,} roll entries -> {OUT}/")


if __name__ == "__main__":
    main()
