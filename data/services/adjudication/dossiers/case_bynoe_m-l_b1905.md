<!-- {"case_id": "case_bynoe_m-l_b1905", "bio_ids": ["bynoe_m-l_b1905"], "stint_ids": ["Bynoe, Miss L___Barbados___1936"]} -->
# Dossier case_bynoe_m-l_b1905

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 12 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `bynoe_m-l_b1905`

- Printed name: **BYNOE, M. L**
- Birth year: 1905 (attested in editions [1955, 1956, 1957])
- Appears in editions: [1955, 1956, 1957]

### Verbatim printed entry text (OCR)

**Version `col1955-L20000.v` — printed in editions [1955, 1956, 1957]:**

> BYNOE, M. L.—b. 1905; ed. Harrison Coll., Barb., King's Coll. and King's Coll. Hosp., Lond.; med. offr., Mal., 1935; Sarawak, 1937-39; admin. med. offr., super-scale gr. B, 1950; gr. A, 1951; ch. med. offr., Penang, 1951; asst. D.M.S., Fed. of Mal., 1953; D.D.M.S., 1954.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1935 | med. offr. | Malaya | [1955, 1956, 1957] |
| 1 | 1937–1939 | med. offr. | Sarawak | [1955, 1956, 1957] |
| 2 | 1950 | admin. med. offr., super-scale gr. B | Sarawak *(inherited from previous clause)* | [1955, 1956, 1957] |
| 3 | 1951 | gr. A | Sarawak *(inherited from previous clause)* | [1955, 1956, 1957] |
| 4 | 1953 | asst. D.M.S., Fed. of Mal | Sarawak *(inherited from previous clause)* | [1955, 1956, 1957] |
| 5 | 1954 | D.D.M.S | Sarawak *(inherited from previous clause)* | [1955, 1956, 1957] |

## Candidate stint `Bynoe, Miss L___Barbados___1936`

- Staff-list name: **Bynoe, Miss L** | colony: **Barbados** | listed 1936–1937 | editions [1936, 1937]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | Miss L. Bynoe | Assistant Master | Educational | — | — |
| 1937 | Miss L. Bynoe | — | Educational | — | — |

### Deterministic checks: `bynoe_m-l_b1905` vs `Bynoe, Miss L___Barbados___1936`

- [PASS] surname_gate: bio 'BYNOE' vs stint 'Bynoe, Miss L' (exact)
- [PASS] initials: bio ['M', 'L'] ~ stint ['M', 'L']
- [PASS] age_gate: stint starts 1936, birth 1905 (age 31)
- [FAIL] colony: no placed event resolves to 'Barbados'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1936-1937
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

