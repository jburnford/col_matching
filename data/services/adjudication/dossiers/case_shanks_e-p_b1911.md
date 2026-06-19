<!-- {"case_id": "case_shanks_e-p_b1911", "bio_ids": ["shanks_e-p_b1911"], "stint_ids": ["Shanks, E. P___Singapore___1949", "Shanks, E. P___Singapore___1958"]} -->
# Dossier case_shanks_e-p_b1911

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `shanks_e-p_b1911`

- Printed name: **SHANKS, E. P**
- Birth year: 1911 (attested in editions [1957, 1958, 1959, 1960, 1961])
- Appears in editions: [1957, 1958, 1959, 1960, 1961]

### Verbatim printed entry text (OCR)

**Version `col1957-L27092.v` — printed in editions [1957, 1958, 1959, 1960, 1961]:**

> SHANKS, E. P., Q.C.—b. 1911; ed. Mill Hill Sch., Weber's Sch. and Univ., Bonn, and Downing Coll., Camb.; barrister-at-law, Inner Temple; mil. serv., 1939-46 (desps.); dist. judge, Mal., 1946; 1st mag., S'pore, 1947; crown coun., 1950; senr. crown coun., 1955; solr.-gen., 1956; atty.-gen., 1957-59.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | dist. judge | Malaya | [1957, 1958, 1959, 1960, 1961] |
| 1 | 1947 | 1st mag., S'pore | Malaya *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961] |
| 2 | 1950 | crown coun | Malaya *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961] |
| 3 | 1955 | senr. crown coun | Malaya *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961] |
| 4 | 1956 | solr.-gen | Malaya *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961] |
| 5 | 1957–1959 | atty.-gen | Malaya *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961] |

## Candidate stint `Shanks, E. P___Singapore___1949`

- Staff-list name: **Shanks, E. P** | colony: **Singapore** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | E. P. Shanks | District Judges | Judicial | — | — |
| 1951 | E. P. Shanks | Crown-Counsel | Legal | — | — |

### Deterministic checks: `shanks_e-p_b1911` vs `Shanks, E. P___Singapore___1949`

- [PASS] surname_gate: bio 'SHANKS' vs stint 'Shanks, E. P' (exact)
- [PASS] initials: bio ['E', 'P'] ~ stint ['E', 'P']
- [PASS] age_gate: stint starts 1949, birth 1911 (age 38)
- [FAIL] colony: no placed event resolves to 'Singapore'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Shanks, E. P___Singapore___1958`

- Staff-list name: **Shanks, E. P** | colony: **Singapore** | listed 1958–1959 | editions [1958, 1959]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1958 | E. P. Shanks | Attorney-General | Civil Establishment | — | — |
| 1959 | E. P. Shanks | Attorney-General | Civil Establishment | — | — |

### Deterministic checks: `shanks_e-p_b1911` vs `Shanks, E. P___Singapore___1958`

- [PASS] surname_gate: bio 'SHANKS' vs stint 'Shanks, E. P' (exact)
- [PASS] initials: bio ['E', 'P'] ~ stint ['E', 'P']
- [PASS] age_gate: stint starts 1958, birth 1911 (age 47)
- [FAIL] colony: no placed event resolves to 'Singapore'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1958-1959
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

