<!-- {"case_id": "case_walford_d-s_b1923", "bio_ids": ["walford_d-s_b1923"], "stint_ids": ["Walford, D. S___Western Pacific___1961"]} -->
# Dossier case_walford_d-s_b1923

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `walford_d-s_b1923`

- Printed name: **WALFORD, D. S**
- Birth year: 1923 (attested in editions [1963, 1964, 1965, 1966])
- Honours: B.E.M, C.P.M (1964)
- Appears in editions: [1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1963-L25952.v` — printed in editions [1963, 1964, 1965, 1966]:**

> WALFORD, D. S., B.E.M., C.P.M. (1964).—b. 1923; ed. Aldeburgh Lodge Sch., and Bradfield Coll.; mil. serv., 1942–46/48–50; asst. supt., Mal. police, 1951; dep. supt., B.S.I.P., 1957; secon. Br. commdt., police, N. Heb., 1959.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1951 | asst. supt., Mal. police | Malaya | [1963, 1964, 1965, 1966] |
| 1 | 1957 | dep. supt., B.S.I.P | Malaya *(inherited from previous clause)* | [1963, 1964, 1965, 1966] |
| 2 | 1959 | secon. Br. commdt., police, N. Heb | Malaya *(inherited from previous clause)* | [1963, 1964, 1965, 1966] |

## Candidate stint `Walford, D. S___Western Pacific___1961`

- Staff-list name: **Walford, D. S** | colony: **Western Pacific** | listed 1961–1966 | editions [1961, 1962, 1964, 1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1961 | D. S. Walford | Commandant of Police | British National Administration | — | — |
| 1962 | D. S. Walford | Commandant of Police | British National Administration | — | — |
| 1964 | D. S. Walford | Commandant of Police | British National Administration | — | — |
| 1965 | D. S. Walford | Commandant of Police | British National Administration | B.E.M. | — |
| 1966 | D. S. Walford | Commandant of Police | British National Administration | — | — |

### Deterministic checks: `walford_d-s_b1923` vs `Walford, D. S___Western Pacific___1961`

- [PASS] surname_gate: bio 'WALFORD' vs stint 'Walford, D. S' (exact)
- [PASS] initials: bio ['D', 'S'] ~ stint ['D', 'S']
- [PASS] age_gate: stint starts 1961, birth 1923 (age 38)
- [FAIL] colony: no placed event resolves to 'Western Pacific'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1961-1966
- [FAIL] position_sim: no overlapping placed event to compare
- [PASS] honour: shared: B.E.M
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

