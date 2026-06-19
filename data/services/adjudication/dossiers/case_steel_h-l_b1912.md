<!-- {"case_id": "case_steel_h-l_b1912", "bio_ids": ["steel_h-l_b1912", "steel_h_b1926"], "stint_ids": ["Steel, H. L___Kenya___1949"]} -->
# Dossier case_steel_h-l_b1912

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 12 official(s) with this surname in the graph's staff lists; 10 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['steel_h_b1926'] carry a single initial only — the namesake trap applies.
- CONTESTED: stint(s) ['Steel, H. L___Kenya___1949'] have more than one claimant biography in this case.

## Biography `steel_h-l_b1912`

- Printed name: **STEEL, H. L**
- Birth year: 1912 (attested in editions [1958, 1959, 1960, 1961, 1962])
- Appears in editions: [1958, 1959, 1960, 1961, 1962]

### Verbatim printed entry text (OCR)

**Version `col1958-L27219.v` — printed in editions [1958, 1959, 1960, 1961, 1962]:**

> STEEL, H. L.—b. 1912; ed. Allan Glen's Sch., Glasgow, and Glasgow Univ.; assessor, E.A. income tax, 1940; asst. sec., Ken., 1952; under sec., 1961; ret.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1940 | assessor, E.A. income tax | — | [1958, 1959, 1960, 1961, 1962] |
| 1 | 1952 | asst. sec. | Kenya | [1958, 1959, 1960, 1961, 1962] |
| 2 | 1961 | under sec | Kenya *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962] |

## Biography `steel_h_b1926`

- Printed name: **STEEL, H**
- Birth year: 1926 (attested in editions [1966])
- Honours: O.B.E (1965)
- Appears in editions: [1966]

### Verbatim printed entry text (OCR)

**Version `col1966-L18149.v` — printed in editions [1966]:**

> STEEL, H., O.B.E. (1965).—b. 1926; ed. Christ’s Coll., Finchley, and New Coll., Oxford; mil. serv., 1944-47, R.A.S.C. and Intel. Corps., sgt.; legal asst., C.O., 1955; senr. legal asst., 1960; on loan C.R.O., 1965.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1955 | legal asst. | Colonial Office | [1966] |
| 1 | 1960 | senr. legal asst | Colonial Office *(inherited from previous clause)* | [1966] |
| 2 | 1965 | on loan C.R.O | Colonial Office *(inherited from previous clause)* | [1966] |

## Candidate stint `Steel, H. L___Kenya___1949`

- Staff-list name: **Steel, H. L** | colony: **Kenya** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | H. L. Steel | Executive Officer European Hospital Authority | Health and Local Government | — | — |
| 1950 | H. L. Steel | Executive Officer, European Hospital Authority | HEALTH AND LOCAL GOVERNMENT | — | — |
| 1951 | H. L. Steel | Executive Officer, European Hospital Authority | Health and Local Government | — | — |

### Deterministic checks: `steel_h-l_b1912` vs `Steel, H. L___Kenya___1949`

- [PASS] surname_gate: bio 'STEEL' vs stint 'Steel, H. L' (exact)
- [PASS] initials: bio ['H', 'L'] ~ stint ['H', 'L']
- [PASS] age_gate: stint starts 1949, birth 1912 (age 37)
- [PASS] colony: 2 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 19 vs bar 60: 'asst. sec.' ~ 'Executive Officer, European Hospital Authority'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

### Deterministic checks: `steel_h_b1926` vs `Steel, H. L___Kenya___1949`

- [PASS] surname_gate: bio 'STEEL' vs stint 'Steel, H. L' (exact)
- [PASS] initials: bio ['H'] ~ stint ['H', 'L']
- [PASS] age_gate: stint starts 1949, birth 1926 (age 23)
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
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

