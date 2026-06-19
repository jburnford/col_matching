<!-- {"case_id": "case_adshead_j-w_b1923", "bio_ids": ["adshead_j-w_b1923"], "stint_ids": ["Adshead, J. W___Gambia___1961", "Adshead, J. W___St Helena___1955"]} -->
# Dossier case_adshead_j-w_b1923

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `adshead_j-w_b1923`

- Printed name: **ADSHEAD, J. W**
- Birth year: 1923 (attested in editions [1961, 1962, 1963, 1964, 1965, 1966])
- Honours: M.B.E (1965)
- Appears in editions: [1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1961-L19031.v` — printed in editions [1961, 1962, 1963, 1964, 1965, 1966]:**

> ADSHEAD, J. W., M.B.E. (1965).—b. 1923; ed. Tennehall Coll., Staffs., Blundell's Sch., and Birmingham Univ.; mil. serv., 1942-47; senr. auditor, N. Nig., 1958; prin. auditor, Gam., 1960; redesig. dir. audit, 1963-65. (Gambia Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1958 | senr. auditor | Northern Nigeria | [1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1960 | prin. auditor, Gam | Northern Nigeria *(inherited from previous clause)* | [1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1963–1965 | redesig. dir. audit | Northern Nigeria *(inherited from previous clause)* | [1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Adshead, J. W___Gambia___1961`

- Staff-list name: **Adshead, J. W** | colony: **Gambia** | listed 1961–1965 | editions [1961, 1962, 1963, 1964, 1965]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1961 | J. W. Adshead | Principal Auditor | Civil Establishment | — | — |
| 1962 | J. W. Adshead | Principal Auditor | Civil Establishment | — | — |
| 1963 | J. W. Adshead | Principal Auditor | Non-Ministerial | — | — |
| 1964 | J. W. Adshead | Director of Audit | Non-Ministerial | — | — |
| 1965 | J. W. Adshead | Director of Audit | Non-Ministerial | — | — |

### Deterministic checks: `adshead_j-w_b1923` vs `Adshead, J. W___Gambia___1961`

- [PASS] surname_gate: bio 'ADSHEAD' vs stint 'Adshead, J. W' (exact)
- [PASS] initials: bio ['J', 'W'] ~ stint ['J', 'W']
- [PASS] age_gate: stint starts 1961, birth 1923 (age 38)
- [FAIL] colony: no placed event resolves to 'Gambia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1961-1965
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Adshead, J. W___St Helena___1955`

- Staff-list name: **Adshead, J. W** | colony: **St Helena** | listed 1955–1957 | editions [1955, 1956, 1957]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1955 | J. W. Adshead | Aide-de-Camp (Honorary) | Civil Establishment | — | — |
| 1956 | J. W. Adshead | Aide-de-Camp (Honorary) | Civil Establishment | — | — |
| 1957 | J. W. Adshead | Aide-de-Camp (Honorary) | CIVIL ESTABLISHMENT | — | — |

### Deterministic checks: `adshead_j-w_b1923` vs `Adshead, J. W___St Helena___1955`

- [PASS] surname_gate: bio 'ADSHEAD' vs stint 'Adshead, J. W' (exact)
- [PASS] initials: bio ['J', 'W'] ~ stint ['J', 'W']
- [PASS] age_gate: stint starts 1955, birth 1923 (age 32)
- [FAIL] colony: no placed event resolves to 'St Helena'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1955-1957
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

