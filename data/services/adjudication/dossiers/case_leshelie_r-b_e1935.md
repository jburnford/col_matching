<!-- {"case_id": "case_leshelie_r-b_e1935", "bio_ids": ["leshelie_r-b_e1935", "leslie_r-b-m-o_e1936"], "stint_ids": ["Leslie, R. B___Ceylon___1936"]} -->
# Dossier case_leshelie_r-b_e1935

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 20 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Leslie, R. B___Ceylon___1936'] have more than one claimant biography in this case.

## Biography `leshelie_r-b_e1935`

- Printed name: **LESHELIE, R. B**
- Birth year: not printed
- Honours: M.C
- Appears in editions: [1940]

### Verbatim printed entry text (OCR)

**Version `col1940-L66096.v` — printed in editions [1940]:**

> LESHELIE, COL. R. B., M.C., Lincolnshire Regt.—Commtd., Ceylon defence force, Mar., 1935.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1935 | Commtd., Ceylon defence force | Ceylon | [1940] |

## Biography `leslie_r-b-m-o_e1936`

- Printed name: **LESLIE, R. B. M.O**
- Birth year: not printed
- Appears in editions: [1939]

### Verbatim printed entry text (OCR)

**Version `col1939-L68612.v` — printed in editions [1939]:**

> LESLIE, COL. R. B. M.O., Lincolnshire Regt.—Commdt., Ceylon defence force, Mar., 1936.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1936 | Commdt., Ceylon defence force | Ceylon | [1939] |

## Candidate stint `Leslie, R. B___Ceylon___1936`

- Staff-list name: **Leslie, R. B** | colony: **Ceylon** | listed 1936–1937 | editions [1936, 1937]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | R. B. Leslie | Commandant | Ceylon Defence Force | — | Colonel |
| 1937 | R. B. Leslie | Commandant | Ceylon Defence Force | — | Colonel |

### Deterministic checks: `leshelie_r-b_e1935` vs `Leslie, R. B___Ceylon___1936`

- [PASS] surname_gate: bio 'LESHELIE' vs stint 'Leslie, R. B' (fuzzy:2)
- [PASS] initials: bio ['R', 'B'] ~ stint ['R', 'B']
- [PASS] age_gate: stint starts 1936; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1936-1937
- [FAIL] position_sim: best 32 vs bar 60: 'Commtd., Ceylon defence force' ~ 'Commandant'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

### Deterministic checks: `leslie_r-b-m-o_e1936` vs `Leslie, R. B___Ceylon___1936`

- [PASS] surname_gate: bio 'LESLIE' vs stint 'Leslie, R. B' (exact)
- [PASS] initials: bio ['R', 'B', 'M', 'O'] ~ stint ['R', 'B']
- [PASS] age_gate: stint starts 1936; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1936-1937
- [FAIL] position_sim: best 32 vs bar 60: 'Commdt., Ceylon defence force' ~ 'Commandant'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

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

