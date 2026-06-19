<!-- {"case_id": "case_blair_doreen-josephine-bernard_b1898", "bio_ids": ["blair_doreen-josephine-bernard_b1898"], "stint_ids": ["Blair, D___Bermuda___1965", "Blair, D___Uganda___1921"]} -->
# Dossier case_blair_doreen-josephine-bernard_b1898

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 25 official(s) with this surname in the graph's staff lists; 19 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Blair, D___Bermuda___1965` is also gate-compatible with biography(ies) outside this case: ['blair_dyson_b1874'] (already linked elsewhere or filtered).
- NOTE: stint `Blair, D___Uganda___1921` is also gate-compatible with biography(ies) outside this case: ['blair_dyson_b1874'] (already linked elsewhere or filtered).

## Biography `blair_doreen-josephine-bernard_b1898`

- Printed name: **BLAIR, DOREEN JOSEPHINE BERNARD**
- Birth year: 1898 (attested in editions [1929, 1930, 1931, 1932, 1933])
- Appears in editions: [1929, 1930, 1931, 1932, 1933]

### Verbatim printed entry text (OCR)

**Version `col1929-L58482.v` — printed in editions [1929, 1930, 1931, 1932, 1933]:**

> BLAIR, DOREEN JOSEPHINE BERNARD.—B. 1898; ed. Ladies' Coll., Eastbourne, Ladies' Coll., Cheltenham, Lady Margaret Hall, Oxford; mistress, Achimota Coll., Gold Coast, Oct., 1927.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1927 | mistress, Achimota Coll. | Gold Coast | [1929, 1930, 1931, 1932, 1933] |

## Candidate stint `Blair, D___Bermuda___1965`

- Staff-list name: **Blair, D** | colony: **Bermuda** | listed 1965–1966 | editions [1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1965 | D. Blair | Aide-de-Camp | Civil Establishment | — | — |
| 1966 | D. Blair | Aide-de-Camp | Civil Establishment | — | — |

### Deterministic checks: `blair_doreen-josephine-bernard_b1898` vs `Blair, D___Bermuda___1965`

- [PASS] surname_gate: bio 'BLAIR' vs stint 'Blair, D' (exact)
- [PASS] initials: bio ['D', 'J', 'B'] ~ stint ['D']
- [PASS] age_gate: stint starts 1965, birth 1898 (age 67)
- [FAIL] colony: no placed event resolves to 'Bermuda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1965-1966
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Blair, D___Uganda___1921`

- Staff-list name: **Blair, D** | colony: **Uganda** | listed 1921–1929 | editions [1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1921 | D. Blair | Deputy Director of Surveys | Land and Survey | — | — |
| 1922 | D. Blair | Deputy Director of Surveys | Land and Survey Department | — | — |
| 1923 | D. Blair | Deputy Director of Surveys | Land and Survey Department | — | — |
| 1924 | D. Blair | Deputy Director of Surveys | Land and Survey Department | — | — |
| 1925 | D. Blair | Director of Surveys, Land Officer and Commissioner of Mines | Land and Survey Department | — | — |
| 1927 | D. Blair | Director of Surveys, Land Officer and Commissioner of Mines | Land and Survey Department | — | — |
| 1928 | D. Blair | Director of Surveys, Land Officer and Commissioner of Mines | Land and Survey Department | — | — |
| 1929 | D. Blair | Director of Surveys, Land Officer and Commissioner of Mines | Land and Survey Department | — | — |

### Deterministic checks: `blair_doreen-josephine-bernard_b1898` vs `Blair, D___Uganda___1921`

- [PASS] surname_gate: bio 'BLAIR' vs stint 'Blair, D' (exact)
- [PASS] initials: bio ['D', 'J', 'B'] ~ stint ['D']
- [PASS] age_gate: stint starts 1921, birth 1898 (age 23)
- [FAIL] colony: no placed event resolves to 'Uganda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1921-1929
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

