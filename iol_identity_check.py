#!/usr/bin/env python3
"""IOL identity invariants, fail-loud (volume_identity_check.py pattern).

Run after any change to the IOL person layers (dedup maps, structured
corpus, graph_stage3 rebuild). Pins every identity-layer invariant to a
baseline measured 2026-07-11 and exits nonzero the moment one degrades.

Baselines are ceilings, not targets — drive them down by adjudication,
then lower the constant here in the same commit.

  python3 iol_identity_check.py            # check, exit 1 on regression
"""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

from volume_identity_screens import (screen_a1, screen_a2_birth_from_honour,
                                     screen_a2_invariants)
from iol_identity_screens import load_persons

ROOT = Path("data/iol")

BASELINES = {
    # ---- structural invariants (must stay 0) ----
    # (the school-pass compose's 16 unflattened chains were fixed by the
    # audited-map rebuild of 2026-07-11 — iol_merge_apply.py flattens)
    "map_unflattened": 0,          # map key also appears as another's canonical
    "map_self_rows": 0,            # person_id == canonical_person_id rows
    "map_key_not_in_corpus": 0,    # merge-map key absent from valid corpus
    "map_canon_not_in_corpus": 0,  # merge-map canonical absent from valid corpus
    "deduped_vs_map_diff": 0,      # applying map to corpus != shipped deduped set
    "gs3_vs_deduped_diff": 0,      # graph_stage3 persons != deduped set
    "gs3_orphan_event_refs": 0,    # career_events person_id not in persons
    "gs3_orphan_honour_refs": 0,   # honours person_id not in persons
    "dup_person_ids": 0,           # duplicate person_id in deduped corpus
    # ---- corpus census (exact — a change means a rebuild happened;
    #      re-measure and update in the same commit) ----
    # post-audit rebuild 2026-07-11 (Nibi 17505330 + a6-honour-override):
    # 12,540 school edges - 1,557 judged drops + 113 unions (27 A6-confirmed
    # + 86 honour-key reinstatements of judged drops), flattened
    "valid_records": 30446,
    "merge_edges": 11095,
    "canonical_persons": 19351,
    # ---- screen ceilings (re-measured post-rebuild 2026-07-11) ----
    "honour_precedence": 1,
    "age_invariants": 105,
    "birth_from_honour": 0,
}


def jload(path: Path):
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            yield json.loads(line)


def main() -> None:
    measured: dict[str, int] = {}

    valid_ids = [r["person_id"]
                 for r in jload(ROOT / "llm_struct_corpus.valid.jsonl")]
    # the audited (post-adjudication, flattened) map supersedes the school
    # compose once it exists
    live_map = ROOT / "dedup_stage3_merge_map.audited.jsonl"
    if not live_map.exists():
        live_map = ROOT / "dedup_stage3_merge_map.school.jsonl"
    mrows = list(jload(live_map))
    mmap = {r["person_id"]: r["canonical_person_id"] for r in mrows}
    deduped_ids = [r["person_id"] for r in
                   jload(ROOT / "llm_struct_corpus.stage3.deduped.jsonl")]
    gs3_ids = [r["person_id"]
               for r in jload(ROOT / "graph_stage3/persons.jsonl")]

    # merge-map structure
    canon_set = set(mmap.values())
    measured["map_unflattened"] = sum(1 for k in mmap if k in canon_set)
    measured["map_self_rows"] = sum(1 for k, v in mmap.items() if k == v)
    vset = set(valid_ids)
    measured["map_key_not_in_corpus"] = sum(1 for k in mmap if k not in vset)
    measured["map_canon_not_in_corpus"] = sum(
        1 for v in canon_set if v not in vset)
    measured["merge_edges"] = len(mrows)

    # partition: applying the map reproduces the shipped person table
    applied = {mmap.get(p, p) for p in valid_ids}
    measured["deduped_vs_map_diff"] = len(applied ^ set(deduped_ids))
    measured["gs3_vs_deduped_diff"] = len(set(gs3_ids) ^ set(deduped_ids))
    measured["valid_records"] = len(valid_ids)
    measured["canonical_persons"] = len(deduped_ids)
    measured["dup_person_ids"] = sum(
        1 for _, c in Counter(deduped_ids).items() if c > 1)

    # KG layer referential integrity
    pset = set(gs3_ids)
    measured["gs3_orphan_event_refs"] = sum(
        1 for r in jload(ROOT / "graph_stage3/career_events.jsonl")
        if r["person_id"] not in pset)
    measured["gs3_orphan_honour_refs"] = sum(
        1 for r in jload(ROOT / "graph_stage3/honours.jsonl")
        if r["person_id"] not in pset)

    # screens (recomputed live so a regression in the person table shows
    # up here even if the screen output files are stale)
    persons = load_persons()
    measured["honour_precedence"] = len(screen_a1(persons))
    measured["age_invariants"] = len(screen_a2_invariants(persons))
    measured["birth_from_honour"] = len(screen_a2_birth_from_honour(persons))

    exact = {"valid_records", "merge_edges", "canonical_persons"}
    failures = []
    for key, base in BASELINES.items():
        got = measured[key]
        bad = (got != base) if key in exact else (got > base)
        status = "FAIL" if bad else "ok"
        print(f"  {status:4} {key:26} measured {got:>7,}  baseline {base:,}")
        if bad:
            failures.append(key)

    if failures:
        print(f"\nFAILED: {len(failures)} invariant(s) regressed: "
              f"{', '.join(failures)}", file=sys.stderr)
        sys.exit(1)
    print("\nAll IOL identity invariants green.")


if __name__ == "__main__":
    main()
