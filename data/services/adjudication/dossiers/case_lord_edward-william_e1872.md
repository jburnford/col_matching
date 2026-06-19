<!-- {"case_id": "case_lord_edward-william_e1872", "bio_ids": ["lord_edward-william_e1872"], "stint_ids": ["Lord, E. W___St Lucia___1888", "Lord, E.W___Windward Islands___1883"]} -->
# Dossier case_lord_edward-william_e1872

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 33 official(s) with this surname in the graph's staff lists; 10 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `lord_edward-william_e1872`

- Printed name: **LORD, EDWARD WILLIAM**
- Birth year: not printed
- Appears in editions: [1886, 1888, 1889, 1890, 1894, 1896, 1897]

### Verbatim printed entry text (OCR)

**Version `col1886-L34542.v` — printed in editions [1886, 1888, 1889, 1890, 1894, 1896, 1897]:**

> LORD, EDWARD WILLIAM.—Entered police department, St. Lucia, 1872; acted keeper of the prison, Oct., 1876, to Mar., 1877; sub-inspector of revenue and police, Jan., 1880; chief revenue officer and landing waiter, Jan., 1882.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1872 | police department | St. Lucia | [1886, 1888, 1889, 1890, 1894, 1896, 1897] |
| 1 | 1876–1877 | acted keeper of the prison | — | [1886, 1888, 1889, 1890, 1894, 1896, 1897] |
| 2 | 1880 | sub-inspector of revenue and police | — | [1886, 1888, 1889, 1890, 1894, 1896, 1897] |
| 3 | 1882 | chief revenue officer and landing waiter | — | [1886, 1888, 1889, 1890, 1894, 1896, 1897] |

## Candidate stint `Lord, E. W___St Lucia___1888`

- Staff-list name: **Lord, E. W** | colony: **St Lucia** | listed 1888–1890 | editions [1888, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | E. W. Lord | Chief Landing Waiter and Revenue Officer | Treasury, Customs, and Inland Revenue Department | — | — |
| 1890 | E. W. Lord | Chief Landing Waiter and Revenue Officer | Treasury, Customs, and Inland Revenue Department | — | — |

### Deterministic checks: `lord_edward-william_e1872` vs `Lord, E. W___St Lucia___1888`

- [PASS] surname_gate: bio 'LORD' vs stint 'Lord, E. W' (exact)
- [PASS] initials: bio ['E', 'W'] ~ stint ['E', 'W']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'St Lucia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1888-1890
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Lord, E.W___Windward Islands___1883`

- Staff-list name: **Lord, E.W** | colony: **Windward Islands** | listed 1883–1889 | editions [1883, 1889]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1883 | E.W. Lord | Chief Landing Waiter and Revenue Officer | Treasury, Customs, and Inland Revenue Department | — | — |
| 1889 | E. W. Lord | Chief Landing Waiter and Revenue Officer | Treasury, Customs, and Inland Revenue Department | — | — |

### Deterministic checks: `lord_edward-william_e1872` vs `Lord, E.W___Windward Islands___1883`

- [PASS] surname_gate: bio 'LORD' vs stint 'Lord, E.W' (exact)
- [PASS] initials: bio ['E', 'W'] ~ stint ['E', 'W']
- [PASS] age_gate: stint starts 1883; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Windward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1883-1889
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

