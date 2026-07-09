#!/usr/bin/env python3
"""Extract the front-matter "COLONIAL GOVERNORS, &c." snapshot tables.

Unlike the per-colony succession lists (volume_governors.py), these are
ANNUAL PANELS: one row per colony per edition with the sitting governor,
office, commission + assumption dates, residence, and SALARY — 65 tables
across 36 editions (1877-1948). Region rows ("NORTH AMERICAN.") and ditto
marks ('' = same office as previous row) are handled.

Output: data/volume/context/governor_panel.jsonl
  {edition, region, colony_raw, office, name_raw, given, surname, honours,
   commission, assumed, residence, salary}
"""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

from col_match.volume import reader
from volume_governors import _parse_person

ROOT = Path("data/volume")
OUT = ROOT / "context"

_ROW = re.compile(r"<tr[^>]*>(.*?)</tr>", re.S)
_CELL = re.compile(r"<t[dh][^>]*>(.*?)</t[dh]>", re.S)
_TAG = re.compile(r"<[^>]+>")
_YEAR = re.compile(r"(1[89]\d\d)")
_SNAP = re.compile(r"COLONIAL GOVERNORS|DOMINION GOVERNORS", re.I)


def _clean(s: str) -> str:
    return re.sub(r"\s+", " ", _TAG.sub(" ", s)).strip(" .·…")


def parse_panel(html: str, edition: int) -> list[dict]:
    out = []
    region = None
    prev_office = None
    for row in _ROW.findall(html):
        cells = [_clean(c) for c in _CELL.findall(row)]
        if not cells or cells[0].lower().startswith("colonies"):
            continue
        filled = [c for c in cells[1:] if c and c not in ("''", '"', ",,")]
        if cells[0] and not filled:                 # region / group row
            region = cells[0].strip("—- ")
            continue
        if len(cells) < 3 or not cells[0]:
            continue
        colony = cells[0]
        office = cells[1] if len(cells) > 1 else None
        if office in ("''", '"', ",,", ""):
            office = prev_office
        else:
            prev_office = office
        name_raw = cells[2] if len(cells) > 2 else ""
        name_raw = re.sub(r"^His (?:Excellency|Honour)\s+", "", name_raw).strip()
        person = _parse_person(name_raw)
        if person is None or not name_raw:
            continue
        _, given, surname, honours = person
        commission = cells[3] if len(cells) > 3 else None
        assumed = cells[4] if len(cells) > 4 else None
        residence = cells[5] if len(cells) > 5 else None
        salary = cells[6] if len(cells) > 6 else None
        cy = _YEAR.search(commission or "")
        out.append({
            "edition": edition, "region": region, "colony_raw": colony,
            "office": office, "name_raw": name_raw, "given": given,
            "surname": surname, "honours": honours,
            "commission": commission or None,
            "commission_year": int(cy.group(1)) if cy else None,
            "assumed": assumed or None, "residence": residence or None,
            "salary": salary or None,
        })
    return out


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    locs = defaultdict(list)
    for line in open(ROOT / "block_index.jsonl", encoding="utf-8"):
        r = json.loads(line)
        if r["section"] == "governors_list" and r["category"] == "table" \
                and _SNAP.search(r["title"]):
            locs[r["year"]].append(r)

    rows = []
    for year in sorted(locs):
        bmap = {(b.page, b.index): b for b in reader.load_volume(year, "col")}
        for r in locs[year]:
            b = bmap.get((r["page"], r["block"]))
            if b is not None:
                rows.extend(parse_panel(b.text, year))

    with (OUT / "governor_panel.jsonl").open("w", encoding="utf-8") as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")

    eds = Counter(r["edition"] for r in rows)
    with_sal = sum(1 for r in rows if r["salary"] and any(ch.isdigit()
                                                          for ch in r["salary"]))
    print(f"governor panel: {len(rows):,} rows across {len(eds)} editions; "
          f"{with_sal:,} with salary; median rows/edition "
          f"{sorted(eds.values())[len(eds)//2]}")
    print("sample:", json.dumps(rows[len(rows)//2], ensure_ascii=False)[:220])


if __name__ == "__main__":
    main()
