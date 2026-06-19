<!-- {"case_id": "case_king_e-e-s_b1906", "bio_ids": ["king_e-e-s_b1906"], "stint_ids": ["King, E. E___British Guiana___1921"]} -->
# Dossier case_king_e-e-s_b1906

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 187 official(s) with this surname in the graph's staff lists; 68 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `king_e-e-s_b1906`

- Printed name: **KING, E. E. S**
- Birth year: 1906 (attested in editions [1959, 1960, 1961, 1962])
- Honours: M.B.E (1960)
- Appears in editions: [1959, 1960, 1961, 1962]

### Verbatim printed entry text (OCR)

**Version `col1959-L24894.v` — printed in editions [1959, 1960, 1961, 1962]:**

> KING, Miss E. E. S., M.B.E. (1960).—b. 1906; ed. St. Margaret’s Sch., Bushey, and King’s Coll. Hosp., London; nursing sister, Spore, 1938; Aden, 1941; Uga., 1947; matron, gr. II, 1949; prin. matron, Nyasa., 1951; matron, Aden, 1955–61.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1938 | nursing sister, Spore | — | [1959, 1960, 1961, 1962] |
| 1 | 1941 | nursing sister, Spore | Aden | [1959, 1960, 1961, 1962] |
| 2 | 1947 | nursing sister, Spore | Uganda | [1959, 1960, 1961, 1962] |
| 3 | 1949 | matron, gr. II | Uganda *(inherited from previous clause)* | [1959, 1960, 1961, 1962] |
| 4 | 1951 | prin. matron | Nyasaland | [1959, 1960, 1961, 1962] |
| 5 | 1955–1961 | matron | Aden | [1959, 1960, 1961, 1962] |

## Candidate stint `King, E. E___British Guiana___1921`

- Staff-list name: **King, E. E** | colony: **British Guiana** | listed 1921–1922 | editions [1921, 1922]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1921 | E. E. King | Assistant Sanitary Inspector | Public Health Department | — | — |
| 1922 | E. E. King | Assistant Sanitary Inspector | Public Health Department | — | — |

### Deterministic checks: `king_e-e-s_b1906` vs `King, E. E___British Guiana___1921`

- [PASS] surname_gate: bio 'KING' vs stint 'King, E. E' (exact)
- [PASS] initials: bio ['E', 'E', 'S'] ~ stint ['E', 'E']
- [PASS] age_gate: stint starts 1921, birth 1906 (age 15)
- [FAIL] colony: no placed event resolves to 'British Guiana'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1921-1922
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

