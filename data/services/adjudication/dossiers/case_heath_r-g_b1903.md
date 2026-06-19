<!-- {"case_id": "case_heath_r-g_b1903", "bio_ids": ["heath_r-g_b1903"], "stint_ids": ["Heath, C. R. G___Ceylon___1922"]} -->
# Dossier case_heath_r-g_b1903

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 38 official(s) with this surname in the graph's staff lists; 16 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `heath_r-g_b1903`

- Printed name: **HEATH, R. G**
- Birth year: 1903 (attested in editions [1953, 1954, 1955, 1956, 1957])
- Appears in editions: [1953, 1954, 1955, 1956, 1957]

### Verbatim printed entry text (OCR)

**Version `col1953-L17667.v` — printed in editions [1953, 1954, 1955, 1956, 1957]:**

> HEATH, R. G.—b. 1903; Brewwood Sch. and Reading Univ.; mil. serv., 1941-45; agric. offr., F.M.S., 1927; senr., 1946; ch. field offr., 1948; dep. dir., agric., 1952; dir., Fed. of Mal., 1955.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1927 | agric. offr. | Federated Malay States | [1953, 1954, 1955, 1956, 1957] |
| 1 | 1946 | senr | Federated Malay States *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957] |
| 2 | 1948 | ch. field offr | Federated Malay States *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957] |
| 3 | 1952 | dep. dir., agric | Federated Malay States *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957] |
| 4 | 1955 | dir., Fed. of Mal | Federated Malay States *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957] |

## Candidate stint `Heath, C. R. G___Ceylon___1922`

- Staff-list name: **Heath, C. R. G** | colony: **Ceylon** | listed 1922–1923 | editions [1922, 1923]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | C. R. G. Heath | Junior Assistant Superintendent of Surveys | Survey Department | — | — |
| 1923 | C. R. G. Heath | Junior Assistant Superintendent of Surveys | Survey Department | — | — |

### Deterministic checks: `heath_r-g_b1903` vs `Heath, C. R. G___Ceylon___1922`

- [PASS] surname_gate: bio 'HEATH' vs stint 'Heath, C. R. G' (exact)
- [PASS] initials: bio ['R', 'G'] ~ stint ['C', 'R', 'G']
- [PASS] age_gate: stint starts 1922, birth 1903 (age 19)
- [FAIL] colony: no placed event resolves to 'Ceylon'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1922-1923
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

