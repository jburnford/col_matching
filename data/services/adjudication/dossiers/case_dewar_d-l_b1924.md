<!-- {"case_id": "case_dewar_d-l_b1924", "bio_ids": ["dewar_d-l_b1924", "dewar_l_b1916"], "stint_ids": ["Dewar, L___British Guiana___1964", "Dewar, Miss L___British Guiana___1963"]} -->
# Dossier case_dewar_d-l_b1924

## Case context

- 2 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 16 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['dewar_l_b1916'] carry a single initial only — the namesake trap applies.
- CONTESTED: stint(s) ['Dewar, L___British Guiana___1964'] have more than one claimant biography in this case.

## Biography `dewar_d-l_b1924`

- Printed name: **DEWAR, D. L**
- Birth year: 1924 (attested in editions [1966])
- Appears in editions: [1966]

### Verbatim printed entry text (OCR)

**Version `col1966-L14296.v` — printed in editions [1966]:**

> DEWAR, Miss D. L.—b. 1924; ed. St. Kitts High Sch., Montserrat Sec. Sch., Whittington Hosp., Paddington Hosp. and Royal Coll. of Nursing, London; asst. matron, Antigua, 1958; ag. matron, Montserrat; matron, Glendon Hosp., 1961.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1958 | asst. matron | Antigua | [1966] |
| 1 | 1961 | matron, Glendon Hosp | Antigua *(inherited from previous clause)* | [1966] |

## Biography `dewar_l_b1916`

- Printed name: **DEWAR, L**
- Birth year: 1916 (attested in editions [1963, 1964, 1965, 1966])
- Appears in editions: [1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1963-L19045.v` — printed in editions [1963, 1964, 1965, 1966]:**

> DEWAR, Miss L.—b. 1916; ed. Bishop's H. Sch., B.G. and Bedford Coll., London Univ.; asst. mistress, Bishop's H. Sch., B.G., 1943; dep. hd. mistress, 1952; hd. mistress, 1962.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1943 | asst. mistress, Bishop's H. Sch. | British Guiana | [1963, 1964, 1965, 1966] |
| 1 | 1952 | dep. hd. mistress | British Guiana *(inherited from previous clause)* | [1963, 1964, 1965, 1966] |
| 2 | 1962 | hd. mistress | British Guiana *(inherited from previous clause)* | [1963, 1964, 1965, 1966] |

## Candidate stint `Dewar, L___British Guiana___1964`

- Staff-list name: **Dewar, L** | colony: **British Guiana** | listed 1964–1966 | editions [1964, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1964 | Miss L. Dewar | Headmistress, Bishops' High School | Civil Establishment | — | — |
| 1966 | Miss L. Dewar | Headmistress, Bishops' High School | Civil Establishment | — | — |

### Deterministic checks: `dewar_d-l_b1924` vs `Dewar, L___British Guiana___1964`

- [PASS] surname_gate: bio 'DEWAR' vs stint 'Dewar, L' (exact)
- [PASS] initials: bio ['D', 'L'] ~ stint ['L']
- [PASS] age_gate: stint starts 1964, birth 1924 (age 40)
- [FAIL] colony: no placed event resolves to 'British Guiana'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1964-1966
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `dewar_l_b1916` vs `Dewar, L___British Guiana___1964`

- [PASS] surname_gate: bio 'DEWAR' vs stint 'Dewar, L' (exact)
- [PASS] initials: bio ['L'] ~ stint ['L']
- [PASS] age_gate: stint starts 1964, birth 1916 (age 48)
- [PASS] colony: 3 placed event(s) resolve to 'British Guiana'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1964-1966
- [FAIL] position_sim: best 47 vs bar 60: 'hd. mistress' ~ 'Headmistress, Bishops' High School'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

## Candidate stint `Dewar, Miss L___British Guiana___1963`

- Staff-list name: **Dewar, Miss L** | colony: **British Guiana** | listed 1963–1965 | editions [1963, 1965]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1963 | Miss L. Dewar | Headmistress, Bishops' High School | Civil Establishment | — | — |
| 1965 | Miss L. Dewar | Headmistress, Bishops' High School | Civil Establishment | — | — |

### Deterministic checks: `dewar_l_b1916` vs `Dewar, Miss L___British Guiana___1963`

- [PASS] surname_gate: bio 'DEWAR' vs stint 'Dewar, Miss L' (exact)
- [PASS] initials: bio ['L'] ~ stint ['M', 'L']
- [PASS] age_gate: stint starts 1963, birth 1916 (age 47)
- [PASS] colony: 3 placed event(s) resolve to 'British Guiana'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1963-1965
- [FAIL] position_sim: best 51 vs bar 60: 'dep. hd. mistress' ~ 'Headmistress, Bishops' High School'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

