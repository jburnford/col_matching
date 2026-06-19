<!-- {"case_id": "case_amoroso-centeno_m_b1908", "bio_ids": ["amoroso-centeno_m_b1908"], "stint_ids": ["Amoroso-Centeno, M___Trinidad and Tobago___1933"]} -->
# Dossier case_amoroso-centeno_m_b1908

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['amoroso-centeno_m_b1908'] carry a single initial only — the namesake trap applies.

## Biography `amoroso-centeno_m_b1908`

- Printed name: **AMOROSO-CENTENO, M**
- Birth year: 1908 (attested in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964])
- Appears in editions: [1958, 1959, 1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1958-L20028.v` — printed in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964]:**

> AMOROSO-CENTENO, M.—b. 1908; ed. St. Mary's Coll., T'dad; clk., customs and excise, T'dad, 1928; senr. offr., 1940; prtn. offr., 1943; supvr., cl. II, 1946; cl. I, 1948; asst. compt., customs and excise, 1954; dep. compt., 1956. (T'dad Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | clk., customs and excise | Trinidad | [1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 1 | 1940 | senr. offr | Trinidad *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 2 | 1943 | prtn. offr | Trinidad *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 3 | 1946 | supvr., cl. II | Trinidad *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 4 | 1948 | cl. I | Trinidad *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 5 | 1954 | asst. compt., customs and excise | Trinidad *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 6 | 1956 | dep. compt | Trinidad *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964] |

## Candidate stint `Amoroso-Centeno, M___Trinidad and Tobago___1933`

- Staff-list name: **Amoroso-Centeno, M** | colony: **Trinidad and Tobago** | listed 1933–1939 | editions [1933, 1934, 1937, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | M. Amoroso-Centeno | 2nd Class Clerk | Customs and Excise Department | — | — |
| 1934 | M. Amoroso-Centeno | 2nd Class Clerk | Customs and Excise Department | — | — |
| 1937 | M. Amoroso-Centeno | 1st Class Clerk | Customs and Excise Department | — | — |
| 1939 | M. Amoroso-Centeno | 1st Class Clerk | Customs and Excise Department | — | — |

### Deterministic checks: `amoroso-centeno_m_b1908` vs `Amoroso-Centeno, M___Trinidad and Tobago___1933`

- [PASS] surname_gate: bio 'AMOROSO-CENTENO' vs stint 'Amoroso-Centeno, M' (exact)
- [PASS] initials: bio ['M'] ~ stint ['M']
- [PASS] age_gate: stint starts 1933, birth 1908 (age 25)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1933-1939
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

