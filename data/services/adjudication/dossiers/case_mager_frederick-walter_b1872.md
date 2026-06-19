<!-- {"case_id": "case_mager_frederick-walter_b1872", "bio_ids": ["mager_frederick-walter_b1872"], "stint_ids": ["Magee, Fred___Canada___1918", "Magee, W___Jamaica___1920"]} -->
# Dossier case_mager_frederick-walter_b1872

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mager_frederick-walter_b1872`

- Printed name: **MAGER, FREDERICK WALTER**
- Birth year: 1872 (attested in editions [1927, 1928])
- Honours: M.I.C.E
- Appears in editions: [1927, 1928]

### Verbatim printed entry text (OCR)

**Version `col1927-L61122.v` — printed in editions [1927, 1928]:**

> MAGER, FREDERICK WALTER, M.I.C.E.—B. 1872; ed. King Ed. VI Sch., Bath; exec. engr., P.W.D., F.M.S., 1904-17; state engrnr., Pahang, 1918-20; state engrnr., Perak, 1920.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1904–1917 | exec. engr., P.W.D. | Federated Malay States | [1927, 1928] |
| 1 | 1918–1920 | state engrnr., Pahang | Federated Malay States *(inherited from previous clause)* | [1927, 1928] |
| 2 | 1920 | state engrnr., Perak | Federated Malay States *(inherited from previous clause)* | [1927, 1928] |

## Candidate stint `Magee, Fred___Canada___1918`

- Staff-list name: **Magee, Fred** | colony: **Canada** | listed 1918–1922 | editions [1918, 1919, 1922]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1918 | Fred Magee | — | Constituencies | — | — |
| 1919 | Fred Magee | Member | Constituencies | — | — |
| 1922 | Fred. Magee | Without Portfolio | Executive Council | — | — |
| 1922 | Fred Magee | — | — | — | — |

### Deterministic checks: `mager_frederick-walter_b1872` vs `Magee, Fred___Canada___1918`

- [PASS] surname_gate: bio 'MAGER' vs stint 'Magee, Fred' (fuzzy:1)
- [PASS] initials: bio ['F', 'W'] ~ stint ['F']
- [PASS] age_gate: stint starts 1918, birth 1872 (age 46)
- [FAIL] colony: no placed event resolves to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1918-1922
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Magee, W___Jamaica___1920`

- Staff-list name: **Magee, W** | colony: **Jamaica** | listed 1920–1934 | editions [1920, 1921, 1922, 1923, 1925, 1927, 1928, 1930, 1933, 1934]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1920 | W. Magee | Sub-Inspector | Jamaica Constabulary | — | Captain |
| 1921 | W. Magee | Sub-Inspector | Jamaica Constabulary | — | Captain |
| 1922 | W. Magee | 3rd Class Inspector | Jamaica Constabulary | — | — |
| 1923 | W. Magee | 3rd Class Inspector | Jamaica Constabulary | — | — |
| 1925 | W. Magee | 2nd Class Inspector | Jamaica Constabulary | — | — |
| 1927 | W. Magee | 2nd Class Inspector | Jamaica Constabulary | — | — |
| 1928 | W. Magee | Inspector of Police (acting) | Defence | — | — |
| 1928 | W. Magee | 2nd Class Inspector | Jamaica Constabulary | — | — |
| 1930 | W. Magee | 2nd Class Inspector | Jamaica Constabulary | — | — |
| 1933 | W. Magee | 2nd Class Inspector | Jamaica Constabulary | — | — |
| 1934 | W. Magee | 2nd Class Inspector | Jamaica Constabulary | — | — |

### Deterministic checks: `mager_frederick-walter_b1872` vs `Magee, W___Jamaica___1920`

- [PASS] surname_gate: bio 'MAGER' vs stint 'Magee, W' (fuzzy:1)
- [PASS] initials: bio ['F', 'W'] ~ stint ['W']
- [PASS] age_gate: stint starts 1920, birth 1872 (age 48)
- [FAIL] colony: no placed event resolves to 'Jamaica'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1920-1934
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

