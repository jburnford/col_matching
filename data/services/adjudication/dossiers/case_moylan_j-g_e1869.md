<!-- {"case_id": "case_moylan_j-g_e1869", "bio_ids": ["moylan_j-g_e1869", "moylan_j-g_e1875"], "stint_ids": ["Moylan, J. G___Canada___1877"]} -->
# Dossier case_moylan_j-g_e1869

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Moylan, J. G___Canada___1877'] have more than one claimant biography in this case.
- Phase 1 found `moylan_j-g_e1869` ↔ `Moylan, J. G___Canada___1877` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- Phase 1 found `moylan_j-g_e1875` ↔ `Moylan, J. G___Canada___1877` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).

## Biography `moylan_j-g_e1869`

- Printed name: **MOYLAN, J. G**
- Birth year: not printed
- Appears in editions: [1886, 1889, 1890, 1894, 1896, 1897, 1898, 1899]

### Verbatim printed entry text (OCR)

**Version `col1889-L34744.v` — printed in editions [1889, 1890, 1894, 1896, 1897, 1898, 1899]:**

> MOYLAN, J. G.—Commissioner of emigration from Canada to Ireland, 1869-72; director of penitentiaries, Canada, 1872; inspector of penitentiaries, 1875.

**Version `col1886-L34925.v` — printed in editions [1886]:**

> MOYLAN, J. G.—Inspector of penitentiaries, Canada, 1st November, 1875.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1869–1872 | Commissioner of emigration from Canada to Ireland | — | [1889, 1890, 1894, 1896, 1897, 1898, 1899] |
| 1 | 1872 | director of penitentiaries | Canada | [1889, 1890, 1894, 1896, 1897, 1898, 1899] |
| 2 | 1875 | inspector of penitentiaries | Canada | [1886, 1889, 1890, 1894, 1896, 1897, 1898, 1899] |

## Biography `moylan_j-g_e1875`

- Printed name: **MOYLAN, J. G**
- Birth year: not printed
- Appears in editions: [1883, 1888]

### Verbatim printed entry text (OCR)

**Version `col1883-L28785.v` — printed in editions [1883, 1888]:**

> MOYLAN, J. G.—Inspector of penitentiaries, Canada, 1st Nov., 1875.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1875 | Inspector of penitentiaries | Canada | [1883, 1888] |

## Candidate stint `Moylan, J. G___Canada___1877`

- Staff-list name: **Moylan, J. G** | colony: **Canada** | listed 1877–1896 | editions [1877, 1878, 1879, 1880, 1883, 1886, 1888, 1889, 1890, 1894, 1896]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | J. G. Moylan | Director of Penitentiaries | DEPARTMENT OF JUSTICE | — | — |
| 1878 | J. G. Moylan | Inspector of Penitentiaries | Department of Justice | — | — |
| 1879 | J. G. Moylan | Inspector of Penitentiaries | Department of Justice | — | — |
| 1880 | J. G. Moylan | Inspector of Penitentiaries | Department of Justice | — | — |
| 1883 | J. G. Moylan | Inspector of Penitentiaries | Department of Justice | — | — |
| 1886 | J. G. Moylan | Inspector of Penitentiaries | Department of Justice | — | — |
| 1888 | J. G. Moylan | Inspector of Penitentiaries | Department of Justice | — | — |
| 1889 | J. G. Moylan | Inspector of Penitentiaries | Department of Justice | — | — |
| 1890 | J. G. Moylan | Inspector of Penitentiaries | Department of Justice | — | — |
| 1894 | J. G. Moylan | Inspector of Penitentiaries | Department of Justice | — | — |
| 1896 | J. G. Moylan | Inspector of Penitentiaries | Department of Justice | — | — |

### Deterministic checks: `moylan_j-g_e1869` vs `Moylan, J. G___Canada___1877`

- [PASS] surname_gate: bio 'MOYLAN' vs stint 'Moylan, J. G' (exact)
- [PASS] initials: bio ['J', 'G'] ~ stint ['J', 'G']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Canada'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1896
- [PASS] position_sim: best 100 vs bar 60: 'inspector of penitentiaries' ~ 'Inspector of Penitentiaries'
- [FAIL] honour: no shared honour
- [PASS] edition_cooccurrence: 2 agreeing edition-year(s) [1886, 1889] pos~100 (bar: >=2)
- [PASS] place_inherited: at least one supporting event names its place in print

### Deterministic checks: `moylan_j-g_e1875` vs `Moylan, J. G___Canada___1877`

- [PASS] surname_gate: bio 'MOYLAN' vs stint 'Moylan, J. G' (exact)
- [PASS] initials: bio ['J', 'G'] ~ stint ['J', 'G']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Canada'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1896
- [PASS] position_sim: best 100 vs bar 60: 'Inspector of penitentiaries' ~ 'Inspector of Penitentiaries'
- [FAIL] honour: no shared honour
- [PASS] edition_cooccurrence: 2 agreeing edition-year(s) [1883, 1888] pos~100 (bar: >=2)
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

