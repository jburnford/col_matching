<!-- {"case_id": "case_charles_lawrence-justin_b1915", "bio_ids": ["charles_lawrence-justin_b1915"], "stint_ids": ["Charles, L. J___Leeward Islands___1949"]} -->
# Dossier case_charles_lawrence-justin_b1915

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 24 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `charles_lawrence-justin_b1915`

- Printed name: **CHARLES, Lawrence Justin**
- Birth year: 1915 (attested in editions [1951])
- Honours: D.T.M, M.B, M.P.H
- Appears in editions: [1951]

### Verbatim printed entry text (OCR)

**Version `col1951-L36881.v` — printed in editions [1951]:**

> CHARLES, Lawrence Justin, M.B., Ch.B., D.T.M., D.Th., M.P.H.—b. 1915; ed. Dominica Gram. Sch., Edin. Univ., Liverp. S.T.M. and Harvard Sch. Public Health; apptd. 1939; med. offr., Antigua, 1941; Montserrat, 1947; Antigua, 1949; ch. offr., mosquito cont. serv., B. Guiana, 1950.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1939 | apptd | — | [1951] |
| 1 | 1941 | med. offr. | Antigua | [1951] |
| 2 | 1947 | med. offr. | Montserrat | [1951] |
| 3 | 1949 | med. offr. | Antigua | [1951] |
| 4 | 1950 | ch. offr., mosquito cont. serv., B. Guiana | Antigua *(inherited from previous clause)* | [1951] |

## Candidate stint `Charles, L. J___Leeward Islands___1949`

- Staff-list name: **Charles, L. J** | colony: **Leeward Islands** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | L. J. Charles | Medical Officer, District 2 | Medical Officers | — | — |
| 1950 | L. J. Charles | Medical Officer, District 2 | Medical | — | — |
| 1951 | L. J. Charles | Medical Officer, District B | MEDICAL | — | — |

### Deterministic checks: `charles_lawrence-justin_b1915` vs `Charles, L. J___Leeward Islands___1949`

- [PASS] surname_gate: bio 'CHARLES' vs stint 'Charles, L. J' (exact)
- [PASS] initials: bio ['L', 'J'] ~ stint ['L', 'J']
- [PASS] age_gate: stint starts 1949, birth 1915 (age 34)
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
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

