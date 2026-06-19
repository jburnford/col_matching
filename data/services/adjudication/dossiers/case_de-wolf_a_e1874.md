<!-- {"case_id": "case_de-wolf_a_e1874", "bio_ids": ["de-wolf_a_e1874"], "stint_ids": ["De Wolf, J. A___Trinidad and Tobago___1899", "De Wolf, J. A___Trinidad___1877"]} -->
# Dossier case_de-wolf_a_e1874

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['de-wolf_a_e1874'] carry a single initial only — the namesake trap applies.
- NOTE: stint `De Wolf, J. A___Trinidad and Tobago___1899` is also gate-compatible with biography(ies) outside this case: ['de-wolf_jan-a_e1874'] (already linked elsewhere or filtered).
- NOTE: stint `De Wolf, J. A___Trinidad___1877` is also gate-compatible with biography(ies) outside this case: ['de-wolf_jan-a_e1874'] (already linked elsewhere or filtered).

## Biography `de-wolf_a_e1874`

- Printed name: **DE WOLF, A**
- Birth year: not printed
- Appears in editions: [1907]

### Verbatim printed entry text (OCR)

**Version `col1907-L43940.v` — printed in editions [1907]:**

> DE WOLF, A.—Med. visitor of estates, Trinidad, 1st Apr., 1874; dist. med. offr., St. Joseph, 1st Jan., 1876; ditto, Port of Spain North, med. insp. of imigrts., and health offr. of shipping, Aug., 1890; ag. surg.-gen., on several occasions, 1884-1899; surg.-gen., 5th Nov., 1901.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1874 | Med. visitor of estates | Trinidad | [1907] |
| 1 | 1876 | dist. med. offr., St. Joseph | Trinidad *(inherited from previous clause)* | [1907] |
| 2 | 1884–1899 | ag. surg.-gen., on several occasions | Trinidad *(inherited from previous clause)* | [1907] |
| 3 | 1890 | ditto, Port of Spain North, med. insp. of imigrts., and health offr. of shipping | Trinidad *(inherited from previous clause)* | [1907] |
| 4 | 1901 | surg.-gen | Trinidad *(inherited from previous clause)* | [1907] |

## Candidate stint `De Wolf, J. A___Trinidad and Tobago___1899`

- Staff-list name: **De Wolf, J. A** | colony: **Trinidad and Tobago** | listed 1899–1907 | editions [1899, 1900, 1905, 1906, 1907]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1899 | J. A. De Wolf | Health Officer Shipping, Medical Inspector of Immigrants | Government Medical Officers | — | — |
| 1900 | J. A. De Wolf | Health Officer Shipping, Medical Inspector of Immigrants | Government Medical Officers | — | — |
| 1905 | J. A. De Wolf | Surgeon-General and Medical Officer of Health | Medical Establishment | — | — |
| 1906 | J. A. De Wolf | Surgeon-General and Medical Officer of Health | Medical Establishment | — | — |
| 1907 | J. A. De Wolf | Surgeon-General and Medical Officer of Health | Medical Establishment | — | — |

### Deterministic checks: `de-wolf_a_e1874` vs `De Wolf, J. A___Trinidad and Tobago___1899`

- [PASS] surname_gate: bio 'DE WOLF' vs stint 'De Wolf, J. A' (exact)
- [PASS] initials: bio ['A'] ~ stint ['J', 'A']
- [PASS] age_gate: stint starts 1899; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1899-1907
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `De Wolf, J. A___Trinidad___1877`

- Staff-list name: **De Wolf, J. A** | colony: **Trinidad** | listed 1877–1898 | editions [1877, 1878, 1879, 1880, 1886, 1888, 1889, 1890, 1894, 1896, 1897, 1898]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | J. A. De Wolf | Government Medical Officer | Government Medical Officers | — | — |
| 1878 | J. A. De Wolf | Medical Officer | Medical Establishment | — | — |
| 1879 | J. A. De Wolf | St. Joseph's District | Medical Establishment | — | — |
| 1880 | J. A. De Wolf | St. Joseph's District | Government Medical Officers | — | — |
| 1886 | J. A. De Wolf | District Medical Officer, St. Joseph | Government Medical Officers | — | — |
| 1888 | J. A. De Wolf | District Officer | District Officers | — | — |
| 1889 | J. A. De Wolf | District Officer | District Officers | — | — |
| 1890 | J. A. De Wolf | Government Medical Officer | Government Medical Officers | — | — |
| 1894 | J. A. De Wolf | Health Officer, Shipping and Medical Inspector of Immigrants | Government Medical Officers | — | — |
| 1896 | J. A. De Wolf | Health Officer, Shipping and Medical Inspector of Immigrants | Government Medical Officers | — | — |
| 1897 | J. A. De Wolf | Health Officer Shipping, and Medical Inspector of Immigrants | Government Medical Officers | — | — |
| 1898 | J. A. De Wolf | Health Officer Shipping, Medical Inspector of Immigrants | Government Medical Officers | — | — |

### Deterministic checks: `de-wolf_a_e1874` vs `De Wolf, J. A___Trinidad___1877`

- [PASS] surname_gate: bio 'DE WOLF' vs stint 'De Wolf, J. A' (exact)
- [PASS] initials: bio ['A'] ~ stint ['J', 'A']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 5 placed event(s) resolve to 'Trinidad'
- [PASS] tenure_overlap: 4 event tenure(s) overlap stint years 1877-1898
- [PASS] position_sim: best 81 vs bar 60: 'dist. med. offr., St. Joseph' ~ 'District Medical Officer, St. Joseph'
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

