<!-- {"case_id": "case_mercer_guy-henry-vifnot_e1895", "bio_ids": ["mercer_guy-henry-vifnot_e1895"], "stint_ids": ["Mercer, G. H___Mauritius___1920"]} -->
# Dossier case_mercer_guy-henry-vifnot_e1895

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 18 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mercer_guy-henry-vifnot_e1895`

- Printed name: **MERCER, GUY HENRY VIFNOT**
- Birth year: not printed
- Appears in editions: [1910]

### Verbatim printed entry text (OCR)

**Version `col1910-L47545.v` — printed in editions [1910]:**

> MERCER, GUY HENRY VIFNOT.—2nd clk., registr. and provost-marshal's office, Antigua, 1895; 4th clk., col. sec.'s office, 1897; clk. to registr. and provost-marshal, Nevis, 1898; dep. coroner, Nevis, 1901; rev. offr., Nevis, 1901; clk., British vice-consulate, Chinde, Apr., 1905.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1895 | 2nd clk., registr. and provost-marshal's office | Antigua | [1910] |
| 1 | 1897 | 4th clk., col. sec.'s office | Antigua *(inherited from previous clause)* | [1910] |
| 2 | 1898 | clk. to registr. and provost-marshal | Nevis | [1910] |
| 3 | 1901 | dep. coroner | Nevis | [1910] |
| 4 | 1905 | clk., British vice-consulate, Chinde | Nevis *(inherited from previous clause)* | [1910] |

## Candidate stint `Mercer, G. H___Mauritius___1920`

- Staff-list name: **Mercer, G. H** | colony: **Mauritius** | listed 1920–1923 | editions [1920, 1921, 1922, 1923]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1920 | G. H. Mercer | Civil Chaplain | Church of England | — | — |
| 1921 | G. H. Mercer | Civil Chaplain | Church of England | — | — |
| 1922 | G. H. Mercer | Civil Chaplain | Church of England | — | — |
| 1923 | G. H. Mercer | Civil Chaplain | Church of England | — | — |

### Deterministic checks: `mercer_guy-henry-vifnot_e1895` vs `Mercer, G. H___Mauritius___1920`

- [PASS] surname_gate: bio 'MERCER' vs stint 'Mercer, G. H' (exact)
- [PASS] initials: bio ['G', 'H', 'V'] ~ stint ['G', 'H']
- [PASS] age_gate: stint starts 1920; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Mauritius'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1920-1923
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

