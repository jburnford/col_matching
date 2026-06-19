<!-- {"case_id": "case_page_arthur-geo_e1879", "bio_ids": ["page_arthur-geo_e1879"], "stint_ids": ["Page, A. G___Cyprus___1905", "Page, A. G___Gold Coast___1949"]} -->
# Dossier case_page_arthur-geo_e1879

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 34 official(s) with this surname in the graph's staff lists; 15 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `page_arthur-geo_e1879`

- Printed name: **PAGE, Arthur Geo**
- Birth year: not printed
- Appears in editions: [1894, 1896, 1897, 1898]

### Verbatim printed entry text (OCR)

**Version `col1894-L33346.v` — printed in editions [1894, 1896, 1897, 1898]:**

> PAGE, Arthur Geo.—Clerk to judicial commissioner, Cyprus, Dec., 1879; ag. regtr., High Ct. of Justice, Feb., 1882; asst. regtr. sup. ct., and clerk to the judges, Mar., 1883.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1879 | Clerk to judicial commissioner | Cyprus | [1894, 1896, 1897, 1898] |
| 1 | 1882 | ag. regtr., High Ct. of Justice | Cyprus *(inherited from previous clause)* | [1894, 1896, 1897, 1898] |
| 2 | 1883 | asst. regtr. sup. ct., and clerk to the judges | Cyprus *(inherited from previous clause)* | [1894, 1896, 1897, 1898] |

## Candidate stint `Page, A. G___Cyprus___1905`

- Staff-list name: **Page, A. G** | colony: **Cyprus** | listed 1905–1908 | editions [1905, 1906, 1907, 1908]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | A. G. Page | 1st Class Clerk | Office of the Chief Secretary to Government. | — | — |
| 1906 | A. G. Page | 1st Class Clerk | Office of the Chief Secretary to Government | — | — |
| 1907 | A. G. Page | 1st Class Clerk | Office of the Chief Secretary to Government | — | — |
| 1908 | A. G. Page | Commissioner | Kyrenia District Administration | — | — |

### Deterministic checks: `page_arthur-geo_e1879` vs `Page, A. G___Cyprus___1905`

- [PASS] surname_gate: bio 'PAGE' vs stint 'Page, A. G' (exact)
- [PASS] initials: bio ['A', 'G'] ~ stint ['A', 'G']
- [PASS] age_gate: stint starts 1905; no printed birth year — UNCHECKED
- [PASS] colony: 3 placed event(s) resolve to 'Cyprus'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1908
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Page, A. G___Gold Coast___1949`

- Staff-list name: **Page, A. G** | colony: **Gold Coast** | listed 1949–1950 | editions [1949, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | A. G. Page | Education Officer | Education | — | — |
| 1950 | A. G. Page | Education Officers | Education | — | — |

### Deterministic checks: `page_arthur-geo_e1879` vs `Page, A. G___Gold Coast___1949`

- [PASS] surname_gate: bio 'PAGE' vs stint 'Page, A. G' (exact)
- [PASS] initials: bio ['A', 'G'] ~ stint ['A', 'G']
- [PASS] age_gate: stint starts 1949; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Gold Coast'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1950
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

