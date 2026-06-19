<!-- {"case_id": "case_groves_robert_b1900", "bio_ids": ["groves_robert_b1900"], "stint_ids": ["Groves, G. R___Bermuda___1939", "Groves, G. R___Bermuda___1950"]} -->
# Dossier case_groves_robert_b1900

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['groves_robert_b1900'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Groves, G. R___Bermuda___1939` is also gate-compatible with biography(ies) outside this case: ['groves_g-r_b1910'] (already linked elsewhere or filtered).
- NOTE: stint `Groves, G. R___Bermuda___1950` is also gate-compatible with biography(ies) outside this case: ['groves_g-r_b1910'] (already linked elsewhere or filtered).

## Biography `groves_robert_b1900`

- Printed name: **GROVES, Robert**
- Birth year: 1900 (attested in editions [1948])
- Honours: A.M.I.E.E
- Appears in editions: [1948]

### Verbatim printed entry text (OCR)

**Version `col1948-L33037.v` — printed in editions [1948]:**

> GROVES, Robert, A.M.I.E.E.—b. 1900; ed. Harris Acad. Dundee and Tech. Coll., Dundee; on mil. serv. 1918-20; Br. P.O., 1916; inspr., 1925; engnr., posts and tels., Nig., 1927; senr. engnr., 1942.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1916 | Br. P.O | — | [1948] |
| 1 | 1925 | inspr | — | [1948] |
| 2 | 1927 | engnr., posts and tels. | Nigeria | [1948] |
| 3 | 1942 | senr. engnr | Nigeria *(inherited from previous clause)* | [1948] |

## Candidate stint `Groves, G. R___Bermuda___1939`

- Staff-list name: **Groves, G. R** | colony: **Bermuda** | listed 1939–1940 | editions [1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | G. R. Groves | Horticulturist | Department of Agriculture | — | — |
| 1940 | G. R. Groves | Horticulturist | Department of Agriculture | — | — |

### Deterministic checks: `groves_robert_b1900` vs `Groves, G. R___Bermuda___1939`

- [PASS] surname_gate: bio 'GROVES' vs stint 'Groves, G. R' (exact)
- [PASS] initials: bio ['R'] ~ stint ['G', 'R']
- [PASS] age_gate: stint starts 1939, birth 1900 (age 39)
- [FAIL] colony: no placed event resolves to 'Bermuda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1939-1940
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Groves, G. R___Bermuda___1950`

- Staff-list name: **Groves, G. R** | colony: **Bermuda** | listed 1950–1966 | editions [1950, 1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | G. R. Groves | Assistant Director of Agriculture | Agricultural | — | — |
| 1951 | G. R. Groves | Assistant Director of Agriculture | Agricultural | — | — |
| 1953 | G. R. Groves | Assistant Director of Agriculture | Civil Establishment | — | — |
| 1954 | G. R. Groves | Assistant Director of Agriculture | Civil Establishment | — | — |
| 1955 | G. R. Groves | Assistant Director of Agriculture | Civil Establishment | — | — |
| 1956 | G. R. Groves | Director of Agriculture | Civil Establishment | — | — |
| 1957 | G. R. Groves | Director of Agriculture | Civil Establishment | — | — |
| 1958 | G. R. Groves | Director of Agriculture | Civil Establishment | — | — |
| 1959 | G. R. Groves | Director of Agriculture | Civil Establishment | — | — |
| 1960 | G. R. Groves | Director of Agriculture | Civil Establishment | — | — |
| 1961 | G. R. Groves | Director of Agriculture | Civil Establishment | — | — |
| 1962 | G. R. Groves | Director of Agriculture and Fisheries | Civil Establishment | — | — |
| 1963 | G. R. Groves | Director of Agriculture and Fisheries | Civil Establishment | — | — |
| 1964 | G. R. Groves | Director of Agriculture and Fisheries | Civil Establishment | — | — |
| 1965 | G. R. Groves | Director of Agriculture and Fisheries | Civil Establishment | — | — |
| 1966 | G. R. Groves | Director of Agriculture and Fisheries | Civil Establishment | — | — |

### Deterministic checks: `groves_robert_b1900` vs `Groves, G. R___Bermuda___1950`

- [PASS] surname_gate: bio 'GROVES' vs stint 'Groves, G. R' (exact)
- [PASS] initials: bio ['R'] ~ stint ['G', 'R']
- [PASS] age_gate: stint starts 1950, birth 1900 (age 50)
- [FAIL] colony: no placed event resolves to 'Bermuda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1950-1966
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

