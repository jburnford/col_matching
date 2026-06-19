<!-- {"case_id": "case_bishop_cecil-william-edwin_b1899", "bio_ids": ["bishop_cecil-william-edwin_b1899"], "stint_ids": ["Bishop, C. W. E___Hong Kong___1914", "Bishop, C. W. E___Hong Kong___1923"]} -->
# Dossier case_bishop_cecil-william-edwin_b1899

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 43 official(s) with this surname in the graph's staff lists; 10 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `bishop_cecil-william-edwin_b1899`

- Printed name: **BISHOP, CECIL WILLIAM EDWIN**
- Birth year: 1899 (attested in editions [1934, 1935, 1937, 1940])
- Appears in editions: [1934, 1935, 1937, 1940]

### Verbatim printed entry text (OCR)

**Version `col1934-L56668.v` — printed in editions [1934, 1935, 1937, 1940]:**

> BISHOP, CECIL WILLIAM EDWIN, B.Sc. (Eng.), A.M.Inst.C.E., M.Inst.W.E.—B. 1899; ed. Reigate Grammar Schl. and King's Coll., Lond. Univ.; war serv., 1918-19; engr., P.W.D., Hong Kong, 1922; ag. ex. engr., waterworks constr., 1935-36 and 1939.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1918–1919 | war serv. | — | [1934, 1935, 1937, 1940] |
| 1 | 1922–1922 | engr., P.W.D. | Hong Kong | [1934, 1935, 1937, 1940] |
| 2 | 1935–1939 | ag. ex. engr., waterworks constr. | — | [1934, 1935, 1937, 1940] |

## Candidate stint `Bishop, C. W. E___Hong Kong___1914`

- Staff-list name: **Bishop, C. W. E** | colony: **Hong Kong** | listed 1914–1915 | editions [1914, 1915]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1914 | Bishop | Assistant Mistress | Victoria British School | — | — |
| 1915 | Mrs. Bishop | Assistant Mistress | Victoria British School | — | — |

### Deterministic checks: `bishop_cecil-william-edwin_b1899` vs `Bishop, C. W. E___Hong Kong___1914`

- [PASS] surname_gate: bio 'BISHOP' vs stint 'Bishop, C. W. E' (exact)
- [PASS] initials: bio ['C', 'W', 'E'] ~ stint ['C', 'W', 'E']
- [PASS] age_gate: stint starts 1914, birth 1899 (age 15)
- [PASS] colony: 1 placed event(s) resolve to 'Hong Kong'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1914-1915
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Bishop, C. W. E___Hong Kong___1923`

- Staff-list name: **Bishop, C. W. E** | colony: **Hong Kong** | listed 1923–1940 | editions [1923, 1924, 1925, 1928, 1929, 1930, 1931, 1932, 1934, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1923 | C. W. E. Bishop | Engineers | General Staff | — | — |
| 1924 | C. W. E. Bishop | Engineers | General Staff | — | — |
| 1925 | C. W. Bishop | Engineers | Waterworks | — | — |
| 1928 | C. W. E. Bishop | Engineers | Waterworks | — | — |
| 1929 | C. W. E. Bishop | Engineers | Waterworks | — | — |
| 1930 | C. W. E. Bishop | Engineer | Waterworks | — | — |
| 1931 | C. W. E. Bishop | Engineer | Waterworks | — | — |
| 1932 | C.W.E. Bishop | Engineer | Public Works Department | — | — |
| 1934 | C. W. E. Bishop | Engineer | Public Works Department | — | — |
| 1937 | C. W. E. Bishop | Engineer | Public Works Department | — | — |
| 1939 | C. W. E. Bishop | Engineer | Public Works Department | — | — |
| 1940 | C. W. E. Bishop | Executive Engineers | Public Works Department | — | — |

### Deterministic checks: `bishop_cecil-william-edwin_b1899` vs `Bishop, C. W. E___Hong Kong___1923`

- [PASS] surname_gate: bio 'BISHOP' vs stint 'Bishop, C. W. E' (exact)
- [PASS] initials: bio ['C', 'W', 'E'] ~ stint ['C', 'W', 'E']
- [PASS] age_gate: stint starts 1923, birth 1899 (age 24)
- [PASS] colony: 1 placed event(s) resolve to 'Hong Kong'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1923-1940
- [FAIL] position_sim: best 50 vs bar 60: 'engr., P.W.D.' ~ 'Engineer'
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

