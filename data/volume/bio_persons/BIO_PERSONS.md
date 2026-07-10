# Unified bio-person table (volume bios ↔ stage-3 career KG)

Person identity adopts the stage-3 spine partition — kgp_* person_ids are
stable with graph_stage3 career facts/honours/groundings. This layer
re-derives names from the new volume parses (Qwen bios had none), votes
across editions, merges event chains, and QA-flags conflicts.

- volume bios (excl. not_a_bio): 202,100
- persons: 27,525 (27,471 real; 54 junk chains flagged not_a_person)
- multi-edition persons: 23,186 (84.4% of real)
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
- spine: 983
- none: 11

## Flags

- no_primary_members: 1,090
- surname_variants: 1,056
- birth_year_conflict: 862
- namesake_same_edition: 108
- undermerge_applied: 107
- not_a_person: 54
- orphan_attached: 25
- suspect_surname: 19
- orphan_singleton: 1

## Edition-span distribution (real persons)

| editions attested | persons |
|---|---|
| 1 | 4,285 |
| 2 | 2,487 |
| 3 | 2,168 |
| 4 | 3,015 |
| 5 | 1,916 |
| 6 | 1,733 |
| 7 | 1,454 |
| 8 | 1,505 |
| 9 | 1,312 |
| 10 | 1,097 |
| 11 | 890 |
| 12 | 753 |
| 13 | 623 |
| 14 | 583 |
| 15 | 504 |
| 16 | 481 |
| 17 | 377 |
| 18 | 314 |
| 19 | 246 |
| 20 | 235 |
| 21 | 239 |
| 22 | 204 |
| 23 | 159 |
| 24 | 148 |
| 25 | 129 |
| 26 | 120 |
| 27 | 92 |
| 28 | 83 |
| 29 | 74 |
| 30 | 54 |
| 31 | 42 |
| 32 | 27 |
| 33 | 24 |
| 34 | 16 |
| 35 | 21 |
| 36 | 16 |
| 37 | 6 |
| 38 | 9 |
| 39 | 6 |
| 40 | 6 |
| 41 | 8 |
| 42 | 6 |
| 43 | 2 |
| 44 | 1 |
| 45 | 1 |

## Roster-career join (careers.jsonl bio links -> persons)

- non-suspect roster careers: 171,180; bio-linked: 20,482 — all resolve to a person (the partition is total over bios)
- distinct persons behind bio-linked careers: 12,130
- persons with roster careers in >1 colony: 2,319
- careers whose bios map to >1 person (link noise / residual under-merge): 672

## Under-merge candidates (new-event appointment chains)

2 candidate pairs (>= 3 shared exact (position-stem, year) appointments, given-compatible, edition-disjoint):

- tier A (>=4 shared, birth years not in conflict): 1
- tier B (3 shared, birth years not in conflict): 1
- tier C (birth-year conflict — likely OCR-garbled years): 0

Review file: undermerge_candidates.jsonl — NOT auto-applied.
