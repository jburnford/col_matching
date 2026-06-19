<!-- {"case_id": "case_steemson_bernard-thomas_b1902", "bio_ids": ["steemson_bernard-thomas_b1902"], "stint_ids": ["Steemson, B. T___Gold Coast___1927", "Steemson, B. T___Gold Coast___1934"]} -->
# Dossier case_steemson_bernard-thomas_b1902

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `steemson_bernard-thomas_b1902`

- Printed name: **STEEMSON, Bernard Thomas**
- Birth year: 1902 (attested in editions [1948, 1949, 1950])
- Honours: B.A
- Appears in editions: [1948, 1949, 1950]

### Verbatim printed entry text (OCR)

**Version `col1948-L36114.v` — printed in editions [1948, 1949, 1950]:**

> STEEMSON, Bernard Thomas, B.A., E.D.—b. 1902; ed. Workspol Coll. and Brasenose Coll., Oxford; post. grad. course at I.C.T.A.; on mil. serv. 1939-45; agric. offr., G.C., 1925; senr., 1937; dep. dir. of agric., 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1925 | agric. offr. | Gold Coast | [1948, 1949, 1950] |
| 1 | 1937 | senr | Gold Coast *(inherited from previous clause)* | [1948, 1949, 1950] |
| 2 | 1946 | dep. dir. of agric | Gold Coast *(inherited from previous clause)* | [1948, 1949, 1950] |

## Candidate stint `Steemson, B. T___Gold Coast___1927`

- Staff-list name: **Steemson, B. T** | colony: **Gold Coast** | listed 1927–1929 | editions [1927, 1929]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | B. T. Steemson | Assistant Superintendent | Provincial Staff | — | — |
| 1929 | B. T. Steemson | Training Centre | Training Centre | — | — |

### Deterministic checks: `steemson_bernard-thomas_b1902` vs `Steemson, B. T___Gold Coast___1927`

- [PASS] surname_gate: bio 'STEEMSON' vs stint 'Steemson, B. T' (exact)
- [PASS] initials: bio ['B', 'T'] ~ stint ['B', 'T']
- [PASS] age_gate: stint starts 1927, birth 1902 (age 25)
- [PASS] colony: 3 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1927-1929
- [FAIL] position_sim: best 24 vs bar 60: 'agric. offr.' ~ 'Training Centre'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Steemson, B. T___Gold Coast___1934`

- Staff-list name: **Steemson, B. T** | colony: **Gold Coast** | listed 1934–1936 | editions [1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | B. T. Steemson | Superintendents and Assistant Superintendents | Agricultural Staff | — | — |
| 1936 | B. T. Steemson | Superintendent/Assistant Superintendent | Agricultural Staff | — | — |

### Deterministic checks: `steemson_bernard-thomas_b1902` vs `Steemson, B. T___Gold Coast___1934`

- [PASS] surname_gate: bio 'STEEMSON' vs stint 'Steemson, B. T' (exact)
- [PASS] initials: bio ['B', 'T'] ~ stint ['B', 'T']
- [PASS] age_gate: stint starts 1934, birth 1902 (age 32)
- [PASS] colony: 3 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1934-1936
- [FAIL] position_sim: best 21 vs bar 60: 'agric. offr.' ~ 'Superintendents and Assistant Superintendents'
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

