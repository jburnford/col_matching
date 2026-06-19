<!-- {"case_id": "case_johnston_robert-stewart_b1898", "bio_ids": ["johnston_robert-stewart_b1898"], "stint_ids": ["Johnston, R. S___Straits Settlements___1931", "Johnston, T. R. St___Fiji___1915", "Johnston, T. R. St___Leeward Islands___1928"]} -->
# Dossier case_johnston_robert-stewart_b1898

## Case context

- 1 biography(ies) and 3 candidate stint(s) are entangled in this case.
- Corpus context: 112 official(s) with this surname in the graph's staff lists; 27 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `johnston_robert-stewart_b1898`

- Printed name: **JOHNSTON, ROBERT STEWART**
- Birth year: 1898 (attested in editions [1939, 1940])
- Honours: M.B
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L68012.v` — printed in editions [1939, 1940]:**

> JOHNSTON, ROBERT STEWART, M.B., B.Ch., B.A.O. (Belfast), D.T.M. & H. (Eng.), D.P.H. (Lond.), Cert. L.S.T.M.—B. 1898; ed. R. Acad. Inst., Belfast and Queen's Univ., Belfast; war serv., 1916-19; health offr., Malaya, Mar., 1928.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | health offr. | Malaya | [1939, 1940] |

## Candidate stint `Johnston, R. S___Straits Settlements___1931`

- Staff-list name: **Johnston, R. S** | colony: **Straits Settlements** | listed 1931–1933 | editions [1931, 1933]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | R. S. Johnston | Health Officer | Health Branch | — | — |
| 1933 | R. S. Johnston | Health Officer | Health Branch | — | — |

### Deterministic checks: `johnston_robert-stewart_b1898` vs `Johnston, R. S___Straits Settlements___1931`

- [PASS] surname_gate: bio 'JOHNSTON' vs stint 'Johnston, R. S' (exact)
- [PASS] initials: bio ['R', 'S'] ~ stint ['R', 'S']
- [PASS] age_gate: stint starts 1931, birth 1898 (age 33)
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1931-1933
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Johnston, T. R. St___Fiji___1915`

- Staff-list name: **Johnston, T. R. St** | colony: **Fiji** | listed 1915–1918 | editions [1915, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1915 | T. R. St. Johnston | Medical Officer with Judicial Powers | Department of Justice | — | — |
| 1918 | T. R. St. Johnston | Medical Officer | Medical Officers with Judicial Powers | — | — |

### Deterministic checks: `johnston_robert-stewart_b1898` vs `Johnston, T. R. St___Fiji___1915`

- [PASS] surname_gate: bio 'JOHNSTON' vs stint 'Johnston, T. R. St' (exact)
- [PASS] initials: bio ['R', 'S'] ~ stint ['T', 'R', 'S']
- [PASS] age_gate: stint starts 1915, birth 1898 (age 17)
- [FAIL] colony: no placed event resolves to 'Fiji'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1915-1918
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Johnston, T. R. St___Leeward Islands___1928`

- Staff-list name: **Johnston, T. R. St** | colony: **Leeward Islands** | listed 1928–1930 | editions [1928, 1930]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1928 | Lt.-Col. T. R. St. Johnston | Administrator | Civil Establishment | C.M.G. | Lt.-Col. |
| 1930 | T. R. St. Johnston | Governor, Lt.-Col. | Civil Establishment | C.M.G. | Lt.-Col. |

### Deterministic checks: `johnston_robert-stewart_b1898` vs `Johnston, T. R. St___Leeward Islands___1928`

- [PASS] surname_gate: bio 'JOHNSTON' vs stint 'Johnston, T. R. St' (exact)
- [PASS] initials: bio ['R', 'S'] ~ stint ['T', 'R', 'S']
- [PASS] age_gate: stint starts 1928, birth 1898 (age 30)
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1928-1930
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

