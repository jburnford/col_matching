<!-- {"case_id": "case_belleau_narcisse-f_b1808", "bio_ids": ["belleau_narcisse-f_b1808"], "stint_ids": ["Belleau, N. F___Canada___1886"]} -->
# Dossier case_belleau_narcisse-f_b1808

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `belleau_narcisse-f_b1808`

- Printed name: **BELLEAU, NARCISSE F.**
- Birth year: 1808 (attested in editions [1883, 1886, 1888, 1890, 1894])
- Honours: K.C.M.G. (1879)
- Appears in editions: [1883, 1886, 1888, 1890, 1894]

### Verbatim printed entry text (OCR)

**Version `col1883-L26397.v` — printed in editions [1883, 1886, 1888, 1890, 1894]:**

> BELLEAU, HON. SIR NARCISSE F., K.C.M.G. (1879).—Born 1808; called to the bar 1832; created a Q.C. 1854; appointed speaker of the Legislative Council of the province of Canada and minister of agriculture, subsequently premier and receiver-general, 7th Aug., 1865; called to the senate 1867, and was lieutenant-governor of Quebec from 1st July, 1867, to 1873.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1832–1832 | called to the bar | — | [1883, 1886, 1888, 1890, 1894] |
| 1 | 1854–1854 | Q.C. | — | [1883, 1886, 1888, 1890, 1894] |
| 2 | 1865 | speaker of the Legislative Council and minister of agriculture, subsequently premier and receiver-general | Canada | [1883, 1886, 1888, 1890, 1894] |
| 3 | 1867–1867 | called to the senate | — | [1883, 1886, 1888, 1890, 1894] |
| 4 | 1867–1873 | lieutenant-governor | Quebec | [1883, 1886, 1888, 1890, 1894] |

## Candidate stint `Belleau, N. F___Canada___1886`

- Staff-list name: **Belleau, N. F** | colony: **Canada** | listed 1886–1908 | editions [1886, 1888, 1889, 1890, 1894, 1897, 1898, 1899, 1900, 1906, 1907, 1908]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1886 | Sir N. F. Belleau | — | — | K.C.M.G. | — |
| 1888 | Sir N. F. Belleau | — | — | K.C.M.G. | — |
| 1889 | Sir N. F. Belleau | — | — | K.C.M.G. | — |
| 1890 | Sir N. F. Belleau | — | — | K.C.M.G. | — |

### Deterministic checks: `belleau_narcisse-f_b1808` vs `Belleau, N. F___Canada___1886`

- [PASS] surname_gate: bio 'BELLEAU' vs stint 'Belleau, N. F' (exact)
- [PASS] initials: bio ['N', 'F'] ~ stint ['N', 'F']
- [PASS] age_gate: stint starts 1886, birth 1808 (age 78)
- [PASS] colony: 1 placed event(s) resolve to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1886-1908
- [FAIL] position_sim: no overlapping placed event to compare
- [PASS] honour: shared: K.C.M.G.
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

