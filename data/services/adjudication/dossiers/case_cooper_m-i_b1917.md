<!-- {"case_id": "case_cooper_m-i_b1917", "bio_ids": ["cooper_m-i_b1917"], "stint_ids": ["Cooper, M. I___Uganda___1949"]} -->
# Dossier case_cooper_m-i_b1917

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 75 official(s) with this surname in the graph's staff lists; 41 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `cooper_m-i_b1917`

- Printed name: **COOPER, M. I**
- Birth year: 1917 (attested in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965])
- Appears in editions: [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965]

### Verbatim printed entry text (OCR)

**Version `col1958-L21608.v` — printed in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965]:**

> COOPER, M. I.—b. 1917; ed. Pontfean Gram. Sch., and R.M.C.; mil. serv., 1940-45, capt.; mil. affrs. offr., Uga., 1945; asst. sec., devel., 1949; co-op. offr., 1952. (Uga. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1945 | mil. affrs. offr. | Uganda | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 1 | 1949 | asst. sec., devel | Uganda *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 2 | 1952 | co-op. offr | Uganda *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |

## Candidate stint `Cooper, M. I___Uganda___1949`

- Staff-list name: **Cooper, M. I** | colony: **Uganda** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | M. I. Cooper | Development Assistant | Secretariat | — | — |
| 1951 | M. I. Cooper | Development Assistant | Secretariat | — | — |

### Deterministic checks: `cooper_m-i_b1917` vs `Cooper, M. I___Uganda___1949`

- [PASS] surname_gate: bio 'COOPER' vs stint 'Cooper, M. I' (exact)
- [PASS] initials: bio ['M', 'I'] ~ stint ['M', 'I']
- [PASS] age_gate: stint starts 1949, birth 1917 (age 32)
- [PASS] colony: 3 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1949-1951
- [PASS] position_sim: best 63 vs bar 60: 'asst. sec., devel' ~ 'Development Assistant'
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

