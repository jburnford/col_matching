<!-- {"case_id": "case_anthony_william-thomas_b1874", "bio_ids": ["anthony_william-thomas_b1874"], "stint_ids": ["Anthony, W. T___Cape of Good Hope___1896"]} -->
# Dossier case_anthony_william-thomas_b1874

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `anthony_william-thomas_b1874`

- Printed name: **ANTHONY, WILLIAM THOMAS**
- Birth year: 1874 (attested in editions [1931, 1932, 1934])
- Appears in editions: [1931, 1932, 1934]

### Verbatim printed entry text (OCR)

**Version `col1931-L62030.v` — printed in editions [1931, 1932, 1934]:**

> ANTHONY, WILLIAM THOMAS.—B. 1874; clk., mag's office, Kokstad, S. Africa, 1894; elk., cust., Port Elizabeth, 1894; essg. off., 1899; 1st cls. clk., Cape Town, 1903; prin. clk., Port Elizabeth, 1915; ch. clk., Durban, 1926; head office, Pretoria, 1926; collr., cust. and shipping mast., Port Elizabeth, 1930; Cape Town, 1930.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1894 | clk., mag's office, Kokstad, S. Africa | — | [1931, 1932, 1934] |
| 1 | 1894 | elk., cust., Port Elizabeth | — | [1931, 1932, 1934] |
| 2 | 1899 | essg. off | — | [1931, 1932, 1934] |
| 3 | 1903 | 1st cls. clk., Cape Town | Cape of Good Hope | [1931, 1932, 1934] |
| 4 | 1915 | prin. clk., Port Elizabeth | Cape of Good Hope *(inherited from previous clause)* | [1931, 1932, 1934] |
| 5 | 1926 | ch. clk., Durban | Cape of Good Hope *(inherited from previous clause)* | [1931, 1932, 1934] |
| 6 | 1930 | collr., cust. and shipping mast., Port Elizabeth | Cape of Good Hope | [1931, 1932, 1934] |

## Candidate stint `Anthony, W. T___Cape of Good Hope___1896`

- Staff-list name: **Anthony, W. T** | colony: **Cape of Good Hope** | listed 1896–1900 | editions [1896, 1898, 1899, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1896 | W. T. Anthony | Clerk | PORT OF PORT ELIZABETH | — | — |
| 1898 | W. Anthony | Clerks | PORT OF PORT ELIZABETH | — | — |
| 1899 | W. T. Anthony | Third Class Examining Officers | Waterside Branch | — | — |
| 1900 | W. T. Anthony | Third Class Examining Officer | Waterside Branch | — | — |

### Deterministic checks: `anthony_william-thomas_b1874` vs `Anthony, W. T___Cape of Good Hope___1896`

- [PASS] surname_gate: bio 'ANTHONY' vs stint 'Anthony, W. T' (exact)
- [PASS] initials: bio ['W', 'T'] ~ stint ['W', 'T']
- [PASS] age_gate: stint starts 1896, birth 1874 (age 22)
- [PASS] colony: 4 placed event(s) resolve to 'Cape of Good Hope'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1896-1900
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

