<!-- {"case_id": "case_simpson_archibald-henry_b1843", "bio_ids": ["simpson_archibald-henry_b1843"], "stint_ids": ["Simpson, A. H___Sarawak___1962", "Simpson, H___Palestine___1921"]} -->
# Dossier case_simpson_archibald-henry_b1843

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 73 official(s) with this surname in the graph's staff lists; 29 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Simpson, A. H___Sarawak___1962` is also gate-compatible with biography(ies) outside this case: ['simpson_a-h_b1914'] (already linked elsewhere or filtered).

## Biography `simpson_archibald-henry_b1843`

- Printed name: **SIMPSON, ARCHIBALD HENRY**
- Birth year: 1843 (attested in editions [1909, 1910, 1911, 1912, 1913, 1914, 1915, 1918])
- Appears in editions: [1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918]

### Verbatim printed entry text (OCR)

**Version `col1909-L49612.v` — printed in editions [1909, 1910, 1911, 1912, 1913, 1914, 1915, 1918]:**

> SIMPSON, ARCHIBALD HENRY, M.A.—B. 1843; chf. judge in equity, N.S. Wales, 1896.

**Version `col1917-L53151.v` — printed in editions [1917]:**

> SIMPSON, Archibald Henry, M.A.—B. 1843; chf. judge in equity, N.S. Wales, 1896.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1896 | chf. judge in equity, N.S. Wales | Nova Scotia | [1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918] |

## Candidate stint `Simpson, A. H___Sarawak___1962`

- Staff-list name: **Simpson, A. H** | colony: **Sarawak** | listed 1962–1963 | editions [1962, 1963]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1962 | A. H. Simpson | Puisne Judges | Judiciary | — | — |
| 1963 | A. H. Simpson | Puisne Judge | Judiciary | — | — |

### Deterministic checks: `simpson_archibald-henry_b1843` vs `Simpson, A. H___Sarawak___1962`

- [PASS] surname_gate: bio 'SIMPSON' vs stint 'Simpson, A. H' (exact)
- [PASS] initials: bio ['A', 'H'] ~ stint ['A', 'H']
- [PASS] age_gate: stint starts 1962, birth 1843 (age 119)
- [FAIL] colony: no placed event resolves to 'Sarawak'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1962-1963
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Simpson, H___Palestine___1921`

- Staff-list name: **Simpson, H** | colony: **Palestine** | listed 1921–1932 | editions [1921, 1923, 1925, 1927, 1928, 1929, 1930, 1931, 1932]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1921 | H. Simpson | District Traffic Superintendent | Palestine Railways | — | — |
| 1923 | H. Simpson | District Traffic Superintendent | Palestine Railways | — | — |
| 1925 | H. Simpson | District Traffic Superintendent | Palestine Railways | — | — |
| 1927 | H. Simpson | District Traffic Superintendents | Palestine Railways | — | — |
| 1928 | H. Simpson | District Traffic Superintendents | Palestine Railways | — | — |
| 1929 | H. Simpson | District Traffic Superintendent | Palestine Railways | — | — |
| 1930 | H. Simpson | District Traffic Superintendents | Palestine Railways | — | — |
| 1931 | H. Simpson | District Traffic Superintendents | Palestine Railways | — | — |
| 1932 | H. Simpson | District Traffic Superintendent | Palestine Railways | — | — |

### Deterministic checks: `simpson_archibald-henry_b1843` vs `Simpson, H___Palestine___1921`

- [PASS] surname_gate: bio 'SIMPSON' vs stint 'Simpson, H' (exact)
- [PASS] initials: bio ['A', 'H'] ~ stint ['H']
- [PASS] age_gate: stint starts 1921, birth 1843 (age 78)
- [FAIL] colony: no placed event resolves to 'Palestine'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1921-1932
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

