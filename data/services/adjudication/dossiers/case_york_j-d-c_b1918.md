<!-- {"case_id": "case_york_j-d-c_b1918", "bio_ids": ["york_j-d-c_b1918"], "stint_ids": ["York, J. D. C___Nyasaland___1950"]} -->
# Dossier case_york_j-d-c_b1918

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `york_j-d-c_b1918`

- Printed name: **YORK, J. D. C**
- Birth year: 1918 (attested in editions [1963, 1964])
- Honours: C.P.M (1958)
- Appears in editions: [1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1963-L26621.v` — printed in editions [1963, 1964]:**

> YORK, J. D. C., C.P.M. (1958).—b. 1918; ed. Repton Sch.; mil. serv., 1942-48; S. Rhod. police, 1939; asst. supt., Nyas., 1949; supt., 1957; senr. supt., 1961.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1939 | S. Rhod. police | Southern Rhodesia | [1963, 1964] |
| 1 | 1949 | asst. supt., Nyas | Southern Rhodesia *(inherited from previous clause)* | [1963, 1964] |
| 2 | 1957 | supt | Southern Rhodesia *(inherited from previous clause)* | [1963, 1964] |
| 3 | 1961 | senr. supt | Southern Rhodesia *(inherited from previous clause)* | [1963, 1964] |

## Candidate stint `York, J. D. C___Nyasaland___1950`

- Staff-list name: **York, J. D. C** | colony: **Nyasaland** | listed 1950–1951 | editions [1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | J. D. C. York | Assistant Superintendents | Police and Immigration | — | — |
| 1951 | J. D. C. York | Assistant Superintendent | POLICE | — | — |

### Deterministic checks: `york_j-d-c_b1918` vs `York, J. D. C___Nyasaland___1950`

- [PASS] surname_gate: bio 'YORK' vs stint 'York, J. D. C' (exact)
- [PASS] initials: bio ['J', 'D', 'C'] ~ stint ['J', 'D', 'C']
- [PASS] age_gate: stint starts 1950, birth 1918 (age 32)
- [FAIL] colony: no placed event resolves to 'Nyasaland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1950-1951
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

