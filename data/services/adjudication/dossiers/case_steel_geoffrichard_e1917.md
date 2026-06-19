<!-- {"case_id": "case_steel_geoffrichard_e1917", "bio_ids": ["steel_geoffrichard_e1917"], "stint_ids": ["Steel, E. G___Western Pacific___1965", "Steel, George___Canada___1905", "Steel, O. G___New South Wales___1906"]} -->
# Dossier case_steel_geoffrichard_e1917

## Case context

- 1 biography(ies) and 3 candidate stint(s) are entangled in this case.
- Corpus context: 12 official(s) with this surname in the graph's staff lists; 10 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['steel_geoffrichard_e1917'] carry a single initial only — the namesake trap applies.

## Biography `steel_geoffrichard_e1917`

- Printed name: **STEEL, GEOFFRICHARD**
- Birth year: not printed
- Appears in editions: [1930]

### Verbatim printed entry text (OCR)

**Version `col1930-L68415.v` — printed in editions [1930]:**

> STEEL, GEOFFRICHARD, M.R.C.S. (Eng.) L.R.C.P. (Lond.), Cert. London S.H.T.M. (distincte) D.T.M. & H. (Eng.)—Milly. serv., 1917-19; med. offr., Tanganyika Territory, Jan., 1925.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1917–1919 | Milly. serv | — | [1930] |
| 1 | 1925 | med. offr., Tanganyika Territory | Tanganyika | [1930] |

## Candidate stint `Steel, E. G___Western Pacific___1965`

- Staff-list name: **Steel, E. G** | colony: **Western Pacific** | listed 1965–1966 | editions [1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1965 | E. G. Steel | Manager | Bermuda Trade Development Board | — | — |
| 1966 | E. G. Steel | Manager | Bermuda Trade Development Board | — | — |

### Deterministic checks: `steel_geoffrichard_e1917` vs `Steel, E. G___Western Pacific___1965`

- [PASS] surname_gate: bio 'STEEL' vs stint 'Steel, E. G' (exact)
- [PASS] initials: bio ['G'] ~ stint ['E', 'G']
- [PASS] age_gate: stint starts 1965; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Western Pacific'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1965-1966
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Steel, George___Canada___1905`

- Staff-list name: **Steel, George** | colony: **Canada** | listed 1905–1915 | editions [1905, 1906, 1908, 1912, 1914, 1915]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | George Steel | Member of Legislative Assembly | Legislative Assembly | — | — |
| 1906 | George Steel | Member for Cypress | Legislative Assembly | — | — |
| 1908 | George Steel | Member | Legislative Assembly | — | — |
| 1912 | George Steel | Member | Members | — | — |
| 1914 | George Steel | Member of Legislative Assembly | Legislative Assembly | — | — |
| 1915 | George Steel | Member for Cypress | — | — | — |

### Deterministic checks: `steel_geoffrichard_e1917` vs `Steel, George___Canada___1905`

- [PASS] surname_gate: bio 'STEEL' vs stint 'Steel, George' (exact)
- [PASS] initials: bio ['G'] ~ stint ['G']
- [PASS] age_gate: stint starts 1905; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1915
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Steel, O. G___New South Wales___1906`

- Staff-list name: **Steel, O. G** | colony: **New South Wales** | listed 1906–1917 | editions [1906, 1917]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1906 | O. G. Steel | Vice-President | Hunter District Water Supply and Sewerage Board | — | — |
| 1917 | O. G. Steel | District Representative | Hunter District Water Supply and Sewerage Board | — | — |

### Deterministic checks: `steel_geoffrichard_e1917` vs `Steel, O. G___New South Wales___1906`

- [PASS] surname_gate: bio 'STEEL' vs stint 'Steel, O. G' (exact)
- [PASS] initials: bio ['G'] ~ stint ['O', 'G']
- [PASS] age_gate: stint starts 1906; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'New South Wales'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1906-1917
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

