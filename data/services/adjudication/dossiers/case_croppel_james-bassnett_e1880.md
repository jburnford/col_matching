<!-- {"case_id": "case_croppel_james-bassnett_e1880", "bio_ids": ["croppel_james-bassnett_e1880"], "stint_ids": ["Cropper, J___Gibraltar___1922", "Cropper, James B___St Lucia___1888", "Cropper, James B___Windward Islands___1883"]} -->
# Dossier case_croppel_james-bassnett_e1880

## Case context

- 1 biography(ies) and 3 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Cropper, J___Gibraltar___1922` is also gate-compatible with biography(ies) outside this case: ['cropper_james-bassnett_e1880'] (already linked elsewhere or filtered).
- NOTE: stint `Cropper, James B___St Lucia___1888` is also gate-compatible with biography(ies) outside this case: ['cropper_james-bassnett_e1880'] (already linked elsewhere or filtered).
- NOTE: stint `Cropper, James B___Windward Islands___1883` is also gate-compatible with biography(ies) outside this case: ['cropper_james-bassnett_e1880'] (already linked elsewhere or filtered).

## Biography `croppel_james-bassnett_e1880`

- Printed name: **CROPPEL, JAMES BASSNETT**
- Birth year: not printed
- Appears in editions: [1889]

### Verbatim printed entry text (OCR)

**Version `col1889-L32561.v` — printed in editions [1889]:**

> CROPPEL, JAMES BASSNETT.—Assistant protector of immigrants, St. Lucia, Sept., 1880; acting protector of immigrants, 1882; acting chief clerk, government office, and clerk of councils, Sept., 1884.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1880 | Assistant protector of immigrants | St. Lucia | [1889] |
| 1 | 1882 | acting protector of immigrants | St. Lucia *(inherited from previous clause)* | [1889] |
| 2 | 1884 | acting chief clerk, government office, and clerk of councils | St. Lucia *(inherited from previous clause)* | [1889] |

## Candidate stint `Cropper, J___Gibraltar___1922`

- Staff-list name: **Cropper, J** | colony: **Gibraltar** | listed 1922–1927 | editions [1922, 1923, 1924, 1925, 1927]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | J. Cropper | Dean of Gibraltar | Ecclesiastical | — | — |
| 1923 | J. Cropper | Dean of Gibraltar | Ecclesiastical | — | — |
| 1924 | J. Cropper | Dean of Gibraltar | Ecclesiastical | — | — |
| 1925 | J. Cropper | Dean of Gibraltar | Ecclesiastical | — | — |
| 1927 | J. Cropper | Dean of Gibraltar | Ecclesiastical | — | — |

### Deterministic checks: `croppel_james-bassnett_e1880` vs `Cropper, J___Gibraltar___1922`

- [PASS] surname_gate: bio 'CROPPEL' vs stint 'Cropper, J' (fuzzy:1)
- [PASS] initials: bio ['J', 'B'] ~ stint ['J']
- [PASS] age_gate: stint starts 1922; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Gibraltar'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1922-1927
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Cropper, James B___St Lucia___1888`

- Staff-list name: **Cropper, James B** | colony: **St Lucia** | listed 1888–1894 | editions [1888, 1890, 1894]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | J. B. Cropper | Chief Clerk, Government Office (acting) | Civil Establishment | — | — |
| 1888 | James B. Cropper | Assistant Protector of Immigrants, Clerk | Immigration | — | — |
| 1890 | J. B. Cropper | Chief Clerk, Government Office | Civil Establishment | — | — |
| 1894 | J. B. Cropper | Chief Clerk | Civil Establishment | — | — |

### Deterministic checks: `croppel_james-bassnett_e1880` vs `Cropper, James B___St Lucia___1888`

- [PASS] surname_gate: bio 'CROPPEL' vs stint 'Cropper, James B' (fuzzy:1)
- [PASS] initials: bio ['J', 'B'] ~ stint ['J', 'B']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [PASS] colony: 3 placed event(s) resolve to 'St Lucia'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1888-1894
- [PASS] position_sim: best 100 vs bar 60: 'acting chief clerk, government office, and clerk of councils' ~ 'Chief Clerk'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

## Candidate stint `Cropper, James B___Windward Islands___1883`

- Staff-list name: **Cropper, James B** | colony: **Windward Islands** | listed 1883–1889 | editions [1883, 1889]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1883 | James B. Cropper | Assistant Protector of Immigrants, Clerk | Immigration | — | — |
| 1889 | James B. Cropper | Assistant Protector of Immigrants, Clerk | Immigration | — | — |
| 1889 | J. B. Cropper | Chief Clerk, Government Office (acting) | Civil Establishment | — | — |
| 1889 | J. B. Cropper | Clerk (acting) | Executive Council | — | — |

### Deterministic checks: `croppel_james-bassnett_e1880` vs `Cropper, James B___Windward Islands___1883`

- [PASS] surname_gate: bio 'CROPPEL' vs stint 'Cropper, James B' (fuzzy:1)
- [PASS] initials: bio ['J', 'B'] ~ stint ['J', 'B']
- [PASS] age_gate: stint starts 1883; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Windward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1883-1889
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

