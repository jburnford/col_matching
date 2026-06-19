<!-- {"case_id": "case_lewison_iavin-boych_b1884", "bio_ids": ["lewison_iavin-boych_b1884"], "stint_ids": ["Lewison, I. B___Zanzibar___1927", "Lewison, I___Kenya___1915"]} -->
# Dossier case_lewison_iavin-boych_b1884

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Lewison, I. B___Zanzibar___1927` is also gate-compatible with biography(ies) outside this case: ['lewison_irvine-boych_b1884'] (already linked elsewhere or filtered).
- NOTE: stint `Lewison, I___Kenya___1915` is also gate-compatible with biography(ies) outside this case: ['lewison_irvine-boych_b1884'] (already linked elsewhere or filtered).

## Biography `lewison_iavin-boych_b1884`

- Printed name: **LEWISON, IAVIN BOYCH**
- Birth year: 1884 (attested in editions [1932])
- Appears in editions: [1932]

### Verbatim printed entry text (OCR)

**Version `col1932-L61956.v` — printed in editions [1932]:**

> LEWISON, IAVIN BOYCH.—B. 1884; ed. Marlar Brothers Schl., Johannesburg; clk., survey dept., Kenya, 1911; survr., survey dept., Kenya, 1912; served in E.A.M.R. and 1/2nd K.A.R., Aug., 1914 to Dec., 1918; ast. survr., Zanzibar, 1922; ag. survr. for various periods, 1923-26 and 1928-30.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1911–1911 | clk., survey dept. | Kenya | [1932] |
| 1 | 1912–1912 | survr., survey dept. | Kenya | [1932] |
| 2 | 1914–1918 | served in E.A.M.R. and 1/2nd K.A.R. | — | [1932] |
| 3 | 1922–1922 | ast. survr. | Zanzibar | [1932] |
| 4 | 1923–1930 | ag. survr. | — | [1932] |

## Candidate stint `Lewison, I. B___Zanzibar___1927`

- Staff-list name: **Lewison, I. B** | colony: **Zanzibar** | listed 1927–1932 | editions [1927, 1928, 1929, 1930, 1931, 1932]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | I. B. Lewison | Assistant Surveyor | Public Works Department | — | — |
| 1928 | I. B. Lewison | Assistant Surveyor | Public Works Department | — | — |
| 1929 | I. B. Lewison | Assistant Surveyor | Public Works Department | — | — |
| 1930 | I. B. Lewison | Assistant Surveyor | Public Works Department | — | — |
| 1931 | I. B. Lewison | Assistant Surveyor | Public Works Department | — | — |
| 1932 | I. B. Lewison | Assistant Surveyor | Public Works Department | — | — |

### Deterministic checks: `lewison_iavin-boych_b1884` vs `Lewison, I. B___Zanzibar___1927`

- [PASS] surname_gate: bio 'LEWISON' vs stint 'Lewison, I. B' (exact)
- [PASS] initials: bio ['I', 'B'] ~ stint ['I', 'B']
- [PASS] age_gate: stint starts 1927, birth 1884 (age 43)
- [PASS] colony: 1 placed event(s) resolve to 'Zanzibar'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1927-1932
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Lewison, I___Kenya___1915`

- Staff-list name: **Lewison, I** | colony: **Kenya** | listed 1915–1922 | editions [1915, 1917, 1918, 1919, 1920, 1922]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1915 | I. Lewison | Junior Staff Surveyors | Cadastral Survey | — | — |
| 1917 | I. Lewison | Junior Staff Surveyors | Cadastral Survey | — | — |
| 1918 | I. Lewison | Junior Staff Surveyors | Cadastral Survey | — | — |
| 1919 | I. Lewison | Junior Staff Surveyors | Cadastral Survey | — | — |
| 1920 | I. Lewison | Junior Staff Surveyors | Land Survey Branch | — | — |
| 1922 | I. Lewison | Junior Staff Surveyor | Department of Lands | — | — |

### Deterministic checks: `lewison_iavin-boych_b1884` vs `Lewison, I___Kenya___1915`

- [PASS] surname_gate: bio 'LEWISON' vs stint 'Lewison, I' (exact)
- [PASS] initials: bio ['I', 'B'] ~ stint ['I']
- [PASS] age_gate: stint starts 1915, birth 1884 (age 31)
- [PASS] colony: 2 placed event(s) resolve to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1915-1922
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

