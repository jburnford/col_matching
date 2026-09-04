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
    # overlay layers (role/employment/honour/qualification/education edges,
    # career_facts) are emitted SEPARATELY from the spine and go stale when
    # only the spine is rebuilt (2026-09-03 review: 5,351 orphan role edges)
    "gs3_orphan_overlay_refs": 0,  # overlay-edge person_id not in persons
    "gs3_events_no_role_edge": 0,  # persons with events but no role edge
    "dup_person_ids": 0,           # duplicate person_id in deduped corpus
    # ---- corpus census (exact — a change means a rebuild happened;
    #      re-measure and update in the same commit) ----
    # bios-fix rebuild 2026-07-12 (section max-span + no-comma headwords
    # + mid-text splits; 265,959 bios, stage-2 30,257 chains, 5
    # unstructurable monster segments): corpus 30,252; map = 11,118
    # surviving school edges - 1,398 drops + 1,343 delta/A6 unions
    # (Nibi 17539869: 1,247 judged same of 1,438 delta pairs) -> 10,739;
    # overlays re-applied in-build (100 births, 487 roll honour dates,
    # 2,076 deaths; 104 rows target vanished pre-rechain ids)
    "valid_records": 30252,
    "merge_edges": 10739,
    "canonical_persons": 19513,
    # ---- screen ceilings (re-measured post-rebuild 2026-07-12) ----
    "honour_precedence": 1,
    # 8 fresh garbled birth years arrived with the 6.1k recovered bios —
    # the next adjudication batch's A2 pool
    "age_invariants": 8,
    "birth_from_honour": 0,
    # A7 (events after linked death, iol_link_exits.py) — read from the
    # screen's output file; RERUN iol_link_exits.py after any person-table
    # change or this pins a stale count. 2 pinned (edition-lag singleton +
    # hand-review fusion candidate) + 2 new from reorganized chains
    "events_after_death": 4,
    # ---- no-bio layer (steps 1-3 build 2026-07-12; exact — the
    #      judged apply will change these in its own commit) ----
    # (re-measured after the silver-audit fixes: plural office nouns,
    #  commissariat + function-word junk rules, grad_exit rank gate,
    #  content-derived chain ids)
    "nobio_union": 32287,          # census: chains + gradation - overlap
    "nobio_chains": 17816,
    "nobio_gradation_unlinked": 14984,
    "nobio_class_A": 18804,
    "nobio_class_B": 2368,
    "nobio_class_C": 7940,
    "nobio_class_U": 3688,
    "nobio_det_edges": 1860,
    # structural (must stay 0)
    "nobio_edge_orphans": 0,       # unify edge endpoint in no layer
    "nobio_member_dups": 0,        # identity in >1 nobio component
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

    overlay_orphans = 0
    for layer in ("role_edges", "employment_edges", "honour_edges",
                  "qualification_edges", "education_edges", "career_facts"):
        f = ROOT / f"graph_stage3/{layer}.jsonl"
        if f.exists():
            overlay_orphans += sum(
                1 for r in jload(f) if r["person_id"] not in pset)
    measured["gs3_orphan_overlay_refs"] = overlay_orphans
    ev_people = {r["person_id"]
                 for r in jload(ROOT / "graph_stage3/career_events.jsonl")}
    role_people = {r["person_id"]
                   for r in jload(ROOT / "graph_stage3/role_edges.jsonl")}
    measured["gs3_events_no_role_edge"] = len(ev_people - role_people)

    # screens (recomputed live so a regression in the person table shows
    # up here even if the screen output files are stale)
    persons = load_persons()
    measured["honour_precedence"] = len(screen_a1(persons))
    measured["age_invariants"] = len(screen_a2_invariants(persons))
    measured["birth_from_honour"] = len(screen_a2_birth_from_honour(persons))

    a7 = ROOT / "identity/a7_events_after_death.jsonl"
    measured["events_after_death"] = \
        sum(1 for _ in open(a7, encoding="utf-8")) if a7.exists() else 0

    # no-bio layer (iol_nobio_census/_unify/_classes/_apply outputs)
    idd = ROOT / "identity"
    census = json.load(open(idd / "nobio_census.json"))
    measured["nobio_union"] = census["nobio_union"]
    chain_ids = {r["chain_id"]
                 for r in jload(idd / "nobio_civil_chains.jsonl")}
    measured["nobio_chains"] = len(chain_ids)
    measured["nobio_gradation_unlinked"] = census["gradation_unlinked"]
    cls = Counter(r["cls"] for r in jload(idd / "nobio_classes.jsonl"))
    for k in "ABCU":
        measured[f"nobio_class_{k}"] = cls[k]
    grad_ids = {r["gradation_id"] for r in
                jload(ROOT / "gradation/gradation_identities.jsonl")}
    edges = list(jload(idd / "nobio_unify_edges.jsonl"))
    measured["nobio_det_edges"] = len(edges)
    known = chain_ids | grad_ids
    measured["nobio_edge_orphans"] = sum(
        1 for e in edges
        if e["a"] not in known
        or (e["edge_type"] in ("chain_grad", "chain_chain")
            and e["b"] not in known))
    members = [m for r in jload(idd / "nobio_persons.jsonl")
               for m in r["members"]]
    measured["nobio_member_dups"] = sum(
        1 for _, c in Counter(members).items() if c > 1)

    exact = {"valid_records", "merge_edges", "canonical_persons",
             "nobio_union", "nobio_chains", "nobio_gradation_unlinked",
             "nobio_class_A", "nobio_class_B", "nobio_class_C",
             "nobio_class_U", "nobio_det_edges"}
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
