<!-- {"case_id": "case_mcdonald_george_e1876", "bio_ids": ["mcdonald_george_e1876"], "stint_ids": ["McDonald, G. T___Victoria___1878"]} -->
# Dossier case_mcdonald_george_e1876

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 87 official(s) with this surname in the graph's staff lists; 30 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['mcdonald_george_e1876'] carry a single initial only — the namesake trap applies.

## Biography `mcdonald_george_e1876`

- Printed name: **McDONALD, GEORGE**
- Birth year: not printed
- Appears in editions: [1899]

### Verbatim printed entry text (OCR)

**Version `col1899-L36145.v` — printed in editions [1899]:**

> McDONALD, GEORGE.—1st class Queen's scholar, 1876; sen. master, academy, Banbury, 1877; sen. master, Br. schl., London, N.W., 1878; ditto, Eastbourne schls., 1881; sen. asst. to H.M.'s inspr. of schls., Marylebone, 1883; dir. of educn., G. Coast, June, 1893. Author of several schoolbooks and manuals.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1876–1876 | 1st class Queen's scholar | — | [1899] |
| 1 | 1877–1877 | sen. master, academy | — | [1899] |
| 2 | 1878–1878 | sen. master, Br. schl. | — | [1899] |
| 3 | 1881–1881 | ditto | — | [1899] |
| 4 | 1883–1883 | sen. asst. to H.M.'s inspr. of schls. | — | [1899] |
| 5 | 1893 | dir. of educn. | Gold Coast | [1899] |

## Candidate stint `McDonald, G. T___Victoria___1878`

- Staff-list name: **McDonald, G. T** | colony: **Victoria** | listed 1878–1879 | editions [1878, 1879]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1878 | G. T. McDonald | District Surveyor | Commissioner of Crown Lands and Survey Division | — | — |
| 1879 | G. T. McDonald | District Surveyor | District Surveyors | — | — |

### Deterministic checks: `mcdonald_george_e1876` vs `McDonald, G. T___Victoria___1878`

- [PASS] surname_gate: bio 'McDONALD' vs stint 'McDonald, G. T' (exact)
- [PASS] initials: bio ['G'] ~ stint ['G', 'T']
- [PASS] age_gate: stint starts 1878; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Victoria'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1878-1879
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

