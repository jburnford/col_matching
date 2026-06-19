<!-- {"case_id": "case_lindley_e-p_b1919", "bio_ids": ["lindley_e-p_b1919"], "stint_ids": ["Windley, Edward___Gambia___1958"]} -->
# Dossier case_lindley_e-p_b1919

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Windley, Edward___Gambia___1958` is also gate-compatible with biography(ies) outside this case: ['windley_edward-henry_b1909'] (already linked elsewhere or filtered).

## Biography `lindley_e-p_b1919`

- Printed name: **LINDLEY, E. P**
- Birth year: 1919 (attested in editions [1960, 1961, 1963, 1964])
- Appears in editions: [1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1960-L25285.v` — printed in editions [1960, 1961, 1963, 1964]:**

> LINDLEY, E. P.—b. 1919; ed. High Pavement Sch., Nott., Royal (Dick) Vet. Coll., Edin. Univ. and London Univ.; mil. serv., 1940-46; vet. research offr., Nig., 1949; prin. vet. research offr., 1957; publ. pp. on anthrax, blackleg, and contagious bovine pleuro-pneumonia.

**Version `col1962-L23646.v` — printed in editions [1962]:**

> LINDLEY, E. P.—b. 1919; ed. High Pavement Sch., Nott., Royal (Dick) Vet. Coll., Edin. Univ. and London Univ.; mil. serv., 1940-46; vet. research offr., Nig., 1949; prin. vet. research offr., 1957.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1949 | vet. research offr. | Nigeria | [1960, 1961, 1962, 1963, 1964] |
| 1 | 1957 | prin. vet. research offr | Nigeria *(inherited from previous clause)* | [1960, 1961, 1962, 1963, 1964] |

## Candidate stint `Windley, Edward___Gambia___1958`

- Staff-list name: **Windley, Edward** | colony: **Gambia** | listed 1958–1961 | editions [1958, 1959, 1960, 1961]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1958 | E. H. Windley | Governor and Commander-in-Chief (designate) | Civil Establishment | C.M.G. | — |
| 1959 | Sir Edward Windley | Governor and Commander-in-Chief | Civil Establishment | K.C.M.G. | — |
| 1960 | Sir Edward Windley | Governor and Commander-in-Chief | Civil Establishment | K.C.M.G. | — |
| 1961 | Sir Edward Windley | Governor and Commander-in-Chief | Civil Establishment | K.C.M.G. | — |

### Deterministic checks: `lindley_e-p_b1919` vs `Windley, Edward___Gambia___1958`

- [PASS] surname_gate: bio 'LINDLEY' vs stint 'Windley, Edward' (fuzzy:1)
- [PASS] initials: bio ['E', 'P'] ~ stint ['E']
- [PASS] age_gate: stint starts 1958, birth 1919 (age 39)
- [FAIL] colony: no placed event resolves to 'Gambia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1958-1961
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

