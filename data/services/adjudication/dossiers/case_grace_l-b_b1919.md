<!-- {"case_id": "case_grace_l-b_b1919", "bio_ids": ["grace_l-b_b1919"], "stint_ids": ["Grace, L. B___Uganda___1949"]} -->
# Dossier case_grace_l-b_b1919

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `grace_l-b_b1919`

- Printed name: **GRACE, L. B**
- Birth year: 1919 (attested in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964])
- Appears in editions: [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1957-L23496.v` — printed in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]:**

> GRACE, L. B.—b. 1919; ed. St. Stanislaus Coll., Georgetown, B. Guiana and Imp. Coll. of Science and Tech., London; dist. engrnr., B. Guiana, 1943; exec. engrnr., P.W.D., Uga., 1948; senr., 1954; asst., D.P.W., 1956; asst. engrnr.-in-chief, min. of works, 1960; dep. engrnr.-in-ch., 1962. (Uga. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1943 | dist. engrnr., B. Guiana | — | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 1 | 1948 | exec. engrnr., P.W.D. | Uganda | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 2 | 1954 | senr | Uganda *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 3 | 1956 | asst., D.P.W | Uganda *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 4 | 1960 | asst. engrnr.-in-chief, min. of works | Uganda *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 5 | 1962 | dep. engrnr.-in-ch | Uganda *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |

## Candidate stint `Grace, L. B___Uganda___1949`

- Staff-list name: **Grace, L. B** | colony: **Uganda** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | L. B. Grace | Executive Engineers and Assistant Engineers | Public Works | — | — |
| 1951 | L. B. Grace | Executive Engineers and Assistant Engineers | Public Works | — | — |

### Deterministic checks: `grace_l-b_b1919` vs `Grace, L. B___Uganda___1949`

- [PASS] surname_gate: bio 'GRACE' vs stint 'Grace, L. B' (exact)
- [PASS] initials: bio ['L', 'B'] ~ stint ['L', 'B']
- [PASS] age_gate: stint starts 1949, birth 1919 (age 30)
- [PASS] colony: 5 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 42 vs bar 60: 'exec. engrnr., P.W.D.' ~ 'Executive Engineers and Assistant Engineers'
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

