<!-- {"case_id": "case_wilders_e-p-l_b1909", "bio_ids": ["wilders_e-p-l_b1909"], "stint_ids": ["Wilders, E. P. L___British Somaliland___1955"]} -->
# Dossier case_wilders_e-p-l_b1909

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `wilders_e-p-l_b1909`

- Printed name: **WILDERS, E. P. L**
- Birth year: 1909 (attested in editions [1957, 1958, 1959, 1960, 1962, 1963])
- Honours: O.B.E (1959)
- Appears in editions: [1957, 1958, 1959, 1960, 1961, 1962, 1963]

### Verbatim printed entry text (OCR)

**Version `col1957-L28355.v` — printed in editions [1957, 1958, 1959, 1960, 1962, 1963]:**

> WILDERS, E. P. L., O.B.E. (1959)—b. 1909; ed. Clifton Coll. and King's Coll., London; mil. serv., 1939-47, major; asst. engnr., Uga., 1936; exec. engnr., P.W.D., Ken., 1947; D.P.W., Som., 1955. (Som. Govt. service.)

**Version `col1961-L28719.v` — printed in editions [1961]:**

> WILDES, E. P. L., O.B.E. (1959)—b. 1909; ed. Clifton Coll. and King's Coll., London; mil. serv., 1939-47, major; asst. engnr., Uga., 1936; exec. engnr., P.W.D., Ken., 1947; D.P.W., Som., 1955.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1936 | asst. engnr. | Uganda | [1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 1 | 1947 | exec. engnr., P.W.D. | Kenya | [1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 2 | 1955 | D.P.W. | Somaliland | [1957, 1958, 1959, 1960, 1961, 1962, 1963] |

## Candidate stint `Wilders, E. P. L___British Somaliland___1955`

- Staff-list name: **Wilders, E. P. L** | colony: **British Somaliland** | listed 1955–1960 | editions [1955, 1956, 1957, 1958, 1959, 1960]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1955 | E. P. Wilders | Director of Public Works | Civil Establishment | — | — |
| 1956 | E. P. L. Wilders | Director of Public Works | Civil Establishment | — | — |
| 1957 | E. P. L. Wilders | Director of Public Works | Civil Establishment | — | — |
| 1958 | E. P. L. Wilders | Director of Public Works | Civil Establishment | — | — |
| 1959 | E. P. L. Wilders | Director of Public Works | Civil Establishment | — | — |
| 1960 | E. P. L. Wilders | Director of Public Works | Civil Establishment | — | — |

### Deterministic checks: `wilders_e-p-l_b1909` vs `Wilders, E. P. L___British Somaliland___1955`

- [PASS] surname_gate: bio 'WILDERS' vs stint 'Wilders, E. P. L' (exact)
- [PASS] initials: bio ['E', 'P', 'L'] ~ stint ['E', 'P', 'L']
- [PASS] age_gate: stint starts 1955, birth 1909 (age 46)
- [PASS] colony: 1 placed event(s) resolve to 'British Somaliland'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1955-1960
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

