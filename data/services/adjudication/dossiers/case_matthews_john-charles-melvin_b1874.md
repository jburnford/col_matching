<!-- {"case_id": "case_matthews_john-charles-melvin_b1874", "bio_ids": ["matthews_john-charles-melvin_b1874"], "stint_ids": ["Matthews, M___Fiji___1922"]} -->
# Dossier case_matthews_john-charles-melvin_b1874

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 46 official(s) with this surname in the graph's staff lists; 22 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Matthews, M___Fiji___1922` is also gate-compatible with biography(ies) outside this case: ['matthews_marmduke-humphrey_e1914', 'matthews_maynard-reginald-nelson_b1865'] (already linked elsewhere or filtered).

## Biography `matthews_john-charles-melvin_b1874`

- Printed name: **MATTHEWS, JOHN CHARLES MELVIN**
- Birth year: 1874 (attested in editions [1925, 1927])
- Honours: M.I.E.E
- Appears in editions: [1925, 1927]

### Verbatim printed entry text (OCR)

**Version `col1925-L57815.v` — printed in editions [1925, 1927]:**

> MATTHEWS, JOHN CHARLES MELVIN, M.I.E.E.—B. 1874; ed. Portsmouth Grammar Schl. and King's Coll., London; asst. elec. engr., Kuala Lumpur, F.M.S., 1904; engr. in ch., 1906; 2nd lieut. and lieut. M.S.V.R. (C.A.F.L.S. Medal), 1915-20; ag. ch. elec. inspr., in addn., 1914-16; sec. elec. bd., in addn., 1921; ch. elec. engr., F.M.S., 1923.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1904 | asst. elec. engr., Kuala Lumpur | Federated Malay States | [1925, 1927] |
| 1 | 1906 | engr. in ch | Federated Malay States *(inherited from previous clause)* | [1925, 1927] |
| 2 | 1914–1916 | ag. ch. elec. inspr., in addn | Federated Malay States *(inherited from previous clause)* | [1925, 1927] |
| 3 | 1915–1920 | 2nd lieut. and lieut. M.S.V.R. (C.A.F.L.S. Medal) | Federated Malay States *(inherited from previous clause)* | [1925, 1927] |
| 4 | 1921 | sec. elec. bd., in addn | Federated Malay States *(inherited from previous clause)* | [1925, 1927] |
| 5 | 1923 | ch. elec. engr. | Federated Malay States | [1925, 1927] |

## Candidate stint `Matthews, M___Fiji___1922`

- Staff-list name: **Matthews, M** | colony: **Fiji** | listed 1922–1923 | editions [1922, 1923]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | M. Matthews | 5th Class Clerks | Postal Department | — | — |
| 1923 | M. Matthews | 3rd Class Clerk | Postal Department | — | — |

### Deterministic checks: `matthews_john-charles-melvin_b1874` vs `Matthews, M___Fiji___1922`

- [PASS] surname_gate: bio 'MATTHEWS' vs stint 'Matthews, M' (exact)
- [PASS] initials: bio ['J', 'C', 'M'] ~ stint ['M']
- [PASS] age_gate: stint starts 1922, birth 1874 (age 48)
- [FAIL] colony: no placed event resolves to 'Fiji'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1922-1923
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

