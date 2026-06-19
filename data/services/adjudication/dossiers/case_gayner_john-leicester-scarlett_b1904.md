<!-- {"case_id": "case_gayner_john-leicester-scarlett_b1904", "bio_ids": ["gayner_john-leicester-scarlett_b1904"], "stint_ids": ["Gayner, J. L. S___Jamaica___1925"]} -->
# Dossier case_gayner_john-leicester-scarlett_b1904

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `gayner_john-leicester-scarlett_b1904`

- Printed name: **GAYNER, John Leicester Scarlett**
- Birth year: 1904 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L32780.v` — printed in editions [1948, 1949, 1950, 1951]:**

> GAYNER, John Leicester Scarlett.—b. 1904; ed. St. George's Coll.; outdoor offr., customs, J'ca., 1921; asst., collr.-gen.'s off., 1923; asst., col. sec.'s off., 1925; 2nd cl. clk., admin.-gen.'s off., 1927; 1st cl. 1937; ch. clk., marketing dept., 1940; asst. to comsrs. of commerce and industries, 1943; dep. comsrs. of commerce and industries, 1946; seconded as man. of the salt industry, Turks and Caicos Is. and acted as fond contrfr. for a period of three yrs. from 1940.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1921 | outdoor offr., customs | Jamaica | [1948, 1949, 1950, 1951] |
| 1 | 1923 | asst., collr.-gen.'s off | Jamaica *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 2 | 1925 | asst., col. sec.'s off | Jamaica *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 3 | 1927 | 2nd cl. clk., admin.-gen.'s off | Jamaica *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 4 | 1937 | 1st cl | Jamaica *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 5 | 1940 | ch. clk., marketing dept | Jamaica *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 6 | 1943 | asst. to comsrs. of commerce and industries | Jamaica *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 7 | 1946 | dep. comsrs. of commerce and industries | Jamaica *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Gayner, J. L. S___Jamaica___1925`

- Staff-list name: **Gayner, J. L. S** | colony: **Jamaica** | listed 1925–1927 | editions [1925, 1927]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1925 | J. L. Gayner | — | Revenue Department | — | — |
| 1927 | J. L. Gayner | Assistant | Colonial Secretary's Office | — | — |

### Deterministic checks: `gayner_john-leicester-scarlett_b1904` vs `Gayner, J. L. S___Jamaica___1925`

- [PASS] surname_gate: bio 'GAYNER' vs stint 'Gayner, J. L. S' (exact)
- [PASS] initials: bio ['J', 'L', 'S'] ~ stint ['J', 'L', 'S']
- [PASS] age_gate: stint starts 1925, birth 1904 (age 21)
- [PASS] colony: 8 placed event(s) resolve to 'Jamaica'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1925-1927
- [FAIL] position_sim: best 37 vs bar 60: 'asst., collr.-gen.'s off' ~ 'Assistant'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

