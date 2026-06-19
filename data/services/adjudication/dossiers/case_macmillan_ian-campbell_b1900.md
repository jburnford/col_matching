<!-- {"case_id": "case_macmillan_ian-campbell_b1900", "bio_ids": ["macmillan_ian-campbell_b1900"], "stint_ids": ["Macmillan, I. C___Straits Settlements___1921", "Macmillan, I. C___Straits Settlements___1934"]} -->
# Dossier case_macmillan_ian-campbell_b1900

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 14 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `macmillan_ian-campbell_b1900`

- Printed name: **MACMILLAN, IAN CAMPBELL**
- Birth year: 1900 (attested in editions [1939])
- Appears in editions: [1939]

### Verbatim printed entry text (OCR)

**Version `col1939-L68840.v` — printed in editions [1939]:**

> MACMILLAN, IAN CAMPBELL.—B. 1900; ed. Glasgow High Schl.; pol. prob., S.S., June, 1919; attd. H.B.M. legn., Bangkok, Nov., 1919; asst. supt., pol., Aug., 1922; asst. commr., Kedah, Apr., 1924; ag. state vet. surg., Kedah, in addn., Mar., 1925; dep. commr., pol., F.M.S., Apr., 1935; commdt., S.S. pol. depot., S'pore, Oct., 1936.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1919 | pol. prob. | Straits Settlements | [1939] |
| 1 | 1922 | asst. supt., pol | Straits Settlements *(inherited from previous clause)* | [1939] |
| 2 | 1924 | asst. commr. | Kedah | [1939] |
| 3 | 1925 | ag. state vet. surg., Kedah, in addn | Kedah *(inherited from previous clause)* | [1939] |
| 4 | 1935 | dep. commr., pol. | Federated Malay States | [1939] |
| 5 | 1936 | commdt., S.S. pol. depot., S'pore | Federated Malay States *(inherited from previous clause)* | [1939] |

## Candidate stint `Macmillan, I. C___Straits Settlements___1921`

- Staff-list name: **Macmillan, I. C** | colony: **Straits Settlements** | listed 1921–1931 | editions [1921, 1922, 1923, 1925, 1931]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1921 | I. C. Macmillan | Probationers | Police | — | — |
| 1922 | I. C. Macmillan | Probationers | Police | — | — |
| 1923 | I. C. Macmillan | Assistant Superintendent | Police | — | — |
| 1925 | I. C. Macmillan | Assistant Superintendents | Police | — | — |
| 1931 | I. C. Macmillan | Head of Preventive Service | Government Monopolies Department Singapore | — | — |
| 1931 | I. C. Macmillan | Assistant Superintendent | Police | — | — |

### Deterministic checks: `macmillan_ian-campbell_b1900` vs `Macmillan, I. C___Straits Settlements___1921`

- [PASS] surname_gate: bio 'MACMILLAN' vs stint 'Macmillan, I. C' (exact)
- [PASS] initials: bio ['I', 'C'] ~ stint ['I', 'C']
- [PASS] age_gate: stint starts 1921, birth 1900 (age 21)
- [PASS] colony: 2 placed event(s) resolve to 'Straits Settlements'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1921-1931
- [FAIL] position_sim: best 49 vs bar 60: 'asst. supt., pol' ~ 'Assistant Superintendent'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Macmillan, I. C___Straits Settlements___1934`

- Staff-list name: **Macmillan, I. C** | colony: **Straits Settlements** | listed 1934–1939 | editions [1934, 1936, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | I. C. Macmillan | Assistant Superintendents | Police | — | — |
| 1936 | I. C. Macmillan | Assistant Superintendent | Police | — | — |
| 1939 | I. C. Macmillan | Superintendent | Police | — | — |

### Deterministic checks: `macmillan_ian-campbell_b1900` vs `Macmillan, I. C___Straits Settlements___1934`

- [PASS] surname_gate: bio 'MACMILLAN' vs stint 'Macmillan, I. C' (exact)
- [PASS] initials: bio ['I', 'C'] ~ stint ['I', 'C']
- [PASS] age_gate: stint starts 1934, birth 1900 (age 34)
- [PASS] colony: 2 placed event(s) resolve to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1934-1939
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

