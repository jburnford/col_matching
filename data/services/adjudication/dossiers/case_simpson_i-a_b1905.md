<!-- {"case_id": "case_simpson_i-a_b1905", "bio_ids": ["simpson_i-a_b1905"], "stint_ids": ["Simpson, I. A___Straits Settlements___1931"]} -->
# Dossier case_simpson_i-a_b1905

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 73 official(s) with this surname in the graph's staff lists; 29 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `simpson_i-a_b1905`

- Printed name: **SIMPSON, I. A**
- Birth year: 1905 (attested in editions [1956, 1957])
- Appears in editions: [1956, 1957]

### Verbatim printed entry text (OCR)

**Version `col1956-L24128.v` — printed in editions [1956, 1957]:**

> SIMPSON, I. A.—b. 1905; ed. Brighton Coll. and L'pool Univ.; mil. serv., 1941-45; asst. chmst., inst. for med. research, Mal., 1927; chmst., 1929; senr. biochmst. and offr. i/c nutrition divn., 1951; specialist, gr. A, 1956; mem. U.K. del. to 1st mtg. of nutrition comtce. for S. & E. Asia, F.A.O., 1948; mem. F.A.O. inter. comtce. to study rice enrichment in the Philippines, 1952; hd. of U.K. del. to 3rd mtg. of nutrition comtce. for S. & E. Asia, F.A.O./W.H.O., 1953.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1927 | asst. chmst., inst. for med. research | Malaya | [1956, 1957] |
| 1 | 1929 | chmst | Malaya *(inherited from previous clause)* | [1956, 1957] |
| 2 | 1948 | mem. U.K. del. to 1st mtg. of nutrition comtce. for S. & E. Asia, F.A.O | Malaya *(inherited from previous clause)* | [1956, 1957] |
| 3 | 1951 | senr. biochmst. and offr. i/c nutrition divn | Malaya *(inherited from previous clause)* | [1956, 1957] |
| 4 | 1952 | mem. F.A.O. inter. comtce. to study rice enrichment in the Philippines | Malaya *(inherited from previous clause)* | [1956, 1957] |
| 5 | 1953 | hd. of U.K. del. to 3rd mtg. of nutrition comtce. for S. & E. Asia, F.A.O./W.H.O | Malaya *(inherited from previous clause)* | [1956, 1957] |
| 6 | 1956 | specialist, gr. A | Malaya *(inherited from previous clause)* | [1956, 1957] |

## Candidate stint `Simpson, I. A___Straits Settlements___1931`

- Staff-list name: **Simpson, I. A** | colony: **Straits Settlements** | listed 1931–1933 | editions [1931, 1932, 1933]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | I. A. Simpson | Chemist | Institute for Medical Research | — | — |
| 1931 | I. A. Simpson | Chemist | Public Works | — | — |
| 1932 | I. A. Simpson | Chemist | Institute for Medical Research | — | — |
| 1933 | I. A. Simpson | Chemist | Institute for Medical Research | — | — |

### Deterministic checks: `simpson_i-a_b1905` vs `Simpson, I. A___Straits Settlements___1931`

- [PASS] surname_gate: bio 'SIMPSON' vs stint 'Simpson, I. A' (exact)
- [PASS] initials: bio ['I', 'A'] ~ stint ['I', 'A']
- [PASS] age_gate: stint starts 1931, birth 1905 (age 26)
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1931-1933
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

