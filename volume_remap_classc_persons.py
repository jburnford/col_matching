#!/usr/bin/env python3
"""Remap class-C career->person links after a bio-persons rebuild.

volume_bio_persons.py absorbs under-merged person ids (survivor keeps the
id; person_id_merges.jsonl records absorbed_id -> person_id). The class-C
overlay (classc/career_person_links.jsonl) references person ids from
link time; any link pointing at an absorbed id is retargeted to the
survivor here. Idempotent; duplicate (career, person) rows after
retargeting collapse to one. Run volume_identity_check.py after — its
classc_bad_refs invariant proves the overlay resolves again.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path("data/volume")
LINKS = ROOT / "classc/career_person_links.jsonl"


def main() -> None:
    remap = {}
    for r in map(json.loads, open(ROOT / "bio_persons/person_id_merges.jsonl",
                                  encoding="utf-8")):
        remap[r["absorbed_id"]] = r["person_id"]
    # chase chains (absorbed id whose survivor was itself absorbed later)
    for k in list(remap):
        v = remap[k]
        while v in remap:
            v = remap[v]
        remap[k] = v

    rows, seen, hit = [], set(), 0
    for r in map(json.loads, open(LINKS, encoding="utf-8")):
        if r["person_id"] in remap:
            r["person_id"] = remap[r["person_id"]]
            hit += 1
        key = (r["career_id"], r["person_id"])
        if key in seen:
            continue
        seen.add(key)
        rows.append(r)
    with open(LINKS, "w", encoding="utf-8") as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"retargeted {hit} links; {len(rows)} rows kept (dedup applied)")


if __name__ == "__main__":
    main()
