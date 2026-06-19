<!-- {"case_id": "case_carvell_frank-broadstreet_b1862", "bio_ids": ["carvell_frank-broadstreet_b1862"], "stint_ids": ["Carvell, Frank Broadstreet___Canada___1905", "Carvell, Frank Broadstreet___Canada___1918"]} -->
# Dossier case_carvell_frank-broadstreet_b1862

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `carvell_frank-broadstreet_b1862`

- Printed name: **CARVELL, Frank Broadstreet**
- Birth year: 1862 (attested in editions [1918, 1920, 1921, 1922, 1923, 1924])
- Honours: K.C., LL.B.
- Appears in editions: [1918, 1920, 1921, 1922, 1923, 1924]

### Verbatim printed entry text (OCR)

**Version `col1918-L49265.v` — printed in editions [1918, 1920, 1921, 1922, 1923, 1924]:**

> CARVELL, Hon. Frank Broadstreet, K.C., LL.B.—B. 1862; ed. New Brunswick pub. schls. and Boston Univ.; barrister; elected to legis. assem., N.B., 1899; resig. 1900 to contest Carleton Co. in federal g.e., unsuccessful; elected to H. of C., Canada, 1904; re-elected 1908, 1911, 1917; min. of pub. wks., Oct., 1917; ch. comsnr., bd. of rly. comsnrs., Aug., 1919.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1899 | elected to legis. assem. | New Brunswick | [1918, 1920, 1921, 1922, 1923, 1924] |
| 1 | 1900 | — | — | [1918, 1920, 1921, 1922, 1923, 1924] |
| 2 | 1904 | elected to H. of C. | Canada | [1918, 1920, 1921, 1922, 1923, 1924] |
| 3 | 1908–1917 | re-elected | — | [1918, 1920, 1921, 1922, 1923, 1924] |
| 4 | 1917 | min. of pub. wks. | — | [1918, 1920, 1921, 1922, 1923, 1924] |
| 5 | 1919 | ch. comsnr., bd. of rly. comsnrs. | — | [1918, 1920, 1921, 1922, 1923, 1924] |

## Candidate stint `Carvell, Frank Broadstreet___Canada___1905`

- Staff-list name: **Carvell, Frank Broadstreet** | colony: **Canada** | listed 1905–1908 | editions [1905, 1906, 1907, 1908]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | F. B. Carvell | — | — | — | — |
| 1906 | Frank Broadstreet Carvell | — | — | — | — |
| 1907 | Frank Broadstreet Carvell | — | Province of New Brunswick | — | — |
| 1908 | Frank Broadstreet Carvell | — | — | — | — |

### Deterministic checks: `carvell_frank-broadstreet_b1862` vs `Carvell, Frank Broadstreet___Canada___1905`

- [PASS] surname_gate: bio 'CARVELL' vs stint 'Carvell, Frank Broadstreet' (exact)
- [PASS] initials: bio ['F', 'B'] ~ stint ['F', 'B']
- [PASS] age_gate: stint starts 1905, birth 1862 (age 43)
- [PASS] colony: 2 placed event(s) resolve to 'Canada'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1905-1908
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Carvell, Frank Broadstreet___Canada___1918`

- Staff-list name: **Carvell, Frank Broadstreet** | colony: **Canada** | listed 1918–1922 | editions [1918, 1919, 1920, 1922]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1918 | Frank B. Carvell | Minister of Public Works | Public Works | — | — |
| 1918 | Frank Broadstreet Carvell | Minister of Public Works | The King's Privy Council for Canada | — | — |
| 1919 | Frank B. Carvell | Minister of Public Works | Public Works | — | — |
| 1919 | Frank Broadstreet Carvell | Minister of Public Works | Ministry | K.C. | — |
| 1920 | F. B. Carvell | Chief Commissioner | Permanent Railway Commission | — | — |
| 1922 | Frank Broadstreet Carvell | Privy Councillor | Privy Council | — | — |
| 1922 | F. B. Carvell | Chief Commissioner | Railway Commission | — | — |

### Deterministic checks: `carvell_frank-broadstreet_b1862` vs `Carvell, Frank Broadstreet___Canada___1918`

- [PASS] surname_gate: bio 'CARVELL' vs stint 'Carvell, Frank Broadstreet' (exact)
- [PASS] initials: bio ['F', 'B'] ~ stint ['F', 'B']
- [PASS] age_gate: stint starts 1918, birth 1862 (age 56)
- [PASS] colony: 2 placed event(s) resolve to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1918-1922
- [FAIL] position_sim: no overlapping placed event to compare
- [PASS] honour: shared: K.C.
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

