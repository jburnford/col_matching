<!-- {"case_id": "case_andrews_walter-reginald-nahum_b1900", "bio_ids": ["andrews_walter-reginald-nahum_b1900"], "stint_ids": ["Andrews, W. R. N___Hong Kong___1929"]} -->
# Dossier case_andrews_walter-reginald-nahum_b1900

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 65 official(s) with this surname in the graph's staff lists; 15 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `andrews_walter-reginald-nahum_b1900`

- Printed name: **ANDREWS, Walter Reginald Nahum**
- Birth year: 1900 (attested in editions [1951])
- Appears in editions: [1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1951-L35703.v` — printed in editions [1951]:**

> ANDREWS, Walter Reginald Nahum.—b. 1900; ed. Edward Worlidge Sch., Gt. Yarmouth; on mil. serv., 1940-45, lieut.; P.C., H.K., 1919; 2nd and 1st cl. overseer, P.W.D., 1920; S.C. and A.S., cl. II, 1928; cl. I, 1935; spl. cl., 1946; senr. exec. offr., cl. II, 1947.

**Version `col1950-L33237.v` — printed in editions [1950]:**

> ANDREWS, Walter Reginald Nahum.—b. 1900; ed. Worlledge Sch., Gt. Yarmouth; on mil. serv., 1941–45, lieut.; P.C., H.K., 1919; senr. exec. offr., cl. II, 1947; cust. of property, 1948.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1919 | P.C. | Hong Kong | [1950, 1951] |
| 1 | 1920 | 2nd and 1st cl. overseer, P.W.D | Hong Kong *(inherited from previous clause)* | [1951] |
| 2 | 1928 | S.C. and A.S., cl. II | Hong Kong *(inherited from previous clause)* | [1951] |
| 3 | 1935 | cl. I | Hong Kong *(inherited from previous clause)* | [1951] |
| 4 | 1946 | spl. cl | Hong Kong *(inherited from previous clause)* | [1951] |
| 5 | 1947 | senr. exec. offr., cl. II | Hong Kong *(inherited from previous clause)* | [1950, 1951] |
| 6 | 1948 | cust. of property | Hong Kong *(inherited from previous clause)* | [1950] |

## Candidate stint `Andrews, W. R. N___Hong Kong___1929`

- Staff-list name: **Andrews, W. R. N** | colony: **Hong Kong** | listed 1929–1939 | editions [1929, 1930, 1931, 1932, 1933, 1934, 1936, 1937, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1929 | W. R. Andrews | Deputy Registrar and Appraiser, Accountant | Supreme Court | — | — |
| 1930 | W. R. N. Andrews | Accountant | Supreme Court | — | — |
| 1931 | W. R. N. Andrews | Accountant | Supreme Court | — | — |
| 1932 | W. R. N. Andrews | Accountant | Supreme Court | — | — |
| 1933 | W. R. N. Andrews | Accountant | Supreme Court | — | — |
| 1934 | W. R. N. Andrews | Accountant | Supreme Court | — | — |
| 1936 | W. R. N. Andrews | Accountant | Supreme Court | — | — |
| 1937 | W. R. N. Andrews | Accountant | Supreme Court | — | — |
| 1939 | W. R. N. Andrews | Chief Accountant | Kowloon-Canton Railway | — | — |

### Deterministic checks: `andrews_walter-reginald-nahum_b1900` vs `Andrews, W. R. N___Hong Kong___1929`

- [PASS] surname_gate: bio 'ANDREWS' vs stint 'Andrews, W. R. N' (exact)
- [PASS] initials: bio ['W', 'R', 'N'] ~ stint ['W', 'R', 'N']
- [PASS] age_gate: stint starts 1929, birth 1900 (age 29)
- [PASS] colony: 7 placed event(s) resolve to 'Hong Kong'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1929-1939
- [FAIL] position_sim: best 39 vs bar 60: 'S.C. and A.S., cl. II' ~ 'Chief Accountant'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

