<!-- {"case_id": "case_goring_edith-francis_b1899", "bio_ids": ["goring_edith-francis_b1899"], "stint_ids": ["Goring, E. F___Northern Rhodesia___1949", "Goring, F___British Guiana___1918"]} -->
# Dossier case_goring_edith-francis_b1899

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `goring_edith-francis_b1899`

- Printed name: **GORING, Edith Francis**
- Birth year: 1899 (attested in editions [1948, 1949, 1951])
- Appears in editions: [1948, 1949, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L32907.v` — printed in editions [1948, 1949, 1951]:**

> GORING, Edith Francis.—b. 1899; ed. Eunice High Sch., O.F.S., Grey Univ. Coll. and Johannesburg Univ. Coll., B.A. (S. Africa), T.I., T.II., Transvaal; head-mistress, N. Rhod., 1934.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1934 | head-mistress | Northern Rhodesia | [1948, 1949, 1951] |

## Candidate stint `Goring, E. F___Northern Rhodesia___1949`

- Staff-list name: **Goring, E. F** | colony: **Northern Rhodesia** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | E. F. Goring | Principal | Education | — | — |
| 1951 | Miss E. F. Goring | Principal | Education | — | — |

### Deterministic checks: `goring_edith-francis_b1899` vs `Goring, E. F___Northern Rhodesia___1949`

- [PASS] surname_gate: bio 'GORING' vs stint 'Goring, E. F' (exact)
- [PASS] initials: bio ['E', 'F'] ~ stint ['E', 'F']
- [PASS] age_gate: stint starts 1949, birth 1899 (age 50)
- [PASS] colony: 1 placed event(s) resolve to 'Northern Rhodesia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Goring, F___British Guiana___1918`

- Staff-list name: **Goring, F** | colony: **British Guiana** | listed 1918–1921 | editions [1918, 1919, 1920, 1921]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1918 | F. Goring | Clerical and Laboratory Assistant | Science and Agriculture | — | — |
| 1919 | F. Goring | Clerical and Laboratory Assistants | Science and Agriculture | — | — |
| 1920 | F. Goring | Clerical and Laboratory Assistants | Department of Science and Agriculture | — | — |
| 1921 | F. Goring | Clerical and Laboratory Assistants | Department of Science and Agriculture | — | — |

### Deterministic checks: `goring_edith-francis_b1899` vs `Goring, F___British Guiana___1918`

- [PASS] surname_gate: bio 'GORING' vs stint 'Goring, F' (exact)
- [PASS] initials: bio ['E', 'F'] ~ stint ['F']
- [PASS] age_gate: stint starts 1918, birth 1899 (age 19)
- [FAIL] colony: no placed event resolves to 'British Guiana'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1918-1921
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

