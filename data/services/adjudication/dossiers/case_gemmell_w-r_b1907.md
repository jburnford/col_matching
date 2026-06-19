<!-- {"case_id": "case_gemmell_w-r_b1907", "bio_ids": ["gemmell_w-r_b1907"], "stint_ids": ["Gemmell, W. R___High Commission Territories___1963", "Gemmell, W___Gold Coast___1927"]} -->
# Dossier case_gemmell_w-r_b1907

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `gemmell_w-r_b1907`

- Printed name: **GEMMELL, W. R**
- Birth year: 1907 (attested in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964])
- Appears in editions: [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1957-L23293.v` — printed in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]:**

> GEMMELL, W. R.—b. 1907; ed. Dollar Academy and Glasgow and Edin. Univs.; mil. serv., 1939-45, hon. major, R.A.M.C.; M.O., Bech. Prot., 1945; S.M.O., 1959; D.M.S., 1960.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1945 | M.O. | Bechuanaland | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 1 | 1959 | S.M.O | Bechuanaland *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 2 | 1960 | D.M.S | Bechuanaland *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |

## Candidate stint `Gemmell, W. R___High Commission Territories___1963`

- Staff-list name: **Gemmell, W. R** | colony: **High Commission Territories** | listed 1963–1964 | editions [1963, 1964]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1963 | W. R. Gemmell | Director of Medical Services | Secretariat | — | — |
| 1964 | W. R. Gemmell | Director of Medical Services | Secretariat | — | — |

### Deterministic checks: `gemmell_w-r_b1907` vs `Gemmell, W. R___High Commission Territories___1963`

- [PASS] surname_gate: bio 'GEMMELL' vs stint 'Gemmell, W. R' (exact)
- [PASS] initials: bio ['W', 'R'] ~ stint ['W', 'R']
- [PASS] age_gate: stint starts 1963, birth 1907 (age 56)
- [FAIL] colony: no placed event resolves to 'High Commission Territories'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1963-1964
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Gemmell, W___Gold Coast___1927`

- Staff-list name: **Gemmell, W** | colony: **Gold Coast** | listed 1927–1930 | editions [1927, 1929, 1930]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | W. Gemmell | Surveyors | Provincial Survey Sections | — | — |
| 1929 | W. Gemmell | Surveyors | Provincial Survey Sections | — | — |
| 1930 | W. Gemmell | Surveyors | Survey Department | — | — |

### Deterministic checks: `gemmell_w-r_b1907` vs `Gemmell, W___Gold Coast___1927`

- [PASS] surname_gate: bio 'GEMMELL' vs stint 'Gemmell, W' (exact)
- [PASS] initials: bio ['W', 'R'] ~ stint ['W']
- [PASS] age_gate: stint starts 1927, birth 1907 (age 20)
- [FAIL] colony: no placed event resolves to 'Gold Coast'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1927-1930
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

