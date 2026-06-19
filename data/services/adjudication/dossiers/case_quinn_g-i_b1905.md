<!-- {"case_id": "case_quinn_g-i_b1905", "bio_ids": ["quinn_g-i_b1905"], "stint_ids": ["Quinn, G. I___Trinidad and Tobago___1949"]} -->
# Dossier case_quinn_g-i_b1905

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 11 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `quinn_g-i_b1905`

- Printed name: **QUINN, G. I**
- Birth year: 1905 (attested in editions [1956, 1957])
- Appears in editions: [1956, 1957]

### Verbatim printed entry text (OCR)

**Version `col1956-L23649.v` — printed in editions [1956, 1957]:**

> QUINN, G. I.—b. 1905; ed. St. Francis Xavier's Coll., L'pool and L'pool Univ.; H.M. inspr., factories, H.O., 1936; senr. factory inspr., Trin., 1947.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1936 | H.M. inspr., factories, H.O | — | [1956, 1957] |
| 1 | 1947 | senr. factory inspr. | Trinidad | [1956, 1957] |

## Candidate stint `Quinn, G. I___Trinidad and Tobago___1949`

- Staff-list name: **Quinn, G. I** | colony: **Trinidad and Tobago** | listed 1949–1954 | editions [1949, 1953, 1954]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | G. I. Quinn | Senior Factory Inspector | Industrial Adviser | — | — |
| 1953 | G. I. Quinn | Senior Factory Inspector | Civil Establishment | — | — |
| 1954 | G. I. Quinn | Senior Factory Inspector | Civil Establishment | — | — |

### Deterministic checks: `quinn_g-i_b1905` vs `Quinn, G. I___Trinidad and Tobago___1949`

- [PASS] surname_gate: bio 'QUINN' vs stint 'Quinn, G. I' (exact)
- [PASS] initials: bio ['G', 'I'] ~ stint ['G', 'I']
- [PASS] age_gate: stint starts 1949, birth 1905 (age 44)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1954
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

