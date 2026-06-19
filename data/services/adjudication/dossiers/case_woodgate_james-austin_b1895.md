<!-- {"case_id": "case_woodgate_james-austin_b1895", "bio_ids": ["woodgate_james-austin_b1895"], "stint_ids": ["Woodgate, J. A___Falkland Islands___1940"]} -->
# Dossier case_woodgate_james-austin_b1895

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `woodgate_james-austin_b1895`

- Printed name: **WOODGATE, James Austin**
- Birth year: 1895 (attested in editions [1950, 1951])
- Honours: A.R.I.B.A, O.B.E
- Appears in editions: [1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1950-L40917.v` — printed in editions [1950, 1951]:**

> WOODGATE, James Austin, O.B.E., A.R.I.B.A.—b. 1895; ed. Chatham House Sch., Ramsgate; on mil. serv., 1915-19; apptd. Falkland Is., 1939; arch., P.W.D., Tang., 1947.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1939 | apptd. Falkland Is | — | [1950, 1951] |
| 1 | 1947 | arch., P.W.D. | Tanganyika | [1950, 1951] |

## Candidate stint `Woodgate, J. A___Falkland Islands___1940`

- Staff-list name: **Woodgate, J. A** | colony: **Falkland Islands** | listed 1940–1946 | editions [1940, 1946]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1940 | J. A. Woodgate | Executive Engineer | Public Works | — | — |
| 1946 | J. A. Woodgate | Executive Council Member | Executive Council | — | — |

### Deterministic checks: `woodgate_james-austin_b1895` vs `Woodgate, J. A___Falkland Islands___1940`

- [PASS] surname_gate: bio 'WOODGATE' vs stint 'Woodgate, J. A' (exact)
- [PASS] initials: bio ['J', 'A'] ~ stint ['J', 'A']
- [PASS] age_gate: stint starts 1940, birth 1895 (age 45)
- [FAIL] colony: no placed event resolves to 'Falkland Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1940-1946
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

