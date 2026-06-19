<!-- {"case_id": "case_shuel_ronald-stuart_b1900", "bio_ids": ["shuel_ronald-stuart_b1900"], "stint_ids": ["Shuel, R. S___Nigeria___1927", "Shuel, R. S___Trinidad and Tobago___1922"]} -->
# Dossier case_shuel_ronald-stuart_b1900

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `shuel_ronald-stuart_b1900`

- Printed name: **SHUEL, Ronald Stuart**
- Birth year: 1900 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L35883.v` — printed in editions [1948, 1949, 1950, 1951]:**

> SHUEL, Ronald Stuart.—b. 1900; ed. St. Columba's Coll., Rathfarnham, Dublin, and The Abbey Sch., Tipperary; sub-inspr. of constab., Trin., 1921; trans. to Nig. N.P. police, 1925; supt., 1937; asst. comsnr., 1945.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1921 | sub-inspr. of constab. | Trinidad | [1948, 1949, 1950, 1951] |
| 1 | 1925 | trans. to Nig. N.P. police | Trinidad *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 2 | 1937 | supt | Trinidad *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 3 | 1945 | asst. comsnr | Trinidad *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Shuel, R. S___Nigeria___1927`

- Staff-list name: **Shuel, R. S** | colony: **Nigeria** | listed 1927–1939 | editions [1927, 1929, 1930, 1933, 1934, 1936, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | R. S. Shuel | Commissioner | Police, Northern Provinces | — | — |
| 1929 | R. S. Shuel | Commissioners and Assistant Commissioners | Marine | — | — |
| 1930 | R. S. Shuel | Commissioners and Assistant Commissioners | Police | — | — |
| 1933 | R. S. Shuel | Commissioner/Assistant Commissioner | Police | — | — |
| 1934 | R. S. Shuel | Commissioner/Assistant Commissioner | Police | — | — |
| 1936 | R. S. Shuel | Commissioners and Assistant Commissioners | Police | — | — |
| 1939 | R. S. Shuel | Superintendent | Police | — | — |

### Deterministic checks: `shuel_ronald-stuart_b1900` vs `Shuel, R. S___Nigeria___1927`

- [PASS] surname_gate: bio 'SHUEL' vs stint 'Shuel, R. S' (exact)
- [PASS] initials: bio ['R', 'S'] ~ stint ['R', 'S']
- [PASS] age_gate: stint starts 1927, birth 1900 (age 27)
- [FAIL] colony: no placed event resolves to 'Nigeria'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1927-1939
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Shuel, R. S___Trinidad and Tobago___1922`

- Staff-list name: **Shuel, R. S** | colony: **Trinidad and Tobago** | listed 1922–1925 | editions [1922, 1923, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | R. S. Shuel | Sub-Inspector | Constabulary and Gaols | — | — |
| 1923 | R. S. Shuel | Sub-Inspector | Constabulary and Gaols | — | — |
| 1925 | R. S. Shuel | Sub-Inspector | Constabulary and Gaols | — | — |

### Deterministic checks: `shuel_ronald-stuart_b1900` vs `Shuel, R. S___Trinidad and Tobago___1922`

- [PASS] surname_gate: bio 'SHUEL' vs stint 'Shuel, R. S' (exact)
- [PASS] initials: bio ['R', 'S'] ~ stint ['R', 'S']
- [PASS] age_gate: stint starts 1922, birth 1900 (age 22)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1922-1925
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

