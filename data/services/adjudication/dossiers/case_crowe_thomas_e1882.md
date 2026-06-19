<!-- {"case_id": "case_crowe_thomas_e1882", "bio_ids": ["crowe_thomas_e1882", "crowf_thomas_e1882"], "stint_ids": ["Crow, A. T___Gold Coast___1949", "Crowe, T___Cape of Good Hope___1888"]} -->
# Dossier case_crowe_thomas_e1882

## Case context

- 2 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['crowe_thomas_e1882', 'crowf_thomas_e1882'] carry a single initial only — the namesake trap applies.
- CONTESTED: stint(s) ['Crowe, T___Cape of Good Hope___1888'] have more than one claimant biography in this case.

## Biography `crowe_thomas_e1882`

- Printed name: **CROWE, THOMAS**
- Birth year: not printed
- Appears in editions: [1894, 1896, 1897]

### Verbatim printed entry text (OCR)

**Version `col1894-L31031.v` — printed in editions [1894, 1896, 1897]:**

> CROWE, THOMAS.—Served in inland revenue department (England) to Oct., 1882; temporary employment as inspector of excise, Cape, Oct., 1882; chief inspector of excise, July, 1884; controller of licences and stamps, Dec., 1887, and administrator of foods, drugs and seeds act, Dec., 1890.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1882 | Served in inland revenue department (England) to | — | [1894, 1896, 1897] |
| 1 | 1882 | temporary employment as inspector of excise | Cape of Good Hope | [1894, 1896, 1897] |
| 2 | 1884 | chief inspector of excise | Cape of Good Hope *(inherited from previous clause)* | [1894, 1896, 1897] |
| 3 | 1887 | controller of licences and stamps | Cape of Good Hope *(inherited from previous clause)* | [1894, 1896, 1897] |
| 4 | 1890 | administrator of foods, drugs and seeds act | Cape of Good Hope *(inherited from previous clause)* | [1894, 1896, 1897] |

## Biography `crowf_thomas_e1882`

- Printed name: **CROWF, THOMAS**
- Birth year: not printed
- Appears in editions: [1898]

### Verbatim printed entry text (OCR)

**Version `col1898-L32878.v` — printed in editions [1898]:**

> CROWF, THOMAS.—Served in inland rev. dep. (England) to Oct., 1882; temporary employment as inspr. of excise, Cape, Oct., 1882; ch. inspr. of excise, July, 1884; controller of licences and stamps, Dec., 1887, and admstr. of Foods, Drugs, and Seeds Act, Dec., 1890.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1882 | temporary employment as inspr. of excise | Cape | [1898] |
| 1 | 1884 | ch. inspr. of excise | — | [1898] |
| 2 | 1887 | controller of licences and stamps | — | [1898] |
| 3 | 1890 | admstr. of Foods, Drugs, and Seeds Act | — | [1898] |
| 4 | ?–1882 | Served in inland rev. dep. | England | [1898] |

## Candidate stint `Crow, A. T___Gold Coast___1949`

- Staff-list name: **Crow, A. T** | colony: **Gold Coast** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | A. T. Crow | Geologists | Geological Survey | — | — |
| 1950 | A. T. Crow | Geologists | Geological Survey | — | — |
| 1951 | A. T. Crow | Geologists | GEOLOGICAL SURVEY | — | — |

### Deterministic checks: `crowf_thomas_e1882` vs `Crow, A. T___Gold Coast___1949`

- [PASS] surname_gate: bio 'CROWF' vs stint 'Crow, A. T' (fuzzy:1)
- [PASS] initials: bio ['T'] ~ stint ['A', 'T']
- [PASS] age_gate: stint starts 1949; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Gold Coast'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Crowe, T___Cape of Good Hope___1888`

- Staff-list name: **Crowe, T** | colony: **Cape of Good Hope** | listed 1888–1897 | editions [1888, 1889, 1890, 1896, 1897]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | T. Crowe | Chief Inspector | Excise Department | — | — |
| 1889 | T. Crowe | Chief Inspector | Excise Department | — | — |
| 1890 | T. Crowe | Controller | Licenses and Stamps Branch | — | — |
| 1896 | T. Crowe | Controller | Excise, Licenses, and Stamps Branch | — | — |
| 1897 | T. Crowe | Controller | Excise, Licenses, and Stamps Branch | — | — |

### Deterministic checks: `crowe_thomas_e1882` vs `Crowe, T___Cape of Good Hope___1888`

- [PASS] surname_gate: bio 'CROWE' vs stint 'Crowe, T' (exact)
- [PASS] initials: bio ['T'] ~ stint ['T']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [PASS] colony: 4 placed event(s) resolve to 'Cape of Good Hope'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1888-1897
- [PASS] position_sim: best 100 vs bar 60: 'chief inspector of excise' ~ 'Chief Inspector'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

### Deterministic checks: `crowf_thomas_e1882` vs `Crowe, T___Cape of Good Hope___1888`

- [PASS] surname_gate: bio 'CROWF' vs stint 'Crowe, T' (fuzzy:1)
- [PASS] initials: bio ['T'] ~ stint ['T']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Cape of Good Hope'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1888-1897
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

