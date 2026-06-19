<!-- {"case_id": "case_parks_william-john_b1909", "bio_ids": ["parks_william-john_b1909"], "stint_ids": ["Parks, W. J___Singapore___1949", "Parks, W. J___Straits Settlements___1931"]} -->
# Dossier case_parks_william-john_b1909

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `parks_william-john_b1909`

- Printed name: **PARKS, William John**
- Birth year: 1909 (attested in editions [1956, 1957, 1958, 1959])
- Honours: K.P.M (1949)
- Appears in editions: [1950, 1951, 1956, 1957, 1958, 1959]

### Verbatim printed entry text (OCR)

**Version `col1956-L23411.v` — printed in editions [1956, 1957, 1958, 1959]:**

> PARKS, W. J., K.P.M. (1949).—b. 1909; ed. Cheltenham Coll.; interned, 1942-45; police probr., S.S., 1928; asst. supt., police, 1932; a.d.c. to gov., S.S., 1935; chief police offr., Muar, 1941; comdt., training sch., S'pore, 1946; supt., police, 1946; asst. comsnr., 1949; senr. asst. comsnr., police, 1953-58.

**Version `col1950-L38566.v` — printed in editions [1950, 1951]:**

> PARKS, William John, K.P.M.—b. 1909; ed. Cheltenham Coll.; interned, 1942-45; police probr., S.S., 1928; asst. supt., 1932; a.d.c. to gov., 1935; ch. pol. offr., Maur., 1941; comdt., training sch., S'pore., 1946; supt., police, 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | police probr. | Straits Settlements | [1950, 1951, 1956, 1957, 1958, 1959] |
| 1 | 1932 | asst. supt., police | Straits Settlements *(inherited from previous clause)* | [1950, 1951, 1956, 1957, 1958, 1959] |
| 2 | 1935 | a.d.c. to gov. | Straits Settlements | [1950, 1951, 1956, 1957, 1958, 1959] |
| 3 | 1941 | chief police offr., Muar | Straits Settlements *(inherited from previous clause)* | [1956, 1957, 1958, 1959] |
| 4 | 1941 | ch. pol. offr. | Mauritius | [1950, 1951] |
| 5 | 1942–1945 | interned | — | [1950, 1951, 1956, 1957, 1958, 1959] |
| 6 | 1946 | comdt., training sch., S'pore | Straits Settlements *(inherited from previous clause)* | [1950, 1951, 1956, 1957, 1958, 1959] |
| 7 | 1946 | supt., police | Mauritius *(inherited from previous clause)* | [1950, 1951] |
| 8 | 1949 | asst. comsnr | Straits Settlements *(inherited from previous clause)* | [1956, 1957, 1958, 1959] |
| 9 | 1953–1958 | senr. asst. comsnr., police | Straits Settlements *(inherited from previous clause)* | [1956, 1957, 1958, 1959] |

## Candidate stint `Parks, W. J___Singapore___1949`

- Staff-list name: **Parks, W. J** | colony: **Singapore** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | W. J. Parks | Superintendents of Police | Police | — | — |
| 1951 | W. J. Parks | Deputy Commissioners of Police | Police | — | — |

### Deterministic checks: `parks_william-john_b1909` vs `Parks, W. J___Singapore___1949`

- [PASS] surname_gate: bio 'PARKS' vs stint 'Parks, W. J' (exact)
- [PASS] initials: bio ['W', 'J'] ~ stint ['W', 'J']
- [PASS] age_gate: stint starts 1949, birth 1909 (age 40)
- [FAIL] colony: no placed event resolves to 'Singapore'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Parks, W. J___Straits Settlements___1931`

- Staff-list name: **Parks, W. J** | colony: **Straits Settlements** | listed 1931–1936 | editions [1931, 1933, 1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | W. J. Parks | Probationer | Police | — | — |
| 1933 | W. J. Parks | Assistant Superintendent | Police | — | — |
| 1934 | W. J. Parks | Assistant Superintendents | Police | — | — |
| 1936 | W. J. Parks | Assistant Superintendent | Police | — | — |

### Deterministic checks: `parks_william-john_b1909` vs `Parks, W. J___Straits Settlements___1931`

- [PASS] surname_gate: bio 'PARKS' vs stint 'Parks, W. J' (exact)
- [PASS] initials: bio ['W', 'J'] ~ stint ['W', 'J']
- [PASS] age_gate: stint starts 1931, birth 1909 (age 22)
- [PASS] colony: 7 placed event(s) resolve to 'Straits Settlements'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1931-1936
- [FAIL] position_sim: best 45 vs bar 60: 'asst. supt., police' ~ 'Assistant Superintendent'
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

