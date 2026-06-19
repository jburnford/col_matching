<!-- {"case_id": "case_mujir_john-cochran_b1902", "bio_ids": ["mujir_john-cochran_b1902"], "stint_ids": ["Muir, J. C___Gold Coast___1927", "Muir, J. C___Zanzibar___1936"]} -->
# Dossier case_mujir_john-cochran_b1902

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 17 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Muir, J. C___Gold Coast___1927` is also gate-compatible with biography(ies) outside this case: ['muir_john-cochran_b1902'] (already linked elsewhere or filtered).
- Phase 1 found `mujir_john-cochran_b1902` ↔ `Muir, J. C___Zanzibar___1936` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Muir, J. C___Zanzibar___1936` is also gate-compatible with biography(ies) outside this case: ['muir_john-cochran_b1902'] (already linked elsewhere or filtered).

## Biography `mujir_john-cochran_b1902`

- Printed name: **MUJIR, John Cochran**
- Birth year: 1902 (attested in editions [1950])
- Honours: O.B.E (1944), Zanz (1944)
- Appears in editions: [1950]

### Verbatim printed entry text (OCR)

**Version `col1950-L38200.v` — printed in editions [1950]:**

> MUJIR, John Cochran, O.B.E. (1944), Order Brill. Star, Zanz. (1944).—b. 1902; ed. Allan Glen's Sch., Glasgow Univ., and West of Scotland Agr. Coll., B.Sc. (Agric.), N.D.A., N.D.D., post-grad. course I.C.T.A.; asst. supt., agric., G.C., 1925; senr. agric. offr., Zanz., 1935; dir., agric., 1940; Trin., 1944; Tang., 1948; mem. for agric. and natural resources, 1949; chmn., econ. cont. bd., food contrlr. and price contrlr., Zanz., 1940–44.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1925 | asst. supt., agric. | Gold Coast | [1950] |
| 1 | 1935 | senr. agric. offr. | Zanzibar | [1950] |
| 2 | 1940 | dir., agric | Zanzibar | [1950] |
| 3 | 1944 | dir., agric | Trinidad | [1950] |
| 4 | 1948 | dir., agric | Tanganyika | [1950] |
| 5 | 1949 | mem. for agric. and natural resources | Tanganyika *(inherited from previous clause)* | [1950] |

## Candidate stint `Muir, J. C___Gold Coast___1927`

- Staff-list name: **Muir, J. C** | colony: **Gold Coast** | listed 1927–1934 | editions [1927, 1928, 1929, 1932, 1934]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | J. C. Muir | Assistant Superintendent | Provincial Staff | — | — |
| 1928 | J. C. Muir | Assistant Superintendent | Provincial Staff | — | — |
| 1929 | J. C. Muir | Statistics and Surveys Division | Statistics and Surveys Division | — | — |
| 1932 | J. C. Muir | Rural Economics | Divisions | — | — |
| 1934 | J. C. Muir | Superintendents and Assistant Superintendents | Agricultural Staff | — | — |

### Deterministic checks: `mujir_john-cochran_b1902` vs `Muir, J. C___Gold Coast___1927`

- [PASS] surname_gate: bio 'MUJIR' vs stint 'Muir, J. C' (fuzzy:1)
- [PASS] initials: bio ['J', 'C'] ~ stint ['J', 'C']
- [PASS] age_gate: stint starts 1927, birth 1902 (age 25)
- [PASS] colony: 1 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1927-1934
- [FAIL] position_sim: best 50 vs bar 60: 'asst. supt., agric.' ~ 'Superintendents and Assistant Superintendents'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Muir, J. C___Zanzibar___1936`

- Staff-list name: **Muir, J. C** | colony: **Zanzibar** | listed 1936–1940 | editions [1936, 1937, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | J. C. Muir | Senior Agricultural Officer | Agricultural Department | — | — |
| 1937 | J. C. Muir | Senior Agricultural Officer | Agricultural Department | — | — |
| 1940 | J. C. Muir | Senior Agricultural Officer | Agricultural Department | — | — |

### Deterministic checks: `mujir_john-cochran_b1902` vs `Muir, J. C___Zanzibar___1936`

- [PASS] surname_gate: bio 'MUJIR' vs stint 'Muir, J. C' (fuzzy:1)
- [PASS] initials: bio ['J', 'C'] ~ stint ['J', 'C']
- [PASS] age_gate: stint starts 1936, birth 1902 (age 34)
- [PASS] colony: 2 placed event(s) resolve to 'Zanzibar'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1936-1940
- [PASS] position_sim: best 71 vs bar 60: 'senr. agric. offr.' ~ 'Senior Agricultural Officer'
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

