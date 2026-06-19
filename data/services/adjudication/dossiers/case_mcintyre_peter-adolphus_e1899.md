<!-- {"case_id": "case_mcintyre_peter-adolphus_e1899", "bio_ids": ["mcintyre_peter-adolphus_e1899"], "stint_ids": ["McIntyre, Peter A___Canada___1877"]} -->
# Dossier case_mcintyre_peter-adolphus_e1899

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 26 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mcintyre_peter-adolphus_e1899`

- Printed name: **McINTYRE, PETER ADOLPHUS**
- Birth year: not printed
- Appears in editions: [1905, 1906, 1908, 1909]

### Verbatim printed entry text (OCR)

**Version `col1905-L44644.v` — printed in editions [1905, 1906, 1908, 1909]:**

> McINTYRE, PETER ADOLPHUS, M.D.—Lieut. govt., Prince Edward Island, Canada, 23rd May, 1899.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1899 | Lieut. govt., Prince Edward Island | Canada | [1905, 1906, 1908, 1909] |

## Candidate stint `McIntyre, Peter A___Canada___1877`

- Staff-list name: **McIntyre, Peter A** | colony: **Canada** | listed 1877–1922 | editions [1877, 1878, 1879, 1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897, 1898, 1900, 1905, 1906, 1907, 1912, 1914, 1915, 1917, 1918, 1920, 1922]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | P. McIntyre | Bishop of Charlottetown | Province of Prince Edward Island | — | — |
| 1878 | P. McIntyre | Bishop of Charlottetown | Province of Prince Edward Island | — | — |
| 1879 | P. McIntyre | Bishop of Charlottetown | Province of Prince Edward Island | — | — |
| 1883 | Peter A. McIntyre | Member | — | — | — |
| 1883 | P. McIntyre | Bishop of Charlottetown | Province of Prince Edward Island | — | — |
| 1883 | P. McIntyre | Bishop of Charlottetown | Ecclesiastical | — | — |
| 1886 | P. McIntyre | Bishop of Charlottetown | — | — | — |
| 1886 | P. McIntyre | Bishop of Charlottetown (R.C.), Rt. Rev. | Ecclesiastical | — | — |
| 1886 | Peter A. McIntyre | — | — | — | — |
| 1888 | Peter A. McIntyre | — | — | — | — |
| 1888 | P. McIntyre | Bishop of Charlottetown (R.C.) | Ecclesiastical | — | — |
| 1888 | P. McIntyre | Bishop of Charlottetown | Province of Prince Edward Island | — | — |
| 1889 | Peter A. McIntyre | Member | — | — | — |
| 1889 | P. McIntyre | Bishop of Charlottetown | Roman Catholic Church | — | — |
| 1890 | Peter A. McIntyre | — | — | — | — |
| 1890 | P. McIntyre | Bishop of Charlottetown | ROMAN CATHOLIC CHURCH. | — | — |
| 1894 | P. C. McIntyre | Member | Members | — | — |
| 1896 | P. C. McIntyre | Member of Legislative Assembly | Legislative Assembly | — | — |
| 1897 | P. C. McIntyre | Member | Members | — | — |
| 1898 | P. C. McIntyre | Member | Legislative Assembly | — | — |
| 1905 | Peter A. McIntyre | Esq. | — | — | — |

### Deterministic checks: `mcintyre_peter-adolphus_e1899` vs `McIntyre, Peter A___Canada___1877`

- [PASS] surname_gate: bio 'McINTYRE' vs stint 'McIntyre, Peter A' (exact)
- [PASS] initials: bio ['P', 'A'] ~ stint ['P', 'A']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Canada'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1922
- [FAIL] position_sim: best 36 vs bar 60: 'Lieut. govt., Prince Edward Island' ~ 'Member of Legislative Assembly'
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

