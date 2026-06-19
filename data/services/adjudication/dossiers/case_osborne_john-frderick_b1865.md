<!-- {"case_id": "case_osborne_john-frderick_b1865", "bio_ids": ["osborne_john-frderick_b1865"], "stint_ids": ["Osborne, J___Australia___1912", "Osborne, J___Tasmania___1909"]} -->
# Dossier case_osborne_john-frderick_b1865

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 35 official(s) with this surname in the graph's staff lists; 12 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `osborne_john-frderick_b1865`

- Printed name: **OSBORNE, JOHN FRDERICK**
- Birth year: 1865 (attested in editions [1911])
- Appears in editions: [1911]

### Verbatim printed entry text (OCR)

**Version `col1911-L47108.v` — printed in editions [1911]:**

> OSBORNE, JOHN FRDERICK.—B. 1865; set articles with R. Fabian Russell, F.R.I.B.A., London; asst. engr. on construction, Manc'ship Canal, Nov., 1887, to Dec., 1891; attached to P.W.D., Jamaica, July, 1892, to Nov., 1896; surveys for and construction of bridges; irrigation engr., Rio Cobre canals; col. sur. and inspr. of P. W. Turks and Caicos Is., Nov., 1896; J.P. 1901; ag. asst. commr., Cay., Apr., 1902, to July, 1903, and from May, 1904; transd. to lands and wks. div., Fiji, Nov., 1904; asst. commr., P.W.D., Jan., 1906.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1887–1891 | asst. engr. on construction | — | [1911] |
| 1 | 1892–1896 | attached to P.W.D. | Jamaica | [1911] |
| 2 | 1896 | col. sur. and inspr. of P. W. | Turks and Caicos Islands | [1911] |
| 3 | 1901 | J.P. | — | [1911] |
| 4 | 1902 | ag. asst. commr. | Cayman Islands | [1911] |
| 5 | 1904 | transd. to lands and wks. div. | Fiji | [1911] |
| 6 | 1906 | asst. commr., P.W.D. | — | [1911] |

## Candidate stint `Osborne, J___Australia___1912`

- Staff-list name: **Osborne, J** | colony: **Australia** | listed 1912–1918 | editions [1912, 1913, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | J. Osborne, jr. | Fruit Expert | Agricultural Department | — | — |
| 1913 | J. Osborne, jr. | Fruit Expert | Agricultural Department | — | — |
| 1918 | J. Osborne, jr. | Fruit Expert | Agricultural Department | — | — |

### Deterministic checks: `osborne_john-frderick_b1865` vs `Osborne, J___Australia___1912`

- [PASS] surname_gate: bio 'OSBORNE' vs stint 'Osborne, J' (exact)
- [PASS] initials: bio ['J', 'F'] ~ stint ['J']
- [PASS] age_gate: stint starts 1912, birth 1865 (age 47)
- [FAIL] colony: no placed event resolves to 'Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1918
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Osborne, J___Tasmania___1909`

- Staff-list name: **Osborne, J** | colony: **Tasmania** | listed 1909–1917 | editions [1909, 1917]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1909 | J. Osborne, jr. | Fruit Expert | Council of Agriculture | — | — |
| 1917 | J. Osborne, jr. | Fruit Expert | Agricultural Department | — | — |

### Deterministic checks: `osborne_john-frderick_b1865` vs `Osborne, J___Tasmania___1909`

- [PASS] surname_gate: bio 'OSBORNE' vs stint 'Osborne, J' (exact)
- [PASS] initials: bio ['J', 'F'] ~ stint ['J']
- [PASS] age_gate: stint starts 1909, birth 1865 (age 44)
- [FAIL] colony: no placed event resolves to 'Tasmania'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1909-1917
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

