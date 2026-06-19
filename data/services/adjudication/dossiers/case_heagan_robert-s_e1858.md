<!-- {"case_id": "case_heagan_robert-s_e1858", "bio_ids": ["heagan_robert-s_e1858"], "stint_ids": ["Heagan, R. S___Leeward Islands___1877"]} -->
# Dossier case_heagan_robert-s_e1858

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `heagan_robert-s_e1858`

- Printed name: **HEAGAN, ROBERT S**
- Birth year: not printed
- Appears in editions: [1883, 1886, 1888]

### Verbatim printed entry text (OCR)

**Version `col1883-L27934.v` — printed in editions [1883, 1886, 1888]:**

> HEAGAN, ROBERT S.—Inspector of weights and measures, Antigua, 1858; clerk to road commissioners, and secretary of the board of health, 1861; excise officer, 1864; clerk of vestries, 1871; clerk of parochial boards, 1874; is an elected member of the legislative council.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1858 | Inspector of weights and measures | Antigua | [1883, 1886, 1888] |
| 1 | 1861 | clerk to road commissioners, and secretary of the board of health | Antigua *(inherited from previous clause)* | [1883, 1886, 1888] |
| 2 | 1864 | excise officer | Antigua *(inherited from previous clause)* | [1883, 1886, 1888] |
| 3 | 1871 | clerk of vestries | Antigua *(inherited from previous clause)* | [1883, 1886, 1888] |
| 4 | 1874 | clerk of parochial boards | Antigua *(inherited from previous clause)* | [1883, 1886, 1888] |

## Candidate stint `Heagan, R. S___Leeward Islands___1877`

- Staff-list name: **Heagan, R. S** | colony: **Leeward Islands** | listed 1877–1886 | editions [1877, 1879, 1880, 1883, 1886]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | R. S. Heagan | Secretary to the Board of Health | Civil Establishment | — | — |
| 1877 | R. S. Heagan | Member | Legislative Council (Local) | — | — |
| 1879 | R. S. Heagan | Vice-President | Legislative Council (Local) | — | — |
| 1879 | R. S. Heagan | Secretary to the Board of Health | Civil Establishment | — | — |
| 1880 | R. S. Heagan | Secretary to the Board of Health | Civil Establishment | — | — |
| 1880 | R. S. Heagan | Member | Legislative Council (Local) | — | — |
| 1883 | R. S. Heagan | Secretary to the Board of Health | Civil Establishment | — | — |
| 1886 | R. S. Heagan | Secretary to the Board of Health | Civil Establishment | — | — |

### Deterministic checks: `heagan_robert-s_e1858` vs `Heagan, R. S___Leeward Islands___1877`

- [PASS] surname_gate: bio 'HEAGAN' vs stint 'Heagan, R. S' (exact)
- [PASS] initials: bio ['R', 'S'] ~ stint ['R', 'S']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1886
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

