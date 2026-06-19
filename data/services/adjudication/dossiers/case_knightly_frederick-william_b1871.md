<!-- {"case_id": "case_knightly_frederick-william_b1871", "bio_ids": ["knightly_frederick-william_b1871"], "stint_ids": ["Knightly, F. W___Kenya___1928", "Knightly, F. W___South Africa___1912"]} -->
# Dossier case_knightly_frederick-william_b1871

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `knightly_frederick-william_b1871`

- Printed name: **KNIGHTLY, FREDERICK WILLIAM**
- Birth year: 1871 (attested in editions [1919, 1920, 1921, 1922, 1923, 1924, 1925])
- Appears in editions: [1919, 1920, 1921, 1922, 1923, 1924, 1925]

### Verbatim printed entry text (OCR)

**Version `col1919-L53698.v` — printed in editions [1919, 1920, 1921, 1922, 1923, 1924, 1925]:**

> KNIGHTLY, FREDERICK WILLIAM.—B. 1871; stationery storekeeper, I.M.R., 10th Nov., 1901; govt. printer, Transvaal, 1st Apr., 1907; mem., Transvaal tender bd., 1905; govt. printer, Union of S. Africa, 31st May, 1910; mem., Union of S. Africa tender bd., 1910; chmn., 1919.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1901 | stationery storekeeper, I.M.R | — | [1919, 1920, 1921, 1922, 1923, 1924, 1925] |
| 1 | 1905 | mem., Transvaal tender bd | Transvaal | [1919, 1920, 1921, 1922, 1923, 1924, 1925] |
| 2 | 1907 | govt. printer | Transvaal | [1919, 1920, 1921, 1922, 1923, 1924, 1925] |
| 3 | 1910 | govt. printer, Union of S. Africa | Transvaal *(inherited from previous clause)* | [1919, 1920, 1921, 1922, 1923, 1924, 1925] |
| 4 | 1919 | chmn | Transvaal *(inherited from previous clause)* | [1919, 1920, 1921, 1922, 1923, 1924, 1925] |

## Candidate stint `Knightly, F. W___Kenya___1928`

- Staff-list name: **Knightly, F. W** | colony: **Kenya** | listed 1928–1934 | editions [1928, 1929, 1930, 1932, 1934]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1928 | F. W. Knightly | Government Printer | Government Press | — | — |
| 1929 | F. W. Knightly | Government Printer | Government Press | — | — |
| 1930 | F. W. Knightly | Government Printer | Government Press | — | — |
| 1932 | F. W. Knightly | Government Printer | Government Press | — | — |
| 1934 | F. W. Knightly | Government Printer | Government Press | — | — |

### Deterministic checks: `knightly_frederick-william_b1871` vs `Knightly, F. W___Kenya___1928`

- [PASS] surname_gate: bio 'KNIGHTLY' vs stint 'Knightly, F. W' (exact)
- [PASS] initials: bio ['F', 'W'] ~ stint ['F', 'W']
- [PASS] age_gate: stint starts 1928, birth 1871 (age 57)
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1928-1934
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Knightly, F. W___South Africa___1912`

- Staff-list name: **Knightly, F. W** | colony: **South Africa** | listed 1912–1918 | editions [1912, 1914, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | F. W. Knightly | Government Printer | Printing and Stationery | — | — |
| 1914 | F. W. Knightly | Government Printer | Printing and Stationery | — | — |
| 1918 | F. W. Knightly | Government Printer | Printing and Stationery | — | — |

### Deterministic checks: `knightly_frederick-william_b1871` vs `Knightly, F. W___South Africa___1912`

- [PASS] surname_gate: bio 'KNIGHTLY' vs stint 'Knightly, F. W' (exact)
- [PASS] initials: bio ['F', 'W'] ~ stint ['F', 'W']
- [PASS] age_gate: stint starts 1912, birth 1871 (age 41)
- [FAIL] colony: no placed event resolves to 'South Africa'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1918
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

