<!-- {"case_id": "case_munro_j-s_e1918", "bio_ids": ["munro_j-s_e1918"], "stint_ids": ["Munro, J. S___Kenya___1919", "Munro, J___Palestine___1927", "Munro, S___Trinidad and Tobago___1925"]} -->
# Dossier case_munro_j-s_e1918

## Case context

- 1 biography(ies) and 3 candidate stint(s) are entangled in this case.
- Corpus context: 34 official(s) with this surname in the graph's staff lists; 10 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Munro, J___Palestine___1927` is also gate-compatible with biography(ies) outside this case: ['munro_j-p-g_e1876'] (already linked elsewhere or filtered).

## Biography `munro_j-s_e1918`

- Printed name: **MUNRO, J. S**
- Birth year: not printed
- Appears in editions: [1920, 1921, 1922, 1923, 1924, 1927]

### Verbatim printed entry text (OCR)

**Version `col1920-L55964.v` — printed in editions [1920, 1921, 1922, 1923, 1924, 1927]:**

> MUNRO, J. S.—Asst. loco. supt., Uganda Railway, Jan., 1918.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1918 | Asst. loco. supt., Uganda Railway | Uganda | [1920, 1921, 1922, 1923, 1924, 1927] |

## Candidate stint `Munro, J. S___Kenya___1919`

- Staff-list name: **Munro, J. S** | colony: **Kenya** | listed 1919–1920 | editions [1919, 1920]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1919 | J. S. Munro | Assistant Locomotive Superintendent | Locomotive, Carriage and Wagon Department | — | — |
| 1920 | J. S. Munro | Assistant Locomotive Superintendent | Locomotive, Carriage and Wagon Department | — | — |

### Deterministic checks: `munro_j-s_e1918` vs `Munro, J. S___Kenya___1919`

- [PASS] surname_gate: bio 'MUNRO' vs stint 'Munro, J. S' (exact)
- [PASS] initials: bio ['J', 'S'] ~ stint ['J', 'S']
- [PASS] age_gate: stint starts 1919; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1919-1920
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Munro, J___Palestine___1927`

- Staff-list name: **Munro, J** | colony: **Palestine** | listed 1927–1940 | editions [1927, 1928, 1929, 1930, 1931, 1932, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | J. Munro | Deputy Superintendents | Department of Police and Prisons | — | — |
| 1928 | J. Munro | Deputy Superintendents | Department of Police and Prisons | — | — |
| 1929 | J. Munro | Deputy Superintendents | Department of Police and Prisons | — | — |
| 1930 | J. Munro | Deputy Superintendents | Department of Police and Prisons | — | — |
| 1931 | J. Munro | Deputy Superintendents | Department of Police and Prisons. | — | — |
| 1932 | J. Munro | Deputy Superintendents | Department of Police and Prisons | — | — |
| 1940 | J. Munro | District Superintendent | Department of Police and Prisons. | — | — |

### Deterministic checks: `munro_j-s_e1918` vs `Munro, J___Palestine___1927`

- [PASS] surname_gate: bio 'MUNRO' vs stint 'Munro, J' (exact)
- [PASS] initials: bio ['J', 'S'] ~ stint ['J']
- [PASS] age_gate: stint starts 1927; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Palestine'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1927-1940
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Munro, S___Trinidad and Tobago___1925`

- Staff-list name: **Munro, S** | colony: **Trinidad and Tobago** | listed 1925–1928 | editions [1925, 1927, 1928]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1925 | S. Munro | Assistant Locomotive Engineer | Locomotive Branch | — | — |
| 1927 | S. Munro | Assistant Locomotive Engineer | Locomotive Branch | — | — |
| 1928 | S. Munro | Assistant Locomotive Engineer | Locomotive Branch | — | — |

### Deterministic checks: `munro_j-s_e1918` vs `Munro, S___Trinidad and Tobago___1925`

- [PASS] surname_gate: bio 'MUNRO' vs stint 'Munro, S' (exact)
- [PASS] initials: bio ['J', 'S'] ~ stint ['S']
- [PASS] age_gate: stint starts 1925; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1925-1928
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

