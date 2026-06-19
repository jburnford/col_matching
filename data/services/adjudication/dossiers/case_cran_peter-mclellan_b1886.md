<!-- {"case_id": "case_cran_peter-mclellan_b1886", "bio_ids": ["cran_peter-mclellan_b1886"], "stint_ids": ["Cran, P. M___Sierra Leone___1929", "Cran, P.M___Cyprus___1934"]} -->
# Dossier case_cran_peter-mclellan_b1886

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `cran_peter-mclellan_b1886`

- Printed name: **CRAN, PETER MCLELLAN**
- Birth year: 1886 (attested in editions [1936, 1937, 1940])
- Honours: O.B.E
- Appears in editions: [1936, 1937, 1940]

### Verbatim printed entry text (OCR)

**Version `col1936-L59987.v` — printed in editions [1936, 1937, 1940]:**

> CRAN, CAPT. PETER MCLELLAN, O.B.E., B.Sc., M.Inst.C.E.—B. 1886; ed. George Watson's Coll., Edin. and Edin. Univ.; 2nd lieut. R.E. (S.R.), 1911; ast. engrnr., govt. rlys., N. Nigeria, 1911; dist. engrnr., P.W.D., Gold Coast, 1912; ast. div. offr., R.E., Forth and Clyde Defences, Scottish Comd., Mar., 1914; div. offr., do., Oct., 1914; ast. to cmdng. royal engrnr., do., Nov., 1916; ment. in desps., Feb., 1917 and Aug., 1919; exec. engrnr., P.W.D., Sierra Leone, 1928; temp. ast. engrnr., P.W.D., Cyprus, Jan., 1931; divnl. engrnr., Mar., 1931; title changed to exec. engrnr., Jan., 1939.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1911 | 2nd lieut. R.E. (S.R.) | — | [1936, 1937, 1940] |
| 1 | 1911 | ast. engrnr., govt. rlys., N. Nigeria | — | [1936, 1937, 1940] |
| 2 | 1912 | dist. engrnr., P.W.D. | Gold Coast | [1936, 1937, 1940] |
| 3 | 1914 | ast. div. offr., R.E., Forth and Clyde Defences, Scottish Comd | Dominions Office | [1936, 1937, 1940] |
| 4 | 1916 | ast. to cmdng. royal engrnr. | Dominions Office | [1936, 1937, 1940] |
| 5 | 1917 | ment. in desps | Dominions Office *(inherited from previous clause)* | [1936, 1937, 1940] |
| 6 | 1919 | ment. in desps | Dominions Office *(inherited from previous clause)* | [1936, 1937, 1940] |
| 7 | 1928 | exec. engrnr., P.W.D. | Sierra Leone | [1936, 1937, 1940] |
| 8 | 1931 | temp. ast. engrnr., P.W.D. | Cyprus | [1936, 1937, 1940] |
| 9 | 1939 | title changed to exec. engrnr | Cyprus *(inherited from previous clause)* | [1936, 1937, 1940] |

## Candidate stint `Cran, P. M___Sierra Leone___1929`

- Staff-list name: **Cran, P. M** | colony: **Sierra Leone** | listed 1929–1931 | editions [1929, 1930, 1931]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1929 | P. M. Cran | Executive Engineer, Grade 2 | Public Works Department | — | — |
| 1930 | P. M. Cran | Executive Engineers, Grade 2 | Public Works Department | — | — |
| 1931 | P. M. Cran | Executive Engineer, Grade 2 | Public Works Department | — | — |

### Deterministic checks: `cran_peter-mclellan_b1886` vs `Cran, P. M___Sierra Leone___1929`

- [PASS] surname_gate: bio 'CRAN' vs stint 'Cran, P. M' (exact)
- [PASS] initials: bio ['P', 'M'] ~ stint ['P', 'M']
- [PASS] age_gate: stint starts 1929, birth 1886 (age 43)
- [PASS] colony: 1 placed event(s) resolve to 'Sierra Leone'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1929-1931
- [FAIL] position_sim: best 59 vs bar 60: 'exec. engrnr., P.W.D.' ~ 'Executive Engineer, Grade 2'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Cran, P.M___Cyprus___1934`

- Staff-list name: **Cran, P.M** | colony: **Cyprus** | listed 1934–1939 | editions [1934, 1936, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | P. M Cran | Engineer | Public Works Department | — | — |
| 1936 | P.M. Cran | Engineer | Public Works Department | — | — |
| 1939 | P. M. Cran | Divisional Engineer | Public Works Department | — | — |

### Deterministic checks: `cran_peter-mclellan_b1886` vs `Cran, P.M___Cyprus___1934`

- [PASS] surname_gate: bio 'CRAN' vs stint 'Cran, P.M' (exact)
- [PASS] initials: bio ['P', 'M'] ~ stint ['P', 'M']
- [PASS] age_gate: stint starts 1934, birth 1886 (age 48)
- [PASS] colony: 2 placed event(s) resolve to 'Cyprus'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1934-1939
- [FAIL] position_sim: best 37 vs bar 60: 'temp. ast. engrnr., P.W.D.' ~ 'Engineer'
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

