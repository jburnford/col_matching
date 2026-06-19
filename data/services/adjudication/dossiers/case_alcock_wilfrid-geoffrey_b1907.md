<!-- {"case_id": "case_alcock_wilfrid-geoffrey_b1907", "bio_ids": ["alcock_wilfrid-geoffrey_b1907"], "stint_ids": ["Alcock, G___Kenya___1932", "Alcock, W. G___Singapore___1953"]} -->
# Dossier case_alcock_wilfrid-geoffrey_b1907

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `alcock_wilfrid-geoffrey_b1907`

- Printed name: **ALCOCK, Wilfrid Geoffrey**
- Birth year: 1907 (attested in editions [1950, 1951])
- Honours: M.A
- Appears in editions: [1950, 1951, 1953, 1954, 1955, 1956, 1957]

### Verbatim printed entry text (OCR)

**Version `col1950-L33131.v` — printed in editions [1950, 1951]:**

> ALCOCK, Wilfrid Geoffrey, M.A., LL.B.—b. 1907; ed. Oxford Prep. Sch., Glasgow Acad., and Glasgow Univ., solr. (Scotland); asst. lands offr., T.T., 1935; lands offr. and registr.-gen., Nyasa, 1939; official assignee, S'pore, 1948.

**Version `col1953-L16322.v` — printed in editions [1953, 1954, 1955, 1956, 1957]:**

> ALCOCK, W. G.—b. 1907 ; ed. Oxford Prep. Sch., Glasgow Acad. and Glasgow Univ.; solr. (Scotland); asst. lands offr., Tang., 1935 ; lands offr. and registr.-gen., Nyasa., 1939 ; official assignee, S'pore, 1948 ; comsnr. of estate duties and stamps in addition.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1935 | asst. lands offr., T.T | Tanganyika | [1950, 1951, 1953, 1954, 1955, 1956, 1957] |
| 1 | 1939 | lands offr. and registr.-gen. | Nyasaland | [1950, 1951, 1953, 1954, 1955, 1956, 1957] |
| 2 | 1948 | official assignee, S'pore | Nyasaland *(inherited from previous clause)* | [1950, 1951, 1953, 1954, 1955, 1956, 1957] |

## Candidate stint `Alcock, G___Kenya___1932`

- Staff-list name: **Alcock, G** | colony: **Kenya** | listed 1932–1934 | editions [1932, 1934]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1932 | G. Alcock | Stock Inspector | Veterinary | — | — |
| 1934 | G. Alcock | Stock Inspectors | Veterinary | — | — |

### Deterministic checks: `alcock_wilfrid-geoffrey_b1907` vs `Alcock, G___Kenya___1932`

- [PASS] surname_gate: bio 'ALCOCK' vs stint 'Alcock, G' (exact)
- [PASS] initials: bio ['W', 'G'] ~ stint ['G']
- [PASS] age_gate: stint starts 1932, birth 1907 (age 25)
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1932-1934
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Alcock, W. G___Singapore___1953`

- Staff-list name: **Alcock, W. G** | colony: **Singapore** | listed 1953–1957 | editions [1953, 1954, 1955, 1956, 1957]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1953 | W. G. Alcock | Commissioner of Estate Duties and Stamps | Civil Establishment | — | — |
| 1954 | W. G. Alcock | Commissioner of Estate Duties and Stamps (officiating) | Civil Establishment | — | — |
| 1955 | W. G. Alcock | Official Assignee (including duties as Public Trustee, Custodian of Property and Commissioner of Estate Duties and Stamps) | Civil Establishment | — | — |
| 1956 | W. G. Alcock | Official Assignee (including duties as Public Trustee, Custodian of Property and Commissioner of Estate Duties) | Civil Establishment | — | — |
| 1957 | W. G. Alcock | Official Assignee (including duties as Public Trustee, Custodian of Property and Commissioner of Estate Duties) | Civil Establishment | — | — |

### Deterministic checks: `alcock_wilfrid-geoffrey_b1907` vs `Alcock, W. G___Singapore___1953`

- [PASS] surname_gate: bio 'ALCOCK' vs stint 'Alcock, W. G' (exact)
- [PASS] initials: bio ['W', 'G'] ~ stint ['W', 'G']
- [PASS] age_gate: stint starts 1953, birth 1907 (age 46)
- [FAIL] colony: no placed event resolves to 'Singapore'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1953-1957
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

