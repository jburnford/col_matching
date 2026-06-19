<!-- {"case_id": "case_freegard_d-m_b1918", "bio_ids": ["freegard_d-m_b1918"], "stint_ids": ["Freegard, D. M___Western Pacific___1951", "Freegard, D. M___Western Pacific___1964"]} -->
# Dossier case_freegard_d-m_b1918

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `freegard_d-m_b1918`

- Printed name: **FREEGARD, D. M**
- Birth year: 1918 (attested in editions [1962, 1963, 1964, 1965])
- Appears in editions: [1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1962-L21255.v` — printed in editions [1962, 1963, 1964, 1965]:**

> FREEGARD, D. M.—b. 1918; ed. Cheltenham Coll. and Queen's Coll., Oxford; mil. serv., 1939-50, maj. (desp.), R.A.R.O.; admin. offr., N. Heb., 1950; G. & E.I.C., 1953; W. Pac. H.C., 1958; admin. offr., cl. A, 1962; G. & E.C.I., 1963.

**Version `col1966-L14803.v` — printed in editions [1966]:**

> FREGARD, D. M.—b. 1918; ed. Cheltenham Coll. and Queen's Coll., Oxford; mil. serv., 1939-50, maj. (desp.), R.A.R.O.; admin offr., N. Heb., 1950; G. & E.I.C., 1953; W. Pac. H.C., 1958; admin. offr., cl. A, 1962; G. & E.I.C., 1963.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1950 | admin. offr., N. Heb | — | [1962, 1963, 1964, 1965, 1966] |
| 1 | 1953 | G. & E.I.C | — | [1962, 1963, 1964, 1965, 1966] |
| 2 | 1958 | W. Pac. H.C | Western Pacific | [1962, 1963, 1964, 1965, 1966] |
| 3 | 1962 | admin. offr., cl. A | Western Pacific *(inherited from previous clause)* | [1962, 1963, 1964, 1965, 1966] |
| 4 | 1963 | G. & E.C.I | Western Pacific *(inherited from previous clause)* | [1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Freegard, D. M___Western Pacific___1951`

- Staff-list name: **Freegard, D. M** | colony: **Western Pacific** | listed 1951–1958 | editions [1951, 1953, 1955, 1956, 1957, 1958]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1951 | D. M. Freegard | Administrative Officer | British National Administration | — | — |
| 1953 | D. M. Freegard | Administration Officer | British National Administration | — | — |
| 1955 | D. M. Freegard | Administrative Officer | Civil Establishment | — | — |
| 1956 | D. M. Freegard | Administrative Officer | Civil Establishment | — | — |
| 1957 | D. M. Freegard | Administrative Officer | Civil Establishment | — | — |
| 1958 | D. M. Freegard | Administrative Officers | Civil Establishment | — | — |

### Deterministic checks: `freegard_d-m_b1918` vs `Freegard, D. M___Western Pacific___1951`

- [PASS] surname_gate: bio 'FREEGARD' vs stint 'Freegard, D. M' (exact)
- [PASS] initials: bio ['D', 'M'] ~ stint ['D', 'M']
- [PASS] age_gate: stint starts 1951, birth 1918 (age 33)
- [PASS] colony: 3 placed event(s) resolve to 'Western Pacific'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1951-1958
- [FAIL] position_sim: best 13 vs bar 60: 'W. Pac. H.C' ~ 'Administrative Officer'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Freegard, D. M___Western Pacific___1964`

- Staff-list name: **Freegard, D. M** | colony: **Western Pacific** | listed 1964–1966 | editions [1964, 1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1964 | D. M. Freegard | Administrative Officer | Civil Establishment | — | — |
| 1965 | D. M. Freegard | Administrative Officer | Civil Establishment | — | — |
| 1966 | D. M. Freegard | Administrative Officer (Class A) | Civil Establishment | — | — |

### Deterministic checks: `freegard_d-m_b1918` vs `Freegard, D. M___Western Pacific___1964`

- [PASS] surname_gate: bio 'FREEGARD' vs stint 'Freegard, D. M' (exact)
- [PASS] initials: bio ['D', 'M'] ~ stint ['D', 'M']
- [PASS] age_gate: stint starts 1964, birth 1918 (age 46)
- [PASS] colony: 3 placed event(s) resolve to 'Western Pacific'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1964-1966
- [PASS] position_sim: best 67 vs bar 60: 'admin. offr., cl. A' ~ 'Administrative Officer (Class A)'
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

