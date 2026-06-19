<!-- {"case_id": "case_enstone_edwin-john_b1888", "bio_ids": ["enstone_edwin-john_b1888"], "stint_ids": ["Elstone, J___Ceylon___1911", "Elstone, J___Ceylon___1921"]} -->
# Dossier case_enstone_edwin-john_b1888

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `enstone_edwin-john_b1888`

- Printed name: **ENSTONE, EDWIN JOHN**
- Birth year: 1888 (attested in editions [1929])
- Appears in editions: [1929]

### Verbatim printed entry text (OCR)

**Version `col1929-L59933.v` — printed in editions [1929]:**

> ENSTONE, EDWIN JOHN.—B. 1888; on mil. serv. with 4th Hants Regt., 4 years 11 months in Mesopotamia, etc.; twice ment. in desps.; shorthand instr. and office asst. to dir., educn., Gold Coast, 28th July, 1920.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1920 | shorthand instr. and office asst. to dir., educn. | Gold Coast | [1929] |

## Candidate stint `Elstone, J___Ceylon___1911`

- Staff-list name: **Elstone, J** | colony: **Ceylon** | listed 1911–1912 | editions [1911, 1912]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1911 | J. Elstone | Assistant Superintendent | Police | — | — |
| 1912 | J. Elstone (acting) | Assistant Superintendent | Police | — | — |

### Deterministic checks: `enstone_edwin-john_b1888` vs `Elstone, J___Ceylon___1911`

- [PASS] surname_gate: bio 'ENSTONE' vs stint 'Elstone, J' (fuzzy:1)
- [PASS] initials: bio ['E', 'J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1911, birth 1888 (age 23)
- [FAIL] colony: no placed event resolves to 'Ceylon'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1911-1912
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Elstone, J___Ceylon___1921`

- Staff-list name: **Elstone, J** | colony: **Ceylon** | listed 1921–1923 | editions [1921, 1922, 1923]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1921 | J. Elstone | 3rd Assistant Superintendent of Prisons | Prisons | — | — |
| 1922 | J. Elstone | Assistant Superintendent of Prisons | Prisons | — | — |
| 1923 | J. Elstone | Assistant Superintendent of Prisons | Prisons | — | — |

### Deterministic checks: `enstone_edwin-john_b1888` vs `Elstone, J___Ceylon___1921`

- [PASS] surname_gate: bio 'ENSTONE' vs stint 'Elstone, J' (fuzzy:1)
- [PASS] initials: bio ['E', 'J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1921, birth 1888 (age 33)
- [FAIL] colony: no placed event resolves to 'Ceylon'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1921-1923
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

