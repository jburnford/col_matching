<!-- {"case_id": "case_louw_andries-de-roos-eckard_b1873", "bio_ids": ["louw_andries-de-roos-eckard_b1873"], "stint_ids": ["Louw, A. de R. E___Cape of Good Hope___1898"]} -->
# Dossier case_louw_andries-de-roos-eckard_b1873

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `louw_andries-de-roos-eckard_b1873`

- Printed name: **LOUW, ANDRIES DE ROOS ECKARD**
- Birth year: 1873 (attested in editions [1931, 1932, 1933, 1934])
- Appears in editions: [1931, 1932, 1933, 1934]

### Verbatim printed entry text (OCR)

**Version `col1931-L66211.v` — printed in editions [1931, 1932, 1933, 1934]:**

> LOUW, ANDRIES DE ROOS ECKARD.—B. 1873; clk., cust., Cape Town, 1893; examr., offr., 1896; prin. clk., E. London, 1912; survr., Durban, 1915; ch. clk., Cape Town, 1916; collr., eust., E. London, 1928; Port Elizabeth, 1929; collr., cust. and shipping mast., Durban, 1930.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1893 | clk., cust., Cape Town | Cape of Good Hope | [1931, 1932, 1933, 1934] |
| 1 | 1896 | examr., offr | Cape of Good Hope *(inherited from previous clause)* | [1931, 1932, 1933, 1934] |
| 2 | 1912 | prin. clk., E. London | Cape of Good Hope *(inherited from previous clause)* | [1931, 1932, 1933, 1934] |
| 3 | 1915 | survr., Durban | Cape of Good Hope *(inherited from previous clause)* | [1931, 1932, 1933, 1934] |
| 4 | 1916 | ch. clk., Cape Town | Cape of Good Hope | [1931, 1932, 1933, 1934] |
| 5 | 1928 | collr., eust., E. London | Cape of Good Hope *(inherited from previous clause)* | [1931, 1932, 1933, 1934] |
| 6 | 1929 | Port Elizabeth | Cape of Good Hope *(inherited from previous clause)* | [1931, 1932, 1933, 1934] |
| 7 | 1930 | collr., cust. and shipping mast., Durban | Cape of Good Hope *(inherited from previous clause)* | [1931, 1932, 1933, 1934] |

## Candidate stint `Louw, A. de R. E___Cape of Good Hope___1898`

- Staff-list name: **Louw, A. de R. E** | colony: **Cape of Good Hope** | listed 1898–1899 | editions [1898, 1899]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1898 | A. de R. E. Louw | Examining Officers | PORT OF PORT ELIZABETH | — | — |
| 1899 | A. de R. E. Louw | Third Class Examining Officers | Waterside Branch | — | — |

### Deterministic checks: `louw_andries-de-roos-eckard_b1873` vs `Louw, A. de R. E___Cape of Good Hope___1898`

- [PASS] surname_gate: bio 'LOUW' vs stint 'Louw, A. de R. E' (exact)
- [PASS] initials: bio ['A', 'D', 'R', 'E'] ~ stint ['A', 'D', 'R', 'E']
- [PASS] age_gate: stint starts 1898, birth 1873 (age 25)
- [PASS] colony: 8 placed event(s) resolve to 'Cape of Good Hope'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1898-1899
- [PASS] position_sim: best 64 vs bar 60: 'examr., offr' ~ 'Examining Officers'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

