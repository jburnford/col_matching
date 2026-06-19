<!-- {"case_id": "case_carter_john-lionel_b1900", "bio_ids": ["carter_john-lionel_b1900"], "stint_ids": ["Carter, J. L___Kenya___1929", "Carter, J___Uganda___1920"]} -->
# Dossier case_carter_john-lionel_b1900

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 80 official(s) with this surname in the graph's staff lists; 31 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `carter_john-lionel_b1900`

- Printed name: **CARTER, John Lionel**
- Birth year: 1900 (attested in editions [1948, 1949, 1950, 1951])
- Honours: C.P.M (1949)
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L31663.v` — printed in editions [1948, 1949, 1950, 1951]:**

> CARTER, John Lionel, C.P.M. (1949).—b. 1900; ed. Kingston Gram. Sch.; police const., Ken., 1925; asst. inspr., 1927; inspr., 1938; asst. supt., 1940; G.C., 1948; supt., 1950.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1925 | police const. | Kenya | [1948, 1949, 1950, 1951] |
| 1 | 1927 | asst. inspr | Kenya *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 2 | 1938 | inspr | Kenya *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 3 | 1940 | asst. supt | Kenya *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 4 | 1948 | asst. supt | Gold Coast | [1948, 1949, 1950, 1951] |
| 5 | 1950 | supt | Gold Coast *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Carter, J. L___Kenya___1929`

- Staff-list name: **Carter, J. L** | colony: **Kenya** | listed 1929–1930 | editions [1929, 1930]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1929 | J. L. Carter | Assistant Inspector | Police Department | — | — |
| 1930 | J. L. Carter | Assistant Inspector | Police Department | — | — |

### Deterministic checks: `carter_john-lionel_b1900` vs `Carter, J. L___Kenya___1929`

- [PASS] surname_gate: bio 'CARTER' vs stint 'Carter, J. L' (exact)
- [PASS] initials: bio ['J', 'L'] ~ stint ['J', 'L']
- [PASS] age_gate: stint starts 1929, birth 1900 (age 29)
- [PASS] colony: 4 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1929-1930
- [PASS] position_sim: best 69 vs bar 60: 'asst. inspr' ~ 'Assistant Inspector'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

## Candidate stint `Carter, J___Uganda___1920`

- Staff-list name: **Carter, J** | colony: **Uganda** | listed 1920–1940 | editions [1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1933, 1936, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1920 | J. Carter | Road Foreman | Public Works | — | — |
| 1921 | J. Carter | Road Foreman | Public Works | — | — |
| 1922 | J. Carter | Foreman | Public Works | — | — |
| 1923 | J. Carter | Foreman | Public Works | — | — |
| 1924 | J. Carter | Foreman | Public Works | — | — |
| 1925 | J. Carter | Foreman | Public Works | — | — |
| 1927 | J. Carter | Foreman | Public Works | — | — |
| 1928 | J. Carter | Foreman | Public Works | — | — |
| 1929 | J. Carter | Road Foreman | Public Works | — | — |
| 1930 | J. Carter | Road Foreman | Police and Prisons | — | — |
| 1933 | J. Carter | Assistant Storekeeper | Public Works Department | — | — |
| 1936 | J. Carter | Assistant Storekeeper | Public Works Department | — | — |
| 1939 | J. Carter | Assistant Storekeeper | Public Works Department | — | — |
| 1940 | J. Carter | Assistant Storekeeper | Public Works Department | — | — |

### Deterministic checks: `carter_john-lionel_b1900` vs `Carter, J___Uganda___1920`

- [PASS] surname_gate: bio 'CARTER' vs stint 'Carter, J' (exact)
- [PASS] initials: bio ['J', 'L'] ~ stint ['J']
- [PASS] age_gate: stint starts 1920, birth 1900 (age 20)
- [FAIL] colony: no placed event resolves to 'Uganda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1920-1940
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

