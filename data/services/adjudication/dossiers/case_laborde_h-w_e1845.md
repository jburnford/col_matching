<!-- {"case_id": "case_laborde_h-w_e1845", "bio_ids": ["laborde_h-w_e1845"], "stint_ids": ["Laborde, H. W___St Vincent___1879", "Laborde, H. W___Windward Islands___1877"]} -->
# Dossier case_laborde_h-w_e1845

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 15 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `laborde_h-w_e1845`

- Printed name: **LABORDE, H. W**
- Birth year: not printed
- Appears in editions: [1883, 1886, 1888, 1889, 1890, 1894]

### Verbatim printed entry text (OCR)

**Version `col1883-L28276.v` — printed in editions [1883, 1886, 1888, 1889, 1890, 1894]:**

> LABORDE, REV. H. W.—Rector of St. George's and St. Andrew's parishes, and chaplain of the gaol, St. Vincent, 1852; M.A. Cambridge, where he graduated B.A., 1845; was ordained assistant curate in St. Vincent, 1845; was minister of All Saints, chapel and garrison, chaplain of the island of Trinidad, 1850 to 1852; is chaplain to the Bishop of Barbados; rural dean, St. Vincent, 1864; and also member of the legislative council.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1845 | M.A. Cambridge, where he graduated B.A | St. Vincent *(inherited from previous clause)* | [1883, 1886, 1888, 1889, 1890, 1894] |
| 1 | 1850–1852 | was minister of All Saints, chapel and garrison, chaplain of the island of Trinidad | St. Vincent *(inherited from previous clause)* | [1883, 1886, 1888, 1889, 1890, 1894] |
| 2 | 1852 | Rector of St. George's and St. Andrew's parishes, and chaplain of the gaol | St. Vincent | [1883, 1886, 1888, 1889, 1890, 1894] |
| 3 | 1864 | rural dean | St. Vincent | [1883, 1886, 1888, 1889, 1890, 1894] |

## Candidate stint `Laborde, H. W___St Vincent___1879`

- Staff-list name: **Laborde, H. W** | colony: **St Vincent** | listed 1879–1890 | editions [1879, 1880, 1888, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1879 | Rev. H. W. Laborde | Rectors | Ministers of Religion | — | — |
| 1880 | H. W. Laborde | Rectors | Ministers of Religion | — | — |
| 1888 | H. W. Laborde | Rector | Chief Ministers of Religion | — | — |
| 1890 | Rev. H. W. Laborde | Anglican Rector | Chief Ministers of Religion | — | — |

### Deterministic checks: `laborde_h-w_e1845` vs `Laborde, H. W___St Vincent___1879`

- [PASS] surname_gate: bio 'LABORDE' vs stint 'Laborde, H. W' (exact)
- [PASS] initials: bio ['H', 'W'] ~ stint ['H', 'W']
- [PASS] age_gate: stint starts 1879; no printed birth year — UNCHECKED
- [PASS] colony: 4 placed event(s) resolve to 'St Vincent'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1879-1890
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Laborde, H. W___Windward Islands___1877`

- Staff-list name: **Laborde, H. W** | colony: **Windward Islands** | listed 1877–1889 | editions [1877, 1878, 1880, 1883, 1889]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | H. W. Laborde | Rector | Ministers of Religion | — | — |
| 1878 | H. W. Laborde | Rectors | Ministers of Religion | — | — |
| 1880 | H. W. Laborde | Rector | Ministers of Religion | — | — |
| 1883 | H. W. Laborde | Rector | Ministers of Religion | — | — |
| 1889 | Rev. H. W. Laborde | Rector | Chief Ministers of Religion | — | — |

### Deterministic checks: `laborde_h-w_e1845` vs `Laborde, H. W___Windward Islands___1877`

- [PASS] surname_gate: bio 'LABORDE' vs stint 'Laborde, H. W' (exact)
- [PASS] initials: bio ['H', 'W'] ~ stint ['H', 'W']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Windward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1889
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

