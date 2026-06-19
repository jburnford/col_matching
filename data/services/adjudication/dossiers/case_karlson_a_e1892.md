<!-- {"case_id": "case_karlson_a_e1892", "bio_ids": ["karlson_a_e1892"], "stint_ids": ["Carlson, K. A___South Africa___1912", "Carlson, Knut Alexander___Orange River Colony___1905"]} -->
# Dossier case_karlson_a_e1892

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['karlson_a_e1892'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Carlson, K. A___South Africa___1912` is also gate-compatible with biography(ies) outside this case: ['carlson_knut-alexander_b1863'] (already linked elsewhere or filtered).
- NOTE: stint `Carlson, Knut Alexander___Orange River Colony___1905` is also gate-compatible with biography(ies) outside this case: ['carlson_knut-alexander_b1863'] (already linked elsewhere or filtered).

## Biography `karlson_a_e1892`

- Printed name: **KARLSON, A.**
- Birth year: not printed
- Appears in editions: [1914, 1915, 1917]

### Verbatim printed entry text (OCR)

**Version `col1914-L47625.v` — printed in editions [1914, 1915, 1917]:**

> KARLSON, A., M.I.C.E.—Chief engrnr., survey Selati Rlwy., 1892-96; ditto, Pietersburg Rlwy., 1896-99; manager, Pretoria Waterworks, 1898-1903; town engrnr., Pretoria, 1899-1902; consulting engrnr., Pretoria municipality, 1902-904; hydro. survr., irrigation dept., Transvaal, 26th July, 1904.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1892–1896 | Chief engrnr., survey | — | [1914, 1915, 1917] |
| 1 | 1896–1899 | Chief engrnr., survey | — | [1914, 1915, 1917] |
| 2 | 1898–1903 | manager | Pretoria | [1914, 1915, 1917] |
| 3 | 1899–1902 | town engrnr. | Pretoria | [1914, 1915, 1917] |
| 4 | 1902–1904 | consulting engrnr. | Pretoria | [1914, 1915, 1917] |
| 5 | 1904 | hydro. survr. | Transvaal | [1914, 1915, 1917] |

## Candidate stint `Carlson, K. A___South Africa___1912`

- Staff-list name: **Carlson, K. A** | colony: **South Africa** | listed 1912–1918 | editions [1912, 1914, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | K. A. Carlson | Conservator | Department of Forests | — | — |
| 1914 | K. A. Carlson | Conservator | Department of Forests | — | — |
| 1918 | K. A. Carlson | Conservator, Transvaal Conservancy | Department of Forests | — | — |

### Deterministic checks: `karlson_a_e1892` vs `Carlson, K. A___South Africa___1912`

- [PASS] surname_gate: bio 'KARLSON' vs stint 'Carlson, K. A' (fuzzy:1)
- [PASS] initials: bio ['A'] ~ stint ['K', 'A']
- [PASS] age_gate: stint starts 1912; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'South Africa'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1918
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Carlson, Knut Alexander___Orange River Colony___1905`

- Staff-list name: **Carlson, Knut Alexander** | colony: **Orange River Colony** | listed 1905–1909 | editions [1905, 1906, 1907, 1908, 1909]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | Knut Alexander Carlson | Chief, Forestry Div. | Divisions | — | — |
| 1906 | K. A. Carlson | Chief, Forestry Division | Agricultural Department | — | — |
| 1907 | K. A. Carlson | Chief, Forestry Division | Agricultural Department | — | — |
| 1908 | K. A. Carlson | Chief, Forestry Division | Agricultural Department | — | — |
| 1909 | K. A. Carlson | Chief, Forestry Division | Agricultural Department | — | — |

### Deterministic checks: `karlson_a_e1892` vs `Carlson, Knut Alexander___Orange River Colony___1905`

- [PASS] surname_gate: bio 'KARLSON' vs stint 'Carlson, Knut Alexander' (fuzzy:1)
- [PASS] initials: bio ['A'] ~ stint ['K', 'A']
- [PASS] age_gate: stint starts 1905; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Orange River Colony'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1909
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

