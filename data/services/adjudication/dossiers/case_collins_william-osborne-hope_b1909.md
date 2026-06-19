<!-- {"case_id": "case_collins_william-osborne-hope_b1909", "bio_ids": ["collins_william-osborne-hope_b1909"], "stint_ids": ["Collins, W___Gambia___1924"]} -->
# Dossier case_collins_william-osborne-hope_b1909

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 66 official(s) with this surname in the graph's staff lists; 30 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `collins_william-osborne-hope_b1909`

- Printed name: **COLLINS, WILLIAM OSBORNE HOPE**
- Birth year: 1909 (attested in editions [1940])
- Appears in editions: [1940]

### Verbatim printed entry text (OCR)

**Version `col1940-L63302.v` — printed in editions [1940]:**

> COLLINS, WILLIAM OSBORNE HOPE, M.A. (Cantab.).—B. 1909; ed. Tonbridge and St. Catherine's Coll., Cambridge; Br. Guiana pol., 1932; asst. supt., pol., Tanganyika Territory, 1936; asst. dist. commr., Basutoland, 1937.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1932 | Br. Guiana pol | British Guiana | [1940] |
| 1 | 1936 | asst. supt., pol., Tanganyika Territory | Tanganyika | [1940] |
| 2 | 1937 | asst. dist. commr. | Basutoland | [1940] |

## Candidate stint `Collins, W___Gambia___1924`

- Staff-list name: **Collins, W** | colony: **Gambia** | listed 1924–1940 | editions [1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1936, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1924 | W. Collins | Bandmaster | Police Force | — | — |
| 1925 | W. Collins | Bandmaster | Police Force | — | — |
| 1927 | W. Collins | Bandmaster | Police Force | — | — |
| 1928 | W. Collins | Bandmaster | Police Force | — | — |
| 1929 | W. Collins | Bandmaster | Police Force | — | — |
| 1930 | W. Collins | Bandmaster | Police Force | — | — |
| 1931 | W. Collins | Superintendent | Police Force | — | — |
| 1932 | W. Collins | Superintendent | Police Force | — | — |
| 1933 | W. Collins | Superintendent | Police Force | — | — |
| 1934 | W. Collins | Superintendent | Police Force | — | — |
| 1936 | W. Collins | Superintendent | Police Force | — | — |
| 1937 | W. Collins | Superintendent | Police Force | — | — |
| 1939 | W. Collins | Chief Inspector | Police Force | — | — |
| 1940 | W. Collins | Assistant | Police Force | — | — |

### Deterministic checks: `collins_william-osborne-hope_b1909` vs `Collins, W___Gambia___1924`

- [PASS] surname_gate: bio 'COLLINS' vs stint 'Collins, W' (exact)
- [PASS] initials: bio ['W', 'O', 'H'] ~ stint ['W']
- [PASS] age_gate: stint starts 1924, birth 1909 (age 15)
- [FAIL] colony: no placed event resolves to 'Gambia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1924-1940
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

