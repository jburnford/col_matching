<!-- {"case_id": "case_pierre_henry_b1904", "bio_ids": ["pierre_henry_b1904"], "stint_ids": ["Pierre, J. Henry___Trinidad and Tobago___1934"]} -->
# Dossier case_pierre_henry_b1904

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['pierre_henry_b1904'] carry a single initial only — the namesake trap applies.

## Biography `pierre_henry_b1904`

- Printed name: **PIERRE, Henry**
- Birth year: 1904 (attested in editions [1962, 1963, 1964])
- Honours: Kt (1957)
- Appears in editions: [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1962-L25397.v` — printed in editions [1962, 1963, 1964]:**

> PIERRE, Sir Henry, Kt. (1957).—b. 1904; ed. Queen's Royal Coll., Trin. and London Univ.; M.O., Trin., 1932; gr. B, 1937; gr. A, 1943; senr. surgeon, 1950. (T'dad Govt. service.)

**Version `col1957-L26372.v` — printed in editions [1957, 1958, 1959, 1960, 1961]:**

> PIERRE, Sir J. H., Kt. (1957).—b. 1904; ed. Queen's Royal Coll., Trin. and London Univ.; M.O., Trin., 1932; gr. B, 1937; gr. A, 1943.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1932 | M.O. | Trinidad | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 1 | 1937 | gr. B | Trinidad *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 2 | 1943 | gr. A | Trinidad *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 3 | 1950 | senr. surgeon | Trinidad *(inherited from previous clause)* | [1962, 1963, 1964] |

## Candidate stint `Pierre, J. Henry___Trinidad and Tobago___1934`

- Staff-list name: **Pierre, J. Henry** | colony: **Trinidad and Tobago** | listed 1934–1937 | editions [1934, 1937]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | J. H. Pierre | Medical Officer | Government Medical Officers | — | — |
| 1937 | J. H. Pierre | Medical Officer | Medical Officers | — | — |

### Deterministic checks: `pierre_henry_b1904` vs `Pierre, J. Henry___Trinidad and Tobago___1934`

- [PASS] surname_gate: bio 'PIERRE' vs stint 'Pierre, J. Henry' (exact)
- [PASS] initials: bio ['H'] ~ stint ['J', 'H']
- [PASS] age_gate: stint starts 1934, birth 1904 (age 30)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1934-1937
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

