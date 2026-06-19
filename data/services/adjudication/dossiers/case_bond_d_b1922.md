<!-- {"case_id": "case_bond_d_b1922", "bio_ids": ["bond_d_b1922"], "stint_ids": ["Bond, D___Uganda___1949"]} -->
# Dossier case_bond_d_b1922

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 26 official(s) with this surname in the graph's staff lists; 11 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['bond_d_b1922'] carry a single initial only — the namesake trap applies.

## Biography `bond_d_b1922`

- Printed name: **BOND, D**
- Birth year: 1922 (attested in editions [1958, 1959, 1960, 1961, 1962, 1963])
- Appears in editions: [1958, 1959, 1960, 1961, 1962, 1963]

### Verbatim printed entry text (OCR)

**Version `col1958-L20697.v` — printed in editions [1958, 1959, 1960, 1961, 1962, 1963]:**

> BOND, D.—b. 1922; ed. Lindisfarne Coll., Westcliff-on-Sea, and London Univ.; mil. serv., 1943–46, capt.; asst. engr., Uga., 1946; exec. engr., 1951; senr. exec. engr., 1956–62. (Uga. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | asst. engr. | Uganda | [1958, 1959, 1960, 1961, 1962, 1963] |
| 1 | 1951 | exec. engr | Uganda *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963] |
| 2 | 1956–1962 | senr. exec. engr | Uganda *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963] |

## Candidate stint `Bond, D___Uganda___1949`

- Staff-list name: **Bond, D** | colony: **Uganda** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | D. Bond | Executive Engineers and Assistant Engineers | Public Works | — | — |
| 1951 | D. Bond | Executive Engineers and Assistant Engineers | Public Works | — | — |

### Deterministic checks: `bond_d_b1922` vs `Bond, D___Uganda___1949`

- [PASS] surname_gate: bio 'BOND' vs stint 'Bond, D' (exact)
- [PASS] initials: bio ['D'] ~ stint ['D']
- [PASS] age_gate: stint starts 1949, birth 1922 (age 27)
- [PASS] colony: 3 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 43 vs bar 60: 'asst. engr.' ~ 'Executive Engineers and Assistant Engineers'
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

