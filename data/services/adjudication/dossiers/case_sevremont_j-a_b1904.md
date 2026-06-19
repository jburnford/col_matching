<!-- {"case_id": "case_sevremont_j-a_b1904", "bio_ids": ["sevremont_j-a_b1904"], "stint_ids": ["Sevremout, J___Mauritius___1921", "S\u00e8vremont, J___Mauritius___1927"]} -->
# Dossier case_sevremont_j-a_b1904

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `sevremont_j-a_b1904`

- Printed name: **SEVREMONT, J. A**
- Birth year: 1904 (attested in editions [1958, 1959, 1961, 1962, 1963, 1964, 1965])
- Appears in editions: [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965]

### Verbatim printed entry text (OCR)

**Version `col1958-L26807.v` — printed in editions [1958, 1959, 1961, 1962, 1963, 1964, 1965]:**

> SEVREMONT, J. A.—b. 1904; ed. Instn. of Educ., London Univ.; 2nd cl. teacher, Maur., 1923; head teacher, 1938; supt., primary sch., 1948; educ. offr., 1955–64.

**Version `col1960-L27875.v` — printed in editions [1960]:**

> SEVRERONT, J. A.—b. 1904; ed. Instn. of Educ., London Univ.; 2nd cl. teacher, Maur., 1923; head teacher, 1938; supt., primary sch., 1948; educ. offr., 1955.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1923 | 2nd cl. teacher | Mauritius | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 1 | 1938 | head teacher | Mauritius *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 2 | 1948 | supt., primary sch | Mauritius *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |

## Candidate stint `Sevremout, J___Mauritius___1921`

- Staff-list name: **Sevremout, J** | colony: **Mauritius** | listed 1921–1923 | editions [1921, 1923]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1921 | J. Sevremout | Inspector (Revenue) | Inland Revenue Branch | — | — |
| 1923 | J. Sevremout | Inspectors (Revenue) | Inland Revenue Branch | — | — |

### Deterministic checks: `sevremont_j-a_b1904` vs `Sevremout, J___Mauritius___1921`

- [PASS] surname_gate: bio 'SEVREMONT' vs stint 'Sevremout, J' (fuzzy:1)
- [PASS] initials: bio ['J', 'A'] ~ stint ['J']
- [PASS] age_gate: stint starts 1921, birth 1904 (age 17)
- [PASS] colony: 3 placed event(s) resolve to 'Mauritius'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1921-1923
- [FAIL] position_sim: best 32 vs bar 60: '2nd cl. teacher' ~ 'Inspector (Revenue)'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Sèvremont, J___Mauritius___1927`

- Staff-list name: **Sèvremont, J** | colony: **Mauritius** | listed 1927–1928 | editions [1927, 1928]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | J. Sèvremont | Inspector (Revenue) | Inland Revenue Branch | — | — |
| 1928 | J. Sèvremont | Inspectors (Revenue) | Inland Revenue Branch | — | — |

### Deterministic checks: `sevremont_j-a_b1904` vs `Sèvremont, J___Mauritius___1927`

- [PASS] surname_gate: bio 'SEVREMONT' vs stint 'Sèvremont, J' (fuzzy:1)
- [PASS] initials: bio ['J', 'A'] ~ stint ['J']
- [PASS] age_gate: stint starts 1927, birth 1904 (age 23)
- [PASS] colony: 3 placed event(s) resolve to 'Mauritius'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1927-1928
- [FAIL] position_sim: best 32 vs bar 60: '2nd cl. teacher' ~ 'Inspector (Revenue)'
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

