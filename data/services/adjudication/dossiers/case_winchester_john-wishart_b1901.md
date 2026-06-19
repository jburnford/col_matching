<!-- {"case_id": "case_winchester_john-wishart_b1901", "bio_ids": ["winchester_john-wishart_b1901"], "stint_ids": ["Winchester, J. W___Singapore___1949", "Winchester, J. W___Straits Settlements___1931"]} -->
# Dossier case_winchester_john-wishart_b1901

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `winchester_john-wishart_b1901`

- Printed name: **WINCHESTER, JOHN WISHART**
- Birth year: 1901 (attested in editions [1939, 1940])
- Honours: M.D
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L71939.v` — printed in editions [1939, 1940]:**

> WINCHESTER, JOHN WISHART, M.D., Ch.B. (St. Andrews), D.M.R.E. (Camb.), Cert., L.S.T.M. (with dist.).—B. 1901; ed. Harris Acad., Dundee and St. Andrews Univ.; M.O., Malaya, Sept., 1927; port health offr., S'pore, Apr., 1929; med. & health offr., Labuan, June, 1929; M.O. and asst. radiological dept., S'pore, May, 1933; radiologist, Sel., Jan., 1935; do., S'pore, May, 1939.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1927 | M.O. | Malaya | [1939, 1940] |
| 1 | 1929 | port health offr., S'pore | Labuan | [1939, 1940] |
| 2 | 1933 | M.O. and asst. radiological dept., S'pore | Labuan *(inherited from previous clause)* | [1939, 1940] |
| 3 | 1935 | radiologist, Sel | Labuan *(inherited from previous clause)* | [1939, 1940] |
| 4 | 1939 | do., S'pore | Labuan *(inherited from previous clause)* | [1939, 1940] |

## Candidate stint `Winchester, J. W___Singapore___1949`

- Staff-list name: **Winchester, J. W** | colony: **Singapore** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | J. W. Winchester | Radiologist | Hospitals and Dispensaries | — | — |
| 1951 | J. W. Winchester | Radiologist | Hospitals and Dispensaries | — | — |

### Deterministic checks: `winchester_john-wishart_b1901` vs `Winchester, J. W___Singapore___1949`

- [PASS] surname_gate: bio 'WINCHESTER' vs stint 'Winchester, J. W' (exact)
- [PASS] initials: bio ['J', 'W'] ~ stint ['J', 'W']
- [PASS] age_gate: stint starts 1949, birth 1901 (age 48)
- [FAIL] colony: no placed event resolves to 'Singapore'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Winchester, J. W___Straits Settlements___1931`

- Staff-list name: **Winchester, J. W** | colony: **Straits Settlements** | listed 1931–1934 | editions [1931, 1933, 1934]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | J. W. Winchester | Medical Officer | Labuan | — | — |
| 1931 | J. W. Winchester | Medical Officer | Establishment | — | — |
| 1933 | J. W. Winchester | Medical and Health Officer | Medical | — | — |
| 1934 | J. W. Winchester | Medical and Health Officer | Singapore | — | — |

### Deterministic checks: `winchester_john-wishart_b1901` vs `Winchester, J. W___Straits Settlements___1931`

- [PASS] surname_gate: bio 'WINCHESTER' vs stint 'Winchester, J. W' (exact)
- [PASS] initials: bio ['J', 'W'] ~ stint ['J', 'W']
- [PASS] age_gate: stint starts 1931, birth 1901 (age 30)
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1931-1934
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

