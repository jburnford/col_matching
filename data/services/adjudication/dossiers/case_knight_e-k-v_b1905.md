<!-- {"case_id": "case_knight_e-k-v_b1905", "bio_ids": ["knight_e-k-v_b1905"], "stint_ids": ["Knight, E. K. V___Gambia___1949"]} -->
# Dossier case_knight_e-k-v_b1905

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 72 official(s) with this surname in the graph's staff lists; 22 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `knight_e-k-v_b1905`

- Printed name: **KNIGHT, E. K. V**
- Birth year: 1905 (attested in editions [1960, 1961])
- Appears in editions: [1959, 1960, 1961]

### Verbatim printed entry text (OCR)

**Version `col1960-L24954.v` — printed in editions [1960, 1961]:**

> KNIGHT, Miss E. K. V.—b. 1905; ed. Oxford High Sch., and St. Mary's Froebel Coll., London; woman educ. offr., Gam., 1948; N. Nig., 1953; prov. educ. offr., 1955; senr. educ. offr., 1957-60.

**Version `col1959-L24971.v` — printed in editions [1959]:**

> KNIGHT, Miss E. V.—b. 1905; educ. dept., Gam., 1948; woman educ. offr., Nig., 1953; senr. woman educ. offr., N. Nig., 1957.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1948 | woman educ. offr., Gam | — | [1960, 1961] |
| 1 | 1953 | woman educ. offr., Gam | Northern Nigeria | [1959, 1960, 1961] |
| 2 | 1955 | prov. educ. offr | Northern Nigeria *(inherited from previous clause)* | [1960, 1961] |
| 3 | 1957–1960 | senr. educ. offr | Northern Nigeria | [1959, 1960, 1961] |

## Candidate stint `Knight, E. K. V___Gambia___1949`

- Staff-list name: **Knight, E. K. V** | colony: **Gambia** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | E. K. V. Knight | Lady Education Officer | EDUCATION | — | — |
| 1950 | Miss E. K. V. Knight | Lady Education Officer | Education | — | — |
| 1951 | Miss E. K. V. Knight | Lady Education Officer | Education | — | — |

### Deterministic checks: `knight_e-k-v_b1905` vs `Knight, E. K. V___Gambia___1949`

- [PASS] surname_gate: bio 'KNIGHT' vs stint 'Knight, E. K. V' (exact)
- [PASS] initials: bio ['E', 'K', 'V'] ~ stint ['E', 'K', 'V']
- [PASS] age_gate: stint starts 1949, birth 1905 (age 44)
- [FAIL] colony: no placed event resolves to 'Gambia'
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

