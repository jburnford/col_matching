<!-- {"case_id": "case_stewart_neil_b1894", "bio_ids": ["stewart_neil_b1894"], "stint_ids": ["Stewart, Neil___Kenya___1920"]} -->
# Dossier case_stewart_neil_b1894

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 100 official(s) with this surname in the graph's staff lists; 53 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['stewart_neil_b1894'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Stewart, Neil___Kenya___1920` is also gate-compatible with biography(ies) outside this case: ['stewart_neil_b1893'] (already linked elsewhere or filtered).

## Biography `stewart_neil_b1894`

- Printed name: **STEWART, Neil**
- Birth year: 1894 (attested in editions [1948, 1949])
- Appears in editions: [1948, 1949]

### Verbatim printed entry text (OCR)

**Version `col1948-L36162.v` — printed in editions [1948, 1949]:**

> STEWART, Neil, M.M.—b. 1894; ed. Alnwick Nat. Sch.; on mil. serv. 1915-19, 1941-42, lt.-col.; asst. supt., police, Ken., 1919; supt., 1927; dep. comsnr. (C.I.D.) and dir. intell. and security police, T.T., 1939; comdt., Somalia Gendarmerie, Mar., 1941; dep. comsnr. police and dir. intell. and security, T.T., 1942.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1919 | asst. supt., police | Kenya | [1948, 1949] |
| 1 | 1927 | supt | Kenya *(inherited from previous clause)* | [1948, 1949] |
| 2 | 1939 | dep. comsnr. (C.I.D.) and dir. intell. and security police, T.T | Kenya *(inherited from previous clause)* | [1948, 1949] |
| 3 | 1941 | comdt., Somalia Gendarmerie | Kenya *(inherited from previous clause)* | [1948, 1949] |
| 4 | 1942 | dep. comsnr. police and dir. intell. and security, T.T | Kenya *(inherited from previous clause)* | [1948, 1949] |

## Candidate stint `Stewart, Neil___Kenya___1920`

- Staff-list name: **Stewart, Neil** | colony: **Kenya** | listed 1920–1939 | editions [1920, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1934, 1936, 1937, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1920 | N. Stewart | Assistant Superintendent | Police | — | — |
| 1922 | N. Stewart | Assistant Superintendent | Police | — | — |
| 1923 | N. Stewart | Assistant Superintendent | Police | — | — |
| 1924 | N. Stewart | Assistant Superintendent | Police | — | — |
| 1925 | N. Stewart | Assistant Superintendent | Police Department | — | — |
| 1927 | N. Stewart | Assistant Superintendent | Police Department | — | — |
| 1928 | N. Stewart | Superintendent | Police Department | — | — |
| 1929 | N. Stewart | Superintendent | Police Department | — | — |
| 1930 | N. Stewart | Superintendent | Police Department | — | — |
| 1931 | N. Stewart | Superintendent | Police Department | — | — |
| 1932 | N. Stewart | Superintendent | Police Department | — | — |
| 1934 | N. Stewart | Superintendent | Police Department | — | — |
| 1936 | N. Stewart | Superintendent | Police Department | — | — |
| 1937 | N. Stewart | Superintendent | Police Department | — | — |
| 1939 | Neil Stewart | Superintendent | Police Department | — | — |

### Deterministic checks: `stewart_neil_b1894` vs `Stewart, Neil___Kenya___1920`

- [PASS] surname_gate: bio 'STEWART' vs stint 'Stewart, Neil' (exact)
- [PASS] initials: bio ['N'] ~ stint ['N']
- [PASS] age_gate: stint starts 1920, birth 1894 (age 26)
- [PASS] colony: 5 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1920-1939
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

