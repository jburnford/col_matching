<!-- {"case_id": "case_clohete_montebose-claverhouse_b1880", "bio_ids": ["clohete_montebose-claverhouse_b1880", "clokte_montrose-claverhouse_b1880"], "stint_ids": ["Cloete___South Africa___1912"]} -->
# Dossier case_clohete_montebose-claverhouse_b1880

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 14 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Cloete___South Africa___1912'] have more than one claimant biography in this case.
- NOTE: stint `Cloete___South Africa___1912` is also gate-compatible with biography(ies) outside this case: ['cloete_sebastian-valentyn_e1853'] (already linked elsewhere or filtered).
- NOTE: stint `Cloete___South Africa___1912` is also gate-compatible with biography(ies) outside this case: ['cloete_sebastian-valentyn_e1853'] (already linked elsewhere or filtered).

## Biography `clohete_montebose-claverhouse_b1880`

- Printed name: **CLOHETE, MONTEBOSE CLAVERHOUSE**
- Birth year: 1880 (attested in editions [1935])
- Appears in editions: [1935]

### Verbatim printed entry text (OCR)

**Version `dol1935-L57642.v` — printed in editions [1935]:**

> CLOHETE, MONTEBOSE CLAVERHOUSE.—B. 1880; master's office, Cape, 1899; Pretoria, 1902; asst. regtr. high ct., Jo'burg, 1903; asst. regtr., Cape prov. divn., 1921; regtr., appellate divn., 1923.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1899 | master's office | Cape of Good Hope | [1935] |
| 1 | 1902 | Pretoria | Cape of Good Hope *(inherited from previous clause)* | [1935] |
| 2 | 1903 | asst. regtr. high ct., Jo'burg | Cape of Good Hope *(inherited from previous clause)* | [1935] |
| 3 | 1921 | asst. regtr., Cape prov. divn | Cape of Good Hope | [1935] |
| 4 | 1923 | regtr., appellate divn | Cape of Good Hope *(inherited from previous clause)* | [1935] |

## Biography `clokte_montrose-claverhouse_b1880`

- Printed name: **CLOKTE, Montrose Claverhouse**
- Birth year: 1880 (attested in editions [1934])
- Appears in editions: [1934]

### Verbatim printed entry text (OCR)

**Version `col1934-L57680.v` — printed in editions [1934]:**

> CLOKTE, Montrose Claverhouse.—B. 1880; master's office, Cape, 1899; Pretoria, 1902; asst. regtr., high ct., Jo'burg., 1903; asst. regtr., Cape prov. divn., 1921; regtr., appellate divn., 1923.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1899 | master's office | Cape of Good Hope | [1934] |
| 1 | 1902 | Pretoria | Cape of Good Hope *(inherited from previous clause)* | [1934] |
| 2 | 1903 | asst. regtr., high ct., Jo'burg | Cape of Good Hope *(inherited from previous clause)* | [1934] |
| 3 | 1921 | asst. regtr., Cape prov. divn | Cape of Good Hope | [1934] |
| 4 | 1923 | regtr., appellate divn | Cape of Good Hope *(inherited from previous clause)* | [1934] |

## Candidate stint `Cloete___South Africa___1912`

- Staff-list name: **Cloete** | colony: **South Africa** | listed 1912–1918 | editions [1912, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | Colonel Cloete | Colonel | — | — | Colonel |
| 1918 | Colonel Cloete | Colonel | — | — | Colonel |

### Deterministic checks: `clohete_montebose-claverhouse_b1880` vs `Cloete___South Africa___1912`

- [PASS] surname_gate: bio 'CLOHETE' vs stint 'Cloete' (fuzzy:1)
- [PASS] initials: bio ['M', 'C'] ~ stint ['?']
- [PASS] age_gate: stint starts 1912, birth 1880 (age 32)
- [FAIL] colony: no placed event resolves to 'South Africa'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1918
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `clokte_montrose-claverhouse_b1880` vs `Cloete___South Africa___1912`

- [PASS] surname_gate: bio 'CLOKTE' vs stint 'Cloete' (fuzzy:1)
- [PASS] initials: bio ['M', 'C'] ~ stint ['?']
- [PASS] age_gate: stint starts 1912, birth 1880 (age 32)
- [FAIL] colony: no placed event resolves to 'South Africa'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1918
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

