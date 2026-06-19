<!-- {"case_id": "case_morris_h-f_b1918", "bio_ids": ["morris_h-f_b1918"], "stint_ids": ["Morris, H. F___Uganda___1949"]} -->
# Dossier case_morris_h-f_b1918

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 113 official(s) with this surname in the graph's staff lists; 39 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `morris_h-f_b1918`

- Printed name: **MORRIS, H. F**
- Birth year: 1918 (attested in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965])
- Appears in editions: [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965]

### Verbatim printed entry text (OCR)

**Version `col1958-L25426.v` — printed in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965]:**

> MORRIS, H. F.—b. 1918; ed. Cheltenham Coll., and Trinity Coll., Dublin; mil. serv., 1941-46, capt.; cl. I, Burma civil serv., 1946; admin. offr., Uga., 1948; D.O., 1950; native courts advr., 1956; senr. D.O., 1961. (Uga. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | cl. I, Burma civil serv | — | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 1 | 1948 | admin. offr. | Uganda | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 2 | 1950 | admin. offr. | Dominions Office | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 3 | 1956 | native courts advr | Dominions Office *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 4 | 1961 | senr. D.O | Dominions Office *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |

## Candidate stint `Morris, H. F___Uganda___1949`

- Staff-list name: **Morris, H. F** | colony: **Uganda** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | H. F. Morris | District Officers and Assistant District Officers | Provincial Administration | — | — |
| 1951 | H. F. Morris | District Officers and Assistant District Officers | Provincial Administration | — | — |

### Deterministic checks: `morris_h-f_b1918` vs `Morris, H. F___Uganda___1949`

- [PASS] surname_gate: bio 'MORRIS' vs stint 'Morris, H. F' (exact)
- [PASS] initials: bio ['H', 'F'] ~ stint ['H', 'F']
- [PASS] age_gate: stint starts 1949, birth 1918 (age 31)
- [PASS] colony: 1 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 44 vs bar 60: 'admin. offr.' ~ 'District Officers and Assistant District Officers'
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

