<!-- {"case_id": "case_darlow_a-r_b1914", "bio_ids": ["darlow_a-r_b1914"], "stint_ids": ["Darlow, A. R___Uganda___1949"]} -->
# Dossier case_darlow_a-r_b1914

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `darlow_a-r_b1914`

- Printed name: **DARLOW, A. R**
- Birth year: 1914 (attested in editions [1958, 1960, 1961])
- Appears in editions: [1958, 1959, 1960, 1961]

### Verbatim printed entry text (OCR)

**Version `col1958-L21835.v` — printed in editions [1958, 1960, 1961]:**

> DARLOW, A. R., T.D.—b. 1914; ed. Humberstone Foundation Sch., Univ. Coll., Hull, and Guy’s Hosp., London; mil. serv., 1939-45; M.O., Uga., 1946-59; publ. Congenital Syphilis (E.A.M.J., 1949).

**Version `col1959-L22199.v` — printed in editions [1959]:**

> DARLOW, A. R., T.D.—b. 1914; ed. Humsterbone Foundation Sch., Univ. Coll., Hull, and Guy's Hosp., London; mil. serv., 1939-45; M.O., Uga., 1946; publ. Congenital Syphilis (E.A.M.J., 1949).

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946–1959 | M.O. | Uganda | [1958, 1959, 1960, 1961] |
| 1 | 1949 | publ. Congenital Syphilis (E.A.M.J | Uganda *(inherited from previous clause)* | [1958, 1959, 1960, 1961] |

## Candidate stint `Darlow, A. R___Uganda___1949`

- Staff-list name: **Darlow, A. R** | colony: **Uganda** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | A. R. Darlow | Medical Officers | Medical | — | — |
| 1951 | A. R. Darlow | Medical Officers | MEDICAL | — | — |

### Deterministic checks: `darlow_a-r_b1914` vs `Darlow, A. R___Uganda___1949`

- [PASS] surname_gate: bio 'DARLOW' vs stint 'Darlow, A. R' (exact)
- [PASS] initials: bio ['A', 'R'] ~ stint ['A', 'R']
- [PASS] age_gate: stint starts 1949, birth 1914 (age 35)
- [PASS] colony: 2 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 31 vs bar 60: 'publ. Congenital Syphilis (E.A.M.J' ~ 'Medical Officers'
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

