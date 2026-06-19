<!-- {"case_id": "case_roberts_philip-hamer_e1901", "bio_ids": ["roberts_philip-hamer_e1901"], "stint_ids": ["Roberts, P. H___Gold Coast___1912", "Roberts, P. H___Gold Coast___1927"]} -->
# Dossier case_roberts_philip-hamer_e1901

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 150 official(s) with this surname in the graph's staff lists; 67 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `roberts_philip-hamer_e1901`

- Printed name: **ROBERTS, PHILIP HAMER**
- Birth year: not printed
- Appears in editions: [1912, 1913, 1914, 1915, 1917, 1918, 1919, 1921, 1922, 1923, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1912-L47218.v` — printed in editions [1912, 1913, 1914, 1915, 1917, 1918, 1919, 1921, 1922, 1923, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1939, 1940]:**

> ROBERTS, PHILIP HAMER.—Prison offr., Br. Guiana, 19th Nov., 1901; served penal settltm., Massaruni, and at Essequibo and Georgetown county prisons; clerical astt., Georgetown and Essequibo prisons; gaoler, G. Coast, 5th Mar., 1911; keeper, James Fort prison, 1st June, 1911.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1901 | Prison offr. | British Guiana | [1912, 1913, 1914, 1915, 1917, 1918, 1919, 1921, 1922, 1923, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1939, 1940] |
| 1 | 1911 | gaoler, G. Coast | British Guiana *(inherited from previous clause)* | [1912, 1913, 1914, 1915, 1917, 1918, 1919, 1921, 1922, 1923, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1939, 1940] |

## Candidate stint `Roberts, P. H___Gold Coast___1912`

- Staff-list name: **Roberts, P. H** | colony: **Gold Coast** | listed 1912–1917 | editions [1912, 1913, 1915, 1917]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | P. H. Roberts | West Indian Gaoler | Prisons Department | — | — |
| 1913 | P. H. Roberts | West Indian Gaoler | Prisons Department | — | — |
| 1915 | P. H. Roberts | West Indian Gaoler | Prisons Department | — | — |
| 1917 | P. H. Roberts | West Indian Gaoler | Prisons Department | — | — |

### Deterministic checks: `roberts_philip-hamer_e1901` vs `Roberts, P. H___Gold Coast___1912`

- [PASS] surname_gate: bio 'ROBERTS' vs stint 'Roberts, P. H' (exact)
- [PASS] initials: bio ['P', 'H'] ~ stint ['P', 'H']
- [PASS] age_gate: stint starts 1912; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Gold Coast'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1917
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Roberts, P. H___Gold Coast___1927`

- Staff-list name: **Roberts, P. H** | colony: **Gold Coast** | listed 1927–1930 | editions [1927, 1928, 1929, 1930]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | P. H. Roberts | Assistant Prison Superintendent | Prisons Department | — | — |
| 1928 | P. H. Roberts | Assistant Prison Superintendent | Prisons Department | — | — |
| 1929 | P. H. Roberts | Assistant Prison Superintendent | Prisons Department | — | — |
| 1930 | P. H. Roberts | Assistant Prison Superintendent | Prisons Department | — | — |

### Deterministic checks: `roberts_philip-hamer_e1901` vs `Roberts, P. H___Gold Coast___1927`

- [PASS] surname_gate: bio 'ROBERTS' vs stint 'Roberts, P. H' (exact)
- [PASS] initials: bio ['P', 'H'] ~ stint ['P', 'H']
- [PASS] age_gate: stint starts 1927; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Gold Coast'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1927-1930
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

