<!-- {"case_id": "case_bazley_w-r_b1924", "bio_ids": ["bazley_w-r_b1924"], "stint_ids": ["Batley, W___Gold Coast___1949"]} -->
# Dossier case_bazley_w-r_b1924

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `bazley_w-r_b1924`

- Printed name: **BAZLEY, W. R**
- Birth year: 1924 (attested in editions [1962, 1963, 1964, 1965])
- Appears in editions: [1962, 1963, 1964, 1965]

### Verbatim printed entry text (OCR)

**Version `col1962-L18688.v` — printed in editions [1962, 1963, 1964, 1965]:**

> BAZLEY, W. R.—b. 1924; ed. Harrow Sch., and Univ. of Toronto; mil. serv., 1942-47, R.N.V.R., lieut.; admin. cadet, Uga., 1951; dist. offr., 1953. (Uga. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1951 | admin. cadet | Uganda | [1962, 1963, 1964, 1965] |
| 1 | 1953 | dist. offr | Uganda *(inherited from previous clause)* | [1962, 1963, 1964, 1965] |

## Candidate stint `Batley, W___Gold Coast___1949`

- Staff-list name: **Batley, W** | colony: **Gold Coast** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | W. Batley | Executive Engineers, Grade II | Public Works | — | — |
| 1951 | W. Batley | Executive Engineers | Engineering Staff | — | — |

### Deterministic checks: `bazley_w-r_b1924` vs `Batley, W___Gold Coast___1949`

- [PASS] surname_gate: bio 'BAZLEY' vs stint 'Batley, W' (fuzzy:1)
- [PASS] initials: bio ['W', 'R'] ~ stint ['W']
- [PASS] age_gate: stint starts 1949, birth 1924 (age 25)
- [FAIL] colony: no placed event resolves to 'Gold Coast'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
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

