<!-- {"case_id": "case_leacock_a-g_b1918", "bio_ids": ["leacock_a-g_b1918"], "stint_ids": ["Leacock, A. G___Barbados___1950", "Leacock, A. G___Barbados___1955"]} -->
# Dossier case_leacock_a-g_b1918

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `leacock_a-g_b1918`

- Printed name: **LEACOCK, A. G.**
- Birth year: 1918 (attested in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Honours: C.B.E. (1963)
- Appears in editions: [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1956-L22456.v` — printed in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> LEACOCK, A. G., C.B.E. (1963).—b. 1918; ed. Harrison Coll., Barb. and Camb. Univ.; asst. surgeon, B. Guiana, 1946; surgeon-specialist, Barb., 1948-51 and 1954.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946–1946 | asst. surgeon | British Guiana | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1948–1954 | surgeon-specialist | Barbados | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Leacock, A. G___Barbados___1950`

- Staff-list name: **Leacock, A. G** | colony: **Barbados** | listed 1950–1951 | editions [1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | A. G. Leacock | Surgeon Specialist | General Hospital | — | — |
| 1951 | A. G. Leacock | Surgeon Specialist | General Hospital | — | — |

### Deterministic checks: `leacock_a-g_b1918` vs `Leacock, A. G___Barbados___1950`

- [PASS] surname_gate: bio 'LEACOCK' vs stint 'Leacock, A. G' (exact)
- [PASS] initials: bio ['A', 'G'] ~ stint ['A', 'G']
- [PASS] age_gate: stint starts 1950, birth 1918 (age 32)
- [PASS] colony: 1 placed event(s) resolve to 'Barbados'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1950-1951
- [FAIL] position_sim: best 57 vs bar 60: 'surgeon-specialist' ~ 'Surgeon Specialist'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Leacock, A. G___Barbados___1955`

- Staff-list name: **Leacock, A. G** | colony: **Barbados** | listed 1955–1966 | editions [1955, 1956, 1957, 1963, 1964, 1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1955 | A. G. Leacock | Surgeon Specialist, General Hospital | Civil Establishment | — | — |
| 1956 | A. G. Leacock | Surgeon Specialist, General Hospital | Civil Establishment | — | — |
| 1957 | A. G. Leacock | Surgeon Specialist, General Hospital | Civil Establishment | — | — |
| 1963 | A. G. Leacock | Senior Surgeon Specialist, General Hospital | Civil Establishment | — | — |
| 1964 | A. G. Leacock | Senior Surgeon Specialist, General Hospital | Civil Establishment | — | — |
| 1965 | A. G. Leacock | Senior Surgeon Specialist, General Hospital | Civil Establishment | — | — |
| 1966 | A. G. Leacock | Senior Surgeon Specialist, Queen Elizabeth Hospital | Privy Council | — | — |

### Deterministic checks: `leacock_a-g_b1918` vs `Leacock, A. G___Barbados___1955`

- [PASS] surname_gate: bio 'LEACOCK' vs stint 'Leacock, A. G' (exact)
- [PASS] initials: bio ['A', 'G'] ~ stint ['A', 'G']
- [PASS] age_gate: stint starts 1955, birth 1918 (age 37)
- [PASS] colony: 1 placed event(s) resolve to 'Barbados'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1955-1966
- [FAIL] position_sim: best 50 vs bar 60: 'surgeon-specialist' ~ 'Surgeon Specialist, General Hospital'
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

