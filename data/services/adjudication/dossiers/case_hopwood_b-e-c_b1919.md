<!-- {"case_id": "case_hopwood_b-e-c_b1919", "bio_ids": ["hopwood_b-e-c_b1919"], "stint_ids": ["Hopwood, B. E. C___Uganda___1949", "Hopwood, B. E. C___Uganda___1961"]} -->
# Dossier case_hopwood_b-e-c_b1919

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hopwood_b-e-c_b1919`

- Printed name: **HOPWOOD, B. E. C**
- Birth year: 1919 (attested in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963])
- Appears in editions: [1957, 1958, 1959, 1960, 1961, 1962, 1963]

### Verbatim printed entry text (OCR)

**Version `col1957-L24194.v` — printed in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963]:**

> HOPWOOD, B. E. C.—b. 1919; ed. Ardingly Coll., King’s Coll., Taunton and St. Mary’s Hospital; M.O., Falk. Is., 1944; Uga., 1948; S.M.O., 1954; specialist, 1959; dep. chief M.O., 1960. (Uga. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1944 | M.O. | Falkland Islands | [1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 1 | 1948 | M.O. | Uganda | [1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 2 | 1954 | S.M.O | Uganda *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 3 | 1959 | specialist | Uganda *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 4 | 1960 | dep. chief M.O | Uganda *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963] |

## Candidate stint `Hopwood, B. E. C___Uganda___1949`

- Staff-list name: **Hopwood, B. E. C** | colony: **Uganda** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | B. E. C. Hopwood | Medical Officers | Medical | — | — |
| 1951 | B. E. C. Hopwood | Medical Officers | MEDICAL | — | — |

### Deterministic checks: `hopwood_b-e-c_b1919` vs `Hopwood, B. E. C___Uganda___1949`

- [PASS] surname_gate: bio 'HOPWOOD' vs stint 'Hopwood, B. E. C' (exact)
- [PASS] initials: bio ['B', 'E', 'C'] ~ stint ['B', 'E', 'C']
- [PASS] age_gate: stint starts 1949, birth 1919 (age 30)
- [PASS] colony: 4 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 22 vs bar 60: 'M.O.' ~ 'Medical Officers'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Hopwood, B. E. C___Uganda___1961`

- Staff-list name: **Hopwood, B. E. C** | colony: **Uganda** | listed 1961–1962 | editions [1961, 1962]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1961 | B. E. C. Hopwood | Deputy Secretary to the Ministry of Health | Civil Establishment | — | — |
| 1962 | B. E. C. Hopwood | Permanent Secretary and Chief Medical Officer, Ministry of Health | Civil Establishment | — | — |

### Deterministic checks: `hopwood_b-e-c_b1919` vs `Hopwood, B. E. C___Uganda___1961`

- [PASS] surname_gate: bio 'HOPWOOD' vs stint 'Hopwood, B. E. C' (exact)
- [PASS] initials: bio ['B', 'E', 'C'] ~ stint ['B', 'E', 'C']
- [PASS] age_gate: stint starts 1961, birth 1919 (age 42)
- [PASS] colony: 4 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1961-1962
- [FAIL] position_sim: best 59 vs bar 60: 'dep. chief M.O' ~ 'Permanent Secretary and Chief Medical Officer, Ministry of Health'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): 1 agreeing edition-year(s) [1962] pos~59 (bar: >=2)
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

