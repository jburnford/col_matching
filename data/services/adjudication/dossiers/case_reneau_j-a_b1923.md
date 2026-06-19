<!-- {"case_id": "case_reneau_j-a_b1923", "bio_ids": ["reneau_j-a_b1923"], "stint_ids": ["Reneau, J. A___British Honduras___1963"]} -->
# Dossier case_reneau_j-a_b1923

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `reneau_j-a_b1923`

- Printed name: **RENEAU, J. A**
- Birth year: 1923 (attested in editions [1961, 1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1961-L26613.v` — printed in editions [1961, 1962, 1963, 1964, 1965, 1966]:**

> RENEAU, J. A.—b. 1923; ed. St. John’s Coll., Belize, and Universidad de San Carlos de Guatemala; M.O.H., Belize, B. Hond., 1960.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1960 | M.O.H., Belize | British Honduras | [1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Reneau, J. A___British Honduras___1963`

- Staff-list name: **Reneau, J. A** | colony: **British Honduras** | listed 1963–1966 | editions [1963, 1964, 1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1963 | J. A. Reneau | Medical Officers of Health | Civil Establishment | — | — |
| 1964 | J. A. Reneau | Medical Officers of Health | Civil Establishment | — | — |
| 1965 | J. A. Reneau | Medical Officers of Health | Civil Establishment | — | — |
| 1966 | J. A. Reneau | Medical Officer of Health | Civil Establishment | — | — |

### Deterministic checks: `reneau_j-a_b1923` vs `Reneau, J. A___British Honduras___1963`

- [PASS] surname_gate: bio 'RENEAU' vs stint 'Reneau, J. A' (exact)
- [PASS] initials: bio ['J', 'A'] ~ stint ['J', 'A']
- [PASS] age_gate: stint starts 1963, birth 1923 (age 40)
- [PASS] colony: 1 placed event(s) resolve to 'British Honduras'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1963-1966
- [FAIL] position_sim: best 29 vs bar 60: 'M.O.H., Belize' ~ 'Medical Officer of Health'
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

