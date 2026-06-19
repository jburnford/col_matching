<!-- {"case_id": "case_henri_joseph-paul_b1895", "bio_ids": ["henri_joseph-paul_b1895"], "stint_ids": ["Henri, P___Mauritius___1918"]} -->
# Dossier case_henri_joseph-paul_b1895

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Henri, P___Mauritius___1918` is also gate-compatible with biography(ies) outside this case: ['henri_paul_e1928'] (already linked elsewhere or filtered).

## Biography `henri_joseph-paul_b1895`

- Printed name: **HENRI, Joseph Paul**
- Birth year: 1895 (attested in editions [1949, 1951])
- Honours: O.B.E
- Appears in editions: [1949, 1951]

### Verbatim printed entry text (OCR)

**Version `col1949-L32826.v` — printed in editions [1949, 1951]:**

> HENRI, Joseph Paul, O.B.E., B.Sc. (hons. Lond.).—b. 1895; ed. Royal Coll., Maur. and Univ. of Lond. (external student), dip. educ. (Lond.) ; clk., Maur., 1916; asst. mstr., Royal Coll., 1921; mstr., Royal Coll., 1925; supt. schls., 1933; dep. dir. of educ., 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1916 | clk. | Mauritius | [1949, 1951] |
| 1 | 1921 | asst. mstr., Royal Coll | Mauritius *(inherited from previous clause)* | [1949, 1951] |
| 2 | 1925 | mstr., Royal Coll | Mauritius *(inherited from previous clause)* | [1949, 1951] |
| 3 | 1933 | supt. schls | Mauritius *(inherited from previous clause)* | [1949, 1951] |
| 4 | 1946 | dep. dir. of educ | Mauritius *(inherited from previous clause)* | [1949, 1951] |

## Candidate stint `Henri, P___Mauritius___1918`

- Staff-list name: **Henri, P** | colony: **Mauritius** | listed 1918–1939 | editions [1918, 1919, 1920, 1921, 1923, 1925, 1927, 1928, 1929, 1931, 1932, 1936, 1937, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1918 | P. Henri | 6th Class Clerk | Clerical Staff | — | — |
| 1919 | P. Henri | 6th Class Clerk | Clerical Staff | — | — |
| 1919 | P. Henri | Seconded for War Service | Savings Bank | — | — |
| 1920 | P. Henri | 6th Class Clerk | Clerical Staff | — | — |
| 1921 | P. Henri | 6th Class Clerk | Clerical Staff | — | — |
| 1923 | P. Henri | Assistant Masters | Education | — | — |
| 1925 | P. Henri | Assistant Masters | Education | — | — |
| 1927 | P. Henri | Masters | Education | — | — |
| 1928 | P. Henri | Masters | Education | — | — |
| 1929 | P. Henri | Masters | Education | — | — |
| 1931 | P. Henri | Masters | Education | — | — |
| 1932 | P. Henri | Masters | Education | — | — |
| 1936 | P. Henri | Superintendent of Schools | Education | — | — |
| 1937 | P. Henri | Superintendent of Schools | Government Schools | — | — |
| 1939 | P. Henri | Superintendent of Schools | Government Schools | — | — |

### Deterministic checks: `henri_joseph-paul_b1895` vs `Henri, P___Mauritius___1918`

- [PASS] surname_gate: bio 'HENRI' vs stint 'Henri, P' (exact)
- [PASS] initials: bio ['J', 'P'] ~ stint ['P']
- [PASS] age_gate: stint starts 1918, birth 1895 (age 23)
- [PASS] colony: 5 placed event(s) resolve to 'Mauritius'
- [PASS] tenure_overlap: 4 event tenure(s) overlap stint years 1918-1939
- [FAIL] position_sim: best 57 vs bar 60: 'supt. schls' ~ 'Superintendent of Schools'
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

