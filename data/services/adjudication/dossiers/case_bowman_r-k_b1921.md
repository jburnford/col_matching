<!-- {"case_id": "case_bowman_r-k_b1921", "bio_ids": ["bowman_r-k_b1921"], "stint_ids": ["Bowman, R. K___Western Pacific___1958"]} -->
# Dossier case_bowman_r-k_b1921

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 12 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `bowman_r-k_b1921`

- Printed name: **BOWMAN, R. K**
- Birth year: 1921 (attested in editions [1965, 1966])
- Appears in editions: [1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1965-L13747.v` — printed in editions [1965, 1966]:**

> BOWMAN, R. K.—b. 1921; ed. Chesterfield Sch., Univ. of Sheffield and L.S.H.T.M.; med. offr., S. Pac. health serv., 1953; ch. med. offr., Tonga, 1954; British med. offr. N. Heb., 1957; ch. med. offr., G & E.I.C., 1960.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1953 | med. offr., S. Pac. health serv | — | [1965, 1966] |
| 1 | 1954 | ch. med. offr. | Tonga | [1965, 1966] |
| 2 | 1957 | British med. offr. N. Heb | Tonga *(inherited from previous clause)* | [1965, 1966] |
| 3 | 1960 | ch. med. offr., G & E.I.C | Tonga *(inherited from previous clause)* | [1965, 1966] |

## Candidate stint `Bowman, R. K___Western Pacific___1958`

- Staff-list name: **Bowman, R. K** | colony: **Western Pacific** | listed 1958–1966 | editions [1958, 1959, 1961, 1962, 1964, 1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1958 | R. K. Bowman | Medical Officer | British National Administration | — | — |
| 1959 | R. K. Bowman | Medical Officer | British National Administration | — | — |
| 1961 | R. K. Bowman | Senior Medical Officer | Civil Establishment | — | — |
| 1962 | R. K. Bowman | Senior Medical Officer | Civil Establishment | — | — |
| 1964 | R. K. Bowman | Chief Medical Officer | Civil Establishment | — | — |
| 1965 | R. K. Bowman | Chief Medical Officer | Civil Establishment | — | — |
| 1966 | R. K. Bowman | Chief Medical Officer | Civil Establishment | — | — |

### Deterministic checks: `bowman_r-k_b1921` vs `Bowman, R. K___Western Pacific___1958`

- [PASS] surname_gate: bio 'BOWMAN' vs stint 'Bowman, R. K' (exact)
- [PASS] initials: bio ['R', 'K'] ~ stint ['R', 'K']
- [PASS] age_gate: stint starts 1958, birth 1921 (age 37)
- [FAIL] colony: no placed event resolves to 'Western Pacific'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1958-1966
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

