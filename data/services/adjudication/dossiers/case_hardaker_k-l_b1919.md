<!-- {"case_id": "case_hardaker_k-l_b1919", "bio_ids": ["hardaker_k-l_b1919"], "stint_ids": ["Hardaker, K. L___Aden___1958"]} -->
# Dossier case_hardaker_k-l_b1919

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hardaker_k-l_b1919`

- Printed name: **HARDAKER, K. L**
- Birth year: 1919 (attested in editions [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Honours: O.B.E (1965)
- Appears in editions: [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1959-L23828.v` — printed in editions [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> HARDAKER, K. L., O.B.E. (1965).—b. 1919; ed. Kingswood Sch., and Queens' Coll., Camb.; mil. serv., 1940-46, capt.; exec. engr., Tang., 1946; senr., 1955; asst. D.D.W., Aden, 1956; D.D.W., 1957; Fed. D.D.W., 1963.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | exec. engr. | Tanganyika | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1955 | senr | Tanganyika *(inherited from previous clause)* | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1956 | asst. D.D.W. | Aden | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 3 | 1957 | D.D.W | Aden *(inherited from previous clause)* | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 4 | 1963 | Fed. D.D.W | Aden *(inherited from previous clause)* | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Hardaker, K. L___Aden___1958`

- Staff-list name: **Hardaker, K. L** | colony: **Aden** | listed 1958–1966 | editions [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1958 | K. L. Hardaker | Deputy Director of Public Works | Civil Establishment | — | — |
| 1959 | K. L. Hardaker | Deputy Director of Public Works | Civil Establishment | — | — |
| 1960 | K. L. Hardaker | Deputy Director of Public Works | Civil Establishment | — | — |
| 1961 | K. L. Hardaker | Deputy Director of Public Works | Civil Establishment | — | — |
| 1962 | K. L. Hardaker | Deputy Director of Public Works | Civil Establishment | — | — |
| 1963 | K. L. Hardaker | Deputy Director of Public Works | Civil Establishment | — | — |
| 1964 | K. L. Hardaker | Deputy Director of Public Works | Civil Establishment | — | — |
| 1965 | K. L. Hardaker | Deputy Director of Public Works | Civil Establishment | — | — |
| 1966 | K. L. Hardaker | Deputy Director of Public Works | Civil Establishment | — | — |

### Deterministic checks: `hardaker_k-l_b1919` vs `Hardaker, K. L___Aden___1958`

- [PASS] surname_gate: bio 'HARDAKER' vs stint 'Hardaker, K. L' (exact)
- [PASS] initials: bio ['K', 'L'] ~ stint ['K', 'L']
- [PASS] age_gate: stint starts 1958, birth 1919 (age 39)
- [PASS] colony: 3 placed event(s) resolve to 'Aden'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1958-1966
- [FAIL] position_sim: best 21 vs bar 60: 'Fed. D.D.W' ~ 'Deputy Director of Public Works'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

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

