<!-- {"case_id": "case_cherry_j-k-t_b1914", "bio_ids": ["cherry_j-k-t_b1914"], "stint_ids": ["Cherry, J. K___Uganda___1949"]} -->
# Dossier case_cherry_j-k-t_b1914

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `cherry_j-k-t_b1914`

- Printed name: **CHERRY, J. K. T**
- Birth year: 1914 (attested in editions [1958, 1962])
- Appears in editions: [1958, 1959, 1960, 1961, 1962]

### Verbatim printed entry text (OCR)

**Version `col1958-L21345.v` — printed in editions [1958, 1962]:**

> CHERRY, J. K. T.—b. 1914; ed. John Neilson Instn., Paisley, Glasgow and Edin. Univs.; mil. serv., 1940-46, sqdn. ldr.; M.O., Uga., 1946; S.M.O., 1956-61.

**Version `col1959-L21655.v` — printed in editions [1959, 1960, 1961]:**

> CHERRY, J. K. T.—b. 1914; ed. John Neilson Instn., Paisley, Glasgow and Edin. Univs.; mil. serv., 1940-46, sqdn. ldr.; M.O., Uga., 1946; S.M.O., 1956; publ. Prevention and Treatment of Tick Borne Relapsing Fever (Trans. R.S.T.M. and H.).

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | M.O. | Uganda | [1958, 1959, 1960, 1961, 1962] |
| 1 | 1956–1961 | S.M.O | Uganda *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962] |

## Candidate stint `Cherry, J. K___Uganda___1949`

- Staff-list name: **Cherry, J. K** | colony: **Uganda** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | J. K. Cherry | Medical Officers | Medical | — | — |
| 1951 | J. K. Cherry | Medical Officers | MEDICAL | — | — |

### Deterministic checks: `cherry_j-k-t_b1914` vs `Cherry, J. K___Uganda___1949`

- [PASS] surname_gate: bio 'CHERRY' vs stint 'Cherry, J. K' (exact)
- [PASS] initials: bio ['J', 'K', 'T'] ~ stint ['J', 'K']
- [PASS] age_gate: stint starts 1949, birth 1914 (age 35)
- [PASS] colony: 2 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 22 vs bar 60: 'M.O.' ~ 'Medical Officers'
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

