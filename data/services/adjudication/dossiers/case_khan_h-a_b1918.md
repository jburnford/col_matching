<!-- {"case_id": "case_khan_h-a_b1918", "bio_ids": ["khan_h-a_b1918"], "stint_ids": ["Khan, A___British Guiana___1962"]} -->
# Dossier case_khan_h-a_b1918

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `khan_h-a_b1918`

- Printed name: **KHAN, H. A**
- Birth year: 1918 (attested in editions [1966])
- Honours: C.P.M (1959), Q.P.M (1964)
- Appears in editions: [1966]

### Verbatim printed entry text (OCR)

**Version `col1966-L15911.v` — printed in editions [1966]:**

> KHAN, H. A., Q.P.M. (1964), C.P.M. (1959).—b. 1918; police, Aden, 1940; asst. supt., 1956; asst. comsnr., 1962; dep. comsnr., 1965.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1940 | police | Aden | [1966] |
| 1 | 1956 | asst. supt | Aden *(inherited from previous clause)* | [1966] |
| 2 | 1962 | asst. comsnr | Aden *(inherited from previous clause)* | [1966] |
| 3 | 1965 | dep. comsnr | Aden *(inherited from previous clause)* | [1966] |

## Candidate stint `Khan, A___British Guiana___1962`

- Staff-list name: **Khan, A** | colony: **British Guiana** | listed 1962–1966 | editions [1962, 1963, 1964, 1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1962 | A. Khan | Senior Magistrate | Judiciary | — | — |
| 1963 | A. Khan | Puisne Judge | Judiciary | — | — |
| 1964 | A. Khan | Puisne Judge | Judiciary | — | — |
| 1965 | A. Khan | Puisne Judge | Judiciary | — | — |
| 1966 | A. Khan | Puisne Judge | Judiciary | — | — |

### Deterministic checks: `khan_h-a_b1918` vs `Khan, A___British Guiana___1962`

- [PASS] surname_gate: bio 'KHAN' vs stint 'Khan, A' (exact)
- [PASS] initials: bio ['H', 'A'] ~ stint ['A']
- [PASS] age_gate: stint starts 1962, birth 1918 (age 44)
- [FAIL] colony: no placed event resolves to 'British Guiana'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1962-1966
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

