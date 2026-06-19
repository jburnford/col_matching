<!-- {"case_id": "case_crane_v-e_b1919", "bio_ids": ["crane_v-e_b1919"], "stint_ids": ["Crane, V. E___British Guiana___1964"]} -->
# Dossier case_crane_v-e_b1919

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `crane_v-e_b1919`

- Printed name: **CRANE, V. E**
- Birth year: 1919 (attested in editions [1964, 1965, 1966])
- Appears in editions: [1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1964-L16079.v` — printed in editions [1964, 1965, 1966]:**

> CRANE, V. E.—b. 1919; ed. Queen's Coll., B. Guiana and Univ. Coll., London; barrister-at-law, Middle Temple; mil. serv., 1942-46, R.A.F.; prob., B. Guiana, 1942; mag., 1952; mag., Nig., 1956; ch. mag., 1959; puisne judge, B. Guiana, 1963.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1942 | prob., B. Guiana | — | [1964, 1965, 1966] |
| 1 | 1952 | mag | — | [1964, 1965, 1966] |
| 2 | 1956 | mag. | Nigeria | [1964, 1965, 1966] |
| 3 | 1959 | ch. mag | Nigeria *(inherited from previous clause)* | [1964, 1965, 1966] |
| 4 | 1963 | puisne judge, B. Guiana | Nigeria *(inherited from previous clause)* | [1964, 1965, 1966] |

## Candidate stint `Crane, V. E___British Guiana___1964`

- Staff-list name: **Crane, V. E** | colony: **British Guiana** | listed 1964–1966 | editions [1964, 1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1964 | V. E. Crane | Puisne Judge | Judiciary | — | — |
| 1965 | V. E. Crane | Puisne Judge | Judiciary | — | — |
| 1966 | V. E. Crane | Puisne Judge | Judiciary | — | — |

### Deterministic checks: `crane_v-e_b1919` vs `Crane, V. E___British Guiana___1964`

- [PASS] surname_gate: bio 'CRANE' vs stint 'Crane, V. E' (exact)
- [PASS] initials: bio ['V', 'E'] ~ stint ['V', 'E']
- [PASS] age_gate: stint starts 1964, birth 1919 (age 45)
- [FAIL] colony: no placed event resolves to 'British Guiana'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1964-1966
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

