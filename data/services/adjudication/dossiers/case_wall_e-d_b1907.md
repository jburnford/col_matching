<!-- {"case_id": "case_wall_e-d_b1907", "bio_ids": ["wall_e-d_b1907"], "stint_ids": ["Wall, E___Nyasaland___1923"]} -->
# Dossier case_wall_e-d_b1907

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 22 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Wall, E___Nyasaland___1923` is also gate-compatible with biography(ies) outside this case: ['wall_ernest_b1896'] (already linked elsewhere or filtered).

## Biography `wall_e-d_b1907`

- Printed name: **WALL, E. D**
- Birth year: 1907 (attested in editions [1955])
- Appears in editions: [1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1955-L23186.v` — printed in editions [1955]:**

> WALL, E. D.—b. 1907; ed. St. V. Gram. Sch.; asst. o'seer, Fort instns., St. V., 1929; dispenser, 1929; head keeper, Fort instns., 1936; lay supt., mental hosp., 1938; ch. prison offr., 1939; supt., prisons, 1944; asst. supt., prisons, Trin. and Tob., 1946; dep. supt., 1947.

**Version `col1956-L24803.v` — printed in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]:**

> WALL, E. D.—b. 1907; ed. St. V. Gram. Sch.; 1st appt., St. V., 1929; supt., prisons, 1944; asst. supt., prisons, Trin. and Tob., 1946; dep. supt., 1947; secon. B. Guiana prison service, 1954; dep. comsnr., Trin., 1956. (T'dad Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1929 | asst. o'seer, Fort instns. | St. Vincent | [1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 1 | 1936 | head keeper, Fort instns | St. Vincent *(inherited from previous clause)* | [1955] |
| 2 | 1938 | lay supt., mental hosp | St. Vincent *(inherited from previous clause)* | [1955] |
| 3 | 1939 | ch. prison offr | St. Vincent *(inherited from previous clause)* | [1955] |
| 4 | 1944 | supt., prisons | St. Vincent *(inherited from previous clause)* | [1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 5 | 1946 | asst. supt., prisons, Trin. and Tob | Trinidad | [1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 6 | 1947 | dep. supt | Trinidad *(inherited from previous clause)* | [1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 7 | 1954 | secon. B. Guiana prison service | Trinidad *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 8 | 1956 | dep. comsnr. | Trinidad | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |

## Candidate stint `Wall, E___Nyasaland___1923`

- Staff-list name: **Wall, E** | colony: **Nyasaland** | listed 1923–1937 | editions [1923, 1924, 1925, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1936, 1937]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1923 | E. Wall | Assistant Engineer | Public Works Department | — | — |
| 1924 | E. Wall | Assistant Engineer | Public Works Department | — | — |
| 1925 | E. Wall | Assistant Engineers | Public Works Department | — | — |
| 1928 | E. Wall | Assistant Engineers | Public Works | — | — |
| 1929 | E. Wall | Assistant Engineer | Public Works | — | — |
| 1930 | E. Wall | Executive Engineer | Public Works | — | — |
| 1931 | E. Wall | Executive Engineers | Public Works | — | — |
| 1932 | E. Wall | Executive Engineer | Public Works | — | — |
| 1933 | E. Wall | Executive Engineers | Public Works | — | — |
| 1934 | E. Wall | Executive Engineers | Public Works | — | — |
| 1936 | E. Wall | Executive Engineer | Public Works | — | — |
| 1937 | E. Wall | Executive Engineers | Public Works | — | — |

### Deterministic checks: `wall_e-d_b1907` vs `Wall, E___Nyasaland___1923`

- [PASS] surname_gate: bio 'WALL' vs stint 'Wall, E' (exact)
- [PASS] initials: bio ['E', 'D'] ~ stint ['E']
- [PASS] age_gate: stint starts 1923, birth 1907 (age 16)
- [FAIL] colony: no placed event resolves to 'Nyasaland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1923-1937
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

