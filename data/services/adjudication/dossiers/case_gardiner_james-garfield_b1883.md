<!-- {"case_id": "case_gardiner_james-garfield_b1883", "bio_ids": ["gardiner_james-garfield_b1883"], "stint_ids": ["Gardiner, J. G___Canada___1915", "Gardiner, J___High Commission Territories___1952"]} -->
# Dossier case_gardiner_james-garfield_b1883

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 22 official(s) with this surname in the graph's staff lists; 10 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `gardiner_james-garfield_b1883`

- Printed name: **GARDINER, JAMES GARFIELD**
- Birth year: 1883 (attested in editions [1937, 1940])
- Appears in editions: [1937, 1940]

### Verbatim printed entry text (OCR)

**Version `col1937-L61088.v` — printed in editions [1937, 1940]:**

> GARDINER, HON. JAMES GARFIELD, B.A., LL.D., (Assimboia, S.).—B. 1883; ed. pub. schls.; el., Sask. legislature at by-elec., 1914; re-elec., 1917, and at g.e., 1921 by acclm.; min., highways and min. in ch., bureau of lab. and industries, 1922; re-elec. without contest after assuming office at by-elec., 1923; re-elec., g.e., 1925; premier, Sask., 1926; prov. treas., 1926-27; min. of educn., 1928-29; re-elec., g.e., 1929; resigned as premier, 1929; re-elect., g.e., 1934; premier and prov. treas., Sask., 1934; resigned as premier when apptd. min., agr. in Rt. Hon. W. L. Mackenzie King's cabinet, 1935; first elec., H. of C., Canada at a by-elec., Jan., 1936.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914 | Sask. legislature | Saskatchewan | [1937, 1940] |
| 1 | 1917 | — | — | [1937, 1940] |
| 2 | 1921 | — | — | [1937, 1940] |
| 3 | 1922 | min., highways and min. in ch., bureau of lab. and industries | — | [1937, 1940] |
| 4 | 1923 | — | — | [1937, 1940] |
| 5 | 1925 | — | — | [1937, 1940] |
| 6 | 1926 | premier | Saskatchewan | [1937, 1940] |
| 7 | 1926–1927 | prov. treas. | — | [1937, 1940] |
| 8 | 1928–1929 | min. of educn. | — | [1937, 1940] |
| 9 | 1929 | — | — | [1937, 1940] |
| 10 | 1929 | premier | — | [1937, 1940] |
| 11 | 1934 | — | — | [1937, 1940] |
| 12 | 1934 | premier and prov. treas. | Saskatchewan | [1937, 1940] |
| 13 | 1935 | min., agr. | — | [1937, 1940] |
| 14 | 1936 | H. of C. | Canada | [1937, 1940] |

## Candidate stint `Gardiner, J. G___Canada___1915`

- Staff-list name: **Gardiner, J. G** | colony: **Canada** | listed 1915–1917 | editions [1915, 1917]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1915 | J. G. Gardiner | Member | Legislative Assembly | — | — |
| 1917 | J. G. Gardiner | Member for North Qu'Appelle | Legislative Assembly | — | — |

### Deterministic checks: `gardiner_james-garfield_b1883` vs `Gardiner, J. G___Canada___1915`

- [PASS] surname_gate: bio 'GARDINER' vs stint 'Gardiner, J. G' (exact)
- [PASS] initials: bio ['J', 'G'] ~ stint ['J', 'G']
- [PASS] age_gate: stint starts 1915, birth 1883 (age 32)
- [PASS] colony: 1 placed event(s) resolve to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1915-1917
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Gardiner, J___High Commission Territories___1952`

- Staff-list name: **Gardiner, J** | colony: **High Commission Territories** | listed 1952–1960 | editions [1952, 1959, 1960]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1952 | J. Gardiner | Director of Education | BECHUANALAND PROTECTORATE | — | — |
| 1959 | J. Gardiner | Director of Education | BECHUANALAND PROTECTORATE | O.B.E. | — |
| 1960 | J. Gardiner | Director of Education | BECHUANALAND PROTECTORATE | O.B.E. | — |

### Deterministic checks: `gardiner_james-garfield_b1883` vs `Gardiner, J___High Commission Territories___1952`

- [PASS] surname_gate: bio 'GARDINER' vs stint 'Gardiner, J' (exact)
- [PASS] initials: bio ['J', 'G'] ~ stint ['J']
- [PASS] age_gate: stint starts 1952, birth 1883 (age 69)
- [FAIL] colony: no placed event resolves to 'High Commission Territories'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1952-1960
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

