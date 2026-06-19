<!-- {"case_id": "case_wadhams_john-oswald_b1901", "bio_ids": ["wadhams_john-oswald_b1901"], "stint_ids": ["Wadham, J___Australia___1918"]} -->
# Dossier case_wadhams_john-oswald_b1901

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `wadhams_john-oswald_b1901`

- Printed name: **WADHAMS, John Oswald**
- Birth year: 1901 (attested in editions [1951])
- Appears in editions: [1951]

### Verbatim printed entry text (OCR)

**Version `col1951-L43460.v` — printed in editions [1951]:**

> WADHAMS, John Oswald, B.S. (hons.), M.A. (Cantab.), dip. for.—b. 1901; ed. Bolton Sch., Lancs., Owen's Coll., Manchester Univ., and Christ's Coll., Camb.; on war service, 1942-45, lt.-col. (desps. twice); asst. consvtr., forests, Burma, 1924; dep. consvtr., 1930; consvtr., 1947; ch. exec. offr., state timber extraction organ., 1948; resigned, 1949; asst. consvtr., forests (on contract), N. Rhod., 1949.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1924 | asst. consvtr., forests, Burma | — | [1951] |
| 1 | 1930 | dep. consvtr | — | [1951] |
| 2 | 1947 | consvtr | — | [1951] |
| 3 | 1948 | ch. exec. offr., state timber extraction organ | — | [1951] |
| 4 | 1949 | resigned | — | [1951] |
| 5 | 1949 | asst. consvtr., forests (on contract) | Northern Rhodesia | [1951] |

## Candidate stint `Wadham, J___Australia___1918`

- Staff-list name: **Wadham, J** | colony: **Australia** | listed 1918–1927 | editions [1918, 1927]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1918 | J. Wadham | Accountant | Department of Lands and Survey | — | — |
| 1927 | J. Wadham | Accountant | Department of Lands and Survey | — | — |

### Deterministic checks: `wadhams_john-oswald_b1901` vs `Wadham, J___Australia___1918`

- [PASS] surname_gate: bio 'WADHAMS' vs stint 'Wadham, J' (fuzzy:1)
- [PASS] initials: bio ['J', 'O'] ~ stint ['J']
- [PASS] age_gate: stint starts 1918, birth 1901 (age 17)
- [FAIL] colony: no placed event resolves to 'Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1918-1927
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

