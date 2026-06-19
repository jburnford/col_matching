<!-- {"case_id": "case_paul_r_b1914", "bio_ids": ["paul_r_b1914"], "stint_ids": ["Paul, R. J___Northern Rhodesia___1956", "Paul, William R. C___Ceylon___1931"]} -->
# Dossier case_paul_r_b1914

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 41 official(s) with this surname in the graph's staff lists; 16 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['paul_r_b1914'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Paul, R. J___Northern Rhodesia___1956` is also gate-compatible with biography(ies) outside this case: ['paul_john_b1916', 'paul_robert-james_b1888'] (already linked elsewhere or filtered).

## Biography `paul_r_b1914`

- Printed name: **PAUL, R**
- Birth year: 1914 (attested in editions [1957, 1958, 1959, 1960, 1961, 1962])
- Honours: O.B.E (1961)
- Appears in editions: [1957, 1958, 1959, 1960, 1961, 1962]

### Verbatim printed entry text (OCR)

**Version `col1957-L26260.v` — printed in editions [1957, 1958, 1959, 1960, 1961, 1962]:**

> PAUL, R., O.B.E. (1961).—b. 1914; ed. Hamilton Academy and Glasgow Univ.; mil. serv., 1940-45, lt.-col. R.A.M.C.; M.O., N. Rhod., 1948; specialist, 1951; dir., pneumoconiosis med. and research bureau, 1951-61.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1948 | M.O. | Northern Rhodesia | [1957, 1958, 1959, 1960, 1961, 1962] |
| 1 | 1951 | specialist | Northern Rhodesia *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962] |

## Candidate stint `Paul, R. J___Northern Rhodesia___1956`

- Staff-list name: **Paul, R. J** | colony: **Northern Rhodesia** | listed 1956–1961 | editions [1956, 1957, 1958, 1959, 1960, 1961]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1956 | R. Paul | Chairman of the Silicosis Medical Bureau | Civil Establishment | — | — |
| 1957 | R. Paul | Chairman of the Silicosis Medical Bureau | Civil Establishment | — | — |
| 1958 | R. Paul | Chairman of the Pneumoconiosis, Medical and Research Bureau | Civil Establishment | M.B.E. | — |
| 1959 | R. Paul | Chairman of the Pneumoconiosis, Medical and Research Bureau | Civil Establishment | M.B.E. | — |
| 1960 | R. Paul | Chairman of the Pneumoconiosis, Medical and Research Bureau | Civil Establishment | — | — |
| 1961 | R. Paul | Director, Pneumoconiosis, Medical and Research Bureau | Civil Establishment | — | — |

### Deterministic checks: `paul_r_b1914` vs `Paul, R. J___Northern Rhodesia___1956`

- [PASS] surname_gate: bio 'PAUL' vs stint 'Paul, R. J' (exact)
- [PASS] initials: bio ['R'] ~ stint ['R', 'J']
- [PASS] age_gate: stint starts 1956, birth 1914 (age 42)
- [PASS] colony: 2 placed event(s) resolve to 'Northern Rhodesia'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1956-1961
- [FAIL] position_sim: best 32 vs bar 60: 'specialist' ~ 'Chairman of the Silicosis Medical Bureau'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

## Candidate stint `Paul, William R. C___Ceylon___1931`

- Staff-list name: **Paul, William R. C** | colony: **Ceylon** | listed 1931–1940 | editions [1931, 1934, 1936, 1937, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | W. R. C. Paul | Divisional Agricultural Officer (Southern) | Agricultural Branch | — | — |
| 1934 | W. R. C. Paul | Divisional Agricultural Officer (South-Western) | Department of Agriculture | — | — |
| 1936 | William R. C. Paul | Divisional Agricultural Officer (Northern) | Department of Agriculture | — | — |
| 1937 | W. R. C. Paul | Divisional Agricultural Officer (Northern) | Agricultural Branch | — | — |
| 1940 | W. R. C. Paul | Agricultural Officer, Grade I (Central) | Agricultural Branch | — | — |

### Deterministic checks: `paul_r_b1914` vs `Paul, William R. C___Ceylon___1931`

- [PASS] surname_gate: bio 'PAUL' vs stint 'Paul, William R. C' (exact)
- [PASS] initials: bio ['R'] ~ stint ['W', 'R', 'C']
- [PASS] age_gate: stint starts 1931, birth 1914 (age 17)
- [FAIL] colony: no placed event resolves to 'Ceylon'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1931-1940
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

