<!-- {"case_id": "case_inglis_james-duncan-louis_b1894", "bio_ids": ["inglis_james-duncan-louis_b1894"], "stint_ids": ["Inglis, J. D. L___St Lucia___1917", "Inglis, J. D. L___Windward Islands___1918"]} -->
# Dossier case_inglis_james-duncan-louis_b1894

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 13 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `inglis_james-duncan-louis_b1894`

- Printed name: **INGLIS, James Duncan Louis**
- Birth year: 1894 (attested in editions [1949, 1950, 1951])
- Appears in editions: [1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1949-L33136.v` — printed in editions [1949, 1950, 1951]:**

> INGLIS, James Duncan Louis.—b. 1894; ed. St. Mary's Coll., St. L.; copyist, St. L., 1912; treas., Dominica, 1945; comsrr. Barber enq. and sec., inc. tax comsrr., St. L., 1924.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1912 | copyist | St. Lucia | [1949, 1950, 1951] |
| 1 | 1924 | comsrr. Barber enq. and sec., inc. tax comsrr. | St. Lucia | [1949, 1950, 1951] |
| 2 | 1945 | treas. | Dominica | [1949, 1950, 1951] |

## Candidate stint `Inglis, J. D. L___St Lucia___1917`

- Staff-list name: **Inglis, J. D. L** | colony: **St Lucia** | listed 1917–1927 | editions [1917, 1921, 1927]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1917 | J. D. L. Inglis | 5th Clerk | Treasury, Customs, and Inland Revenue Department | — | — |
| 1921 | J. D. L. Inglis | 4th Clerk | Treasury, Customs, and Inland Revenue Department | — | — |
| 1927 | J. D. L. Inglis | 3rd Clerk | Treasury, Customs, and Inland Revenue Department | — | — |

### Deterministic checks: `inglis_james-duncan-louis_b1894` vs `Inglis, J. D. L___St Lucia___1917`

- [PASS] surname_gate: bio 'INGLIS' vs stint 'Inglis, J. D. L' (exact)
- [PASS] initials: bio ['J', 'D', 'L'] ~ stint ['J', 'D', 'L']
- [PASS] age_gate: stint starts 1917, birth 1894 (age 23)
- [PASS] colony: 2 placed event(s) resolve to 'St Lucia'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1917-1927
- [FAIL] position_sim: best 19 vs bar 60: 'comsrr. Barber enq. and sec., inc. tax comsrr.' ~ '3rd Clerk'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Inglis, J. D. L___Windward Islands___1918`

- Staff-list name: **Inglis, J. D. L** | colony: **Windward Islands** | listed 1918–1924 | editions [1918, 1919, 1920, 1922, 1923, 1924]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1918 | J. D. L. Inglis | 4th Clerk | Treasury, Customs, and Inland Revenue Department | — | — |
| 1919 | J. D. L. Inglis | 4th Clerk | Treasury, Customs, and Inland Revenue Department | — | — |
| 1920 | J. D. L. Inglis | 4th Clerk | Treasury, Customs, and Inland Revenue Department | — | — |
| 1922 | J. D. L. Inglis | 4th Clerk | Treasury, Customs, and Inland Revenue Department | — | — |
| 1923 | J. D. L. Inglis | 4th Clerk | Treasury, Customs, and Inland Revenue Department | — | — |
| 1924 | J. D. L. Inglis | 3rd Clerk | Treasury, Customs, and Inland Revenue Department | — | — |

### Deterministic checks: `inglis_james-duncan-louis_b1894` vs `Inglis, J. D. L___Windward Islands___1918`

- [PASS] surname_gate: bio 'INGLIS' vs stint 'Inglis, J. D. L' (exact)
- [PASS] initials: bio ['J', 'D', 'L'] ~ stint ['J', 'D', 'L']
- [PASS] age_gate: stint starts 1918, birth 1894 (age 24)
- [FAIL] colony: no placed event resolves to 'Windward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1918-1924
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

