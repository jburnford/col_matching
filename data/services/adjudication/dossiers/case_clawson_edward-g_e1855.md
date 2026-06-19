<!-- {"case_id": "case_clawson_edward-g_e1855", "bio_ids": ["clawson_edward-g_e1855", "clawson_edward-g_e1859"], "stint_ids": ["Clawson, E. G___Windward Islands___1877"]} -->
# Dossier case_clawson_edward-g_e1855

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Clawson, E. G___Windward Islands___1877'] have more than one claimant biography in this case.

## Biography `clawson_edward-g_e1855`

- Printed name: **CLAWSON, EDWARD G**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L26872.v` — printed in editions [1883]:**

> CLAWSON, EDWARD G.—Harbour and shipping-master, Barbados, May, 1855.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1855 | Harbour and shipping-master | Barbados | [1883] |

## Biography `clawson_edward-g_e1859`

- Printed name: **CLAWSON, Edward G**
- Birth year: not printed
- Appears in editions: [1886, 1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1886-L32696.v` — printed in editions [1886, 1888, 1889, 1890]:**

> CLAWSON, Edward G.—Harbour master, quarantine officer, and captain of the port, Barbados, June, 1859.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1859 | Harbour master, quarantine officer, and captain of the port | Barbados | [1886, 1888, 1889, 1890] |

## Candidate stint `Clawson, E. G___Windward Islands___1877`

- Staff-list name: **Clawson, E. G** | colony: **Windward Islands** | listed 1877–1883 | editions [1877, 1878, 1879, 1880, 1883]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | E. G. Clawson | Harbour-Master | Harbour-Master's Office | — | — |
| 1878 | E. G. Clawson | Harbour-Master | Harbour-Master's Office | — | — |
| 1879 | E. G. Clawson | Harbour-Master | Harbour-Master's Office | — | — |
| 1880 | E. G. Clawson | Harbour-Master | Harbour-Master's Office | — | — |
| 1883 | E. G. Clawson | Harbour-Master | Harbour-Master's Office | — | — |

### Deterministic checks: `clawson_edward-g_e1855` vs `Clawson, E. G___Windward Islands___1877`

- [PASS] surname_gate: bio 'CLAWSON' vs stint 'Clawson, E. G' (exact)
- [PASS] initials: bio ['E', 'G'] ~ stint ['E', 'G']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Windward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1883
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `clawson_edward-g_e1859` vs `Clawson, E. G___Windward Islands___1877`

- [PASS] surname_gate: bio 'CLAWSON' vs stint 'Clawson, E. G' (exact)
- [PASS] initials: bio ['E', 'G'] ~ stint ['E', 'G']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Windward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1883
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

