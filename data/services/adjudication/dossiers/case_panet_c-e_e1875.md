<!-- {"case_id": "case_panet_c-e_e1875", "bio_ids": ["panet_c-e_e1875", "panet_e_e1875"], "stint_ids": ["Panet, E___Canada___1877"]} -->
# Dossier case_panet_c-e_e1875

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['panet_e_e1875'] carry a single initial only — the namesake trap applies.
- CONTESTED: stint(s) ['Panet, E___Canada___1877'] have more than one claimant biography in this case.
- Phase 1 found `panet_c-e_e1875` ↔ `Panet, E___Canada___1877` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- Phase 1 found `panet_e_e1875` ↔ `Panet, E___Canada___1877` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).

## Biography `panet_c-e_e1875`

- Printed name: **PANET, C. E**
- Birth year: not printed
- Appears in editions: [1888, 1889, 1890, 1894, 1896, 1897, 1898]

### Verbatim printed entry text (OCR)

**Version `col1888-L35408.v` — printed in editions [1888, 1889, 1890, 1894, 1896, 1897, 1898]:**

> PANET, Colonel C. E.—Deputy minister of militia and defence, Canada, 5th Feb., 1875.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1875 | Deputy minister of militia and defence | Canada | [1888, 1889, 1890, 1894, 1896, 1897, 1898] |

## Biography `panet_e_e1875`

- Printed name: **PANET, E**
- Birth year: not printed
- Appears in editions: [1883, 1886]

### Verbatim printed entry text (OCR)

**Version `col1883-L29011.v` — printed in editions [1883, 1886]:**

> PANET, Lieutenant-Colonel E.—Deputy minister of militia, Canada, 5 Feb., 1875.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1875 | Deputy minister of militia | Canada | [1883, 1886] |

## Candidate stint `Panet, E___Canada___1877`

- Staff-list name: **Panet, E** | colony: **Canada** | listed 1877–1900 | editions [1877, 1878, 1879, 1880, 1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | Lieut.-Col. E. Panet | Deputy Minister | Militia and Defence Department | — | Lt.-Col. |
| 1878 | E. Panet | Deputy Minister | Militia and Defence Department | — | Lieut.-Col. |
| 1879 | E. Panet | Deputy Minister | Militia and Defence Department | — | Lieut.-Col. |
| 1880 | E. Panet | Deputy Minister | Militia and Defence Department | — | Lieut.-Col. |
| 1883 | E. Panet | Deputy Minister | Militia and Defence Department | — | Lieut.-Col. |
| 1886 | E. Panet | Deputy Minister | Militia and Defence | — | Lt.-Col. |
| 1888 | E. Panet | Deputy Minister | Department of Militia and Defence | — | Colonel |
| 1889 | Col. E. Panet | Deputy Minister | Department of Militia and Defence | — | Colonel |
| 1890 | E. Panet | Deputy Minister | Department of Militia and Defence | — | Colonel |
| 1894 | Col. E. Panet | Deputy Minister | Department of Militia and Defence | — | Colonel |
| 1896 | E. Panet | Deputy Minister | Militia and Defence | — | Colonel |
| 1896 | E. Panet | Deputy Minister | Department of Militia and Defence | — | Colonel |
| 1897 | E. Panet | Deputy Minister | Militia and Defence | — | Colonel |
| 1897 | Panet | Extra Aide-de-Camp | Civil Establishment | — | Lieutenant |
| 1898 | E. Panet | Deputy Minister | Militia and Defence | — | Colonel |
| 1898 | Lieut. Panet | Extra Aide-de-Camp | Lieutenant-Governor | — | — |
| 1899 | E. Panet | Deputy Minister | Department of Militia and Defence | — | Colonel |
| 1900 | Lieut. Panet | Extra Aide-de-Camp | Lieutenant-Governor's Office | — | Lieutenant |

### Deterministic checks: `panet_c-e_e1875` vs `Panet, E___Canada___1877`

- [PASS] surname_gate: bio 'PANET' vs stint 'Panet, E' (exact)
- [PASS] initials: bio ['C', 'E'] ~ stint ['E']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Canada'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1900
- [PASS] position_sim: best 100 vs bar 60: 'Deputy minister of militia and defence' ~ 'Deputy Minister'
- [FAIL] honour: no shared honour
- [PASS] edition_cooccurrence: 2 agreeing edition-year(s) [1888, 1889] pos~100 (bar: >=2)
- [PASS] place_inherited: at least one supporting event names its place in print

### Deterministic checks: `panet_e_e1875` vs `Panet, E___Canada___1877`

- [PASS] surname_gate: bio 'PANET' vs stint 'Panet, E' (exact)
- [PASS] initials: bio ['E'] ~ stint ['E']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Canada'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1900
- [PASS] position_sim: best 100 vs bar 60: 'Deputy minister of militia' ~ 'Deputy Minister'
- [FAIL] honour: no shared honour
- [PASS] edition_cooccurrence: 2 agreeing edition-year(s) [1883, 1886] pos~100 (bar: >=2)
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

