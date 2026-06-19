<!-- {"case_id": "case_goodbun_george-edward_e1848", "bio_ids": ["goodbun_george-edward_e1848"], "stint_ids": ["Goodban, Emily___Trinidad___1879", "Goodban, G. E___Cape of Good Hope___1877"]} -->
# Dossier case_goodbun_george-edward_e1848

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `goodbun_george-edward_e1848`

- Printed name: **GOODBUN, GEORGE EDWARD**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L27680.v` — printed in editions [1883]:**

> GOODBUN, GEORGE EDWARD.—3rd clerk, audit office, 1st Oct., 1848, to 18th Oct., 1858; secretary to harbour board, Cape Town, 1st Jan., 1855, to 31st July, 1857; 2nd clerk, audit office, 19th Oct., 1858, to 14th Jan., 1860; 1st clerk, audit office, 15th Jan., 1860, to 30th Sept., 1867; chief clerk, general management department, customs, Cape Town, 1st Oct., 1867, to 30th June, 1876; assistant collector and controller of customs from 1st July, 1876.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1848–1858 | 3rd clerk, audit office | — | [1883] |
| 1 | 1855–1857 | secretary to harbour board | Cape Town | [1883] |
| 2 | 1858–1860 | 2nd clerk, audit office | — | [1883] |
| 3 | 1860–1867 | 1st clerk, audit office | — | [1883] |
| 4 | 1867–1876 | chief clerk, general management department, customs | Cape Town | [1883] |
| 5 | 1876 | assistant collector and controller of customs | — | [1883] |

## Candidate stint `Goodban, Emily___Trinidad___1879`

- Staff-list name: **Goodban, Emily** | colony: **Trinidad** | listed 1879–1880 | editions [1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1879 | Miss Emily Goodban | Lady Superintendent of Nurses | Medical Establishment | — | — |
| 1880 | Emily Goodban | Lady Superintendent of Nurses | Colonial Hospital, Port of Spain | — | — |

### Deterministic checks: `goodbun_george-edward_e1848` vs `Goodban, Emily___Trinidad___1879`

- [PASS] surname_gate: bio 'GOODBUN' vs stint 'Goodban, Emily' (fuzzy:1)
- [PASS] initials: bio ['G', 'E'] ~ stint ['E']
- [PASS] age_gate: stint starts 1879; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Trinidad'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1879-1880
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Goodban, G. E___Cape of Good Hope___1877`

- Staff-list name: **Goodban, G. E** | colony: **Cape of Good Hope** | listed 1877–1880 | editions [1877, 1878, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | G. E. Goodban | Assistant Collector | General Management Department | — | — |
| 1878 | G. E. Goodban | Assistant Collector | General Management Department | — | — |
| 1880 | G. E. Goodban | Assistant Collector and Controller | General Management Department | — | — |

### Deterministic checks: `goodbun_george-edward_e1848` vs `Goodban, G. E___Cape of Good Hope___1877`

- [PASS] surname_gate: bio 'GOODBUN' vs stint 'Goodban, G. E' (fuzzy:1)
- [PASS] initials: bio ['G', 'E'] ~ stint ['G', 'E']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Cape of Good Hope'
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

