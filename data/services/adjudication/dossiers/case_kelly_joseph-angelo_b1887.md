<!-- {"case_id": "case_kelly_joseph-angelo_b1887", "bio_ids": ["kelly_joseph-angelo_b1887"], "stint_ids": ["Kelly, J. A___Gold Coast___1927"]} -->
# Dossier case_kelly_joseph-angelo_b1887

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 61 official(s) with this surname in the graph's staff lists; 21 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Kelly, J. A___Gold Coast___1927` is also gate-compatible with biography(ies) outside this case: ['kelly_john-o-brien-b-a-mod-ll-b_b1907'] (already linked elsewhere or filtered).

## Biography `kelly_joseph-angelo_b1887`

- Printed name: **KELLY, JOSEPH ANGELO**
- Birth year: 1887 (attested in editions [1936])
- Appears in editions: [1936, 1937]

### Verbatim printed entry text (OCR)

**Version `col1936-L62129.v` — printed in editions [1936]:**

> KELLY, JOSEPH ANGELO.—B. 1887; ed. O'Brien Coll., Marino, Dublin; R.A.F., France, Belgium and Egypt, 1915-19; qmr., 8th Wing, R.A.F., ment. in desp., 1918; polit. dept., Palestine, 1920; secretariat ast., C.S.O. Gold Coast, 1923; acct., transport dept., 1926.

**Version `col1937-L62315.v` — printed in editions [1937]:**

> KELLY, JOSEPH ANGELO.—O'Brien Coll., Marino, Dublin; Belgium and Egypt, 1915-19; R.A.F., ment. in desp., 1919.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1915–1919 | R.A.F., France, Belgium and Egypt | — | [1936, 1937] |
| 1 | 1918 | qmr., 8th Wing, R.A.F., ment. in desp | — | [1936] |
| 2 | 1919 | R.A.F., ment. in desp | — | [1937] |
| 3 | 1920 | polit. dept. | Palestine | [1936] |
| 4 | 1923 | secretariat ast., C.S.O. Gold Coast | Palestine *(inherited from previous clause)* | [1936] |
| 5 | 1926 | acct., transport dept | Palestine *(inherited from previous clause)* | [1936] |

## Candidate stint `Kelly, J. A___Gold Coast___1927`

- Staff-list name: **Kelly, J. A** | colony: **Gold Coast** | listed 1927–1936 | editions [1927, 1928, 1929, 1930, 1932, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | J. A. Kelly | Accountant | Transport Department | — | — |
| 1928 | J. A. Kelly | Accountant | Transport Department | — | — |
| 1929 | J. A. Kelly | Accountant | Transport Department | — | — |
| 1930 | J. A. Kelly | Accountant | Transport Department | — | — |
| 1932 | J. A. Kelly | Accountant | Transport Department | — | — |
| 1936 | J. A. Kelly | Accountant | Transport Department | — | — |

### Deterministic checks: `kelly_joseph-angelo_b1887` vs `Kelly, J. A___Gold Coast___1927`

- [PASS] surname_gate: bio 'KELLY' vs stint 'Kelly, J. A' (exact)
- [PASS] initials: bio ['J', 'A'] ~ stint ['J', 'A']
- [PASS] age_gate: stint starts 1927, birth 1887 (age 40)
- [FAIL] colony: no placed event resolves to 'Gold Coast'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1927-1936
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

