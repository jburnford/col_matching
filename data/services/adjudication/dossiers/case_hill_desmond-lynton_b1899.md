<!-- {"case_id": "case_hill_desmond-lynton_b1899", "bio_ids": ["hill_desmond-lynton_b1899"], "stint_ids": ["Hill, D. L___Nigeria___1929", "Hill, D. L___Tanganyika___1922"]} -->
# Dossier case_hill_desmond-lynton_b1899

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 111 official(s) with this surname in the graph's staff lists; 42 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hill_desmond-lynton_b1899`

- Printed name: **HILL, Desmond Lynton**
- Birth year: 1899 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L33329.v` — printed in editions [1948, 1949, 1950, 1951]:**

> HILL, Desmond Lynton.—b. 1899; ed. Highgate Sch.; on mil. serv. 1917-21, capt.; asst. inspr. of police, T.T., 1921; asst. comsnr., Nig., 1926; comsnr., 1935; supt., 1939.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1921 | asst. inspr. of police, T.T | — | [1948, 1949, 1950, 1951] |
| 1 | 1926 | asst. comsnr. | Nigeria | [1948, 1949, 1950, 1951] |
| 2 | 1935 | comsnr | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 3 | 1939 | supt | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Hill, D. L___Nigeria___1929`

- Staff-list name: **Hill, D. L** | colony: **Nigeria** | listed 1929–1939 | editions [1929, 1930, 1933, 1934, 1936, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1929 | D. L. Hill | Commissioners and Assistant Commissioners | Marine | — | — |
| 1930 | D. L. Hill | Commissioners and Assistant Commissioners | Police | — | — |
| 1933 | D. L. Hill | Commissioner/Assistant Commissioner | Police | — | — |
| 1934 | D. L. Hill | Commissioner/Assistant Commissioner | Police | — | — |
| 1936 | D. L. Hill | Commissioners and Assistant Commissioners | Police | — | — |
| 1939 | D. L. Hill | Senior Assistant Superintendent | Police | — | — |

### Deterministic checks: `hill_desmond-lynton_b1899` vs `Hill, D. L___Nigeria___1929`

- [PASS] surname_gate: bio 'HILL' vs stint 'Hill, D. L' (exact)
- [PASS] initials: bio ['D', 'L'] ~ stint ['D', 'L']
- [PASS] age_gate: stint starts 1929, birth 1899 (age 30)
- [PASS] colony: 3 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1929-1939
- [FAIL] position_sim: best 58 vs bar 60: 'asst. comsnr.' ~ 'Commissioners and Assistant Commissioners'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Hill, D. L___Tanganyika___1922`

- Staff-list name: **Hill, D. L** | colony: **Tanganyika** | listed 1922–1924 | editions [1922, 1923, 1924]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | D. L. Hill | Assistant Inspector | Police and Prisons Department | — | — |
| 1923 | D. L. Hill | Assistant Inspector | Police and Prisons Department | — | — |
| 1924 | D. L. Hill | Assistant Inspector | Police and Prisons Department | — | — |

### Deterministic checks: `hill_desmond-lynton_b1899` vs `Hill, D. L___Tanganyika___1922`

- [PASS] surname_gate: bio 'HILL' vs stint 'Hill, D. L' (exact)
- [PASS] initials: bio ['D', 'L'] ~ stint ['D', 'L']
- [PASS] age_gate: stint starts 1922, birth 1899 (age 23)
- [FAIL] colony: no placed event resolves to 'Tanganyika'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1922-1924
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

