<!-- {"case_id": "case_grimley_s-c_b1909", "bio_ids": ["grimley_s-c_b1909"], "stint_ids": ["Grimley, S. C___Uganda___1949"]} -->
# Dossier case_grimley_s-c_b1909

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `grimley_s-c_b1909`

- Printed name: **GRIMLEY, S. C**
- Birth year: 1909 (attested in editions [1961, 1962, 1964, 1965])
- Honours: C.P.M
- Appears in editions: [1961, 1962, 1964, 1965]

### Verbatim printed entry text (OCR)

**Version `col1961-L22776.v` — printed in editions [1961, 1962, 1964, 1965]:**

> GRIMLEY, S. C., C.P.M.—b. 1909; ed. Commercial Sch., Stratford-on-Avon; B.S.A. police, S. Rhod., 1935; inspr., police, Uga., 1946; chief inspr., 1948; asst. supt., 1950; senr. asst. supt., 1951; supt., 1955; senr. supt., 1959. (Uga. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1935 | B.S.A. police | Southern Rhodesia | [1961, 1962, 1964, 1965] |
| 1 | 1946 | inspr., police | Uganda | [1961, 1962, 1964, 1965] |
| 2 | 1948 | chief inspr | Uganda *(inherited from previous clause)* | [1961, 1962, 1964, 1965] |
| 3 | 1950 | asst. supt | Uganda *(inherited from previous clause)* | [1961, 1962, 1964, 1965] |
| 4 | 1951 | senr. asst. supt | Uganda *(inherited from previous clause)* | [1961, 1962, 1964, 1965] |
| 5 | 1955 | supt | Uganda *(inherited from previous clause)* | [1961, 1962, 1964, 1965] |
| 6 | 1959 | senr. supt | Uganda *(inherited from previous clause)* | [1961, 1962, 1964, 1965] |

## Candidate stint `Grimley, S. C___Uganda___1949`

- Staff-list name: **Grimley, S. C** | colony: **Uganda** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | S. C. Grimley | Chief Inspectors | Police | — | — |
| 1951 | S. C. Grimley | Superintendents, Assistants and Cadets | Police | — | — |

### Deterministic checks: `grimley_s-c_b1909` vs `Grimley, S. C___Uganda___1949`

- [PASS] surname_gate: bio 'GRIMLEY' vs stint 'Grimley, S. C' (exact)
- [PASS] initials: bio ['S', 'C'] ~ stint ['S', 'C']
- [PASS] age_gate: stint starts 1949, birth 1909 (age 40)
- [PASS] colony: 6 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 4 event tenure(s) overlap stint years 1949-1951
- [PASS] position_sim: best 81 vs bar 60: 'chief inspr' ~ 'Chief Inspectors'
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

