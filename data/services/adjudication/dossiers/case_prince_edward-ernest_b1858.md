<!-- {"case_id": "case_prince_edward-ernest_b1858", "bio_ids": ["prince_edward-ernest_b1858"], "stint_ids": ["Prince, Edward E___Canada___1898"]} -->
# Dossier case_prince_edward-ernest_b1858

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `prince_edward-ernest_b1858`

- Printed name: **PRINCE, Edward Ernest**
- Birth year: 1858 (attested in editions [1915])
- Honours: F.R.S.C.
- Appears in editions: [1915, 1919]

### Verbatim printed entry text (OCR)

**Version `col1915-L49865.v` — printed in editions [1915]:**

> PRINCE, Prof. Edward Ernest, F.R.S.C. &c.—B. 1858; ed. Modern Schol., Leeds, and St. Andrews, Camb., and Edin. Univ.; appd. demonstr., zool., Edin. Univ., 1885; naturalist, Scotch fishery bd. laboratory, St. Ands.; prof. zool. and comp. anat., Royal Infirmary Coll., Glasgow, 1890; fishery expert, Irish Fish Survey, 1893; vice-pres. Intern. Fisheries Congress, Washington, Paris, and St. Petersburg, 1903-06-09; vice-pres., biol. sect., Brit. Assoc., 1909; ditto, Royal Soc. of Canada, 1908; mem. of internat. relations coun., American fish. assoc., Rome, 1911; life mem. of British Science Guild; mem. of internat. fisheries comanr.; repres. Canada...

**Version `col1919-L55192.v` — printed in editions [1919]:**

> PRINCE, EDWARD ERNEST, F.R.S.C., &c.—B. 1858; ed. Modern Schl., Leeds, and St. Andrews, Camb., and Edin. Univ.; apptd. demonstr., zool., Edin. Univ., 1885; naturalist, Scotch fishery bd. laboratory, St. Ands.; prof. of

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1885–1885 | demonstr., zool. | — | [1915, 1919] |
| 1 | 1890–1890 | prof. zool. and comp. anat. | — | [1915] |
| 2 | 1893–1893 | fishery expert | — | [1915] |
| 3 | 1903–1909 | vice-pres. Intern. Fisheries Congress | — | [1915] |
| 4 | 1908–1908 | ditto | Canada | [1915] |
| 5 | 1909–1909 | vice-pres., biol. sect. | — | [1915] |
| 6 | 1911–1911 | mem. of internat. relations coun. | — | [1915] |

## Candidate stint `Prince, Edward E___Canada___1898`

- Staff-list name: **Prince, Edward E** | colony: **Canada** | listed 1898–1922 | editions [1898, 1899, 1900, 1905, 1906, 1907, 1908, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1922]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1898 | E. E. Prince | Commissioner and General Inspector of Fisheries for Canada | Marine and Fisheries | — | — |
| 1899 | E. E. Prince | Commissioner and General Inspector of Fisheries for Canada | Department of Marine and Fisheries | — | — |
| 1900 | E. E. Prince | Commissioner and General Inspector of Fisheries for Canada | Department of Marine and Fisheries | — | — |
| 1905 | E. E. Prince | Commissioner and General Inspector of Fisheries for Canada | Department of Marine and Fisheries | — | — |
| 1906 | E. E. Prince | Commissioner and General Inspector of Fisheries for Canada | Department of Marine and Fisheries | — | — |
| 1907 | E. E. Prince | Commissioner and General Inspector of Fisheries for Canada | Department of Marine and Fisheries | — | — |
| 1908 | E. E. Prince | Commissioner and General Inspector of Fisheries for Canada | Department of Marine and Fisheries | — | — |
| 1912 | E. E. Prince | Commissioner of Fisheries and International Commissioner | Marine and Fisheries | — | — |
| 1913 | E. E. Prince | Commissioner of Fisheries and International Commissioner | Department of Marine and Fisheries | — | — |
| 1914 | E. E. Prince | Commissioner of Fisheries and International Commissioner | Marine and Fisheries | — | — |
| 1915 | E. E. Prince | Commissioner of Fisheries and International Commissioner | Department of Marine and Fisheries | — | — |
| 1917 | Edward E. Prince | Commissioner of Fisheries | Department of the Naval Service | — | — |
| 1918 | Edward E. Prince | Commissioner of Fisheries | Department of the Naval Service | — | — |
| 1919 | Edward E. Prince | Commissioner of Fisheries | Naval Service | — | — |
| 1920 | Edward E. Prince | Commissioner of Fisheries | Naval Service | — | — |
| 1922 | E. E. Prince | Fisheries Specialist | Fisheries Branch | — | — |

### Deterministic checks: `prince_edward-ernest_b1858` vs `Prince, Edward E___Canada___1898`

- [PASS] surname_gate: bio 'PRINCE' vs stint 'Prince, Edward E' (exact)
- [PASS] initials: bio ['E', 'E'] ~ stint ['E', 'E']
- [PASS] age_gate: stint starts 1898, birth 1858 (age 40)
- [PASS] colony: 1 placed event(s) resolve to 'Canada'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1898-1922
- [FAIL] position_sim: best 21 vs bar 60: 'ditto' ~ 'Commissioner of Fisheries and International Commissioner'
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

