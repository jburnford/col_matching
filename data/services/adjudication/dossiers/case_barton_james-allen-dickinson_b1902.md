<!-- {"case_id": "case_barton_james-allen-dickinson_b1902", "bio_ids": ["barton_james-allen-dickinson_b1902"], "stint_ids": ["Barton, J. A. D___Gibraltar___1949", "Barton, J. A. D___Gibraltar___1961", "Barton, J. A. D___Sierra Leone___1939"]} -->
# Dossier case_barton_james-allen-dickinson_b1902

## Case context

- 1 biography(ies) and 3 candidate stint(s) are entangled in this case.
- Corpus context: 39 official(s) with this surname in the graph's staff lists; 23 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `barton_james-allen-dickinson_b1902`

- Printed name: **BARTON, James Allen Dickinson**
- Birth year: 1902 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L31011.v` — printed in editions [1948, 1949, 1950, 1951]:**

> BARTON, James Allen Dickinson.—b. 1902; ed. Arnold Sch., Blackpool; chrted. acctnt.; apptd. to gov't. of Iraq, 1927; gov't. of S.L., 1936; Gib., 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1927 | apptd. to gov't. of Iraq | — | [1948, 1949, 1950, 1951] |
| 1 | 1936 | gov't. of S.L | — | [1948, 1949, 1950, 1951] |
| 2 | 1946 | gov't. of S.L | Gibraltar | [1948, 1949, 1950, 1951] |

## Candidate stint `Barton, J. A. D___Gibraltar___1949`

- Staff-list name: **Barton, J. A. D** | colony: **Gibraltar** | listed 1949–1952 | editions [1949, 1950, 1951, 1952]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | J. A. D. Barton | Income Tax Officer | Revenue | — | — |
| 1950 | J. A. D. Barton | Income Tax Officer | Revenue | — | — |
| 1951 | J. A. D. Barton | Income Tax Officer | Revenue | — | — |
| 1952 | J. A. D. Barton | Taxation Officer | Civil Establishment | — | — |

### Deterministic checks: `barton_james-allen-dickinson_b1902` vs `Barton, J. A. D___Gibraltar___1949`

- [PASS] surname_gate: bio 'BARTON' vs stint 'Barton, J. A. D' (exact)
- [PASS] initials: bio ['J', 'A', 'D'] ~ stint ['J', 'A', 'D']
- [PASS] age_gate: stint starts 1949, birth 1902 (age 47)
- [PASS] colony: 1 placed event(s) resolve to 'Gibraltar'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1952
- [FAIL] position_sim: best 36 vs bar 60: 'gov't. of S.L' ~ 'Income Tax Officer'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Barton, J. A. D___Gibraltar___1961`

- Staff-list name: **Barton, J. A. D** | colony: **Gibraltar** | listed 1961–1962 | editions [1961, 1962]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1961 | J. A. D. Barton | Deputy Commissioner of Income Tax | Civil Establishment | — | — |
| 1962 | J. A. D. Barton | Deputy Commissioner of Income Tax | Civil Establishment | — | — |

### Deterministic checks: `barton_james-allen-dickinson_b1902` vs `Barton, J. A. D___Gibraltar___1961`

- [PASS] surname_gate: bio 'BARTON' vs stint 'Barton, J. A. D' (exact)
- [PASS] initials: bio ['J', 'A', 'D'] ~ stint ['J', 'A', 'D']
- [PASS] age_gate: stint starts 1961, birth 1902 (age 59)
- [PASS] colony: 1 placed event(s) resolve to 'Gibraltar'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1961-1962
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Barton, J. A. D___Sierra Leone___1939`

- Staff-list name: **Barton, J. A. D** | colony: **Sierra Leone** | listed 1939–1940 | editions [1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | J. A. D. Barton | Assistant Treasurer | Treasury Department | — | — |
| 1940 | J. A. D. Barton | Assistant Treasurer | Treasury Department | — | — |

### Deterministic checks: `barton_james-allen-dickinson_b1902` vs `Barton, J. A. D___Sierra Leone___1939`

- [PASS] surname_gate: bio 'BARTON' vs stint 'Barton, J. A. D' (exact)
- [PASS] initials: bio ['J', 'A', 'D'] ~ stint ['J', 'A', 'D']
- [PASS] age_gate: stint starts 1939, birth 1902 (age 37)
- [FAIL] colony: no placed event resolves to 'Sierra Leone'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1939-1940
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

