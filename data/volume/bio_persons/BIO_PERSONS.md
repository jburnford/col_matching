# Unified bio-person table (volume bios ↔ stage-3 career KG)

Person identity adopts the stage-3 spine partition — kgp_* person_ids are
stable with graph_stage3 career facts/honours/groundings. This layer
re-derives names from the new volume parses (Qwen bios had none), votes
across editions, merges event chains, and QA-flags conflicts.

- volume bios (excl. not_a_bio): 202,100
- persons: 27,637 (27,583 real; 54 junk chains flagged not_a_person)
- multi-edition persons: 23,248 (84.3% of real)
- orphan bios attached to existing persons: 25; new singletons: 1

## Member roles

- primary: 200,686
- junk: 6,320
- legacy: 5,064
- dupprint: 1,395
- seeref: 19

## Name sources (per primary member)

- rules: 156,122
- header: 44,528
- spine: 1,009
- none: 11

## Flags

- no_primary_members: 1,116
- surname_variants: 1,056
- birth_year_conflict: 860
- namesake_same_edition: 108
- not_a_person: 54
- orphan_attached: 25
- suspect_surname: 25
- orphan_singleton: 1

## Edition-span distribution (real persons)

| editions attested | persons |
|---|---|
| 1 | 4,335 |
| 2 | 2,507 |
| 3 | 2,190 |
| 4 | 3,022 |
| 5 | 1,922 |
| 6 | 1,743 |
| 7 | 1,456 |
| 8 | 1,503 |
| 9 | 1,313 |
| 10 | 1,098 |
| 11 | 893 |
| 12 | 757 |
| 13 | 626 |
| 14 | 587 |
| 15 | 501 |
| 16 | 479 |
| 17 | 375 |
| 18 | 310 |
| 19 | 250 |
| 20 | 233 |
| 21 | 240 |
| 22 | 202 |
| 23 | 158 |
| 24 | 147 |
| 25 | 128 |
| 26 | 120 |
| 27 | 92 |
| 28 | 81 |
| 29 | 72 |
| 30 | 53 |
| 31 | 42 |
| 32 | 27 |
| 33 | 24 |
| 34 | 16 |
| 35 | 21 |
| 36 | 17 |
| 37 | 7 |
| 38 | 7 |
| 39 | 6 |
| 40 | 5 |
| 41 | 8 |
| 42 | 6 |
| 43 | 2 |
| 44 | 1 |
| 45 | 1 |

## Roster-career join (careers.jsonl bio links -> persons)

- non-suspect roster careers: 171,180; bio-linked: 20,482 — all resolve to a person (the partition is total over bios)
- distinct persons behind bio-linked careers: 12,157
- persons with roster careers in >1 colony: 2,320
- careers whose bios map to >1 person (link noise / residual under-merge): 682

## Under-merge candidates (new-event appointment chains)

124 candidate pairs (>= 3 shared exact (position-stem, year) appointments, given-compatible, edition-disjoint):

- tier A (>=4 shared, birth years not in conflict): 64
- tier B (3 shared, birth years not in conflict): 58
- tier C (birth-year conflict — likely OCR-garbled years): 2

Review file: undermerge_candidates.jsonl — NOT auto-applied.
