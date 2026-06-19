<!-- {"case_id": "case_piegrome_joseph-charles_b1896", "bio_ids": ["piegrome_joseph-charles_b1896"], "stint_ids": ["Piegrome, J. C___Cyprus___1957", "Piegrome, J. C___Gold Coast___1924"]} -->
# Dossier case_piegrome_joseph-charles_b1896

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `piegrome_joseph-charles_b1896`

- Printed name: **PIEGROME, JOSEPH CHARLES**
- Birth year: 1896 (attested in editions [1937, 1939])
- Appears in editions: [1937, 1939]

### Verbatim printed entry text (OCR)

**Version `col1937-L63901.v` — printed in editions [1937, 1939]:**

> PIEGROME, JOSEPH CHARLES, M.C.—B. 1896; lieut., Northumberland Fusiliers, 1915; France, 1916-18; wounded, 1916; asst. commr., pol., Gold Coast, Sept., 1921; commr., 1927; title changed to supr., 1937; ag. dep. commr., Apr.-Sept., 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1915 | lieut., Northumberland Fusiliers | — | [1937, 1939] |
| 1 | 1916–1918 | France | — | [1937, 1939] |
| 2 | 1916 | wounded | — | [1937, 1939] |
| 3 | 1921 | asst. commr., pol. | Gold Coast | [1937, 1939] |
| 4 | 1927 | commr | Gold Coast *(inherited from previous clause)* | [1937, 1939] |
| 5 | 1937 | title changed to supr | Gold Coast *(inherited from previous clause)* | [1937, 1939] |
| 6 | 1938 | ag. dep. commr., Apr.- | Gold Coast *(inherited from previous clause)* | [1937, 1939] |

## Candidate stint `Piegrome, J. C___Cyprus___1957`

- Staff-list name: **Piegrome, J. C** | colony: **Cyprus** | listed 1957–1958 | editions [1957, 1958]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1957 | J. C. Piegrome | Director of Detention Camps | Civil Establishment | — | — |
| 1958 | J. C. Piegrome | Director of Detention Camps | Civil Establishment | — | — |

### Deterministic checks: `piegrome_joseph-charles_b1896` vs `Piegrome, J. C___Cyprus___1957`

- [PASS] surname_gate: bio 'PIEGROME' vs stint 'Piegrome, J. C' (exact)
- [PASS] initials: bio ['J', 'C'] ~ stint ['J', 'C']
- [PASS] age_gate: stint starts 1957, birth 1896 (age 61)
- [FAIL] colony: no placed event resolves to 'Cyprus'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1957-1958
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Piegrome, J. C___Gold Coast___1924`

- Staff-list name: **Piegrome, J. C** | colony: **Gold Coast** | listed 1924–1928 | editions [1924, 1927, 1928]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1924 | J. C. Piegrome | Commissioner and Assistant Commissioner of Police | Depot Staff | — | — |
| 1927 | J. C. Piegrome | Commissioner/Assistant Commissioner of Police | Police Department | — | — |
| 1928 | J. C. Piegrome | Commissioners and Assistant Commissioners of Police | Police Department | — | — |

### Deterministic checks: `piegrome_joseph-charles_b1896` vs `Piegrome, J. C___Gold Coast___1924`

- [PASS] surname_gate: bio 'PIEGROME' vs stint 'Piegrome, J. C' (exact)
- [PASS] initials: bio ['J', 'C'] ~ stint ['J', 'C']
- [PASS] age_gate: stint starts 1924, birth 1896 (age 28)
- [PASS] colony: 4 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1924-1928
- [FAIL] position_sim: best 56 vs bar 60: 'asst. commr., pol.' ~ 'Commissioner and Assistant Commissioner of Police'
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

