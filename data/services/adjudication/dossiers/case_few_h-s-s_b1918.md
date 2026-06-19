<!-- {"case_id": "case_few_h-s-s_b1918", "bio_ids": ["few_h-s-s_b1918"], "stint_ids": ["Few, H. S. S___Gambia___1962", "Few, H. S. S___Uganda___1949"]} -->
# Dossier case_few_h-s-s_b1918

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `few_h-s-s_b1918`

- Printed name: **FEW, H. S. S**
- Birth year: 1918 (attested in editions [1957, 1958, 1960, 1961, 1962, 1963, 1964, 1965])
- Appears in editions: [1957, 1958, 1960, 1961, 1962, 1963, 1964, 1965]

### Verbatim printed entry text (OCR)

**Version `col1957-L22982.v` — printed in editions [1957, 1958, 1960, 1961, 1962, 1963, 1964, 1965]:**

> FEW, H. S. S., Q.C.—b. 1918; ed. Mill Hill Sch. and Christ’s Coll., Camb.; barrister-at-law, Inner Temple; mil. serv., 1939-46, maj.; cadet, Uga., 1940; provincial admin., res. mag., secon. as cr. coun., 1954; cr. coun., 1956; atty.-gen., Gam., 1961-64.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1940 | cadet | Uganda | [1957, 1958, 1960, 1961, 1962, 1963, 1964, 1965] |
| 1 | 1954 | provincial admin., res. mag., secon. as cr. coun | Uganda *(inherited from previous clause)* | [1957, 1958, 1960, 1961, 1962, 1963, 1964, 1965] |
| 2 | 1956 | cr. coun | Uganda *(inherited from previous clause)* | [1957, 1958, 1960, 1961, 1962, 1963, 1964, 1965] |
| 3 | 1961–1964 | atty.-gen., Gam | Uganda *(inherited from previous clause)* | [1957, 1958, 1960, 1961, 1962, 1963, 1964, 1965] |

## Candidate stint `Few, H. S. S___Gambia___1962`

- Staff-list name: **Few, H. S. S** | colony: **Gambia** | listed 1962–1964 | editions [1962, 1963, 1964]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1962 | H. S. S. Few | Law Officer: Attorney-General | Civil Establishment | — | — |
| 1963 | H. S. S. Few | Attorney-General | Non-Ministerial | — | — |
| 1964 | H. S. S. Few | Attorney-General | Non-Ministerial | — | — |

### Deterministic checks: `few_h-s-s_b1918` vs `Few, H. S. S___Gambia___1962`

- [PASS] surname_gate: bio 'FEW' vs stint 'Few, H. S. S' (exact)
- [PASS] initials: bio ['H', 'S', 'S'] ~ stint ['H', 'S', 'S']
- [PASS] age_gate: stint starts 1962, birth 1918 (age 44)
- [FAIL] colony: no placed event resolves to 'Gambia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1962-1964
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Few, H. S. S___Uganda___1949`

- Staff-list name: **Few, H. S. S** | colony: **Uganda** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | H. S. S. Few | District Officers and Assistant District Officers | Provincial Administration | — | — |
| 1951 | H. S. S. Few | District Officers and Assistant District Officers | Provincial Administration | — | — |

### Deterministic checks: `few_h-s-s_b1918` vs `Few, H. S. S___Uganda___1949`

- [PASS] surname_gate: bio 'FEW' vs stint 'Few, H. S. S' (exact)
- [PASS] initials: bio ['H', 'S', 'S'] ~ stint ['H', 'S', 'S']
- [PASS] age_gate: stint starts 1949, birth 1918 (age 31)
- [PASS] colony: 4 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 17 vs bar 60: 'cadet' ~ 'District Officers and Assistant District Officers'
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

