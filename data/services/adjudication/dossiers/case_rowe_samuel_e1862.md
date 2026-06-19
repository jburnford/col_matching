<!-- {"case_id": "case_rowe_samuel_e1862", "bio_ids": ["rowe_samuel_e1862"], "stint_ids": ["Rowe, Samuel___Sierra Leone___1878"]} -->
# Dossier case_rowe_samuel_e1862

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 30 official(s) with this surname in the graph's staff lists; 10 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['rowe_samuel_e1862'] carry a single initial only — the namesake trap applies.

## Biography `rowe_samuel_e1862`

- Printed name: **ROWE, SAMUEL**
- Birth year: not printed
- Honours: C.M.G. (1874), K.C.M.G. (1880)
- Appears in editions: [1883, 1886, 1888]

### Verbatim printed entry text (OCR)

**Version `col1883-L29340.v` — printed in editions [1883, 1886, 1888]:**

> ROWE, SIR SAMUEL, K.C.M.G., 1880 (C.M.G., 1874). Surgeon-Major (retired). Engaged on the West Coast of Africa since 1862, and as medical officer and chief of the staff with Sir J. H. Glover during the Ashantee war, 1873-4, in which capacity he accompanied Sir J. H. Glover's force into Ashanti and through Coomassie; despatched on special service to the Gold Coast, November, 1874; lieutenant-governor, West Africa Settlements, 1875; administrator of the Gambia, 1875; conducted two expeditions into the Sherbro country in 1876; governor of the West Africa Settlements, 1876; governor of the Gold Coast Colony, Jan., 1881; again governor of the West Africa Settlements, Dec., 1884.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1862 | — | West Coast of Africa | [1883, 1886, 1888] |
| 1 | 1873–1874 | medical officer and chief of the staff | Ashanti | [1883, 1886, 1888] |
| 2 | 1874–1874 | on special service | Gold Coast | [1883, 1886, 1888] |
| 3 | 1875–1875 | lieutenant-governor | West Africa Settlements | [1883, 1886, 1888] |
| 4 | 1875–1875 | administrator | Gambia | [1883, 1886, 1888] |
| 5 | 1876–1876 | — | Sherbro country | [1883, 1886, 1888] |
| 6 | 1876–1876 | governor | West Africa Settlements | [1883, 1886, 1888] |
| 7 | 1881–1881 | governor | Gold Coast Colony | [1883, 1886, 1888] |
| 8 | 1884–1884 | governor | West Africa Settlements | [1883, 1886, 1888] |

## Candidate stint `Rowe, Samuel___Sierra Leone___1878`

- Staff-list name: **Rowe, Samuel** | colony: **Sierra Leone** | listed 1878–1888 | editions [1878, 1879, 1880, 1886, 1888]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1878 | Samuel Rowe | Governor, Commander-in-Chief, and Vice-Admiral of W. Africa Settlements | Civil Establishment | C.M.G. | — |
| 1878 | Samuel Rowe | Governor | Governors | C.M.G. | — |
| 1879 | Samuel Rowe | Governor, Commander-in-Chief, and Vice-Admiral of W. Africa Settlements | Civil Establishment | C.M.G. | — |
| 1880 | Samuel Rowe | Governor, Commander-in-Chief, and Vice-Admiral of W. Africa Settlements | Civil Establishment | C.M.G. | — |
| 1886 | Sir Samuel Rowe | Governor, Commander-in-Chief, and Vice-Admiral of W. Africa Settlements | Civil Establishment | K.C.M.G. | — |

### Deterministic checks: `rowe_samuel_e1862` vs `Rowe, Samuel___Sierra Leone___1878`

- [PASS] surname_gate: bio 'ROWE' vs stint 'Rowe, Samuel' (exact)
- [PASS] initials: bio ['S'] ~ stint ['S']
- [PASS] age_gate: stint starts 1878; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Sierra Leone'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1878-1888
- [FAIL] position_sim: no overlapping placed event to compare
- [PASS] honour: shared: C.M.G., K.C.M.G.
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

