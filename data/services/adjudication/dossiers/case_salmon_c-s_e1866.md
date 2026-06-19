<!-- {"case_id": "case_salmon_c-s_e1866", "bio_ids": ["salmon_c-s_e1866"], "stint_ids": ["Salmon, C. S___Jamaica___1896", "Salmon, C. S___Mauritius___1877"]} -->
# Dossier case_salmon_c-s_e1866

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 17 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `salmon_c-s_e1866`

- Printed name: **SALMON, C. S.**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L29386.v` — printed in editions [1883]:**

> SALMON, C. S.—Sub-collector of customs and J. P., British Sherbro, 23rd April, 1866; acted as manager and coroner of British Sherbro from 23rd April, 1866, to 8th Feb., 1867, and from 18th Dec., 1867, to 6th March, 1868; land commissioner for Sherbro, 4th April, 1867; acted as collector of customs, Sierra Leone, from May to Oct., 1868; also as registrar for shipping; collector of customs, Gold Coast, 28th Dec., 1869; acted as chief magistrate and judicial assessor, Gold Coast, from 8th April, to 2nd Nov., 1870; acting administrator, Gold Coast, July, 1871, to Dec., 1872; chief civil commissioner, Seychelles (Mauritius), 1874; president of Nevis.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1866 | Sub-collector of customs and J. P. | British Sherbro | [1883] |
| 1 | 1867 | land commissioner | British Sherbro | [1883] |
| 2 | 1868–1868 | collector of customs | Sierra Leone | [1883] |
| 3 | 1869 | collector of customs | Gold Coast | [1883] |
| 4 | 1870–1870 | chief magistrate and judicial assessor | Gold Coast | [1883] |
| 5 | 1871–1872 | acting administrator | Gold Coast | [1883] |
| 6 | 1874 | chief civil commissioner | Seychelles | [1883] |
| 7 | ? | president | Nevis | [1883] |

## Candidate stint `Salmon, C. S___Jamaica___1896`

- Staff-list name: **Salmon, C. S** | colony: **Jamaica** | listed 1896–1897 | editions [1896, 1897]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1896 | C. S. Salmon | Senior Ordnance Store Officer | Officers, Military, Naval, &c. | — | — |
| 1897 | C. S. Salmon | Senior Ordnance Store Officer, Dep. Assist. Com.-Gen. | Officers, Military, Naval, &c. | — | — |

### Deterministic checks: `salmon_c-s_e1866` vs `Salmon, C. S___Jamaica___1896`

- [PASS] surname_gate: bio 'SALMON' vs stint 'Salmon, C. S' (exact)
- [PASS] initials: bio ['C', 'S'] ~ stint ['C', 'S']
- [PASS] age_gate: stint starts 1896; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Jamaica'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1896-1897
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Salmon, C. S___Mauritius___1877`

- Staff-list name: **Salmon, C. S** | colony: **Mauritius** | listed 1877–1879 | editions [1877, 1879]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | C. S. Salmon | Chief Commissioner | Board of Civil Commissioners | — | — |
| 1879 | C. S. Salmon | Chief Civil Commissioner | Board of Civil Commissioners | — | — |

### Deterministic checks: `salmon_c-s_e1866` vs `Salmon, C. S___Mauritius___1877`

- [PASS] surname_gate: bio 'SALMON' vs stint 'Salmon, C. S' (exact)
- [PASS] initials: bio ['C', 'S'] ~ stint ['C', 'S']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Mauritius'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1879
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

