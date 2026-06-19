<!-- {"case_id": "case_royal_joseph_e1888", "bio_ids": ["royal_joseph_e1888"], "stint_ids": ["Royal, Joseph___Canada___1877", "Royal, Joseph___Canada___1886", "Royal, Joseph___Prince Edward Island___1889"]} -->
# Dossier case_royal_joseph_e1888

## Case context

- 1 biography(ies) and 3 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['royal_joseph_e1888'] carry a single initial only — the namesake trap applies.

## Biography `royal_joseph_e1888`

- Printed name: **ROYAL, JOSEPH**
- Birth year: not printed
- Appears in editions: [1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900]

### Verbatim printed entry text (OCR)

**Version `col1889-L35447.v` — printed in editions [1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900]:**

> ROYAL, THE HON. JOSEPH.—I.A.-gov., N.W. Territories, Canada, 1888-93.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1888–1893 | I.A.-gov., N.W. Territories | Canada | [1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900] |

## Candidate stint `Royal, Joseph___Canada___1877`

- Staff-list name: **Royal, Joseph** | colony: **Canada** | listed 1877–1879 | editions [1877, 1878, 1879]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | J. Royal | Provincial Secretary, Minister of Public Works, and Attorney-General | Executive Council | — | — |
| 1878 | J. Royal | Provincial Secretary, Minister of Public Works, and Attorney-General | Executive Council | — | — |
| 1879 | J. Royal | Provincial Secretary, Minister of Public Works, and Attorney-General | Executive Council | — | — |

### Deterministic checks: `royal_joseph_e1888` vs `Royal, Joseph___Canada___1877`

- [PASS] surname_gate: bio 'ROYAL' vs stint 'Royal, Joseph' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1879
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Royal, Joseph___Canada___1886`

- Staff-list name: **Royal, Joseph** | colony: **Canada** | listed 1886–1888 | editions [1886, 1888]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1886 | J. Royal. | Consular Agents | — | — | — |
| 1886 | Joseph Royal | — | — | — | — |
| 1888 | Joseph Royal | — | — | — | — |

### Deterministic checks: `royal_joseph_e1888` vs `Royal, Joseph___Canada___1886`

- [PASS] surname_gate: bio 'ROYAL' vs stint 'Royal, Joseph' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1886; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Canada'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1886-1888
- [FAIL] position_sim: best 34 vs bar 60: 'I.A.-gov., N.W. Territories' ~ 'Consular Agents'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Royal, Joseph___Prince Edward Island___1889`

- Staff-list name: **Royal, Joseph** | colony: **Prince Edward Island** | listed 1889–1909 | editions [1889, 1909]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1889 | Hon. Joseph Royal | Lieut.-Governor | Seat of Government | — | — |
| 1889 | Hon. Joseph Royal | Lieutenant-Governor | Lieutenant-Governors | — | — |
| 1909 | Joseph Royal | Lieutenant-Governor | Lieutenant-Governors before creation of new Provinces | — | — |

### Deterministic checks: `royal_joseph_e1888` vs `Royal, Joseph___Prince Edward Island___1889`

- [PASS] surname_gate: bio 'ROYAL' vs stint 'Royal, Joseph' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1889; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Prince Edward Island'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1889-1909
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

