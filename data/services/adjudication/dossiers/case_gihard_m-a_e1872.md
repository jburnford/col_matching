<!-- {"case_id": "case_gihard_m-a_e1872", "bio_ids": ["gihard_m-a_e1872"], "stint_ids": ["Girard, M'. A___Canada___1877", "Girard, M'. A___Canada___1889"]} -->
# Dossier case_gihard_m-a_e1872

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- Phase 1 found `gihard_m-a_e1872` ↔ `Girard, M'. A___Canada___1877` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Girard, M'. A___Canada___1877` is also gate-compatible with biography(ies) outside this case: ['girard_m-a_e1872'] (already linked elsewhere or filtered).
- NOTE: stint `Girard, M'. A___Canada___1889` is also gate-compatible with biography(ies) outside this case: ['girard_m-a_e1872'] (already linked elsewhere or filtered).

## Biography `gihard_m-a_e1872`

- Printed name: **GIHARD, M. A.**
- Birth year: not printed
- Appears in editions: [1899]

### Verbatim printed entry text (OCR)

**Version `col1899-L35002.v` — printed in editions [1899]:**

> GIHARD, M. A.—Began his political life with the organization of Manitoba as a prov. of the Dominion; was a mem. of the local govt. under the first three lieut.-govs., and occupied the positions of prov. treas., prov. sec., and min. of agricul.; in 1872 apptd. sen. mem. of N.W. coun., and a senator of Canada, which latter position he still holds.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1872 | sen. mem. of N.W. coun., and a senator | Canada | [1899] |
| 1 | ? | — | Manitoba | [1899] |
| 2 | ? | mem. of the local govt., prov. treas., prov. sec., and min. of agricul. | — | [1899] |

## Candidate stint `Girard, M'. A___Canada___1877`

- Staff-list name: **Girard, M'. A** | colony: **Canada** | listed 1877–1883 | editions [1877, 1878, 1879, 1880, 1883]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | M. A. Girard | Senator | Senate of Canada | — | — |
| 1878 | M. A. Girard | Senator | Senate of Canada | — | — |
| 1879 | M. A. Girard | Senator | Senate of Canada | — | — |
| 1880 | M. A. Girard | Senator | Senators | — | — |
| 1883 | M'. A. Girard | Senator | Senators | — | — |

### Deterministic checks: `gihard_m-a_e1872` vs `Girard, M'. A___Canada___1877`

- [PASS] surname_gate: bio 'GIHARD' vs stint 'Girard, M'. A' (fuzzy:1)
- [PASS] initials: bio ['M', 'A'] ~ stint ['M', 'A']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Canada'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1883
- [PASS] position_sim: best 100 vs bar 60: 'sen. mem. of N.W. coun., and a senator' ~ 'Senator'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Girard, M'. A___Canada___1889`

- Staff-list name: **Girard, M'. A** | colony: **Canada** | listed 1889–1890 | editions [1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1889 | M. A. Girard | Senator | Senate of Canada | — | — |
| 1890 | M. A. Girard | Senator | Senate | — | — |

### Deterministic checks: `gihard_m-a_e1872` vs `Girard, M'. A___Canada___1889`

- [PASS] surname_gate: bio 'GIHARD' vs stint 'Girard, M'. A' (fuzzy:1)
- [PASS] initials: bio ['M', 'A'] ~ stint ['M', 'A']
- [PASS] age_gate: stint starts 1889; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1889-1890
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Adjudication constraints (binding)

- The prime directive is NO FALSE MERGES. A missed link is recoverable; a
  wrong one silently corrupts the historical record. When in doubt, leave
  the stint unassigned.
- Surname identity is NOT evidence: every candidate here already shares the
  surname (it is the blocking key). Only position, place, dates, honours,
  initials/forenames, and edition co-occurrence count.
- Single-initial biographies (e.g. "J. Lewis") must never be merged on
  shared-stint or tenure-overlap evidence alone; they need a strong
  independent dimension (specific position match, shared honour, or
  multi-edition co-occurrence).
- A stint belongs to AT MOST one biography. If two biographies in this case
  could plausibly hold the same stint, assign it to neither.
- Respect hard chronology: nobody serves before age ~15 or after death.
- Generic junior titles (clerk, cadet, assistant) recur constantly; a title
  match alone on a common office is weak evidence.

