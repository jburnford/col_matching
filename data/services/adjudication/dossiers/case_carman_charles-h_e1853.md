<!-- {"case_id": "case_carman_charles-h_e1853", "bio_ids": ["carman_charles-h_e1853"], "stint_ids": ["Carman, C. H___Canada___1883"]} -->
# Dossier case_carman_charles-h_e1853

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `carman_charles-h_e1853`

- Printed name: **CARMAN, Charles H**
- Birth year: not printed
- Appears in editions: [1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1889-L32194.v` — printed in editions [1889, 1890]:**

> CARMAN, Charles H.—Served in crown land... office, Nova Scotia, 1853-54; chief clerk of mines and minerals, 1864.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1853–1854 | Served in crown land... office | Nova Scotia | [1889, 1890] |
| 1 | 1864 | chief clerk of mines and minerals | Nova Scotia *(inherited from previous clause)* | [1889, 1890] |

## Candidate stint `Carman, C. H___Canada___1883`

- Staff-list name: **Carman, C. H** | colony: **Canada** | listed 1883–1890 | editions [1883, 1886, 1888, 1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1883 | C. H. Carman | Chief Clerk of Mines and Minerals | Department of Mines and Public Works | — | — |
| 1886 | C. H. Carman | Chief Clerk of Mines and Minerals | Department of Mines and Public Works | — | — |
| 1888 | C. H. Carman | Chief Clerk of Mines and Minerals | Department of Mines and Public Works | — | — |
| 1889 | C. H. Carman | Chief Clerk of Mines and Minerals | Departmental Chiefs and Officers | — | — |
| 1890 | C. H. Carman | Chief Clerk of Mines and Minerals | Departmental Chiefs and Officers | — | — |

### Deterministic checks: `carman_charles-h_e1853` vs `Carman, C. H___Canada___1883`

- [PASS] surname_gate: bio 'CARMAN' vs stint 'Carman, C. H' (exact)
- [PASS] initials: bio ['C', 'H'] ~ stint ['C', 'H']
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

