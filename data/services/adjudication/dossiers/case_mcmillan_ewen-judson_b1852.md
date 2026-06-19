<!-- {"case_id": "case_mcmillan_ewen-judson_b1852", "bio_ids": ["mcmillan_ewen-judson_b1852"], "stint_ids": ["McMillan, E. J___South Africa___1914"]} -->
# Dossier case_mcmillan_ewen-judson_b1852

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 18 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mcmillan_ewen-judson_b1852`

- Printed name: **MCMILLAN, EWEN JUDSON**
- Birth year: 1852 (attested in editions [1912])
- Appears in editions: [1912]

### Verbatim printed entry text (OCR)

**Version `col1912-L45965.v` — printed in editions [1912]:**

> MCMILLAN, EWEN JUDSON.—B. 1852; govt. sta., Charlottetown Business Coll., Guelph Agric. Coll., received degree of B.S.A., June, 1900; O.R.C., R.U.I., govt. experiment farm and lecturer in Canada, 1901-4; chief of experimental farms, Prince of Wales' Coll., Prince Edward Island, Canada, 1901-4; chief of experimental farms, live stock division, O.R.C., June, 1904; agr. instr., div. of agric., July, 1905; ag. dir. of agric. inst., 1906-1908; ag. dir., 1908-1910.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1900 | govt. sta., Charlottetown Business Coll., Guelph Agric. Coll., received degree of B.S.A | — | [1912] |
| 1 | 1901–1904 | O.R.C., R.U.I., govt. experiment farm and lecturer in Canada | — | [1912] |
| 2 | 1901–1904 | chief of experimental farms, Prince of Wales' Coll., Prince Edward Island | Canada | [1912] |
| 3 | 1904 | chief of experimental farms, live stock division, O.R.C | Canada *(inherited from previous clause)* | [1912] |
| 4 | 1905 | agr. instr., div. of agric | Canada *(inherited from previous clause)* | [1912] |
| 5 | 1906–1908 | ag. dir. of agric. inst | Canada *(inherited from previous clause)* | [1912] |
| 6 | 1908–1910 | ag. dir | Canada *(inherited from previous clause)* | [1912] |

## Candidate stint `McMillan, E. J___South Africa___1914`

- Staff-list name: **McMillan, E. J** | colony: **South Africa** | listed 1914–1918 | editions [1914, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1914 | E. J. McMillan | Principal | Agricultural Schools, Stud Farms and Experimental Stations | — | — |
| 1918 | E. J. McMillan | Principal | Agricultural Schools and Experiment Farms | — | — |

### Deterministic checks: `mcmillan_ewen-judson_b1852` vs `McMillan, E. J___South Africa___1914`

- [PASS] surname_gate: bio 'MCMILLAN' vs stint 'McMillan, E. J' (exact)
- [PASS] initials: bio ['E', 'J'] ~ stint ['E', 'J']
- [PASS] age_gate: stint starts 1914, birth 1852 (age 62)
- [FAIL] colony: no placed event resolves to 'South Africa'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1914-1918
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

