<!-- {"case_id": "case_howard_j-j_b1922", "bio_ids": ["howard_j-j_b1922"], "stint_ids": ["Howard, J. J___Sarawak___1949"]} -->
# Dossier case_howard_j-j_b1922

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 34 official(s) with this surname in the graph's staff lists; 20 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `howard_j-j_b1922`

- Printed name: **HOWARD, J. J**
- Birth year: 1922 (attested in editions [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1959-L24325.v` — printed in editions [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> HOWARD, J. J.—b. 1922; ed. Mungret Coll., Limerick, and Univ. Coll., Dublin; asst. exec. engrn., P.W.D., Sarawak, 1948; secon., state engrn., Brunei, 1949-51; exec. engrn., 1953; senr. exec. engrn., 1958; asst. D.P.W., 1960.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1948 | asst. exec. engrn., P.W.D. | Sarawak | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1949–1951 | secon., state engrn. | Brunei | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1953 | exec. engrn | Brunei *(inherited from previous clause)* | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 3 | 1958 | senr. exec. engrn | Brunei *(inherited from previous clause)* | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 4 | 1960 | asst. D.P.W | Brunei *(inherited from previous clause)* | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Howard, J. J___Sarawak___1949`

- Staff-list name: **Howard, J. J** | colony: **Sarawak** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | J. J. Howard | Assistant Executive Engineers | Public Works | — | — |
| 1950 | J. J. Howard | Executive Engineer / Assistant Executive Engineer | PUBLIC WORKS | — | — |
| 1951 | J. J. Howard | Executive Engineer / Assistant Executive Engineer | Public Works | — | — |

### Deterministic checks: `howard_j-j_b1922` vs `Howard, J. J___Sarawak___1949`

- [PASS] surname_gate: bio 'HOWARD' vs stint 'Howard, J. J' (exact)
- [PASS] initials: bio ['J', 'J'] ~ stint ['J', 'J']
- [PASS] age_gate: stint starts 1949, birth 1922 (age 27)
- [PASS] colony: 1 placed event(s) resolve to 'Sarawak'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 60 vs bar 60: 'asst. exec. engrn., P.W.D.' ~ 'Executive Engineer / Assistant Executive Engineer'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

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

