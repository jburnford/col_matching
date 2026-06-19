<!-- {"case_id": "case_carfmael_charles_e1872", "bio_ids": ["carfmael_charles_e1872"], "stint_ids": ["Carpmael, C___Canada___1888", "Carpmel, C___Canada___1890"]} -->
# Dossier case_carfmael_charles_e1872

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['carfmael_charles_e1872'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Carpmael, C___Canada___1888` is also gate-compatible with biography(ies) outside this case: ['carpmael_charles_e1872'] (already linked elsewhere or filtered).

## Biography `carfmael_charles_e1872`

- Printed name: **CARFMAEL, CHARLES**
- Birth year: not printed
- Honours: F.R.S.C, M.A
- Appears in editions: [1890]

### Verbatim printed entry text (OCR)

**Version `col1890-L33048.v` — printed in editions [1890]:**

> CARFMAEL, CHARLES, M.A., F.R.S.C., F.R.A.S. (late Fell. St. John's Coll., Camb.).—Deputy superintendent, meteorological service, Canada, Oct., 1872; director, magnetic observatory, Toronto, and superintendent, meteorological service, Feb., 1880.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1872 | Deputy superintendent, meteorological service | Canada | [1890] |
| 1 | 1880 | director, magnetic observatory, Toronto, and superintendent, meteorological service | Canada *(inherited from previous clause)* | [1890] |

## Candidate stint `Carpmael, C___Canada___1888`

- Staff-list name: **Carpmael, C** | colony: **Canada** | listed 1888–1896 | editions [1888, 1889, 1894, 1896]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | C. Carpmael | Superintendent of Meteorological Office and Director of Magnetic Observatory | Marine | — | — |
| 1889 | C. Carpmael | Superintendent of Meteorological Office or Director of Magnetic Observatory | Department of Marine | — | — |
| 1894 | C. Carpmael | Superintendent of Meteorological Office and Director of Magnetic Observatory | Marine and Fisheries | — | — |
| 1896 | C. Carpmael | Superintendent of Meteorological Office and Director of Magnetic Observatory | Department of Marine and Fisheries | — | — |

### Deterministic checks: `carfmael_charles_e1872` vs `Carpmael, C___Canada___1888`

- [PASS] surname_gate: bio 'CARFMAEL' vs stint 'Carpmael, C' (fuzzy:1)
- [PASS] initials: bio ['C'] ~ stint ['C']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Canada'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1888-1896
- [PASS] position_sim: best 93 vs bar 60: 'director, magnetic observatory, Toronto, and superintendent, meteorological service' ~ 'Superintendent of Meteorological Office and Director of Magnetic Observatory'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

## Candidate stint `Carpmel, C___Canada___1890`

- Staff-list name: **Carpmel, C** | colony: **Canada** | listed 1890–1896 | editions [1890, 1896]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1890 | C. Carpmel | Superintendent of Meteorological Office and Director of Magnetic Observatory | Department of Marine | — | — |
| 1896 | C. Carpmel | Superintendent of Meteorological Office and Director of Magnetic Observatory | Marine and Fisheries | — | — |

### Deterministic checks: `carfmael_charles_e1872` vs `Carpmel, C___Canada___1890`

- [PASS] surname_gate: bio 'CARFMAEL' vs stint 'Carpmel, C' (fuzzy:2)
- [PASS] initials: bio ['C'] ~ stint ['C']
- [PASS] age_gate: stint starts 1890; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Canada'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1890-1896
- [PASS] position_sim: best 93 vs bar 60: 'director, magnetic observatory, Toronto, and superintendent, meteorological service' ~ 'Superintendent of Meteorological Office and Director of Magnetic Observatory'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): 1 agreeing edition-year(s) [1890] pos~93 (bar: >=2)
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

