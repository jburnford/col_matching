<!-- {"case_id": "case_trudeau_t_e1864", "bio_ids": ["trudeau_t_e1864"], "stint_ids": ["Trudeau, T___Canada___1877"]} -->
# Dossier case_trudeau_t_e1864

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['trudeau_t_e1864'] carry a single initial only — the namesake trap applies.

## Biography `trudeau_t_e1864`

- Printed name: **TRUDEAU, T**
- Birth year: not printed
- Appears in editions: [1886, 1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1886-L36048.v` — printed in editions [1886, 1888, 1889, 1890]:**

> TRUDEAU, T., C.E.—Secretary, department of public works, Canada, 1869; chief engineer, 1864; deputy minister of railways and canals, 1864.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1864 | chief engineer | Canada *(inherited from previous clause)* | [1886, 1888, 1889, 1890] |
| 1 | 1869 | Secretary, department of public works | Canada | [1886, 1888, 1889, 1890] |

## Candidate stint `Trudeau, T___Canada___1877`

- Staff-list name: **Trudeau, T** | colony: **Canada** | listed 1877–1890 | editions [1877, 1878, 1879, 1880, 1883, 1886, 1888, 1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | T. Trudeau | Deputy Commissioner | PUBLIC WORKS | — | — |
| 1878 | T. Trudeau | Deputy Commissioner | Public Works | — | — |
| 1879 | T. Trudeau | Deputy Commissioner | Public Works | — | — |
| 1880 | T. Trudeau | Deputy Minister | Railways and Canals | — | — |
| 1883 | T. Trudeau | Deputy Minister | Railways and Canals | — | — |
| 1886 | T. Trudeau | Deputy Minister | RAILWAYS AND CANALS | — | — |
| 1888 | T. Trudeau | Deputy Minister | Railways and Canals | — | — |
| 1889 | T. Trudeau | Deputy Minister | Railways and Canals | — | — |
| 1890 | T. Trudeau | Deputy Minister | Railways and Canals | — | — |

### Deterministic checks: `trudeau_t_e1864` vs `Trudeau, T___Canada___1877`

- [PASS] surname_gate: bio 'TRUDEAU' vs stint 'Trudeau, T' (exact)
- [PASS] initials: bio ['T'] ~ stint ['T']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Canada'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1890
- [FAIL] position_sim: best 39 vs bar 60: 'Secretary, department of public works' ~ 'Deputy Minister'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

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

