<!-- {"case_id": "case_gaass_m-d-i_b1916", "bio_ids": ["gaass_m-d-i_b1916"], "stint_ids": ["Gass, M. D. I___Western Pacific___1959"]} -->
# Dossier case_gaass_m-d-i_b1916

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- Phase 1 found `gaass_m-d-i_b1916` ↔ `Gass, M. D. I___Western Pacific___1959` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Gass, M. D. I___Western Pacific___1959` is also gate-compatible with biography(ies) outside this case: ['gass_michael-david-irving_b1916'] (already linked elsewhere or filtered).

## Biography `gaass_m-d-i_b1916`

- Printed name: **GAASS, M. D. I**
- Birth year: 1916 (attested in editions [1961])
- Honours: C.M.G (1960)
- Appears in editions: [1961]

### Verbatim printed entry text (OCR)

**Version `col1961-L22337.v` — printed in editions [1961]:**

> GAASS, M. D. I., C.M.G. (1960).—b. 1916; ed. King's Sch., Bruton, Christ Church, Oxford, and Queens' Coll., Camb.; mil. serv., 1939-45 (desps. twice); asst. dist. comsnnr., G.C., 1939; dist. comsnnr., 1945; admin. offr., cl. II, 1951; cl. I, 1953; perm. sec., 1956; chief sec., W. Pac. high comsnn., 1958.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1939 | asst. dist. comsnnr. | Gold Coast | [1961] |
| 1 | 1945 | dist. comsnnr | Gold Coast *(inherited from previous clause)* | [1961] |
| 2 | 1951 | admin. offr., cl. II | Gold Coast *(inherited from previous clause)* | [1961] |
| 3 | 1953 | cl. I | Gold Coast *(inherited from previous clause)* | [1961] |
| 4 | 1956 | perm. sec | Gold Coast *(inherited from previous clause)* | [1961] |
| 5 | 1958 | chief sec., W. Pac. high comsnn | Western Pacific | [1961] |

## Candidate stint `Gass, M. D. I___Western Pacific___1959`

- Staff-list name: **Gass, M. D. I** | colony: **Western Pacific** | listed 1959–1965 | editions [1959, 1960, 1961, 1962, 1964, 1965]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1959 | M. D. I. Gass | Chief Secretary | Civil Establishment | — | — |
| 1960 | M. D. I. Gass | Chief Secretary | Civil Establishment | — | — |
| 1961 | M. D. I. Gass | Chief Secretary | Civil Establishment | C.M.G. | — |
| 1962 | M. D. I. Gass | Chief Secretary | Civil Establishment | C.M.G. | — |
| 1964 | M. D. I. Gass | Chief Secretary | Civil Establishment | C.M.G. | — |
| 1965 | M. D. I. Gass | Chief Secretary | Civil Establishment | C.M.G. | — |

### Deterministic checks: `gaass_m-d-i_b1916` vs `Gass, M. D. I___Western Pacific___1959`

- [PASS] surname_gate: bio 'GAASS' vs stint 'Gass, M. D. I' (fuzzy:1)
- [PASS] initials: bio ['M', 'D', 'I'] ~ stint ['M', 'D', 'I']
- [PASS] age_gate: stint starts 1959, birth 1916 (age 43)
- [PASS] colony: 1 placed event(s) resolve to 'Western Pacific'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1959-1965
- [FAIL] position_sim: best 50 vs bar 60: 'chief sec., W. Pac. high comsnn' ~ 'Chief Secretary'
- [PASS] honour: shared: C.M.G
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

