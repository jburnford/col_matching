<!-- {"case_id": "case_perren_g-e_b1917", "bio_ids": ["perren_g-e_b1917"], "stint_ids": ["Perrin, G___North Borneo___1949"]} -->
# Dossier case_perren_g-e_b1917

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Perrin, G___North Borneo___1949` is also gate-compatible with biography(ies) outside this case: ['perrin_geo-samuel_e1880'] (already linked elsewhere or filtered).

## Biography `perren_g-e_b1917`

- Printed name: **PERREN, G. E.**
- Birth year: 1917 (attested in editions [1958, 1959, 1960, 1961, 1962])
- Appears in editions: [1958, 1959, 1960, 1961, 1962]

### Verbatim printed entry text (OCR)

**Version `col1958-L25939.v` — printed in editions [1958, 1959, 1960, 1961, 1962]:**

> PERREN, G. E.—b. 1917; ed. London Univ.; mil. serv., 1940-46, R.N.; educ. offr., Ken., 1947.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1940–1946 | mil. serv. | — | [1958, 1959, 1960, 1961, 1962] |
| 1 | 1947 | educ. offr. | Kenya | [1958, 1959, 1960, 1961, 1962] |

## Candidate stint `Perrin, G___North Borneo___1949`

- Staff-list name: **Perrin, G** | colony: **North Borneo** | listed 1949–1950 | editions [1949, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | G. Perrin | Labour Adviser | Labour Department | — | — |
| 1950 | G. Perrin | Labour Adviser | Labour | — | — |

### Deterministic checks: `perren_g-e_b1917` vs `Perrin, G___North Borneo___1949`

- [PASS] surname_gate: bio 'PERREN' vs stint 'Perrin, G' (fuzzy:1)
- [PASS] initials: bio ['G', 'E'] ~ stint ['G']
- [PASS] age_gate: stint starts 1949, birth 1917 (age 32)
- [FAIL] colony: no placed event resolves to 'North Borneo'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1950
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

