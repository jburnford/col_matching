<!-- {"case_id": "case_burger_x_e1902", "bio_ids": ["burger_x_e1902"], "stint_ids": ["Burger, Andries Jacobus___Orange River Colony___1908", "Burger, S. W___South Africa___1908"]} -->
# Dossier case_burger_x_e1902

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['burger_x_e1902'] carry a single initial only — the namesake trap applies.

## Biography `burger_x_e1902`

- Printed name: **BURGER, (no given names printed)**
- Birth year: not printed
- Appears in editions: [1912]

### Verbatim printed entry text (OCR)

**Version `col1912-L45871.v` — printed in editions [1912]:**

> BURGER REFUGE CAMP, TRANSVAAL, FEB. TO DEC., 1902; MED. OFFR., ANTIGUA, SEPT., 1904; MED. OFFR., ST. KITTA, JAN., 1905.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1902–1902 | — | Transvaal | [1912] |
| 1 | 1904–1904 | MED. OFFR. | Antigua | [1912] |
| 2 | 1905–1905 | MED. OFFR. | St. Kitts | [1912] |

## Candidate stint `Burger, Andries Jacobus___Orange River Colony___1908`

- Staff-list name: **Burger, Andries Jacobus** | colony: **Orange River Colony** | listed 1908–1909 | editions [1908, 1909]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1908 | Andries Jacobus Burger | Member | Electoral Division | — | — |
| 1909 | Andries Jacobus Burger | Member | Electoral Division | — | — |

### Deterministic checks: `burger_x_e1902` vs `Burger, Andries Jacobus___Orange River Colony___1908`

- [PASS] surname_gate: bio 'BURGER' vs stint 'Burger, Andries Jacobus' (exact)
- [PASS] initials: bio ['?'] ~ stint ['A', 'J']
- [PASS] age_gate: stint starts 1908; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Orange River Colony'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1908-1909
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Burger, S. W___South Africa___1908`

- Staff-list name: **Burger, S. W** | colony: **South Africa** | listed 1908–1918 | editions [1908, 1912, 1914, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1908 | S. W. Burger | Member | Inter-Colonial Council | — | — |
| 1912 | S. W. Burger | Elected Member | Provincial Council of the Transvaal | — | — |
| 1914 | S. W. Burger | Elected Member | Provincial Council of the Transvaal | — | — |
| 1918 | S. W. Burger | Senator | Senate | — | — |

### Deterministic checks: `burger_x_e1902` vs `Burger, S. W___South Africa___1908`

- [PASS] surname_gate: bio 'BURGER' vs stint 'Burger, S. W' (exact)
- [PASS] initials: bio ['?'] ~ stint ['S', 'W']
- [PASS] age_gate: stint starts 1908; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'South Africa'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1908-1918
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

