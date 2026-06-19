<!-- {"case_id": "case_sewell_frank-blackwood_b1883", "bio_ids": ["sewell_frank-blackwood_b1883"], "stint_ids": ["Sewell, F B___Straits Settlements___1915", "Sewell, F B___Straits Settlements___1931"]} -->
# Dossier case_sewell_frank-blackwood_b1883

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 11 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `sewell_frank-blackwood_b1883`

- Printed name: **SEWELL, FRANK BLACKWOOD**
- Birth year: 1883 (attested in editions [1932])
- Appears in editions: [1932]

### Verbatim printed entry text (OCR)

**Version `col1932-L63852.v` — printed in editions [1932]:**

> SEWELL, FRANK BLACKWOOD.—B. 1883; lic. surv., New Zealand, Mar., 1905; surv., rev. survey dept., Perak, Oct., 1906; supernumy. asst. supt., F.M.S., Jan., 1912; asst. supt., surveys, Kedah, Dec., 1912; ditto, F.M.S., May, 1921; supt., Jly., 1923; sr. supt., surveys, Singapore, Jan., 1927; mem. of comttee, to inquire into survey procedure in Singapore, Jan., 1928.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1905 | lic. surv. | New Zealand | [1932] |
| 1 | 1906 | surv., rev. survey dept., Perak | New Zealand *(inherited from previous clause)* | [1932] |
| 2 | 1912 | supernumy. asst. supt. | Federated Malay States | [1932] |
| 3 | 1921 | asst. supt., surveys | Federated Malay States | [1932] |
| 4 | 1923 | supt., Jly | Federated Malay States *(inherited from previous clause)* | [1932] |
| 5 | 1927 | sr. supt., surveys | Singapore | [1932] |
| 6 | 1928 | mem. of comttee, to inquire into survey procedure in Singapore | Singapore *(inherited from previous clause)* | [1932] |

## Candidate stint `Sewell, F B___Straits Settlements___1915`

- Staff-list name: **Sewell, F B** | colony: **Straits Settlements** | listed 1915–1917 | editions [1915, 1917]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1915 | F. B. Sewell | Assistant Superintendent | Surveys | — | — |
| 1917 | F. B. Sewell | Assistant Superintendent | Surveys | — | — |

### Deterministic checks: `sewell_frank-blackwood_b1883` vs `Sewell, F B___Straits Settlements___1915`

- [PASS] surname_gate: bio 'SEWELL' vs stint 'Sewell, F B' (exact)
- [PASS] initials: bio ['F', 'B'] ~ stint ['F', 'B']
- [PASS] age_gate: stint starts 1915, birth 1883 (age 32)
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1915-1917
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Sewell, F B___Straits Settlements___1931`

- Staff-list name: **Sewell, F B** | colony: **Straits Settlements** | listed 1931–1932 | editions [1931, 1932]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | F B Sewell | Senior Superintendent Singapore | SURVEYS | — | — |
| 1931 | F. B. Sewell | Senior Superintendent of Surveys | Survey Office | — | — |
| 1932 | F. B. Sewell | Senior Superintendent, Singapore | Surveys | — | — |

### Deterministic checks: `sewell_frank-blackwood_b1883` vs `Sewell, F B___Straits Settlements___1931`

- [PASS] surname_gate: bio 'SEWELL' vs stint 'Sewell, F B' (exact)
- [PASS] initials: bio ['F', 'B'] ~ stint ['F', 'B']
- [PASS] age_gate: stint starts 1931, birth 1883 (age 48)
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1931-1932
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

