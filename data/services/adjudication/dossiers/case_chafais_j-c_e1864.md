<!-- {"case_id": "case_chafais_j-c_e1864", "bio_ids": ["chafais_j-c_e1864", "chapai_j-c_e1864"], "stint_ids": ["Chapais, Jean C___Canada___1877"]} -->
# Dossier case_chafais_j-c_e1864

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Chapais, Jean C___Canada___1877'] have more than one claimant biography in this case.

## Biography `chafais_j-c_e1864`

- Printed name: **CHAFAIS, J. C**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L26802.v` — printed in editions [1883]:**

> CHAFAIS, HON. J. C.—Commissioner of public works, Canada, 30th March, 1864; minister of agriculture, 1st July, 1867; receiver-general, 16th November, 1870; retired from government, January, 1873; called to the senate, 1868.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1864 | Commissioner of public works | Canada | [1883] |
| 1 | 1867 | minister of agriculture | Canada *(inherited from previous clause)* | [1883] |
| 2 | 1868 | called to the senate | Canada *(inherited from previous clause)* | [1883] |
| 3 | 1870 | receiver-general | Canada *(inherited from previous clause)* | [1883] |
| 4 | 1873 | retired from government | Canada *(inherited from previous clause)* | [1883] |

## Biography `chapai_j-c_e1864`

- Printed name: **CHAPAI, J. C**
- Birth year: not printed
- Appears in editions: [1886]

### Verbatim printed entry text (OCR)

**Version `col1886-L32634.v` — printed in editions [1886]:**

> CHAPAI, HON. J. C.—Commissioner of public works, Canada, 30th March, 1864; minister of agriculture, 1st July, 1867; receiver-general, 16th November, 1870; retired from government, January, 1873; called to the senate, 1868.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1864 | Commissioner of public works | Canada | [1886] |
| 1 | 1867 | minister of agriculture | Canada *(inherited from previous clause)* | [1886] |
| 2 | 1868 | called to the senate | Canada *(inherited from previous clause)* | [1886] |
| 3 | 1870 | receiver-general | Canada *(inherited from previous clause)* | [1886] |
| 4 | 1873 | retired from government | Canada *(inherited from previous clause)* | [1886] |

## Candidate stint `Chapais, Jean C___Canada___1877`

- Staff-list name: **Chapais, Jean C** | colony: **Canada** | listed 1877–1883 | editions [1877, 1878, 1879, 1880, 1883]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | Jean C. Chapais | Senator, M.P. | Civil Establishment | — | — |
| 1877 | J. C. Chapais | Senator | Senate of Canada | — | — |
| 1878 | J. C. Chapais | Senator | Senate of Canada | — | — |
| 1878 | Jean C. Chapais | Senator, M.P. | Civil Establishment | — | — |
| 1879 | J. C. Chapais | Senator | Senate of Canada | — | — |
| 1880 | J. C. Chapais | Senator | Senators | — | — |
| 1880 | Jean C. Chapais | Senator | Privy Council | — | — |
| 1883 | J. C. Chapais | Senator | Senators | — | — |
| 1883 | Jean C. Chapais | Senator | THE QUEEN'S PRIVY COUNCIL FOR CANADA | — | — |

### Deterministic checks: `chafais_j-c_e1864` vs `Chapais, Jean C___Canada___1877`

- [PASS] surname_gate: bio 'CHAFAIS' vs stint 'Chapais, Jean C' (fuzzy:1)
- [PASS] initials: bio ['J', 'C'] ~ stint ['J', 'C']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 5 placed event(s) resolve to 'Canada'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1883
- [FAIL] position_sim: best 36 vs bar 60: 'retired from government' ~ 'Senator, M.P.'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

### Deterministic checks: `chapai_j-c_e1864` vs `Chapais, Jean C___Canada___1877`

- [PASS] surname_gate: bio 'CHAPAI' vs stint 'Chapais, Jean C' (fuzzy:1)
- [PASS] initials: bio ['J', 'C'] ~ stint ['J', 'C']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 5 placed event(s) resolve to 'Canada'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1883
- [FAIL] position_sim: best 36 vs bar 60: 'retired from government' ~ 'Senator, M.P.'
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

