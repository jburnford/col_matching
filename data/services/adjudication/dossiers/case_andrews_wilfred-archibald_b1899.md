<!-- {"case_id": "case_andrews_wilfred-archibald_b1899", "bio_ids": ["andrews_wilfred-archibald_b1899"], "stint_ids": ["Andrews, W. A___Kenya___1922"]} -->
# Dossier case_andrews_wilfred-archibald_b1899

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 65 official(s) with this surname in the graph's staff lists; 15 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `andrews_wilfred-archibald_b1899`

- Printed name: **ANDREWS, Wilfred Archibald**
- Birth year: 1899 (attested in editions [1949, 1950, 1951])
- Appears in editions: [1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1949-L30072.v` — printed in editions [1949, 1950, 1951]:**

> ANDREWS, Wilfred Archibald.—b. 1899; inspr., Ken. and Uga. posts and tels. dept., 1923; sub-engr., Ken., Uga. and T.T., 1934; asst. engr. (later, posts and tels., E.A.), 1947.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1923 | inspr., Ken. and Uga. posts and tels. dept | Kenya | [1949, 1950, 1951] |
| 1 | 1934 | sub-engr., Ken., Uga. and T.T | Uganda | [1949, 1950, 1951] |
| 2 | 1947 | asst. engr. (later, posts and tels., E.A.) | Uganda *(inherited from previous clause)* | [1949, 1950, 1951] |

## Candidate stint `Andrews, W. A___Kenya___1922`

- Staff-list name: **Andrews, W. A** | colony: **Kenya** | listed 1922–1932 | editions [1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1932]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | W. A. Andrews | Assistant Carriage and Wagon Superintendent | Locomotive, Carriage and Wagon Department | — | — |
| 1923 | W. A. Andrews | Assistant Carriage and Wagon Superintendent | Locomotive, Carriage and Wagon Department | — | — |
| 1924 | W. A. Andrews | Assistant Carriage and Wagon Superintendent | Locomotive, Carriage and Wagon Department | — | — |
| 1925 | W. A. Andrews | Assistant Works Manager | Locomotive, Carriage and Wagon Department | — | — |
| 1927 | W. A. Andrews | 2nd Class Telegraph Inspectors | Engineering Staff | — | — |
| 1927 | W. A. Andrews | Assistant Workshop Manager | Locomotive, Carriage and Wayon Department | — | — |
| 1928 | W. A. Andrews | 2nd Class Telegraph Inspectors | Engineering Staff | — | — |
| 1929 | W. A. Andrews | Telegraph Inspectors | Engineering Staff | — | — |
| 1930 | W. A. Andrews | Telegraph Inspectors | Posts and Telegraphs Department | — | — |
| 1932 | W. A. Andrews | Telegraph Inspectors | Posts and Telegraphs Department | — | — |
| 1932 | W. A. Andrews | Works Manager | Railways and Harbours | — | — |

### Deterministic checks: `andrews_wilfred-archibald_b1899` vs `Andrews, W. A___Kenya___1922`

- [PASS] surname_gate: bio 'ANDREWS' vs stint 'Andrews, W. A' (exact)
- [PASS] initials: bio ['W', 'A'] ~ stint ['W', 'A']
- [PASS] age_gate: stint starts 1922, birth 1899 (age 23)
- [PASS] colony: 1 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1922-1932
- [FAIL] position_sim: best 54 vs bar 60: 'inspr., Ken. and Uga. posts and tels. dept' ~ '2nd Class Telegraph Inspectors'
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

