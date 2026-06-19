<!-- {"case_id": "case_hargreaves_dennis-james_b1914", "bio_ids": ["hargreaves_dennis-james_b1914"], "stint_ids": ["Hargreaves, J___Hong Kong___1949"]} -->
# Dossier case_hargreaves_dennis-james_b1914

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 17 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Hargreaves, J___Hong Kong___1949` is also gate-compatible with biography(ies) outside this case: ['hargreaves_john_b1898'] (already linked elsewhere or filtered).

## Biography `hargreaves_dennis-james_b1914`

- Printed name: **HARGREAVES, Dennis James**
- Birth year: 1914 (attested in editions [1951])
- Appears in editions: [1951]

### Verbatim printed entry text (OCR)

**Version `col1951-L38849.v` — printed in editions [1951]:**

> HARGREAVES, Dennis James.—b. 1914; ed. Bromsgrove Sch.; standard II, Malay; standard III, Cantonese; interned, 1942-45; prob., Mal., 1935; C.R.O., 1936; O.C.P.D., 1937; to China, 1937-38; A.C.P., 1938; asst. O.C. Dets., 1938; O.C.P.D., 1940; O.S.P.C., 1946; S.I.O.N., 1947; O.S.P.C., 1948.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1935 | prob. | Malaya | [1951] |
| 1 | 1936 | C.R.O | Malaya *(inherited from previous clause)* | [1951] |
| 2 | 1937 | O.C.P.D | Malaya *(inherited from previous clause)* | [1951] |
| 3 | 1938 | A.C.P | Malaya *(inherited from previous clause)* | [1951] |
| 4 | 1940 | O.C.P.D | Malaya *(inherited from previous clause)* | [1951] |
| 5 | 1942–1945 | interned | — | [1951] |
| 6 | 1946 | O.S.P.C | Malaya *(inherited from previous clause)* | [1951] |
| 7 | 1947 | S.I.O.N | Malaya *(inherited from previous clause)* | [1951] |
| 8 | 1948 | O.S.P.C | Malaya *(inherited from previous clause)* | [1951] |

## Candidate stint `Hargreaves, J___Hong Kong___1949`

- Staff-list name: **Hargreaves, J** | colony: **Hong Kong** | listed 1949–1953 | editions [1949, 1950, 1951, 1953]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | J. Hargreaves | Accountant | Stores | — | — |
| 1950 | J. Hargreaves | Assistant Accountant-General | Treasury | — | — |
| 1951 | J. Hargreaves | Assistant Accountant-General | TREASURY | — | — |
| 1953 | J. Hargreaves | Assistant Accountant-General | Civil Establishment | — | — |

### Deterministic checks: `hargreaves_dennis-james_b1914` vs `Hargreaves, J___Hong Kong___1949`

- [PASS] surname_gate: bio 'HARGREAVES' vs stint 'Hargreaves, J' (exact)
- [PASS] initials: bio ['D', 'J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1949, birth 1914 (age 35)
- [FAIL] colony: no placed event resolves to 'Hong Kong'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1953
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

