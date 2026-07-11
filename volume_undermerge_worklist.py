#!/usr/bin/env python3
"""Render the B1-cascade under-merge candidates for Nibi adjudication.

Input  data/volume/identity/b1_multisame_person_candidates.jsonl —
       cross-person bio pairs where BOTH bios were judged 'same' against
       one roster record (823 pairs; several may share a pair via
       different records, grouped here).
Output data/volume/identity/undermerge_worklist.jsonl — person-vs-person
       pairs for qwen_classc_worker.py --mode merge.

Approved verdicts append to bio_persons/undermerge_decisions.jsonl
(volume_merge_undermerge.py) and take effect at the next
volume_bio_persons.py rebuild.
"""

from __future__ import annotations

import json
import random
from collections import defaultdict
from pathlib import Path

ROOT = Path("data/volume")
IDD = ROOT / "identity"
SEED = 20260711


def person_block(p: dict) -> dict:
    lines = []
    for ev in p["events"]:
        span = ev.get("text_span") or (
            (ev.get("position") or "?")
            + (f" [{ev['place']}]" if ev.get("place") else ""))
        lines.append(f"  {ev.get('year_start') or '?'}: {span}")
    eds = p["editions"]
    return {
        "name": f"{p['surname']}, {p.get('given_names')}",
        "birth_year": p.get("birth_year"),
        "honours": [f"{h['award']}{' ' + str(h['year']) if h.get('year') else ''}"
                    for h in p.get("honours", [])],
        "editions": [min(eds), max(eds)],
        "lines": lines[:40],
    }


def main() -> None:
    cands = [json.loads(l) for l in
             open(IDD / "b1_multisame_person_candidates.jsonl",
                  encoding="utf-8")]
    by_pair: dict[tuple, list[str]] = defaultdict(list)
    for c in cands:
        by_pair[(c["person_a"], c["person_b"])].append(c["record_id"])

    persons = {}
    need = {p for pair in by_pair for p in pair}
    for line in open(ROOT / "bio_persons/bio_persons.jsonl",
                     encoding="utf-8"):
        p = json.loads(line)
        if p["person_id"] in need:
            persons[p["person_id"]] = p

    # shared roster rows as printed evidence
    rec_need = defaultdict(set)
    for pair, recs in by_pair.items():
        for r in recs:
            rec_need[int(r.split("-")[0][3:])].add(r)
    rec_txt = {}
    for year, ids in sorted(rec_need.items()):
        for line in open(ROOT / f"col{year}" / "records.jsonl",
                         encoding="utf-8"):
            r = json.loads(line)
            if r["record_id"] in ids:
                t = (f"  {year} {r.get('colony')} | "
                     f"{r.get('surname')}, {r.get('given_names')} | "
                     f"{r.get('position') or '?'}")
                if r.get("department"):
                    t += f" | dept: {r['department']}"
                rec_txt[r["record_id"]] = t

    rows, missing = [], 0
    for (pa, pb), recs in sorted(by_pair.items()):
        a, b = persons.get(pa), persons.get(pb)
        if not a or not b:
            missing += 1
            continue
        rows.append({
            "id": f"um::{pa}::{pb}",
            "career_id": pa, "person_id": pb, "cand_rank": 0,
            "a": person_block(a), "b": person_block(b),
            "shared_records": [rec_txt.get(r, f"  {r}")
                               for r in sorted(set(recs))],
        })
    random.Random(SEED).shuffle(rows)
    with open(IDD / "undermerge_worklist.jsonl", "w",
              encoding="utf-8") as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"pairs: {len(rows)} (missing persons: {missing})")


if __name__ == "__main__":
    main()
