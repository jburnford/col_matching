<!-- {"case_id": "case_farquhar_frederick-colin_b1884", "bio_ids": ["farquhar_frederick-colin_b1884"], "stint_ids": ["Farquhar, F. C___Nigeria___1923"]} -->
# Dossier case_farquhar_frederick-colin_b1884

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 10 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `farquhar_frederick-colin_b1884`

- Printed name: **FARQUHAR, FREDERICK COLIN**
- Birth year: 1884 (attested in editions [1931, 1932, 1933])
- Appears in editions: [1931, 1932, 1933]

### Verbatim printed entry text (OCR)

**Version `col1931-L64122.v` — printed in editions [1931, 1932, 1933]:**

> FARQUHAR, FREDERICK COLIN.—B. 1884; asst. acct., P.W.D., S. Nigeria, 1910; acct., 1911; ch. acct., P.W.D., Nigeria, 1923; transf. treasy., as senr. acct. treasy., 1924; ag. dep. treasy. in 1928.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1910 | asst. acct., P.W.D. | Southern Nigeria | [1931, 1932, 1933] |
| 1 | 1911 | acct | Southern Nigeria *(inherited from previous clause)* | [1931, 1932, 1933] |
| 2 | 1923 | ch. acct., P.W.D. | Nigeria | [1931, 1932, 1933] |
| 3 | 1924 | transf. treasy., as senr. acct. treasy | Nigeria *(inherited from previous clause)* | [1931, 1932, 1933] |
| 4 | 1928 | ag. dep. treasy. in | Nigeria *(inherited from previous clause)* | [1931, 1932, 1933] |

## Candidate stint `Farquhar, F. C___Nigeria___1923`

- Staff-list name: **Farquhar, F. C** | colony: **Nigeria** | listed 1923–1933 | editions [1923, 1925, 1927, 1928, 1929, 1930, 1933]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1923 | F. C. Farquhar | Accountant | Public Works | — | — |
| 1925 | F. C. Farquhar | Senior Assistant Treasurer | Treasury | — | — |
| 1927 | F. C. Farquhar | Senior Assistant Treasurer | Treasury | — | — |
| 1928 | F. C. Farquhar | Senior Assistant Treasurer | Treasury | — | — |
| 1929 | F. C. Farquhar | Senior Assistant Treasurers | Treasury | — | — |
| 1930 | F. C. Farquhar | Senior Assistant Treasurer | Treasury | — | — |
| 1933 | F. C. Farquhar | Senior Assistant Treasurer | Treasury | — | — |

### Deterministic checks: `farquhar_frederick-colin_b1884` vs `Farquhar, F. C___Nigeria___1923`

- [PASS] surname_gate: bio 'FARQUHAR' vs stint 'Farquhar, F. C' (exact)
- [PASS] initials: bio ['F', 'C'] ~ stint ['F', 'C']
- [PASS] age_gate: stint starts 1923, birth 1884 (age 39)
- [PASS] colony: 5 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 4 event tenure(s) overlap stint years 1923-1933
- [PASS] position_sim: best 60 vs bar 60: 'transf. treasy., as senr. acct. treasy' ~ 'Senior Assistant Treasurers'
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

