<!-- {"case_id": "case_widgery_c-s_b1922", "bio_ids": ["widgery_c-s_b1922"], "stint_ids": ["Widgery, C. S___Uganda___1949"]} -->
# Dossier case_widgery_c-s_b1922

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `widgery_c-s_b1922`

- Printed name: **WIDGERY, C. S**
- Birth year: 1922 (attested in editions [1964, 1965, 1966])
- Appears in editions: [1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1964-L23059.v` — printed in editions [1964, 1965, 1966]:**

> WIDGERY, C. S.—b. 1922; ed. Badingham Coll., L'head., and Rhodes Univ., S.A.; admin. asst., Uga., 1945; estab. offr., 1948; secretary, P.S.C., 1959; senr. sec., P.S.C., 1962. (Uga. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1945 | admin. asst. | Uganda | [1964, 1965, 1966] |
| 1 | 1948 | estab. offr | Uganda *(inherited from previous clause)* | [1964, 1965, 1966] |
| 2 | 1959 | secretary, P.S.C | Uganda *(inherited from previous clause)* | [1964, 1965, 1966] |
| 3 | 1962 | senr. sec., P.S.C | Uganda *(inherited from previous clause)* | [1964, 1965, 1966] |

## Candidate stint `Widgery, C. S___Uganda___1949`

- Staff-list name: **Widgery, C. S** | colony: **Uganda** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | C. S. Widgery | Personnel Officer | Public Works | — | — |
| 1951 | C. S. Widgery | Personnel Officer | Public Works | — | — |

### Deterministic checks: `widgery_c-s_b1922` vs `Widgery, C. S___Uganda___1949`

- [PASS] surname_gate: bio 'WIDGERY' vs stint 'Widgery, C. S' (exact)
- [PASS] initials: bio ['C', 'S'] ~ stint ['C', 'S']
- [PASS] age_gate: stint starts 1949, birth 1922 (age 27)
- [PASS] colony: 4 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 30 vs bar 60: 'estab. offr' ~ 'Personnel Officer'
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

