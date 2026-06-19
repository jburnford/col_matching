<!-- {"case_id": "case_oldfield_h_e1919", "bio_ids": ["oldfield_h_e1919"], "stint_ids": ["Oldfield, H. W___Gibraltar___1930"]} -->
# Dossier case_oldfield_h_e1919

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['oldfield_h_e1919'] carry a single initial only — the namesake trap applies.

## Biography `oldfield_h_e1919`

- Printed name: **OLDFIELD, H.**
- Birth year: not printed
- Appears in editions: [1937]

### Verbatim printed entry text (OCR)

**Version `col1937-L63710.v` — printed in editions [1937]:**

> OLDFIELD, H. geria, May-Dec., 1921; ag. res., Prot., June, 1919, to May, 1922; lieut.-gov., N.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1919–1922 | ag. res. | — | [1937] |
| 1 | 1921–1921 | — | Nigeria | [1937] |
| 2 | ? | lieut.-gov. | — | [1937] |

## Candidate stint `Oldfield, H. W___Gibraltar___1930`

- Staff-list name: **Oldfield, H. W** | colony: **Gibraltar** | listed 1930–1931 | editions [1930, 1931]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1930 | H. W. Oldfield | Senior Chaplain to the Forces | Chief Military and Naval Officers | — | — |
| 1931 | H. W. Oldfield | Senior Chaplain to the Forces | Chief Military and Naval Officers | — | — |

### Deterministic checks: `oldfield_h_e1919` vs `Oldfield, H. W___Gibraltar___1930`

- [PASS] surname_gate: bio 'OLDFIELD' vs stint 'Oldfield, H. W' (exact)
- [PASS] initials: bio ['H'] ~ stint ['H', 'W']
- [PASS] age_gate: stint starts 1930; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Gibraltar'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1930-1931
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

