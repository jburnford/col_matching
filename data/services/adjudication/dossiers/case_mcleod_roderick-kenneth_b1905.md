<!-- {"case_id": "case_mcleod_roderick-kenneth_b1905", "bio_ids": ["mcleod_roderick-kenneth_b1905"], "stint_ids": ["McLeod, R___Ceylon___1927"]} -->
# Dossier case_mcleod_roderick-kenneth_b1905

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 51 official(s) with this surname in the graph's staff lists; 12 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mcleod_roderick-kenneth_b1905`

- Printed name: **McLEOD, Roderick Kenneth**
- Birth year: 1905 (attested in editions [1950])
- Honours: A.M.I.M.M, A.R.S.M
- Appears in editions: [1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1950-L37703.v` — printed in editions [1950]:**

> McLEOD, Roderick Kenneth, A.R.S.M., A.M.I.M.M.—b. 1905; ed. Dulwich Coll. and Royal Sch. of Mines; inspr., mines, N. Rhod., 1937; T.T., 1946; senr., 1949.

**Version `col1951-L40518.v` — printed in editions [1951]:**

> MACLEOD, Roderick Kenneth, A.R.S.M., A.M.I.M.M.—b. 1905; ed. Dulwich Coll. and Royal Sch. of Mines; inspr., mines, N. Rhod., 1937; T.T., 1946; senr., 1949.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1937 | inspr., mines | Northern Rhodesia | [1950, 1951] |
| 1 | 1946 | T.T | Northern Rhodesia *(inherited from previous clause)* | [1950, 1951] |
| 2 | 1949 | senr | Northern Rhodesia *(inherited from previous clause)* | [1950, 1951] |

## Candidate stint `McLeod, R___Ceylon___1927`

- Staff-list name: **McLeod, R** | colony: **Ceylon** | listed 1927–1931 | editions [1927, 1928, 1929, 1931]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | R. McLeod | Inspectress of Girls' English Schools | Education Department | — | — |
| 1928 | R. McLeod | Inspectress of Girls' English Schools | Education Department | — | — |
| 1929 | Miss R. McLeod | Inspectress of Girls' English Schools | Education Department | — | — |
| 1931 | R. McLeod | Inspectresses of Girls' English Schools | Education Department | — | — |

### Deterministic checks: `mcleod_roderick-kenneth_b1905` vs `McLeod, R___Ceylon___1927`

- [PASS] surname_gate: bio 'McLEOD' vs stint 'McLeod, R' (exact)
- [PASS] initials: bio ['R', 'K'] ~ stint ['R']
- [PASS] age_gate: stint starts 1927, birth 1905 (age 22)
- [FAIL] colony: no placed event resolves to 'Ceylon'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1927-1931
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

