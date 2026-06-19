<!-- {"case_id": "case_norquay_j_e1878", "bio_ids": ["norquay_j_e1878", "norquay_j_e1878-2"], "stint_ids": ["Norquay, John___Canada___1880"]} -->
# Dossier case_norquay_j_e1878

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['norquay_j_e1878', 'norquay_j_e1878-2'] carry a single initial only — the namesake trap applies.
- CONTESTED: stint(s) ['Norquay, John___Canada___1880'] have more than one claimant biography in this case.
- Phase 1 found `norquay_j_e1878` ↔ `Norquay, John___Canada___1880` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- Phase 1 found `norquay_j_e1878-2` ↔ `Norquay, John___Canada___1880` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).

## Biography `norquay_j_e1878`

- Printed name: **NORQUAY, J**
- Birth year: not printed
- Appears in editions: [1883, 1886]

### Verbatim printed entry text (OCR)

**Version `col1883-L28881.v` — printed in editions [1883, 1886]:**

> NORQUAY, HON. J.—Provincial treasurer and premier, province of Manitoba, Canada, June, 1878.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1878 | Provincial treasurer and premier, province of Manitoba | Canada | [1883, 1886] |

## Biography `norquay_j_e1878-2`

- Printed name: **NORQUAY, J**
- Birth year: not printed
- Appears in editions: [1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909]

### Verbatim printed entry text (OCR)

**Version `col1888-L35272.v` — printed in editions [1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909]:**

> NORQUAY, Hon. J.—Provincial treasurer and premier, province of Manitoba, Canada, June, 1878; railway commissioner and premier until Dec., 1887.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1878 | Provincial treasurer and premier, province of Manitoba | Canada | [1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909] |
| 1 | 1887 | railway commissioner and premier until | Canada *(inherited from previous clause)* | [1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909] |

## Candidate stint `Norquay, John___Canada___1880`

- Staff-list name: **Norquay, John** | colony: **Canada** | listed 1880–1888 | editions [1880, 1883, 1886, 1888]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1880 | J. Norquay | Provincial Secretary (Premier) | Executive Council | — | — |
| 1883 | J. Norquay | Provincial Treasurer (Premier) | Executive Council | — | — |
| 1886 | Hon. J. Norquay | Provincial Treasurer (Premier) | Executive Council | — | — |
| 1888 | John Norquay | Member for St. Andrew's Norquay | Legislative Assembly | — | — |

### Deterministic checks: `norquay_j_e1878` vs `Norquay, John___Canada___1880`

- [PASS] surname_gate: bio 'NORQUAY' vs stint 'Norquay, John' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1880; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Canada'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1880-1888
- [PASS] position_sim: best 100 vs bar 60: 'Provincial treasurer and premier, province of Manitoba' ~ 'Provincial Treasurer (Premier)'
- [FAIL] honour: no shared honour
- [PASS] edition_cooccurrence: 2 agreeing edition-year(s) [1883, 1886] pos~100 (bar: >=2)
- [PASS] place_inherited: at least one supporting event names its place in print

### Deterministic checks: `norquay_j_e1878-2` vs `Norquay, John___Canada___1880`

- [PASS] surname_gate: bio 'NORQUAY' vs stint 'Norquay, John' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1880; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Canada'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1880-1888
- [PASS] position_sim: best 100 vs bar 60: 'Provincial treasurer and premier, province of Manitoba' ~ 'Provincial Treasurer (Premier)'
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

