<!-- {"case_id": "case_addison_w-r-l_b1919", "bio_ids": ["addison_w-r-l_b1919"], "stint_ids": ["Addison, W. R. L___Uganda___1949"]} -->
# Dossier case_addison_w-r-l_b1919

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 21 official(s) with this surname in the graph's staff lists; 10 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `addison_w-r-l_b1919`

- Printed name: **ADDISON, W. R. L**
- Birth year: 1919 (attested in editions [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964])
- Honours: M.B.E (1956)
- Appears in editions: [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1953-L16301.v` — printed in editions [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]:**

> ADDISON, W. R. L., M.B.E. (1956), M.C.—b. 1919; ed. Haileybury Coll. and Queen's Coll., Oxford; mil. serv., 1939-46, maj.; cadet, Uganda, 1948; A.D.O., 1950; asst. sec., E.A.C.S.O., 1952; clk., cent. leg. assembly, 1951-55; asst. sec., Ken., 1957; under sec. (fin. and estab.) min. of agric., 1959-63. (Ken. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1948 | cadet | Uganda | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 1 | 1950 | A.D.O | Uganda *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 2 | 1951–1955 | clk., cent. leg. assembly | Uganda *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 3 | 1952 | asst. sec., E.A.C.S.O | Uganda *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 4 | 1957 | asst. sec. | Kenya | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 5 | 1959–1963 | under sec. (fin. and estab.) min. of agric | Kenya *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |

## Candidate stint `Addison, W. R. L___Uganda___1949`

- Staff-list name: **Addison, W. R. L** | colony: **Uganda** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | W. R. L. Addison | District Officers and Assistant District Officers | Provincial Administration | — | — |
| 1951 | W. R. L. Addison | District Officers and Assistant District Officers | Provincial Administration | — | — |

### Deterministic checks: `addison_w-r-l_b1919` vs `Addison, W. R. L___Uganda___1949`

- [PASS] surname_gate: bio 'ADDISON' vs stint 'Addison, W. R. L' (exact)
- [PASS] initials: bio ['W', 'R', 'L'] ~ stint ['W', 'R', 'L']
- [PASS] age_gate: stint starts 1949, birth 1919 (age 30)
- [PASS] colony: 4 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 4 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 36 vs bar 60: 'asst. sec., E.A.C.S.O' ~ 'District Officers and Assistant District Officers'
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

