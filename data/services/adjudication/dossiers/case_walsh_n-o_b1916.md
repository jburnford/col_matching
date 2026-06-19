<!-- {"case_id": "case_walsh_n-o_b1916", "bio_ids": ["walsh_n-o_b1916"], "stint_ids": ["Walsh, N. O___Jamaica___1955"]} -->
# Dossier case_walsh_n-o_b1916

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 32 official(s) with this surname in the graph's staff lists; 15 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `walsh_n-o_b1916`

- Printed name: **WALSH, N. O**
- Birth year: 1916 (attested in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964])
- Appears in editions: [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1957-L28144.v` — printed in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]:**

> WALSH, N. O.—b. 1916; ed. Excelsior High Sch., J'ca, and Ontario Agric. Coll., Toronto Univ.; asst. to govt. chemist, J'ca, 1945; dep. govt. chemist, 1953. (J'ca Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1945 | asst. to govt. chemist | Jamaica | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 1 | 1953 | dep. govt. chemist | Jamaica *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |

## Candidate stint `Walsh, N. O___Jamaica___1955`

- Staff-list name: **Walsh, N. O** | colony: **Jamaica** | listed 1955–1956 | editions [1955, 1956]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1955 | N. O. Walsh | Deputy Government Chemist | Civil Establishment | — | — |
| 1956 | N. O. Walsh | Deputy Government Chemist | Civil Establishment | — | — |

### Deterministic checks: `walsh_n-o_b1916` vs `Walsh, N. O___Jamaica___1955`

- [PASS] surname_gate: bio 'WALSH' vs stint 'Walsh, N. O' (exact)
- [PASS] initials: bio ['N', 'O'] ~ stint ['N', 'O']
- [PASS] age_gate: stint starts 1955, birth 1916 (age 39)
- [PASS] colony: 2 placed event(s) resolve to 'Jamaica'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1955-1956
- [PASS] position_sim: best 78 vs bar 60: 'dep. govt. chemist' ~ 'Deputy Government Chemist'
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

