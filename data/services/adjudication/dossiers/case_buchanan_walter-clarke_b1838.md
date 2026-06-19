<!-- {"case_id": "case_buchanan_walter-clarke_b1838", "bio_ids": ["buchanan_walter-clarke_b1838"], "stint_ids": ["Buchanan, William___New South Wales___1877"]} -->
# Dossier case_buchanan_walter-clarke_b1838

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 33 official(s) with this surname in the graph's staff lists; 11 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `buchanan_walter-clarke_b1838`

- Printed name: **BUCHANAN, Walter Clarke**
- Birth year: 1838 (attested in editions [1917, 1918, 1920, 1921])
- Honours: K.T. BACH (1912)
- Appears in editions: [1917, 1918, 1920, 1921]

### Verbatim printed entry text (OCR)

**Version `col1917-L48050.v` — printed in editions [1917, 1918, 1920, 1921]:**

> BUCHANAN, Sir Walter Clarke, K.T. BACH, (1912).—B. 1838; ed. High Schl., Greenock; mem. of H. of R., New Zealand, 1881-1899, 1902-1905, and from 1908 to 1914; M.L.C., since 23rd June, 1916.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1881–1899 | mem. of H. of R. | New Zealand | [1917, 1918, 1920, 1921] |
| 1 | 1902–1905 | mem. of H. of R. | New Zealand | [1917, 1918, 1920, 1921] |
| 2 | 1908–1914 | mem. of H. of R. | New Zealand | [1917, 1918, 1920, 1921] |
| 3 | 1916 | M.L.C. | — | [1917, 1918, 1920, 1921] |

## Candidate stint `Buchanan, William___New South Wales___1877`

- Staff-list name: **Buchanan, William** | colony: **New South Wales** | listed 1877–1880 | editions [1877, 1878, 1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | William Buchanan | Postal Inspector | General Post-Office | — | — |
| 1878 | William Buchanan | Postal Inspector | General Post-Office | — | — |
| 1879 | William Buchanan | Postal Inspector | General Post-Office | — | — |
| 1880 | William Buchanan | Postal Inspectors | General Post Office | — | — |

### Deterministic checks: `buchanan_walter-clarke_b1838` vs `Buchanan, William___New South Wales___1877`

- [PASS] surname_gate: bio 'BUCHANAN' vs stint 'Buchanan, William' (exact)
- [PASS] initials: bio ['W', 'C'] ~ stint ['W']
- [PASS] age_gate: stint starts 1877, birth 1838 (age 39)
- [FAIL] colony: no placed event resolves to 'New South Wales'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1880
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

