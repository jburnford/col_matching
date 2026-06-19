<!-- {"case_id": "case_pollwell_edgar-nelson_b1875", "bio_ids": ["pollwell_edgar-nelson_b1875"], "stint_ids": ["Powell, E___Gold Coast___1914", "Powell, E___South Africa___1914"]} -->
# Dossier case_pollwell_edgar-nelson_b1875

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 39 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `pollwell_edgar-nelson_b1875`

- Printed name: **POLLWELL, Edgar Nelson**
- Birth year: 1875 (attested in editions [1923])
- Appears in editions: [1923, 1924, 1925]

### Verbatim printed entry text (OCR)

**Version `col1923-L54406.v` — printed in editions [1923]:**

> POLLWELL, Edgar Nelson.—B. 1875; storekeeper, marine dept., N. Nigeria, 11th Jan., 1911; on amalgamation of N. and S. Nigeria, apptd. asst. acctnt., 1914; paymr., lieut.-comdr., Nigerian Marine Contingent, 1915-18; acctnt., Nigeria, 1916; ag. ch. acctnt., 1919, 1921 and 1922; senr. acctnt., 1920.

**Version `col1924-L54297.v` — printed in editions [1924, 1925]:**

> FOLLWELL, EDGAR NELSON.—B. 1875; storekeeper, marine dept., N. Nigeria, 11th Jul., 1911; on amalgamation of N. and S. Nigeria appended, asst. acctnt., 1914; paymr., lieut.-comdr., Nigerian Marine Contingent, 1915-18; acctnt., Nigeria, 1916; ag. ch. acctnt., 1919, 1921 and 1922; senr. acctnt., 1920.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1911–1911 | storekeeper, marine dept. | Northern Nigeria | [1923, 1924, 1925] |
| 1 | 1914–1914 | asst. acctnt. | Nigeria | [1923, 1924, 1925] |
| 2 | 1915–1918 | paymr., lieut.-comdr. | Nigeria | [1923, 1924, 1925] |
| 3 | 1916–1916 | acctnt. | Nigeria | [1923, 1924, 1925] |
| 4 | 1919–1922 | ag. ch. acctnt. | — | [1923, 1924, 1925] |
| 5 | 1920–1920 | senr. acctnt. | — | [1923, 1924, 1925] |

## Candidate stint `Powell, E___Gold Coast___1914`

- Staff-list name: **Powell, E** | colony: **Gold Coast** | listed 1914–1915 | editions [1914, 1915]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1914 | E. Powell | Assistant Telegraph Engineer | Telegraph Engineering Branch | — | — |
| 1915 | E. Powell | Assistant Telegraph Engineer | Engineering Branch | — | — |

### Deterministic checks: `pollwell_edgar-nelson_b1875` vs `Powell, E___Gold Coast___1914`

- [PASS] surname_gate: bio 'POLLWELL' vs stint 'Powell, E' (fuzzy:2)
- [PASS] initials: bio ['E', 'N'] ~ stint ['E']
- [PASS] age_gate: stint starts 1914, birth 1875 (age 39)
- [FAIL] colony: no placed event resolves to 'Gold Coast'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1914-1915
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Powell, E___South Africa___1914`

- Staff-list name: **Powell, E** | colony: **South Africa** | listed 1914–1918 | editions [1914, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1914 | E. Powell | — | Tobacco Stations | — | — |
| 1914 | E. Powell | Senator | Senate | — | — |
| 1918 | E. Powell | Senator | Senate | — | — |

### Deterministic checks: `pollwell_edgar-nelson_b1875` vs `Powell, E___South Africa___1914`

- [PASS] surname_gate: bio 'POLLWELL' vs stint 'Powell, E' (fuzzy:2)
- [PASS] initials: bio ['E', 'N'] ~ stint ['E']
- [PASS] age_gate: stint starts 1914, birth 1875 (age 39)
- [FAIL] colony: no placed event resolves to 'South Africa'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1914-1918
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

