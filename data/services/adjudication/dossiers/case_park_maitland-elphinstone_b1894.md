<!-- {"case_id": "case_park_maitland-elphinstone_b1894", "bio_ids": ["park_maitland-elphinstone_b1894"], "stint_ids": ["Park, M___Ceylon___1925", "Park, M___Leeward Islands___1955"]} -->
# Dossier case_park_maitland-elphinstone_b1894

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 17 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Park, M___Ceylon___1925` is also gate-compatible with biography(ies) outside this case: ['park_m_b1900'] (already linked elsewhere or filtered).
- NOTE: stint `Park, M___Leeward Islands___1955` is also gate-compatible with biography(ies) outside this case: ['park_m_b1900'] (already linked elsewhere or filtered).

## Biography `park_maitland-elphinstone_b1894`

- Printed name: **PARK, MAITLAND ELPHINSTONE**
- Birth year: 1894 (attested in editions [1927, 1928, 1929])
- Honours: D.S.O
- Appears in editions: [1927, 1928, 1929]

### Verbatim printed entry text (OCR)

**Version `col1927-L61853.v` — printed in editions [1927, 1928, 1929]:**

> PARK, MAITLAND ELPHINSTONE, D.S.O.—B. 1894; capt., reg. army R. of O.; ed., S.A. Coll. Schl. and Magdalen Coll., Oxford; univ. comn't. mily. serv., 1914-25; D.S.O., 1915; capt., 1916; Italian silver med., 1917; twice ment. in desps.; cadet, admstve. dept., Tanganyika Territory, 17th Aug., 1926.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914–1925 | univ. comn't. mily. serv | — | [1927, 1928, 1929] |
| 1 | 1915 | D.S.O | — | [1927, 1928, 1929] |
| 2 | 1916 | capt | — | [1927, 1928, 1929] |
| 3 | 1917 | Italian silver med | — | [1927, 1928, 1929] |
| 4 | 1926 | cadet, admstve. dept., Tanganyika Territory | Tanganyika | [1927, 1928, 1929] |

## Candidate stint `Park, M___Ceylon___1925`

- Staff-list name: **Park, M** | colony: **Ceylon** | listed 1925–1940 | editions [1925, 1927, 1928, 1929, 1931, 1934, 1936, 1937, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1925 | M. Park | Assistant Mycologist | Department of Agriculture | — | — |
| 1927 | M. Park | Assistant Mycologist | Research Branch | — | — |
| 1928 | M. Park | Assistant Mycologist | Department of Agriculture | — | — |
| 1929 | M. Park | Assistant Mycologist | Research Branch | — | — |
| 1931 | M. Park | Assistant Mycologist | Research Branch | — | — |
| 1934 | M. Park | Mycologist | Department of Agriculture | — | — |
| 1936 | M. Park | Mycologist | Department of Agriculture | — | — |
| 1937 | M. Park | Mycologist | Research Laboratories | — | — |
| 1940 | M. Park | Plant Pathologist | Research Laboratories | — | — |

### Deterministic checks: `park_maitland-elphinstone_b1894` vs `Park, M___Ceylon___1925`

- [PASS] surname_gate: bio 'PARK' vs stint 'Park, M' (exact)
- [PASS] initials: bio ['M', 'E'] ~ stint ['M']
- [PASS] age_gate: stint starts 1925, birth 1894 (age 31)
- [FAIL] colony: no placed event resolves to 'Ceylon'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1925-1940
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Park, M___Leeward Islands___1955`

- Staff-list name: **Park, M** | colony: **Leeward Islands** | listed 1955–1957 | editions [1955, 1956, 1957]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1955 | M. Park | Director of Agriculture | Civil Establishment | — | — |
| 1956 | M. Park | Director of Agriculture | Civil Establishment | — | — |
| 1957 | M. Park | Director of Agriculture | Civil Establishment | — | — |

### Deterministic checks: `park_maitland-elphinstone_b1894` vs `Park, M___Leeward Islands___1955`

- [PASS] surname_gate: bio 'PARK' vs stint 'Park, M' (exact)
- [PASS] initials: bio ['M', 'E'] ~ stint ['M']
- [PASS] age_gate: stint starts 1955, birth 1894 (age 61)
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1955-1957
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

