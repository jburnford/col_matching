<!-- {"case_id": "case_bush_francis-john_b1896", "bio_ids": ["bush_francis-john_b1896"], "stint_ids": ["Bush, F. J___Gold Coast___1924", "Bush, F. J___Gold Coast___1932", "Bush, F. J___Sierra Leone___1921"]} -->
# Dossier case_bush_francis-john_b1896

## Case context

- 1 biography(ies) and 3 candidate stint(s) are entangled in this case.
- Corpus context: 11 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `bush_francis-john_b1896`

- Printed name: **BUSH, Francis John**
- Birth year: 1896 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L31542.v` — printed in editions [1948, 1949, 1950, 1951]:**

> BUSH, Francis John.—b. 1896; ed. King Edward VII Gram. Sch., King's Lynn; on mil. serv. 1914-19; asst. traff. supt., govt. rlwy., S.L., 1920; asst. sec. rlwys., G.C., 1923; sec. to gen. man., 1926; redesig. asst. to gen. man., 1932.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1920 | asst. traff. supt., govt. rlwy. | Sierra Leone | [1948, 1949, 1950, 1951] |
| 1 | 1923 | asst. sec. rlwys. | Gold Coast | [1948, 1949, 1950, 1951] |
| 2 | 1926 | sec. to gen. man | Gold Coast *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 3 | 1932 | redesig. asst. to gen. man | Gold Coast *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Bush, F. J___Gold Coast___1924`

- Staff-list name: **Bush, F. J** | colony: **Gold Coast** | listed 1924–1927 | editions [1924, 1927]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1924 | F. J. Bush | Assistant Secretary | Railway Department | — | — |
| 1927 | F. J. Bush | Secretary to General Manager | Railway Department | — | — |

### Deterministic checks: `bush_francis-john_b1896` vs `Bush, F. J___Gold Coast___1924`

- [PASS] surname_gate: bio 'BUSH' vs stint 'Bush, F. J' (exact)
- [PASS] initials: bio ['F', 'J'] ~ stint ['F', 'J']
- [PASS] age_gate: stint starts 1924, birth 1896 (age 28)
- [PASS] colony: 3 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1924-1927
- [PASS] position_sim: best 67 vs bar 60: 'sec. to gen. man' ~ 'Secretary to General Manager'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Bush, F. J___Gold Coast___1932`

- Staff-list name: **Bush, F. J** | colony: **Gold Coast** | listed 1932–1936 | editions [1932, 1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1932 | F. J. Bush | Secretary to General Manager | Railway and Harbour Department | — | — |
| 1934 | F. J. Bush | Assistant to General Manager | Railway and Harbour Department | — | — |
| 1936 | F. J. Bush | Assistant to General Manager | Railway and Harbour Department | — | — |

### Deterministic checks: `bush_francis-john_b1896` vs `Bush, F. J___Gold Coast___1932`

- [PASS] surname_gate: bio 'BUSH' vs stint 'Bush, F. J' (exact)
- [PASS] initials: bio ['F', 'J'] ~ stint ['F', 'J']
- [PASS] age_gate: stint starts 1932, birth 1896 (age 36)
- [PASS] colony: 3 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1932-1936
- [PASS] position_sim: best 67 vs bar 60: 'sec. to gen. man' ~ 'Secretary to General Manager'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

## Candidate stint `Bush, F. J___Sierra Leone___1921`

- Staff-list name: **Bush, F. J** | colony: **Sierra Leone** | listed 1921–1922 | editions [1921, 1922]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1921 | F. J. Bush | Assistant Traffic Superintendent | Railway Department | — | — |
| 1922 | F. J. Bush | Assistant Traffic Superintendent | Railway Department | — | — |

### Deterministic checks: `bush_francis-john_b1896` vs `Bush, F. J___Sierra Leone___1921`

- [PASS] surname_gate: bio 'BUSH' vs stint 'Bush, F. J' (exact)
- [PASS] initials: bio ['F', 'J'] ~ stint ['F', 'J']
- [PASS] age_gate: stint starts 1921, birth 1896 (age 25)
- [PASS] colony: 1 placed event(s) resolve to 'Sierra Leone'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1921-1922
- [FAIL] position_sim: best 56 vs bar 60: 'asst. traff. supt., govt. rlwy.' ~ 'Assistant Traffic Superintendent'
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

