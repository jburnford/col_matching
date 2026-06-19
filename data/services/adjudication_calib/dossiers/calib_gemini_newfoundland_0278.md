<!-- {"case_id": "calib_gemini_newfoundland_0278", "bio_ids": ["casey_james-joseph_e1878"], "stint_ids": ["Casey, John___Newfoundland___1877"]} -->
# Dossier calib_gemini_newfoundland_0278

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 21 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `casey_james-joseph_e1878`

- Printed name: **CASEY, JAMES JOSEPH**
- Birth year: not printed
- Honours: C.M.G
- Appears in editions: [1886, 1888]

### Verbatim printed entry text (OCR)

**Version `col1886-L32589.v` — printed in editions [1886, 1888]:**

> CASEY, JAMES JOSEPH, C.M.G., 1878.—Was president of the Victoria commission and executive commissioner for the colony at the Paris Exhibition, 1878.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1878 | Was president of the Victoria commission and executive commissioner for the colony at the Paris Exhibition | — | [1886, 1888] |

## Candidate stint `Casey, John___Newfoundland___1877`

- Staff-list name: **Casey, John** | colony: **Newfoundland** | listed 1877–1890 | editions [1877, 1878, 1879, 1880, 1883, 1886, 1888, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | John Casey | Commissioner of Poor | Civil Establishment | — | — |
| 1878 | John Casey | Commissioner of Poor | Civil Establishment | — | — |
| 1879 | John Casey | Commissioner of Poor | Civil Establishment | — | — |
| 1880 | John Casey | Commissioner of Poor | Civil Establishment | — | — |
| 1883 | John Casey | Commissioner of Poor | Civil Establishment | — | — |
| 1886 | John Casey | Commissioner of Poor | Civil Establishment | — | — |
| 1888 | John Casey | Commissioner of Poor | Civil Establishment | — | — |
| 1890 | John Casey | Commissioner of Poor | Civil Establishment | — | — |

### Deterministic checks: `casey_james-joseph_e1878` vs `Casey, John___Newfoundland___1877`

- [PASS] surname_gate: bio 'CASEY' vs stint 'Casey, John' (exact)
- [PASS] initials: bio ['J', 'J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Newfoundland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1890
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

