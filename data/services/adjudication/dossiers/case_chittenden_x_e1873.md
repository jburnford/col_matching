<!-- {"case_id": "case_chittenden_x_e1873", "bio_ids": ["chittenden_x_e1873"], "stint_ids": ["Chittenden, J. F___Trinidad___1877", "Chittenden, V. H. W___Hong Kong___1930"]} -->
# Dossier case_chittenden_x_e1873

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['chittenden_x_e1873'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Chittenden, V. H. W___Hong Kong___1930` is also gate-compatible with biography(ies) outside this case: ['chittenden_victor-henry-william_b1897'] (already linked elsewhere or filtered).

## Biography `chittenden_x_e1873`

- Printed name: **CHITTENDEN, (no given names printed)**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L26823.v` — printed in editions [1883]:**

> CHITTENDEN, Dr.—Appointed resident surgeon San Fernando Hospital, Trinidad, 1873; district medical officer, 1875.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1873 | Appointed resident surgeon San Fernando Hospital | Trinidad | [1883] |
| 1 | 1875 | district medical officer | Trinidad *(inherited from previous clause)* | [1883] |

## Candidate stint `Chittenden, J. F___Trinidad___1877`

- Staff-list name: **Chittenden, J. F** | colony: **Trinidad** | listed 1877–1880 | editions [1877, 1878, 1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | J. F. Chittenden | Government Medical Officer | Government Medical Officers | — | — |
| 1878 | J. F. Chittenden | Medical Officer | Medical Establishment | — | — |
| 1879 | J. F. Chittenden | Point à Pierre District | Medical Establishment | — | — |
| 1880 | J. F. Chittenden | Point à Pierre District | Government Medical Officers | — | — |

### Deterministic checks: `chittenden_x_e1873` vs `Chittenden, J. F___Trinidad___1877`

- [PASS] surname_gate: bio 'CHITTENDEN' vs stint 'Chittenden, J. F' (exact)
- [PASS] initials: bio ['?'] ~ stint ['J', 'F']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Trinidad'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1880
- [PASS] position_sim: best 100 vs bar 60: 'district medical officer' ~ 'Medical Officer'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

## Candidate stint `Chittenden, V. H. W___Hong Kong___1930`

- Staff-list name: **Chittenden, V. H. W** | colony: **Hong Kong** | listed 1930–1940 | editions [1930, 1931, 1932, 1933, 1934, 1936, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1930 | V. H. W. Chittenden | Boatswain | Government Slipway | — | — |
| 1931 | V. H. W. Chittenden | Boatswain | Government Slipway | — | — |
| 1932 | V. H. W. Chittenden | Boatswain | Government Slipway | — | — |
| 1933 | V. H. W. Chittenden | Boatswain | Government Slipway | — | — |
| 1934 | V. H. W. Chittenden | Boatswain | Government Slipway | — | — |
| 1936 | V. H. W. Chittenden | Boatswain | Government Slipway | — | — |
| 1937 | V. H. W. Chittenden | Boatswain | Government Slipway | — | — |
| 1939 | V. H. W. Chittenden | Boatswain | Government Slipway | — | — |
| 1940 | V. H. W. Chittenden | Boatswain | Government Slipway | — | — |

### Deterministic checks: `chittenden_x_e1873` vs `Chittenden, V. H. W___Hong Kong___1930`

- [PASS] surname_gate: bio 'CHITTENDEN' vs stint 'Chittenden, V. H. W' (exact)
- [PASS] initials: bio ['?'] ~ stint ['V', 'H', 'W']
- [PASS] age_gate: stint starts 1930; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Hong Kong'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1930-1940
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

