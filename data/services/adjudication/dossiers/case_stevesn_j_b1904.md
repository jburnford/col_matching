<!-- {"case_id": "case_stevesn_j_b1904", "bio_ids": ["stevesn_j_b1904"], "stint_ids": ["Steven, J. L___British Somaliland___1950"]} -->
# Dossier case_stevesn_j_b1904

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['stevesn_j_b1904'] carry a single initial only — the namesake trap applies.

## Biography `stevesn_j_b1904`

- Printed name: **STEVESN, J**
- Birth year: 1904 (attested in editions [1955])
- Honours: E.D (1952), M.B.E (1950), O.B.E (1953)
- Appears in editions: [1955]

### Verbatim printed entry text (OCR)

**Version `col1955-L22856.v` — printed in editions [1955]:**

> STEVESN, J., O.B.E. (1953), M.B.E. (1950), E.D. (1952).—b. 1904; ed. Eastbank Acad. and Glasgow Royal Tech. Coll.; mil. serv., 1939-40; quant. survr., S.L., 1928; Pal., 1933; tech. asst., S.L., 1936; lands offr., and senr. survr., 1944; dir., survs. and lands, 1950.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | quant. survr. | Sierra Leone | [1955] |
| 1 | 1933 | quant. survr. | Palestine | [1955] |
| 2 | 1936 | tech. asst. | Sierra Leone | [1955] |
| 3 | 1944 | lands offr., and senr. survr | Sierra Leone *(inherited from previous clause)* | [1955] |
| 4 | 1950 | dir., survs. and lands | Sierra Leone *(inherited from previous clause)* | [1955] |

## Candidate stint `Steven, J. L___British Somaliland___1950`

- Staff-list name: **Steven, J. L** | colony: **British Somaliland** | listed 1950–1951 | editions [1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | J. L. Steven | Engineers, Grade I and II | Public Works | — | — |
| 1951 | J. L. Steven | Engineers, Grade I and II | PUBLIC WORKS | — | — |

### Deterministic checks: `stevesn_j_b1904` vs `Steven, J. L___British Somaliland___1950`

- [PASS] surname_gate: bio 'STEVESN' vs stint 'Steven, J. L' (fuzzy:1)
- [PASS] initials: bio ['J'] ~ stint ['J', 'L']
- [PASS] age_gate: stint starts 1950, birth 1904 (age 46)
- [FAIL] colony: no placed event resolves to 'British Somaliland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1950-1951
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

