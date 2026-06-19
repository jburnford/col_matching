<!-- {"case_id": "case_pittman_edward-fisher_b1849", "bio_ids": ["pittman_edward-fisher_b1849"], "stint_ids": ["Pittman, E. F___New South Wales___1880", "Pittman, E. F___New South Wales___1898"]} -->
# Dossier case_pittman_edward-fisher_b1849

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `pittman_edward-fisher_b1849`

- Printed name: **PITTMAN, EDWARD FISHER**
- Birth year: 1849 (attested in editions [1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921])
- Appears in editions: [1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921]

### Verbatim printed entry text (OCR)

**Version `col1909-L49028.v` — printed in editions [1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921]:**

> PITTMAN, EDWARD FISHER, A.R.S.M.—B. 1849; entd. mines dept., N.S. Wales, 1877; held positions of mining survr., geological survr., and chief mining survr.; lecr. in mining at Sydney Univ., 1893-1902; under-sec. for mines, N.S. Wales since Sept., 1902, and govt. geologist since Sept., 1901; author of “The Mineral Resources of New South Wales,” 1901, and many geological reports and papers.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1877 | mines dept. | New South Wales | [1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921] |
| 1 | 1893–1902 | lecr. in mining | — | [1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921] |
| 2 | 1901 | govt. geologist | — | [1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921] |
| 3 | 1902 | under-sec. for mines | New South Wales | [1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921] |
| 4 | ? | mining survr., geological survr., and chief mining survr. | — | [1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921] |

## Candidate stint `Pittman, E. F___New South Wales___1880`

- Staff-list name: **Pittman, E. F** | colony: **New South Wales** | listed 1880–1886 | editions [1880, 1886]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1880 | E. F. Pittman | Geological Surveyor | Department of Mines | — | — |
| 1886 | E. F. Pittman | Chief Mining Surveyor | Department of Mines | — | — |

### Deterministic checks: `pittman_edward-fisher_b1849` vs `Pittman, E. F___New South Wales___1880`

- [PASS] surname_gate: bio 'PITTMAN' vs stint 'Pittman, E. F' (exact)
- [PASS] initials: bio ['E', 'F'] ~ stint ['E', 'F']
- [PASS] age_gate: stint starts 1880, birth 1849 (age 31)
- [PASS] colony: 2 placed event(s) resolve to 'New South Wales'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1880-1886
- [FAIL] position_sim: best 39 vs bar 60: 'mines dept.' ~ 'Chief Mining Surveyor'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Pittman, E. F___New South Wales___1898`

- Staff-list name: **Pittman, E. F** | colony: **New South Wales** | listed 1898–1906 | editions [1898, 1899, 1905, 1906]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1898 | E. F. Pittman | Government Geologist and Chief Mining Surveyor | Mines and Agriculture and Subordinate Departments | — | — |
| 1899 | E. F. Pittman | Government Geologist and Chief Mining Surveyor | Mines and Agriculture and Subordinate Departments | — | — |
| 1905 | E. F. Pittman | Under Secretary and Government Geologist | Mines and Agriculture | — | — |
| 1906 | E. F. Pittman | Under Secretary and Government Geologist | Mines and Agriculture | — | — |

### Deterministic checks: `pittman_edward-fisher_b1849` vs `Pittman, E. F___New South Wales___1898`

- [PASS] surname_gate: bio 'PITTMAN' vs stint 'Pittman, E. F' (exact)
- [PASS] initials: bio ['E', 'F'] ~ stint ['E', 'F']
- [PASS] age_gate: stint starts 1898, birth 1849 (age 49)
- [PASS] colony: 2 placed event(s) resolve to 'New South Wales'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1898-1906
- [FAIL] position_sim: best 38 vs bar 60: 'under-sec. for mines' ~ 'Under Secretary and Government Geologist'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
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

