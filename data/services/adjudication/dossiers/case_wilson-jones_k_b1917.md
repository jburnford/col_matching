<!-- {"case_id": "case_wilson-jones_k_b1917", "bio_ids": ["wilson-jones_k_b1917"], "stint_ids": ["Wilson-Jones, K___Aden___1965"]} -->
# Dossier case_wilson-jones_k_b1917

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['wilson-jones_k_b1917'] carry a single initial only — the namesake trap applies.

## Biography `wilson-jones_k_b1917`

- Printed name: **WILSON-JONES, K**
- Birth year: 1917 (attested in editions [1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1962-L28013.v` — printed in editions [1962, 1963, 1964, 1965, 1966]:**

> WILSON-JONES, K.—b. 1917; ed. Altrincham Gram. Sch. and Manchester Univ.; apptd. min. of supply, 1941; econ. botanist, Sudan, 1946; prin. scientific offr., C.O. (scientific sec., pesticides research comte), 1955; dir. of agric., Fed. of S. Arabia, 1964.

**Version `col1959-L29422.v` — printed in editions [1959, 1960, 1961]:**

> WILSON-JONES, K.—b. 1917; ed. Altrincham Gram. Sch. and Manchester Univ.; apptd. min. of supply, 1941; econ. botanist, Sudan, 1946; prin. scientific offr., C.O. (scientific sec., pesticides research comttee.), 1955; publ. sundry pp. on Striga, a parasitic plant of grain crops; and on Water buds in canal systems.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1941 | apptd. min. of supply | — | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1946 | econ. botanist, Sudan | — | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1955 | prin. scientific offr., C.O. (scientific sec., pesticides research comte) | Colonial Office | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 3 | 1964 | dir. of agric., Fed. of S. Arabia | Colonial Office *(inherited from previous clause)* | [1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Wilson-Jones, K___Aden___1965`

- Staff-list name: **Wilson-Jones, K** | colony: **Aden** | listed 1965–1966 | editions [1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1965 | K. Wilson-Jones | Director of Agriculture | Civil Establishment | — | — |
| 1966 | K. Wilson-Jones | Director of Agriculture and Irrigation | Civil Establishment | — | — |

### Deterministic checks: `wilson-jones_k_b1917` vs `Wilson-Jones, K___Aden___1965`

- [PASS] surname_gate: bio 'WILSON-JONES' vs stint 'Wilson-Jones, K' (exact)
- [PASS] initials: bio ['K'] ~ stint ['K']
- [PASS] age_gate: stint starts 1965, birth 1917 (age 48)
- [FAIL] colony: no placed event resolves to 'Aden'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1965-1966
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

