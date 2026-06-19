<!-- {"case_id": "case_davies_l-m_b1922", "bio_ids": ["davies_l-m_b1922"], "stint_ids": ["Davies, L. M___Western Pacific___1957"]} -->
# Dossier case_davies_l-m_b1922

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 137 official(s) with this surname in the graph's staff lists; 84 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `davies_l-m_b1922`

- Printed name: **DAVIES, L. M**
- Birth year: 1922 (attested in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Honours: C.M.G (1966), O.B.E (1962)
- Appears in editions: [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1957-L22426.v` — printed in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> DAVIES, L. M., C.M.G. (1966), O.B.E. (1962).—b. 1922; ed. St. Edward's Sch., Oxford; mil. serv., 1941-46, lieut. (A) R.N.V.R.; asst. dist. comsnr., G.C., 1948; admin. offr., cl. III, 1952; senr. asst. sec. (finan.) W. Pac. H.C., 1956; fin. sec., 1962; ch. sec., 1965.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1948 | asst. dist. comsnr. | Gold Coast | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1952 | admin. offr., cl. III | Gold Coast *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1956 | senr. asst. sec. (finan.) W. Pac. H.C | Gold Coast *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 3 | 1962 | fin. sec | Gold Coast *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 4 | 1965 | ch. sec | Gold Coast *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Davies, L. M___Western Pacific___1957`

- Staff-list name: **Davies, L. M** | colony: **Western Pacific** | listed 1957–1966 | editions [1957, 1958, 1959, 1960, 1961, 1962, 1964, 1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1957 | L. M. Davies | Senior Assistant Secretary (Finance) | Civil Establishment | — | — |
| 1958 | L. M. Davies | Senior Assistant Secretary (Finance) | Civil Establishment | — | — |
| 1959 | L. M. Davies | Senior Assistant Secretary | Civil Establishment | — | — |
| 1960 | L. M. Davies | Senior Assistant Secretary | Civil Establishment | — | — |
| 1961 | L. M. Davies | Senior Assistant Secretary | Civil Establishment | — | — |
| 1962 | L. M. Davies | Senior Assistant Secretary | Civil Establishment | — | — |
| 1964 | L. M. Davies | Financial Secretary | Civil Establishment | — | — |
| 1965 | L. M. Davies | Financial Secretary | Civil Establishment | — | — |
| 1966 | L. M. Davies | Chief Secretary | Civil Establishment | C.M.G., O.B.E. | — |

### Deterministic checks: `davies_l-m_b1922` vs `Davies, L. M___Western Pacific___1957`

- [PASS] surname_gate: bio 'DAVIES' vs stint 'Davies, L. M' (exact)
- [PASS] initials: bio ['L', 'M'] ~ stint ['L', 'M']
- [PASS] age_gate: stint starts 1957, birth 1922 (age 35)
- [FAIL] colony: no placed event resolves to 'Western Pacific'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1957-1966
- [FAIL] position_sim: no overlapping placed event to compare
- [PASS] honour: shared: C.M.G, O.B.E
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

