<!-- {"case_id": "case_herold_arthur-beaufort_b1873", "bio_ids": ["herold_arthur-beaufort_b1873"], "stint_ids": ["Herold, A. B___Cape of Good Hope___1896"]} -->
# Dossier case_herold_arthur-beaufort_b1873

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `herold_arthur-beaufort_b1873`

- Printed name: **HEROLD, ARTHUR BEAUFORT**
- Birth year: 1873 (attested in editions [1932])
- Appears in editions: [1932]

### Verbatim printed entry text (OCR)

**Version `col1932-L61079.v` — printed in editions [1932]:**

> HEROLD, ARTHUR BEAUFORT.—B. 1873; ed. Victoria Coll., Stellenbosch; clk., mag.'s office, Stellenbosch, Jan., 1891; census office, Cape Town, June, 1891; mag.'s office, Richmond, Cape Colony, Dec., 1891; col. sec.'s office, Cape Town, Nov., 1892; ch. examr., deeds office, Pretoria, Mar., 1902; asst. mag., Johannesburg, Sept., 1905; mag., Volksrust, Aug., 1909; Carolina, 1913; Standerton, Oct., 1919; Ermelo, Feb., 1923; Pietersburg, Feb., 1925; Port Elizabeth, Sept., 1928; Pretoria, Jan., 1930.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1891 | clk., mag.'s office, Stellenbosch | — | [1932] |
| 1 | 1891 | census office, Cape Town | Cape of Good Hope | [1932] |
| 2 | 1892 | col. sec.'s office, Cape Town | Cape of Good Hope | [1932] |
| 3 | 1902 | ch. examr., deeds office, Pretoria | Cape of Good Hope *(inherited from previous clause)* | [1932] |
| 4 | 1905 | asst. mag., Johannesburg | Cape of Good Hope *(inherited from previous clause)* | [1932] |
| 5 | 1909 | mag., Volksrust | Cape of Good Hope *(inherited from previous clause)* | [1932] |
| 6 | 1913 | Carolina | Cape of Good Hope *(inherited from previous clause)* | [1932] |
| 7 | 1919 | Standerton | Cape of Good Hope *(inherited from previous clause)* | [1932] |
| 8 | 1923 | Ermelo | Cape of Good Hope *(inherited from previous clause)* | [1932] |
| 9 | 1925 | Pietersburg | Cape of Good Hope *(inherited from previous clause)* | [1932] |
| 10 | 1928 | Port Elizabeth | Cape of Good Hope *(inherited from previous clause)* | [1932] |
| 11 | 1930 | Pretoria | Cape of Good Hope *(inherited from previous clause)* | [1932] |

## Candidate stint `Herold, A. B___Cape of Good Hope___1896`

- Staff-list name: **Herold, A. B** | colony: **Cape of Good Hope** | listed 1896–1900 | editions [1896, 1897, 1898, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1896 | A. B. Herold | Clerks | Stationery and Printing, and Depot for Police and Government Stores | — | — |
| 1897 | A. B. Herold | Clerks | Administrative Branch | — | — |
| 1898 | A. B. Herold | Clerk | Stationery and Printing, and Depot for Police and Government Stores | — | — |
| 1900 | A. B. Herold | Clerks | Stationery and Printing, and Depot for Police and Government Stores | — | — |

### Deterministic checks: `herold_arthur-beaufort_b1873` vs `Herold, A. B___Cape of Good Hope___1896`

- [PASS] surname_gate: bio 'HEROLD' vs stint 'Herold, A. B' (exact)
- [PASS] initials: bio ['A', 'B'] ~ stint ['A', 'B']
- [PASS] age_gate: stint starts 1896, birth 1873 (age 23)
- [PASS] colony: 11 placed event(s) resolve to 'Cape of Good Hope'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1896-1900
- [FAIL] position_sim: best 26 vs bar 60: 'col. sec.'s office, Cape Town' ~ 'Clerks'
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

