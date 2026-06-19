<!-- {"case_id": "case_wann_j-m_b1922", "bio_ids": ["wann_j-m_b1922", "wann_james_b1890"], "stint_ids": ["Wann, J. M___Sierra Leone___1950"]} -->
# Dossier case_wann_j-m_b1922

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['wann_james_b1890'] carry a single initial only — the namesake trap applies.
- CONTESTED: stint(s) ['Wann, J. M___Sierra Leone___1950'] have more than one claimant biography in this case.

## Biography `wann_j-m_b1922`

- Printed name: **WANN, J. M**
- Birth year: 1922 (attested in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962])
- Honours: O.B.E (1960)
- Appears in editions: [1956, 1957, 1958, 1959, 1960, 1961, 1962]

### Verbatim printed entry text (OCR)

**Version `col1956-L24831.v` — printed in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962]:**

> WANN, J. M., O.B.E. (1960).—b. 1922; ed. Morgan Academy and St. Andrews Univ.; mil. serv., 1942-44, lieut.; cadet, S.L., 1944; asst. dist. comsnr., 1947; dist. comsnr., 1953; perm. sec., 1959.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1944 | cadet | Sierra Leone | [1956, 1957, 1958, 1959, 1960, 1961, 1962] |
| 1 | 1947 | asst. dist. comsnr | Sierra Leone *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962] |
| 2 | 1953 | dist. comsnr | Sierra Leone *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962] |
| 3 | 1959 | perm. sec | Sierra Leone *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962] |

## Biography `wann_james_b1890`

- Printed name: **WANN, JAMES**
- Birth year: 1890 (attested in editions [1939, 1940])
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L71570.v` — printed in editions [1939, 1940]:**

> WANN, MAJOR JAMES, B.A. (Oxon.).—B.1890; ed. Dulwich Coll. and New Coll., Oxford; mily. serv., 1915-1919; ment. in desps.; ast. dist. offr., Nigeria, 1920; dist. offr., 1928; admstr. offr., cls. II, 1936; do., cls. I, 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1915–1919 | mily. serv | — | [1939, 1940] |
| 1 | 1920 | ast. dist. offr. | Nigeria | [1939, 1940] |
| 2 | 1928 | dist. offr | Nigeria *(inherited from previous clause)* | [1939, 1940] |
| 3 | 1936 | admstr. offr., cls. II | Nigeria *(inherited from previous clause)* | [1939, 1940] |
| 4 | 1938 | do., cls. I | Nigeria *(inherited from previous clause)* | [1939, 1940] |

## Candidate stint `Wann, J. M___Sierra Leone___1950`

- Staff-list name: **Wann, J. M** | colony: **Sierra Leone** | listed 1950–1951 | editions [1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | J. M. Wann | Assistant District Commissioners and Cadets | Provincial Administration | — | — |
| 1951 | J. M. Wann | Assistant District Commissioner and Cadet | Provincial Administration | — | — |

### Deterministic checks: `wann_j-m_b1922` vs `Wann, J. M___Sierra Leone___1950`

- [PASS] surname_gate: bio 'WANN' vs stint 'Wann, J. M' (exact)
- [PASS] initials: bio ['J', 'M'] ~ stint ['J', 'M']
- [PASS] age_gate: stint starts 1950, birth 1922 (age 28)
- [PASS] colony: 4 placed event(s) resolve to 'Sierra Leone'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1950-1951
- [FAIL] position_sim: best 56 vs bar 60: 'asst. dist. comsnr' ~ 'Assistant District Commissioner and Cadet'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

### Deterministic checks: `wann_james_b1890` vs `Wann, J. M___Sierra Leone___1950`

- [PASS] surname_gate: bio 'WANN' vs stint 'Wann, J. M' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J', 'M']
- [PASS] age_gate: stint starts 1950, birth 1890 (age 60)
- [FAIL] colony: no placed event resolves to 'Sierra Leone'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1950-1951
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

