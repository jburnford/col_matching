<!-- {"case_id": "case_ward_r-c_b1912", "bio_ids": ["ward_r-c_b1912"], "stint_ids": ["Ward, R. C___Northern Rhodesia___1939", "Ward, R. C___Uganda___1949"]} -->
# Dossier case_ward_r-c_b1912

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 112 official(s) with this surname in the graph's staff lists; 43 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `ward_r-c_b1912`

- Printed name: **WARD, R. C**
- Birth year: 1912 (attested in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964])
- Honours: M.B.E (1959)
- Appears in editions: [1958, 1959, 1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1958-L27932.v` — printed in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964]:**

> WARD, R. C., M.B.E. (1959)—b. 1912; ed. Higham Ferrers and Rushden Schs.; mil. serv., 1939–46, capt.; devel. offr., Uga., 1946; senr. estab. offr., 1954; prin. asst. sec., 1961–63. (Uga. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | devel. offr. | Uganda | [1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 1 | 1954 | senr. estab. offr | Uganda *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 2 | 1961–1963 | prin. asst. sec | Uganda *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964] |

## Candidate stint `Ward, R. C___Northern Rhodesia___1939`

- Staff-list name: **Ward, R. C** | colony: **Northern Rhodesia** | listed 1939–1940 | editions [1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | R. C. Ward | Cadet | District Administration | — | — |
| 1940 | R. C. Ward | Cadet | District Administration | — | — |

### Deterministic checks: `ward_r-c_b1912` vs `Ward, R. C___Northern Rhodesia___1939`

- [PASS] surname_gate: bio 'WARD' vs stint 'Ward, R. C' (exact)
- [PASS] initials: bio ['R', 'C'] ~ stint ['R', 'C']
- [PASS] age_gate: stint starts 1939, birth 1912 (age 27)
- [FAIL] colony: no placed event resolves to 'Northern Rhodesia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1939-1940
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Ward, R. C___Uganda___1949`

- Staff-list name: **Ward, R. C** | colony: **Uganda** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | R. C. Ward | Assistant Establishment Officer | Secretariat | — | — |
| 1951 | R. C. Ward | Assistant Establishment Officer | Secretariat | — | — |

### Deterministic checks: `ward_r-c_b1912` vs `Ward, R. C___Uganda___1949`

- [PASS] surname_gate: bio 'WARD' vs stint 'Ward, R. C' (exact)
- [PASS] initials: bio ['R', 'C'] ~ stint ['R', 'C']
- [PASS] age_gate: stint starts 1949, birth 1912 (age 37)
- [PASS] colony: 3 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 34 vs bar 60: 'devel. offr.' ~ 'Assistant Establishment Officer'
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

