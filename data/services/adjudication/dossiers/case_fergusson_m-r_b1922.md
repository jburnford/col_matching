<!-- {"case_id": "case_fergusson_m-r_b1922", "bio_ids": ["fergusson_m-r_b1922"], "stint_ids": ["Fergusson, R___Barbados___1964"]} -->
# Dossier case_fergusson_m-r_b1922

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `fergusson_m-r_b1922`

- Printed name: **FERGUSSON, M. R**
- Birth year: 1922 (attested in editions [1961, 1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1961-L21980.v` — printed in editions [1961, 1962, 1963, 1964, 1965, 1966]:**

> FERGUSSON, M. R.—b. 1922; ed. Fettes Coll., Edin., and Rhodes Univ., S.A.; mil. serv., 1941-45; cadet, Som., 1949; dist. offr., 1951; Br. liaison offr., Ethiopia, 1959; dist. offr., N. Rhod., 1960. (Zambia Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1949 | cadet | Somaliland | [1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1951 | dist. offr | Somaliland *(inherited from previous clause)* | [1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1959 | Br. liaison offr., Ethiopia | Somaliland *(inherited from previous clause)* | [1961, 1962, 1963, 1964, 1965, 1966] |
| 3 | 1960 | dist. offr. | Northern Rhodesia | [1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Fergusson, R___Barbados___1964`

- Staff-list name: **Fergusson, R** | colony: **Barbados** | listed 1964–1965 | editions [1964, 1965]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1964 | R. Fergusson | Aide-de-Camp | Civil Establishment | — | — |
| 1965 | R. Fergusson | Aide-de-Camp | Civil Establishment | — | — |

### Deterministic checks: `fergusson_m-r_b1922` vs `Fergusson, R___Barbados___1964`

- [PASS] surname_gate: bio 'FERGUSSON' vs stint 'Fergusson, R' (exact)
- [PASS] initials: bio ['M', 'R'] ~ stint ['R']
- [PASS] age_gate: stint starts 1964, birth 1922 (age 42)
- [FAIL] colony: no placed event resolves to 'Barbados'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1964-1965
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

