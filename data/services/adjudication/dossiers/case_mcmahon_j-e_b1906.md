<!-- {"case_id": "case_mcmahon_j-e_b1906", "bio_ids": ["mcmahon_j-e_b1906"], "stint_ids": ["McMahon, J. E___Straits Settlements___1931"]} -->
# Dossier case_mcmahon_j-e_b1906

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mcmahon_j-e_b1906`

- Printed name: **McMAHON, J. E**
- Birth year: 1906 (attested in editions [1956, 1957])
- Appears in editions: [1956, 1957]

### Verbatim printed entry text (OCR)

**Version `col1956-L22819.v` — printed in editions [1956, 1957]:**

> McMAHON, J. E.—b. 1906; ed. Trinity Coll., Dublin; M.O., S.S. and F.M.S., 1930; interned, 1941-45; admin. M.O. gr. B, 1949; gr. A, 1950; state med. and health offr., N. Sembilan, 1950; asst. D.M.S., Fed. of Mal., 1952; chief M.O., Malacca, 1953.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1930 | M.O., S.S. and F.M.S | Straits Settlements | [1956, 1957] |
| 1 | 1941–1945 | interned | Straits Settlements *(inherited from previous clause)* | [1956, 1957] |
| 2 | 1949 | admin. M.O. gr. B | Straits Settlements *(inherited from previous clause)* | [1956, 1957] |
| 3 | 1950 | gr. A | Straits Settlements *(inherited from previous clause)* | [1956, 1957] |
| 4 | 1952 | asst. D.M.S., Fed. of Mal | Straits Settlements *(inherited from previous clause)* | [1956, 1957] |
| 5 | 1953 | chief M.O., Malacca | Straits Settlements *(inherited from previous clause)* | [1956, 1957] |

## Candidate stint `McMahon, J. E___Straits Settlements___1931`

- Staff-list name: **McMahon, J. E** | colony: **Straits Settlements** | listed 1931–1934 | editions [1931, 1932, 1933, 1934]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | J. E. McMahon | Medical Officer | Medical | — | — |
| 1932 | J. E. McMahon | Medical Officer | Medical | — | — |
| 1933 | J. E. McMahon | Medical Officer | Medical | — | — |
| 1933 | J. E. McMahon | Medical Officer | Establishment | — | — |
| 1934 | J. E. McMahon | Medical Officer | Establishment | — | — |
| 1934 | J. E. McMahon | Medical Officer | Labuan | — | — |

### Deterministic checks: `mcmahon_j-e_b1906` vs `McMahon, J. E___Straits Settlements___1931`

- [PASS] surname_gate: bio 'McMAHON' vs stint 'McMahon, J. E' (exact)
- [PASS] initials: bio ['J', 'E'] ~ stint ['J', 'E']
- [PASS] age_gate: stint starts 1931, birth 1906 (age 25)
- [PASS] colony: 6 placed event(s) resolve to 'Straits Settlements'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1931-1934
- [FAIL] position_sim: best 21 vs bar 60: 'M.O., S.S. and F.M.S' ~ 'Medical Officer'
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

