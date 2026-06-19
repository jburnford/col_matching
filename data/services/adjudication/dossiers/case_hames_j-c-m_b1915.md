<!-- {"case_id": "case_hames_j-c-m_b1915", "bio_ids": ["hames_j-c-m_b1915"], "stint_ids": ["Hayes, J. C___Cyprus___1949"]} -->
# Dossier case_hames_j-c-m_b1915

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 20 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hames_j-c-m_b1915`

- Printed name: **HAMES, J. C. M**
- Birth year: 1915 (attested in editions [1959, 1960, 1961, 1962])
- Appears in editions: [1959, 1960, 1961, 1962]

### Verbatim printed entry text (OCR)

**Version `col1959-L23786.v` — printed in editions [1959, 1960, 1961, 1962]:**

> HAMES, J. C. M.—b. 1915; ed. Dorking High Sch., and Regent St. Poly. Sch. of Architecture; mil. serv., 1943-46, sub-lieut. (A) R.N.; architect (temp.), P.W.D., Nig., 1948; architect, gr. II, 1954; senr. architect, N. Nig., 1955-61.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1948 | architect (temp.), P.W.D. | Nigeria | [1959, 1960, 1961, 1962] |
| 1 | 1954 | architect, gr. II | Nigeria *(inherited from previous clause)* | [1959, 1960, 1961, 1962] |
| 2 | 1955–1961 | senr. architect | Northern Nigeria | [1959, 1960, 1961, 1962] |

## Candidate stint `Hayes, J. C___Cyprus___1949`

- Staff-list name: **Hayes, J. C** | colony: **Cyprus** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | J. C. Hayes | Lecturers | Education | — | — |
| 1951 | J. C. Hayes | Lecturers | Education | — | — |

### Deterministic checks: `hames_j-c-m_b1915` vs `Hayes, J. C___Cyprus___1949`

- [PASS] surname_gate: bio 'HAMES' vs stint 'Hayes, J. C' (fuzzy:1)
- [PASS] initials: bio ['J', 'C', 'M'] ~ stint ['J', 'C']
- [PASS] age_gate: stint starts 1949, birth 1915 (age 34)
- [FAIL] colony: no placed event resolves to 'Cyprus'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
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

