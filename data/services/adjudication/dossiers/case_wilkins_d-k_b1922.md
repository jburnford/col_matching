<!-- {"case_id": "case_wilkins_d-k_b1922", "bio_ids": ["wilkins_d-k_b1922"], "stint_ids": ["Wilkins, D. K___Western Pacific___1958"]} -->
# Dossier case_wilkins_d-k_b1922

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 12 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `wilkins_d-k_b1922`

- Printed name: **WILKINS, D. K**
- Birth year: 1922 (attested in editions [1963, 1964, 1965, 1966])
- Appears in editions: [1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1963-L26332.v` — printed in editions [1963, 1964, 1965, 1966]:**

> WILKINS, D. K.—b. 1922; ed. The Scots Coll., Sydney and Sydney Univ.; mil. serv., 1941-56, R.N.R., lt.; cadet, Tang., 1952; dist. offr., 1954; secon. admin. offr., N. Hebs., 1957.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1952 | cadet | Tanganyika | [1963, 1964, 1965, 1966] |
| 1 | 1954 | dist. offr | Tanganyika *(inherited from previous clause)* | [1963, 1964, 1965, 1966] |
| 2 | 1957 | secon. admin. offr., N. Hebs | Tanganyika *(inherited from previous clause)* | [1963, 1964, 1965, 1966] |

## Candidate stint `Wilkins, D. K___Western Pacific___1958`

- Staff-list name: **Wilkins, D. K** | colony: **Western Pacific** | listed 1958–1966 | editions [1958, 1959, 1960, 1961, 1962, 1964, 1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1958 | D. K. Wilkins | Administration Officer | British National Administration | — | — |
| 1959 | D. K. Wilkins | Administrative Officer, Class B | British National Administration | — | — |
| 1960 | D. K. Wilkins | Administrative Officer, Class B | British National Administration | — | — |
| 1961 | D. K. Wilkins | Administrative Officer, Class B | British National Administration | — | — |
| 1962 | D. K. Wilkins | Administrative Officer, Class B | British National Administration | — | — |
| 1964 | D. K. Wilkins | Administrative Officer, Class B | British National Administration | — | — |
| 1965 | D. K. Wilkins | Administrative Officer, Class B | British National Administration | — | — |
| 1966 | D. K. Wilkins | Administrative Officer, Class B | British National Administration | — | — |

### Deterministic checks: `wilkins_d-k_b1922` vs `Wilkins, D. K___Western Pacific___1958`

- [PASS] surname_gate: bio 'WILKINS' vs stint 'Wilkins, D. K' (exact)
- [PASS] initials: bio ['D', 'K'] ~ stint ['D', 'K']
- [PASS] age_gate: stint starts 1958, birth 1922 (age 36)
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

