<!-- {"case_id": "case_dickie_r_b1919", "bio_ids": ["dickie_r_b1919"], "stint_ids": ["Dickie, R___Sarawak___1957"]} -->
# Dossier case_dickie_r_b1919

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['dickie_r_b1919'] carry a single initial only — the namesake trap applies.

## Biography `dickie_r_b1919`

- Printed name: **DICKIE, R**
- Birth year: 1919 (attested in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1958-L22029.v` — printed in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> DICKIE, R.—b. 1919; ed. Glasgow and London Univs.; M.O., Nig., 1943; W. regn.; D.D.M.S., Sarawak, 1955; D.M.S.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1943 | M.O. | Nigeria | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1955 | D.D.M.S. | Sarawak | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Dickie, R___Sarawak___1957`

- Staff-list name: **Dickie, R** | colony: **Sarawak** | listed 1957–1963 | editions [1957, 1958, 1959, 1960, 1961, 1962, 1963]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1957 | R. Dickie | Deputy Director of Medical Services | Civil Establishment | — | — |
| 1958 | R. Dickie | Deputy Directors of Medical Services | Civil Establishment | — | — |
| 1959 | R. Dickie | Deputy Directors of Medical Services | Civil Establishment | — | — |
| 1960 | R. Dickie | Deputy Director of Medical Services | Civil Establishment | — | — |
| 1961 | R. Dickie | Deputy Director of Medical Services | Civil Establishment | — | — |
| 1962 | R. Dickie | Deputy Director of Medical Services | Civil Establishment | — | — |
| 1963 | R. Dickie | Deputy Director of Medical Services | Civil Establishment | — | — |

### Deterministic checks: `dickie_r_b1919` vs `Dickie, R___Sarawak___1957`

- [PASS] surname_gate: bio 'DICKIE' vs stint 'Dickie, R' (exact)
- [PASS] initials: bio ['R'] ~ stint ['R']
- [PASS] age_gate: stint starts 1957, birth 1919 (age 38)
- [PASS] colony: 1 placed event(s) resolve to 'Sarawak'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1957-1963
- [FAIL] position_sim: best 21 vs bar 60: 'D.D.M.S.' ~ 'Deputy Director of Medical Services'
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

