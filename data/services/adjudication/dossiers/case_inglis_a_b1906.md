<!-- {"case_id": "case_inglis_a_b1906", "bio_ids": ["inglis_a_b1906"], "stint_ids": ["Inglis, A___Hong Kong___1958"]} -->
# Dossier case_inglis_a_b1906

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 13 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['inglis_a_b1906'] carry a single initial only — the namesake trap applies.

## Biography `inglis_a_b1906`

- Printed name: **INGLIS, A**
- Birth year: 1906 (attested in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964])
- Honours: C.M.G (1962)
- Appears in editions: [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1956-L22119.v` — printed in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]:**

> INGLIS, A., C.M.G. (1962).—b. 1906; ed. Royal High Sch. and Heriot Watt Coll., Edin.; mil. serv., 1942-45; asst. engrnr., S.S., 1930; engrnr. survr., S'pore, 1934; settlement engrnr., Brunei, 1939; exec. engrnr., rural, Mal., 1946; jt. sec., salaries comsnr., 1947; senr. exec. engrnr., 1950; state engrnr., gr. I, 1953; D.P.W., H.K., 1957-63.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1930 | asst. engrnr. | Straits Settlements | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 1 | 1934 | engrnr. survr., S'pore | Straits Settlements *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 2 | 1939 | settlement engrnr. | Brunei | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 3 | 1946 | exec. engrnr., rural | Malaya | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 4 | 1947 | jt. sec., salaries comsnr | Malaya *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 5 | 1950 | senr. exec. engrnr | Malaya *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 6 | 1953 | state engrnr., gr. I | Malaya *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 7 | 1957–1963 | D.P.W. | Hong Kong | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |

## Candidate stint `Inglis, A___Hong Kong___1958`

- Staff-list name: **Inglis, A** | colony: **Hong Kong** | listed 1958–1962 | editions [1958, 1959, 1960, 1961, 1962]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1958 | A. Inglis | Director of Public Works | Civil Establishment | — | — |
| 1959 | A. Inglis | Director of Public Works | Civil Establishment | — | — |
| 1960 | A. Inglis | Director of Public Works | Civil Establishment | — | — |
| 1961 | A. Inglis | Director of Public Works | Civil Establishment | — | — |
| 1962 | A. Inglis | Director of Public Works | Civil Establishment | — | — |

### Deterministic checks: `inglis_a_b1906` vs `Inglis, A___Hong Kong___1958`

- [PASS] surname_gate: bio 'INGLIS' vs stint 'Inglis, A' (exact)
- [PASS] initials: bio ['A'] ~ stint ['A']
- [PASS] age_gate: stint starts 1958, birth 1906 (age 52)
- [PASS] colony: 1 placed event(s) resolve to 'Hong Kong'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1958-1962
- [FAIL] position_sim: best 22 vs bar 60: 'D.P.W.' ~ 'Director of Public Works'
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

