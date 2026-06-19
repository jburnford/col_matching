<!-- {"case_id": "case_warren_john-joseph_b1890", "bio_ids": ["warren_john-joseph_b1890"], "stint_ids": ["Warren, J. J___Straits Settlements___1931"]} -->
# Dossier case_warren_john-joseph_b1890

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 32 official(s) with this surname in the graph's staff lists; 22 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Warren, J. J___Straits Settlements___1931` is also gate-compatible with biography(ies) outside this case: ['warren_john-joseph_b1889'] (already linked elsewhere or filtered).

## Biography `warren_john-joseph_b1890`

- Printed name: **WARREN, JOHN JOSEPH**
- Birth year: 1890 (attested in editions [1937])
- Appears in editions: [1937]

### Verbatim printed entry text (OCR)

**Version `col1937-L65623.v` — printed in editions [1937]:**

> WARREN, JOHN JOSEPH.—B. 1890; 1910-13; inspr., pol., F.M.S., May, 1913; commnr., Mar., 1921; dir. comm., May, 1926; head, prev. serv., Nov., 1927; astt. astt., govt. monops., S.S. No. 1; senr. astt. astt., govt. monops., S.S. No. 2; senr. astt. astt., excise, 1934; ag. astt. astt. and excise, S.S. 1935.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1910–1913 | — | — | [1937] |
| 1 | 1913 | inspr., pol. | Federated Malay States | [1937] |
| 2 | 1921 | commnr | Federated Malay States *(inherited from previous clause)* | [1937] |
| 3 | 1926 | dir. comm | Federated Malay States *(inherited from previous clause)* | [1937] |
| 4 | 1927 | head, prev. serv | Federated Malay States *(inherited from previous clause)* | [1937] |
| 5 | 1934 | senr. astt. astt., excise | Federated Malay States *(inherited from previous clause)* | [1937] |
| 6 | 1935 | ag. astt. astt. and excise | Straits Settlements | [1937] |

## Candidate stint `Warren, J. J___Straits Settlements___1931`

- Staff-list name: **Warren, J. J** | colony: **Straits Settlements** | listed 1931–1936 | editions [1931, 1932, 1933, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | J. J. Warren | Assistant Superintendent | Government Monopolies Department Singapore | — | — |
| 1932 | J. J. Warren | Assistant Superintendent | Government Monopolies Department | — | — |
| 1933 | J. J. Warren | Assistant Superintendents | Government Monopolies Department | — | — |
| 1936 | J. J. Warren | Senior Deputy Commissioner of Excise | Department of Excise | — | — |

### Deterministic checks: `warren_john-joseph_b1890` vs `Warren, J. J___Straits Settlements___1931`

- [PASS] surname_gate: bio 'WARREN' vs stint 'Warren, J. J' (exact)
- [PASS] initials: bio ['J', 'J'] ~ stint ['J', 'J']
- [PASS] age_gate: stint starts 1931, birth 1890 (age 41)
- [PASS] colony: 1 placed event(s) resolve to 'Straits Settlements'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1931-1936
- [FAIL] position_sim: best 50 vs bar 60: 'ag. astt. astt. and excise' ~ 'Senior Deputy Commissioner of Excise'
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

