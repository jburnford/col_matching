<!-- {"case_id": "case_cronen_brian_e1911", "bio_ids": ["cronen_brian_e1911", "cronin_brian_e1911"], "stint_ids": ["Cronin, B. L___Fiji___1939"]} -->
# Dossier case_cronen_brian_e1911

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['cronen_brian_e1911', 'cronin_brian_e1911'] carry a single initial only — the namesake trap applies.
- CONTESTED: stint(s) ['Cronin, B. L___Fiji___1939'] have more than one claimant biography in this case.

## Biography `cronen_brian_e1911`

- Printed name: **CRONEN, BRIAN**
- Birth year: not printed
- Appears in editions: [1932]

### Verbatim printed entry text (OCR)

**Version `col1932-L59434.v` — printed in editions [1932]:**

> CRONEN, BRIAN.—Ed. Dulwich Coll.; served B.S.A. pol. and Bechuanaland Prot. pol., 1911; 2nd grade clk., 1921; ag. sub-inspr., 1922; ag. ast. res. mag., 1926; passed 2nd grade Secwana exam., 1923; ag. res. mag., 1927; 1st grade clk., Apr., 1928; sub-inspr., Bechuanaland Prot. pol., 1929.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1911 | served B.S.A. pol. and Bechuanaland Prot. pol | — | [1932] |
| 1 | 1921 | 2nd grade clk | — | [1932] |
| 2 | 1922 | ag. sub-inspr | — | [1932] |
| 3 | 1923 | passed 2nd grade Secwana exam | — | [1932] |
| 4 | 1926 | ag. ast. res. mag | — | [1932] |
| 5 | 1927 | ag. res. mag | — | [1932] |
| 6 | 1928 | 1st grade clk | — | [1932] |
| 7 | 1929 | sub-inspr., Bechuanaland Prot. pol | Bechuanaland | [1932] |

## Biography `cronin_brian_e1911`

- Printed name: **CRONIN, BRIAN**
- Birth year: not printed
- Appears in editions: [1940]

### Verbatim printed entry text (OCR)

**Version `col1940-L63469.v` — printed in editions [1940]:**

> CRONIN, BRIAN.—Ed. Dulwich Coll.; served B.S.A. pol. and Bechuanaland Prot. pol., 1911; 2nd grade clk., 1921; ag. sub-inspr., 1922; ag. ast. res. mag., 1926; passed 2nd grade Seawana exam., 1923; ag. res. mag., 1927; 1st grade clk., Apr., 1928; sub-inspr., Bechuanaland Prot. pol., 1929.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1911 | served B.S.A. pol. and Bechuanaland Prot. pol | — | [1940] |
| 1 | 1921 | 2nd grade clk | — | [1940] |
| 2 | 1922 | ag. sub-inspr | — | [1940] |
| 3 | 1923 | passed 2nd grade Seawana exam | — | [1940] |
| 4 | 1926 | ag. ast. res. mag | — | [1940] |
| 5 | 1927 | ag. res. mag | — | [1940] |
| 6 | 1928 | 1st grade clk | — | [1940] |
| 7 | 1929 | sub-inspr., Bechuanaland Prot. pol | Bechuanaland | [1940] |

## Candidate stint `Cronin, B. L___Fiji___1939`

- Staff-list name: **Cronin, B. L** | colony: **Fiji** | listed 1939–1951 | editions [1939, 1940, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | B. L. Cronin | Assistant Mechanical Engineer | Public Works Department | — | — |
| 1940 | B. L. Cronin | Assistant Mechanical Engineers | Public Works Department | — | — |
| 1950 | B. L. Cronin | Assistant Engineer (Mechanical) | Public Works | — | — |
| 1951 | B. L. Cronin | Assistant Engineer (Mechanical) | PUBLIC WORKS | — | — |

### Deterministic checks: `cronen_brian_e1911` vs `Cronin, B. L___Fiji___1939`

- [PASS] surname_gate: bio 'CRONEN' vs stint 'Cronin, B. L' (fuzzy:1)
- [PASS] initials: bio ['B'] ~ stint ['B', 'L']
- [PASS] age_gate: stint starts 1939; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Fiji'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1939-1951
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `cronin_brian_e1911` vs `Cronin, B. L___Fiji___1939`

- [PASS] surname_gate: bio 'CRONIN' vs stint 'Cronin, B. L' (exact)
- [PASS] initials: bio ['B'] ~ stint ['B', 'L']
- [PASS] age_gate: stint starts 1939; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Fiji'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1939-1951
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

