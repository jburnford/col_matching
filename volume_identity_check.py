#!/usr/bin/env python3
"""D2: identity invariants, fail-loud (IDENTITY_QA_ROADMAP).

Run at the end of every pipeline chain (after volume_kg). The chain has
enough moving parts that silent regressions are the main risk; this pins
every identity-layer invariant to a measured baseline and exits nonzero
the moment one degrades.

  python3 volume_identity_check.py            # check, exit 1 on regression

Invariants (baseline = state measured 2026-07-11):

  partition          every bio in exactly one person; map == members    0
  same_ed_primary    same-edition multi-primary persons all flagged     0
  classc_refs        career/person refs in the class-C overlay resolve  0
  career_bio_refs    careers' bio_ids resolve in the bio-person map     0
  contested_records  roster records claimed by >1 bio (error queue!)    2907
  honour_precedence  A1 screen: order grades that descend               13
  age_invariants     A2 screen: entry age / service-length violations   661

Baselines are ceilings, not targets — drive them down by adjudication, then
lower the constant here in the same commit.
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

from volume_identity_screens import (screen_a1, screen_a2_birth_from_honour,
                                     screen_a2_invariants)

ROOT = Path("data/volume")

BASELINES = {
    "partition_dup_map": 0,
    "partition_multi_person": 0,
    "partition_map_member_diff": 0,
    "same_ed_primary_unflagged": 0,
    "classc_bad_refs": 0,
    "career_bad_bio_refs": 0,
    # lowered 2026-07-11 after the B1 apply (11,248 refuted links dropped,
    # 14 under-merges folded in); remaining contested records are the
    # keep-keep duplicates (dupprint bios of one person claiming one row)
    "contested_records": 1412,
    "honour_precedence": 13,
    # 661 -> 323 after the birth-year override ledger (2026-07-11):
    # remainder = 268 ambiguous digit repairs + dynastic candidates
    "age_invariants": 323,
    "birth_from_honour": 0,
    "nonword_surname_careers": 302,
    "multiname_given_careers": 1869,
}

_NONWORD = re.compile(
    r"^(the|and|of|for|to|in|on|by|at|per|ditto|do|vacant|office|department"
    r"|board|total|salary|allowance)$", re.I)


def jload(path: Path):
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            yield json.loads(line)


def main() -> None:
    measured: dict[str, int] = {}

    persons = [p for p in jload(ROOT / "bio_persons/bio_persons.jsonl")]
    live = [p for p in persons if "not_a_person" not in p["flags"]]

    # partition totality
    map_ids = Counter(r["bio_id"]
                      for r in jload(ROOT / "bio_persons/bio_person_map.jsonl"))
    memb = Counter(b for p in persons for b in p["members"])
    measured["partition_dup_map"] = sum(1 for c in map_ids.values() if c > 1)
    measured["partition_multi_person"] = sum(1 for c in memb.values() if c > 1)
    measured["partition_map_member_diff"] = len(set(map_ids) ^ set(memb))

    # same-edition multi-primary must carry the namesake flag
    bad = 0
    for p in live:
        ed = Counter(b.split("-")[0] for b, role in p["members"].items()
                     if role == "primary")
        if any(c > 1 for c in ed.values()) \
                and "namesake_same_edition" not in p["flags"]:
            bad += 1
    measured["same_ed_primary_unflagged"] = bad

    # overlay referential integrity
    careers = list(jload(ROOT / "careers/careers.jsonl"))
    career_ids = {c["career_id"] for c in careers}
    person_ids = {p["person_id"] for p in persons}
    measured["classc_bad_refs"] = sum(
        1 for r in jload(ROOT / "classc/career_person_links.jsonl")
        if r["career_id"] not in career_ids or r["person_id"] not in person_ids)
    measured["career_bad_bio_refs"] = sum(
        1 for c in careers for b in c.get("bio_ids", []) if b not in map_ids)

    # link bijectivity: a roster record claimed by >1 bio is a contest at
    # most one side can win — the standing error queue
    contested = 0
    for d in sorted(ROOT.glob("col*")):
        f = d / "links.jsonl"
        if not f.exists():
            continue
        c = Counter(ln["record_id"] for ln in jload(f))
        contested += sum(1 for v in c.values() if v > 1)
    measured["contested_records"] = contested

    # Tier-A screens as regression counters
    measured["honour_precedence"] = len(screen_a1(live))
    measured["age_invariants"] = len(screen_a2_invariants(live))
    measured["birth_from_honour"] = len(screen_a2_birth_from_honour(live))

    # roster-parser leakage into careers (spot-check finds, 2026-07-11):
    # 'ditto'-style surnames and un-split "A and B" multi-person rows
    measured["nonword_surname_careers"] = sum(
        1 for c in careers if not c.get("suspect")
        and _NONWORD.match(c.get("surname") or ""))
    measured["multiname_given_careers"] = sum(
        1 for c in careers if not c.get("suspect")
        and re.search(r"\band\b", c.get("given_names") or ""))

    failed = []
    print(f"{'invariant':28} {'measured':>9} {'baseline':>9}")
    for key, base in BASELINES.items():
        got = measured[key]
        mark = "ok" if got <= base else "FAIL"
        if got > base:
            failed.append(key)
        print(f"{key:28} {got:9,} {base:9,}  {mark}")
        if got < base:
            print(f"{'':28} improved — lower the baseline to {got:,}")

    if failed:
        print(f"\nFAILED: {', '.join(failed)} regressed past baseline")
        sys.exit(1)
    print("\nall identity invariants hold")


if __name__ == "__main__":
    main()
