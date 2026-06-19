<!-- {"case_id": "case_macdonell_d_e1904", "bio_ids": ["macdonell_d_e1904"], "stint_ids": ["Macdonell, D. W___Canada___1883"]} -->
# Dossier case_macdonell_d_e1904

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['macdonell_d_e1904'] carry a single initial only — the namesake trap applies.

## Biography `macdonell_d_e1904`

- Printed name: **MACDONELL, D**
- Birth year: not printed
- Appears in editions: [1911]

### Verbatim printed entry text (OCR)

**Version `col1911-L46406.v` — printed in editions [1911]:**

> MACDONELL, HON. D.—M.L.A., N.S. Wales, 1904; col. sec. and min. of agric. Oct., 1910.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1904 | M.L.A., N.S. Wales | Nova Scotia | [1911] |
| 1 | 1910 | col. sec. and min. of agric | Nova Scotia *(inherited from previous clause)* | [1911] |

## Candidate stint `Macdonell, D. W___Canada___1883`

- Staff-list name: **Macdonell, D. W** | colony: **Canada** | listed 1883–1890 | editions [1883, 1888, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1883 | D. W. Macdonell | Sergeant-at-Arms | House of Commons | — | — |
| 1888 | D. W. Macdonell | Sergeant-at-Arms | House of Commons | — | — |
| 1890 | D. W. Macdonell | Sergeant-at-Arms | House of Commons | — | — |

### Deterministic checks: `macdonell_d_e1904` vs `Macdonell, D. W___Canada___1883`

- [PASS] surname_gate: bio 'MACDONELL' vs stint 'Macdonell, D. W' (exact)
- [PASS] initials: bio ['D'] ~ stint ['D', 'W']
- [PASS] age_gate: stint starts 1883; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1883-1890
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

