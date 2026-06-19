<!-- {"case_id": "case_johns_harold-thomas-smedley_b1889", "bio_ids": ["johns_harold-thomas-smedley_b1889"], "stint_ids": ["Johns, H. T. S___Leeward Islands___1906", "Johns, H___Dominica___1909"]} -->
# Dossier case_johns_harold-thomas-smedley_b1889

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 21 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `johns_harold-thomas-smedley_b1889`

- Printed name: **JOHNS, HAROLD THOMAS SMEDLEY**
- Birth year: 1889 (attested in editions [1912, 1913, 1914, 1915, 1917, 1918, 1919])
- Appears in editions: [1912, 1913, 1914, 1915, 1917, 1918, 1919]

### Verbatim printed entry text (OCR)

**Version `col1912-L45263.v` — printed in editions [1912, 1913, 1914, 1915, 1917, 1918, 1919]:**

> JOHNS, HAROLD THOMAS SMEDLEY.—B., 1889; asst. maist., grammar schl., Dominica, Sept., 1904; ag. head master, April to Sept., 1905; ag. head master and sub-instr. of schools, Feb. to Sept., 1909; govt. offr., treasy., Dominica, Nov., 1910.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1904 | asst. maist., grammar schl. | Dominica | [1912, 1913, 1914, 1915, 1917, 1918, 1919] |
| 1 | 1905 | ag. head master | Dominica *(inherited from previous clause)* | [1912, 1913, 1914, 1915, 1917, 1918, 1919] |
| 2 | 1909 | ag. head master and sub-instr. of schools | Dominica *(inherited from previous clause)* | [1912, 1913, 1914, 1915, 1917, 1918, 1919] |
| 3 | 1910 | govt. offr., treasy. | Dominica | [1912, 1913, 1914, 1915, 1917, 1918, 1919] |

## Candidate stint `Johns, H. T. S___Leeward Islands___1906`

- Staff-list name: **Johns, H. T. S** | colony: **Leeward Islands** | listed 1906–1919 | editions [1906, 1907, 1908, 1911, 1912, 1914, 1915, 1917, 1918, 1919]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1906 | H. Johns | Assistant Master, Dominica Grammar School | Educational Establishment | — | — |
| 1907 | H. Johns | Assistant Master, Dominica Grammar School | Educational Establishment | — | — |
| 1908 | H. Johns | Assistant Master, Dominica Grammar School | Educational Establishment | — | — |
| 1911 | H. Johns | Head Master | Educational Establishment | — | — |
| 1912 | H. T. S. Johns | Treasury Government Officer | Treasury and Customs | — | — |
| 1914 | H. Johns | Quarantine Officer | Medical Establishment | — | — |
| 1914 | H. Johns | Treasury Government Officers | Treasury and Customs | — | — |
| 1915 | H. Johns | Treasury Government Officers | Treasury and Customs | — | — |
| 1915 | H. Johns | Quarantine Officer | Medical Establishment | — | — |
| 1917 | H. Johns | Treasury Government Officers | Treasury and Customs | — | — |
| 1917 | H. Johns | Quarantine Officers | Medical Establishment | — | — |
| 1918 | H. Johns | Quarantine Officer | Medical Establishment | — | — |
| 1919 | H. Johns | Quarantine Officer (as Treasury Officer) | Medical Establishment | — | — |

### Deterministic checks: `johns_harold-thomas-smedley_b1889` vs `Johns, H. T. S___Leeward Islands___1906`

- [PASS] surname_gate: bio 'JOHNS' vs stint 'Johns, H. T. S' (exact)
- [PASS] initials: bio ['H', 'T', 'S'] ~ stint ['H', 'T', 'S']
- [PASS] age_gate: stint starts 1906, birth 1889 (age 17)
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1906-1919
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Johns, H___Dominica___1909`

- Staff-list name: **Johns, H** | colony: **Dominica** | listed 1909–1910 | editions [1909, 1910]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1909 | H. Johns | Assistant Master, Dominica Grammar School | Educational Establishment | — | — |
| 1910 | H. Johns | Assistant Master | Educational Establishment | — | — |

### Deterministic checks: `johns_harold-thomas-smedley_b1889` vs `Johns, H___Dominica___1909`

- [PASS] surname_gate: bio 'JOHNS' vs stint 'Johns, H' (exact)
- [PASS] initials: bio ['H', 'T', 'S'] ~ stint ['H']
- [PASS] age_gate: stint starts 1909, birth 1889 (age 20)
- [PASS] colony: 4 placed event(s) resolve to 'Dominica'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1909-1910
- [PASS] position_sim: best 60 vs bar 60: 'ag. head master' ~ 'Assistant Master'
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

