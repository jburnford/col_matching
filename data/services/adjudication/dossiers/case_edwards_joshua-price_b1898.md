<!-- {"case_id": "case_edwards_joshua-price_b1898", "bio_ids": ["edwards_joshua-price_b1898"], "stint_ids": ["Edwards, J. P. Purnell___Kenya___1928", "Edwards, J. P___Federation of Malaya___1951"]} -->
# Dossier case_edwards_joshua-price_b1898

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 122 official(s) with this surname in the graph's staff lists; 43 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `edwards_joshua-price_b1898`

- Printed name: **EDWARDS, JOSHUA PRICE**
- Birth year: 1898 (attested in editions [1939, 1940])
- Honours: C.B.E
- Appears in editions: [1939, 1940, 1953]

### Verbatim printed entry text (OCR)

**Version `col1939-L66362.v` — printed in editions [1939, 1940]:**

> EDWARDS, JOSHUA PRICE.—B. 1898; ed. Brasenose Coll., Oxford; B.A. (Oxon); asst. conserv., forests, F.M.S., Jan., 1924; ag. conserv., forests, Pahang, Sept., 1930; on sp. dutv in U.K., Sept., 1932; forest offr., S'pore, Nov., 1934; state forest officer, Selangor, Nov., 1936; conserv., forests, Malayan forest service, Sept., 1937; conserv., forests, Johore, Nov., 1937; state forest offr., Pahang, July, 1938.

**Version `col1953-L17221.v` — printed in editions [1953]:**

> EDWARDS, J. P., C.B.E.—b. 1898; ed. Ellesmere Coll. and Oxford Univ.; mil. serv., 1916–19; asst. consvr., forests, Mal., 1924; spec. duty in U.K., 1932; dep. consvr., 1933; consvr., 1937; dep. dir., 1947; ag. dir., 1949.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1924 | asst. conserv., forests | Federated Malay States | [1939, 1940, 1953] |
| 1 | 1930 | ag. conserv., forests, Pahang | Federated Malay States *(inherited from previous clause)* | [1939, 1940] |
| 2 | 1932 | on sp. dutv in U.K | Federated Malay States *(inherited from previous clause)* | [1939, 1940, 1953] |
| 3 | 1933 | dep. consvr | Malaya *(inherited from previous clause)* | [1953] |
| 4 | 1934 | forest offr., S'pore | Federated Malay States *(inherited from previous clause)* | [1939, 1940] |
| 5 | 1936 | state forest officer, Selangor | Federated Malay States *(inherited from previous clause)* | [1939, 1940] |
| 6 | 1937 | conserv., forests, Malayan forest service | Johore | [1939, 1940] |
| 7 | 1937 | consvr | Malaya *(inherited from previous clause)* | [1953] |
| 8 | 1938 | state forest offr., Pahang | Johore *(inherited from previous clause)* | [1939, 1940] |
| 9 | 1947 | dep. dir | Malaya *(inherited from previous clause)* | [1953] |
| 10 | 1949 | ag. dir | Malaya *(inherited from previous clause)* | [1953] |

## Candidate stint `Edwards, J. P. Purnell___Kenya___1928`

- Staff-list name: **Edwards, J. P. Purnell** | colony: **Kenya** | listed 1928–1932 | editions [1928, 1929, 1930, 1932]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1928 | J. P. Purnell Edwards | Engineers (Road Surveys) | Loan Staff | — | — |
| 1929 | J. P. Purnell Edwards | Assistant Engineers, Road Surveys | Loan Staff | — | — |
| 1930 | J. P. Purnell Edwards | Assistant Engineer | Loan Staff | — | — |
| 1932 | J. P. Purnell Edwards | Assistant Engineer (Road Surveys) | Loan Staff | — | — |

### Deterministic checks: `edwards_joshua-price_b1898` vs `Edwards, J. P. Purnell___Kenya___1928`

- [PASS] surname_gate: bio 'EDWARDS' vs stint 'Edwards, J. P. Purnell' (exact)
- [PASS] initials: bio ['J', 'P'] ~ stint ['J', 'P', 'P']
- [PASS] age_gate: stint starts 1928, birth 1898 (age 30)
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1928-1932
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Edwards, J. P___Federation of Malaya___1951`

- Staff-list name: **Edwards, J. P** | colony: **Federation of Malaya** | listed 1951–1952 | editions [1951, 1952]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1951 | J. P. Edwards | Director of Forestry | FORESTRY | — | — |
| 1952 | J. P. Edwards | Director of Forestry | Civil Establishment | — | — |

### Deterministic checks: `edwards_joshua-price_b1898` vs `Edwards, J. P___Federation of Malaya___1951`

- [PASS] surname_gate: bio 'EDWARDS' vs stint 'Edwards, J. P' (exact)
- [PASS] initials: bio ['J', 'P'] ~ stint ['J', 'P']
- [PASS] age_gate: stint starts 1951, birth 1898 (age 53)
- [PASS] colony: 6 placed event(s) resolve to 'Federation of Malaya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1951-1952
- [FAIL] position_sim: best 23 vs bar 60: 'ag. dir' ~ 'Director of Forestry'
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

