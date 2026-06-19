<!-- {"case_id": "case_renwick_j-d-b_b1927", "bio_ids": ["renwick_j-d-b_b1927"], "stint_ids": ["Renwick, J. D. B___Virgin Islands___1963"]} -->
# Dossier case_renwick_j-d-b_b1927

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 10 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `renwick_j-d-b_b1927`

- Printed name: **RENWICK, J. D. B**
- Birth year: 1927 (attested in editions [1963, 1964, 1965, 1966])
- Appears in editions: [1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1963-L24139.v` — printed in editions [1963, 1964, 1965, 1966]:**

> RENWICK, J. D. B.—b. 1927; ed. Grenada Boys’ Sch., and Keble Coll., Oxford; barrister-at-law, Middle Temple; addnl. mag., Antigua; mag. Mont., 1953; legal asst., St. Kitts, 1956; ch. mag., 1960; cr. atty., V.Is., 1962.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1953 | mag. Mont | — | [1963, 1964, 1965, 1966] |
| 1 | 1956 | legal asst. | St. Kitts | [1963, 1964, 1965, 1966] |
| 2 | 1960 | ch. mag | St. Kitts *(inherited from previous clause)* | [1963, 1964, 1965, 1966] |
| 3 | 1962 | cr. atty., V.Is | St. Kitts *(inherited from previous clause)* | [1963, 1964, 1965, 1966] |

## Candidate stint `Renwick, J. D. B___Virgin Islands___1963`

- Staff-list name: **Renwick, J. D. B** | colony: **Virgin Islands** | listed 1963–1965 | editions [1963, 1964, 1965]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1963 | J. D. B. Renwick | Crown Attorney | Civil Establishment | — | — |
| 1964 | J. D. B. Renwick | Crown Attorney | Civil Establishment | — | — |
| 1965 | J. D. B. Renwick | Crown Attorney | Civil Establishment | — | — |

### Deterministic checks: `renwick_j-d-b_b1927` vs `Renwick, J. D. B___Virgin Islands___1963`

- [PASS] surname_gate: bio 'RENWICK' vs stint 'Renwick, J. D. B' (exact)
- [PASS] initials: bio ['J', 'D', 'B'] ~ stint ['J', 'D', 'B']
- [PASS] age_gate: stint starts 1963, birth 1927 (age 36)
- [FAIL] colony: no placed event resolves to 'Virgin Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1963-1965
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

