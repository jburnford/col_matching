<!-- {"case_id": "case_swain_edward-harold-fulcher_b1883", "bio_ids": ["swain_edward-harold-fulcher_b1883"], "stint_ids": ["Swain, E___Falkland Islands___1929"]} -->
# Dossier case_swain_edward-harold-fulcher_b1883

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 12 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `swain_edward-harold-fulcher_b1883`

- Printed name: **SWAIN, EDWARD HAROLD FULCHER**
- Birth year: 1883 (attested in editions [1939, 1940])
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L71027.v` — printed in editions [1939, 1940]:**

> SWAIN, EDWARD HAROLD FULCHER.—B. 1883; dipl. forestry (N.S.W.), M.I.A.W.A.; forestry commnr., N.S.W., Aug., 1935.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1935 | forestry commnr. | New South Wales | [1939, 1940] |

## Candidate stint `Swain, E___Falkland Islands___1929`

- Staff-list name: **Swain, E** | colony: **Falkland Islands** | listed 1929–1930 | editions [1929, 1930]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1929 | E. Swain | Constable | Police and Prisons | — | — |
| 1930 | E. Swain | Constable | Police and Prisons (Stanley) | — | — |

### Deterministic checks: `swain_edward-harold-fulcher_b1883` vs `Swain, E___Falkland Islands___1929`

- [PASS] surname_gate: bio 'SWAIN' vs stint 'Swain, E' (exact)
- [PASS] initials: bio ['E', 'H', 'F'] ~ stint ['E']
- [PASS] age_gate: stint starts 1929, birth 1883 (age 46)
- [FAIL] colony: no placed event resolves to 'Falkland Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1929-1930
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

