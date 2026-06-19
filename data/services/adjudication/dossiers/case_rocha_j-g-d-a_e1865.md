<!-- {"case_id": "case_rocha_j-g-d-a_e1865", "bio_ids": ["rocha_j-g-d-a_e1865"], "stint_ids": ["Roche, A___Victoria___1894"]} -->
# Dossier case_rocha_j-g-d-a_e1865

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 13 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `rocha_j-g-d-a_e1865`

- Printed name: **ROCHA, J. G. D.A.**
- Birth year: not printed
- Appears in editions: [1883, 1886, 1888, 1889, 1890, 1894, 1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909, 1910]

### Verbatim printed entry text (OCR)

**Version `col1888-L35779.v` — printed in editions [1888, 1889, 1890, 1894, 1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909, 1910]:**

> ROCHA, J. G. D.A.—Entered the post office, Hong Kong, Feb., 1865; accountant, July, 1872; acting assistant postmaster, Sept., 1881, to May, 1883.

**Version `col1883-L29285.v` — printed in editions [1883, 1886]:**

> ROCHA, J. G. DA.—Entered the post office, Hong Kong, February, 1865; accountant, July, 1872.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1865 | Entered the post office | Hong Kong | [1883, 1886, 1888, 1889, 1890, 1894, 1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909, 1910] |
| 1 | 1872 | accountant | Hong Kong *(inherited from previous clause)* | [1883, 1886, 1888, 1889, 1890, 1894, 1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909, 1910] |
| 2 | 1881–1883 | acting assistant postmaster | — | [1888, 1889, 1890, 1894, 1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909, 1910] |

## Candidate stint `Roche, A___Victoria___1894`

- Staff-list name: **Roche, A** | colony: **Victoria** | listed 1894–1908 | editions [1894, 1897, 1898, 1899, 1900, 1905, 1906, 1908]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1894 | A. Roche | Inspector of Officers in Charge of Stores | Inspection of Stores | — | — |
| 1897 | A. Roche | Superintendent of Officers in Charge of Stores | Inspection of Stores | — | — |
| 1898 | A. Roche | Inspector of Officers in Charge of Stores | Inspection of Stores | — | — |
| 1899 | A. Roche | Inspector of Officers in Charge of Stores | Inspection of Stores | — | — |
| 1900 | A. Roche | Inspector of Officers in Charge of Stores | Inspection of Stores | — | — |
| 1905 | A. Roche | Inspector of Officers in Charge of Stores | Inspection of Stores. | — | — |
| 1906 | A. Roche | Inspector of Officers in Charge of Stores | Inspection of Stores | — | — |
| 1908 | A. Roche | Inspector of Officers in Charge of Stores | Inspection of Stores | — | — |

### Deterministic checks: `rocha_j-g-d-a_e1865` vs `Roche, A___Victoria___1894`

- [PASS] surname_gate: bio 'ROCHA' vs stint 'Roche, A' (fuzzy:1)
- [PASS] initials: bio ['J', 'G', 'D', 'A'] ~ stint ['A']
- [PASS] age_gate: stint starts 1894; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Victoria'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1894-1908
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

