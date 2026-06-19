<!-- {"case_id": "case_hannam_willoughby_e1860", "bio_ids": ["hannam_willoughby_e1860"], "stint_ids": ["Hannam, Willoughby___Queensland___1886"]} -->
# Dossier case_hannam_willoughby_e1860

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['hannam_willoughby_e1860'] carry a single initial only — the namesake trap applies.

## Biography `hannam_willoughby_e1860`

- Printed name: **HANNAM, WILLOUGHBY**
- Birth year: not printed
- Honours: M.I.C.E
- Appears in editions: [1890, 1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907]

### Verbatim printed entry text (OCR)

**Version `col1890-L34584.v` — printed in editions [1890, 1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907]:**

> HANNAM, WILLOUGHBY, M.I.C.E.—Apprentice to M. Du Bays, C.E., Reading; asst. surveyor, Melbourne and River Murray Rly., Victoria, 1860; engineer Moreton Bay Tramway Co., Brisbane, 1861-63; district engineer (southern dist.) Queensland Govt. Rlys., 1863-8; contractor's engineer on same, 1868-72; district engineer and in charge of surveys, Central Divn., Queensland Rlys., 1872-55; chief engineer, northern divn., 1886; has been engaged on survey of 1,060 miles of rly., and directed survey of 250 miles more.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1860 | asst. surveyor, Melbourne and River Murray Rly. | Victoria | [1890, 1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907] |
| 1 | 1861–1863 | engineer Moreton Bay Tramway Co., Brisbane | Victoria *(inherited from previous clause)* | [1890, 1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907] |
| 2 | 1863–1868 | district engineer (southern dist.) Queensland Govt. Rlys | Victoria *(inherited from previous clause)* | [1890, 1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907] |
| 3 | 1868–1872 | contractor's engineer on same | Victoria *(inherited from previous clause)* | [1890, 1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907] |
| 4 | 1872–1855 | district engineer and in charge of surveys, Central Divn., Queensland Rlys | Queensland | [1890, 1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907] |
| 5 | 1886 | chief engineer, northern divn | Queensland *(inherited from previous clause)* | [1890, 1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907] |

## Candidate stint `Hannam, Willoughby___Queensland___1886`

- Staff-list name: **Hannam, Willoughby** | colony: **Queensland** | listed 1886–1889 | editions [1886, 1888, 1889]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1886 | W. Hannam | Chief Engineer, Carpentaria and Cook Division | Department of Public Works | — | — |
| 1888 | Willoughby Hannam | Chief Engineer, Northern and Carpentaria and Cook Railways | Public Works and Mines | — | — |
| 1889 | Willoughby Hannam | Chief Engineer, Northern and Carpentaria and Cook Railways | Department of Mines and Works | — | — |

### Deterministic checks: `hannam_willoughby_e1860` vs `Hannam, Willoughby___Queensland___1886`

- [PASS] surname_gate: bio 'HANNAM' vs stint 'Hannam, Willoughby' (exact)
- [PASS] initials: bio ['W'] ~ stint ['W']
- [PASS] age_gate: stint starts 1886; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Queensland'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1886-1889
- [PASS] position_sim: best 90 vs bar 60: 'chief engineer, northern divn' ~ 'Chief Engineer, Northern and Carpentaria and Cook Railways'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
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

