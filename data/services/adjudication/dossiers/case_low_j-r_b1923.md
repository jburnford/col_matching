<!-- {"case_id": "case_low_j-r_b1923", "bio_ids": ["low_j-r_b1923"], "stint_ids": ["Low, J. R___Uganda___1949"]} -->
# Dossier case_low_j-r_b1923

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 30 official(s) with this surname in the graph's staff lists; 13 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `low_j-r_b1923`

- Printed name: **LOW, J. R**
- Birth year: 1923 (attested in editions [1963, 1964, 1965, 1966])
- Appears in editions: [1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1963-L22165.v` — printed in editions [1963, 1964, 1965, 1966]:**

> LOW, J. R.—b. 1923; ed. Elementary, Scotland, Prince of Wales Sch., Ken., and Durham Univ.; mil. serv., 1940–46, sgt.; agric., offr., Uga., 1950; prin., Arapai Farm inst., 1962–65. (Uga. Govt. service.)

**Version `col1961-L24631.v` — printed in editions [1961, 1962]:**

> LOW, J. R.—b. 1923; ed. Elementary, Scotland, Prince of Wales Sch., Ken., and Durham Univ.; mil. serv., 1940-46, sgt.; agric. offr., Uga., 1950.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1950 | agric., offr. | Uganda | [1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1962–1965 | prin., Arapai Farm inst | Uganda *(inherited from previous clause)* | [1963, 1964, 1965, 1966] |

## Candidate stint `Low, J. R___Uganda___1949`

- Staff-list name: **Low, J. R** | colony: **Uganda** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | J. R. Low | Senior European Agricultural Assistant | Agricultural | — | — |
| 1951 | J. R. Low | Senior European Agricultural Assistants | Agricultural | — | — |

### Deterministic checks: `low_j-r_b1923` vs `Low, J. R___Uganda___1949`

- [PASS] surname_gate: bio 'LOW' vs stint 'Low, J. R' (exact)
- [PASS] initials: bio ['J', 'R'] ~ stint ['J', 'R']
- [PASS] age_gate: stint starts 1949, birth 1923 (age 26)
- [PASS] colony: 2 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 33 vs bar 60: 'agric., offr.' ~ 'Senior European Agricultural Assistant'
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

