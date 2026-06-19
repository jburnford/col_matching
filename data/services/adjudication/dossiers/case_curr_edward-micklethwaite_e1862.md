<!-- {"case_id": "case_curr_edward-micklethwaite_e1862", "bio_ids": ["curr_edward-micklethwaite_e1862"], "stint_ids": ["Curr, E. M___Victoria___1877", "Curr, E. M___Victoria___1889"]} -->
# Dossier case_curr_edward-micklethwaite_e1862

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `curr_edward-micklethwaite_e1862`

- Printed name: **CURR, EDWARD MICKLETHWAITE**
- Birth year: not printed
- Appears in editions: [1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1888-L32911.v` — printed in editions [1888, 1889, 1890]:**

> CURR, EDWARD MICKLETHWAITE.—Inspector of sheep, Victoria, Nov., 1862; chief inspector, May, 1864, and chief inspector of stock, Jan., 1873; is author of "Pure Saddle Horses," "Recollection of Squatting in Victoria," "The Australian Race its Origin and Languages."

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1862 | Inspector of sheep | Victoria | [1888, 1889, 1890] |
| 1 | 1864 | chief inspector | Victoria *(inherited from previous clause)* | [1888, 1889, 1890] |
| 2 | 1873 | chief inspector of stock | Victoria *(inherited from previous clause)* | [1888, 1889, 1890] |

## Candidate stint `Curr, E. M___Victoria___1877`

- Staff-list name: **Curr, E. M** | colony: **Victoria** | listed 1877–1883 | editions [1877, 1879, 1880, 1883]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | E. M. Curr | Chief Inspector | Inspector of Stock | — | — |
| 1879 | E. M. Curr | Chief Inspector | Inspector of Stock | — | — |
| 1880 | E. M. Curr | Chief Inspector | Inspector of Stock | — | — |
| 1883 | E. M. Curr | Chief Inspector | Inspector of Stock | — | — |

### Deterministic checks: `curr_edward-micklethwaite_e1862` vs `Curr, E. M___Victoria___1877`

- [PASS] surname_gate: bio 'CURR' vs stint 'Curr, E. M' (exact)
- [PASS] initials: bio ['E', 'M'] ~ stint ['E', 'M']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 3 placed event(s) resolve to 'Victoria'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1883
- [PASS] position_sim: best 100 vs bar 60: 'chief inspector of stock' ~ 'Chief Inspector'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

## Candidate stint `Curr, E. M___Victoria___1889`

- Staff-list name: **Curr, E. M** | colony: **Victoria** | listed 1889–1890 | editions [1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1889 | E. M. Curr | Chief Inspector of Stock | Department of Agriculture | — | — |
| 1890 | E. M. Curr | Chief Inspector of Stock | Department of Agriculture | — | — |

### Deterministic checks: `curr_edward-micklethwaite_e1862` vs `Curr, E. M___Victoria___1889`

- [PASS] surname_gate: bio 'CURR' vs stint 'Curr, E. M' (exact)
- [PASS] initials: bio ['E', 'M'] ~ stint ['E', 'M']
- [PASS] age_gate: stint starts 1889; no printed birth year — UNCHECKED
- [PASS] colony: 3 placed event(s) resolve to 'Victoria'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1889-1890
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

