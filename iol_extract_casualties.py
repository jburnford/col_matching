#!/usr/bin/env python3
"""Extract the casualties lists (deaths / resignations / retirements /
dismissals with exact dates) across all IOL editions — the person-EXIT
event layer (docs/IOL_VS_COL.md; col_match/volume/iol_casualties.py).

Semiannual volumes 1861-1895 print six-month change-lists per
establishment; the late annuals print year-end RETIREMENTS + DEATHS
tables in the back matter. Death dates are the strongest over-merge
screen there is: any event after death = two persons fused.

Writes data/iol/casualties/casualties_<tag>.jsonl + CASUALTIES_EXTRACTION.md.
"""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

from col_match.volume import iol_casualties, iol_reader

OUT = Path("data/iol/casualties")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    editions, _ = iol_reader.available_editions()

    rows = []
    for ek in editions:
        recs = iol_casualties.extract_casualties(ek)
        with open(OUT / f"casualties_{ek.tag}.jsonl", "w",
                  encoding="utf-8") as fh:
            for r in recs:
                fh.write(json.dumps(r.to_json(), ensure_ascii=False) + "\n")
        ev = Counter(r.event for r in recs)
        rows.append({"edition": ek.dirpath.name, "tag": ek.tag,
                     "year": ek.year, "records": len(recs),
                     "events": dict(sorted(ev.items()))})
        if recs:
            print(f"{ek.dirpath.name}: {len(recs):4d} "
                  f"({', '.join(f'{k}:{v}' for k, v in sorted(ev.items()))})")

    total = sum(r["records"] for r in rows)
    deaths = sum(r["events"].get("death", 0) for r in rows)
    nonzero = [r for r in rows if r["records"]]
    lines = [
        "# IOL casualties extraction (exit events with exact dates)",
        "",
        f"{len(nonzero)} editions with lists, **{total:,} records** "
        f"(**{deaths:,} deaths**).",
        "",
        "| edition | records | events |",
        "|---|---|---|",
    ]
    for r in nonzero:
        e = ", ".join(f"{k}:{v}" for k, v in r["events"].items())
        lines.append(f"| {r['edition']} | {r['records']:,} | {e} |")
    lines += [
        "",
        "Schema: presidency / establishment (or service, in the late",
        "tables) / event / name / day / month / year / place / note / raw.",
        "Corps prefixes flow into names in some military lists (split",
        "downstream); ditto years in the late tables are inherited.",
    ]
    (OUT / "CASUALTIES_EXTRACTION.md").write_text("\n".join(lines) + "\n",
                                                  encoding="utf-8")
    print(f"\n{total:,} records ({deaths:,} deaths) -> {OUT}/")


if __name__ == "__main__":
    main()
