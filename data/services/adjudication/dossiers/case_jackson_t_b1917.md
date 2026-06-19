<!-- {"case_id": "case_jackson_t_b1917", "bio_ids": ["jackson_t_b1917"], "stint_ids": ["Jackson, T. H___Kenya___1950"]} -->
# Dossier case_jackson_t_b1917

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 144 official(s) with this surname in the graph's staff lists; 60 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['jackson_t_b1917'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Jackson, T. H___Kenya___1950` is also gate-compatible with biography(ies) outside this case: ['jackson_theodore-herbert_b1912'] (already linked elsewhere or filtered).

## Biography `jackson_t_b1917`

- Printed name: **JACKSON, T**
- Birth year: 1917 (attested in editions [1962])
- Appears in editions: [1962]

### Verbatim printed entry text (OCR)

**Version `col1962-L22737.v` — printed in editions [1962]:**

> JACKSON, T.—b. 1917; ed. Manchester Gram. Sch.; mil. serv. 1940–46, lieut.; exec. engr., Tang., 1951.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1951 | exec. engr. | Tanganyika | [1962] |

## Candidate stint `Jackson, T. H___Kenya___1950`

- Staff-list name: **Jackson, T. H** | colony: **Kenya** | listed 1950–1951 | editions [1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | T. H. Jackson | Agricultural Officer | AGRICULTURE | — | — |
| 1951 | T. H. Jackson | Agricultural Officer | Agriculture | — | — |

### Deterministic checks: `jackson_t_b1917` vs `Jackson, T. H___Kenya___1950`

- [PASS] surname_gate: bio 'JACKSON' vs stint 'Jackson, T. H' (exact)
- [PASS] initials: bio ['T'] ~ stint ['T', 'H']
- [PASS] age_gate: stint starts 1950, birth 1917 (age 33)
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1950-1951
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

