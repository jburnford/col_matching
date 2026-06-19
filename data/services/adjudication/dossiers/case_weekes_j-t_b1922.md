<!-- {"case_id": "case_weekes_j-t_b1922", "bio_ids": ["weekes_j-t_b1922"], "stint_ids": ["Weekes, J. T___Uganda___1949"]} -->
# Dossier case_weekes_j-t_b1922

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `weekes_j-t_b1922`

- Printed name: **WEEKES, J. T**
- Birth year: 1922 (attested in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964])
- Appears in editions: [1958, 1959, 1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1958-L28038.v` — printed in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964]:**

> WEEKES, J. T.—b. 1922; ed. King’s Sch., Canterbury, and Glasgow Univ.; admin. offr., Uga., 1946; Sarawak, 1953; seconded, Brunei, 1953; D.O., 1954.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | admin. offr. | Uganda | [1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 1 | 1953 | admin. offr. | Sarawak | [1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 2 | 1953 | seconded | Brunei | [1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 3 | 1954 | seconded | Dominions Office | [1958, 1959, 1960, 1961, 1962, 1963, 1964] |

## Candidate stint `Weekes, J. T___Uganda___1949`

- Staff-list name: **Weekes, J. T** | colony: **Uganda** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | J. T. Weekes | District Officers and Assistant District Officers | Provincial Administration | — | — |
| 1951 | J. T. Weekes | District Officers and Assistant District Officers | Provincial Administration | — | — |

### Deterministic checks: `weekes_j-t_b1922` vs `Weekes, J. T___Uganda___1949`

- [PASS] surname_gate: bio 'WEEKES' vs stint 'Weekes, J. T' (exact)
- [PASS] initials: bio ['J', 'T'] ~ stint ['J', 'T']
- [PASS] age_gate: stint starts 1949, birth 1922 (age 27)
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

