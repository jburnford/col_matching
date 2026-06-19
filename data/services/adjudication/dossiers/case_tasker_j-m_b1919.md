<!-- {"case_id": "case_tasker_j-m_b1919", "bio_ids": ["tasker_j-m_b1919"], "stint_ids": ["Tasker, J. M___Gibraltar___1949"]} -->
# Dossier case_tasker_j-m_b1919

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `tasker_j-m_b1919`

- Printed name: **TASKER, J. M**
- Birth year: 1919 (attested in editions [1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Honours: M.B.E (1955)
- Appears in editions: [1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1955-L22955.v` — printed in editions [1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> TASKER, J. M., M.B.E. (1955).—b. 1919; ed. Westminster Sch. and Trinity Coll., Camb.; mil. serv., 1939-46 (desps.); asst. sec., Gib., 1947; Gam., 1951; colony comsnr., 1953; senr. asst. sec., Ken., 1956; dep. comsnr., community devel., 1957; secon., under sec., 1958. (Ken. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1947 | asst. sec. | Gibraltar | [1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1951 | Gam | Gibraltar *(inherited from previous clause)* | [1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1953 | colony comsnr | Gibraltar *(inherited from previous clause)* | [1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 3 | 1956 | senr. asst. sec. | Kenya | [1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 4 | 1957 | dep. comsnr., community devel | Kenya *(inherited from previous clause)* | [1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 5 | 1958 | secon., under sec | Kenya *(inherited from previous clause)* | [1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Tasker, J. M___Gibraltar___1949`

- Staff-list name: **Tasker, J. M** | colony: **Gibraltar** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | J. M. Tasker | Assistant Secretary | Secretariat | — | — |
| 1950 | J. M. Tasker | Assistant Secretary | Secretariat | — | — |
| 1951 | J. M. Tasker | Assistant Secretaries | Secretariat | — | — |

### Deterministic checks: `tasker_j-m_b1919` vs `Tasker, J. M___Gibraltar___1949`

- [PASS] surname_gate: bio 'TASKER' vs stint 'Tasker, J. M' (exact)
- [PASS] initials: bio ['J', 'M'] ~ stint ['J', 'M']
- [PASS] age_gate: stint starts 1949, birth 1919 (age 30)
- [PASS] colony: 3 placed event(s) resolve to 'Gibraltar'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 59 vs bar 60: 'asst. sec.' ~ 'Assistant Secretary'
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

