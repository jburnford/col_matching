<!-- {"case_id": "case_telfer_elizabeth-wilson_b1895", "bio_ids": ["telfer_elizabeth-wilson_b1895"], "stint_ids": ["Telfer, E. W___Gold Coast___1927", "Telfer, Miss E. W___Gold Coast___1929", "Telfer, W___Gold Coast___1914"]} -->
# Dossier case_telfer_elizabeth-wilson_b1895

## Case context

- 1 biography(ies) and 3 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `telfer_elizabeth-wilson_b1895`

- Printed name: **TELFER, ELIZABETH WILSON**
- Birth year: 1895 (attested in editions [1927, 1928, 1929, 1930, 1931, 1932, 1933])
- Appears in editions: [1927, 1928, 1929, 1930, 1931, 1932, 1933]

### Verbatim printed entry text (OCR)

**Version `col1927-L63241.v` — printed in editions [1927, 1928, 1929, 1930, 1931, 1932, 1933]:**

> TELFER, ELIZABETH WILSON.—B. 1895; headmistress, govt. girls' schl., Accra, Gold Coast, 1st Oct., 1924.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1924 | headmistress, govt. girls' schl., Accra | Gold Coast | [1927, 1928, 1929, 1930, 1931, 1932, 1933] |

## Candidate stint `Telfer, E. W___Gold Coast___1927`

- Staff-list name: **Telfer, E. W** | colony: **Gold Coast** | listed 1927–1928 | editions [1927, 1928]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | E. W. Telfer | Head Mistress | Education Department | — | — |
| 1928 | Miss E. W. Telfer | Head Mistresses | Government Primary Schools, Girls | — | — |

### Deterministic checks: `telfer_elizabeth-wilson_b1895` vs `Telfer, E. W___Gold Coast___1927`

- [PASS] surname_gate: bio 'TELFER' vs stint 'Telfer, E. W' (exact)
- [PASS] initials: bio ['E', 'W'] ~ stint ['E', 'W']
- [PASS] age_gate: stint starts 1927, birth 1895 (age 32)
- [PASS] colony: 1 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1927-1928
- [FAIL] position_sim: best 53 vs bar 60: 'headmistress, govt. girls' schl., Accra' ~ 'Head Mistresses'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Telfer, Miss E. W___Gold Coast___1929`

- Staff-list name: **Telfer, Miss E. W** | colony: **Gold Coast** | listed 1929–1932 | editions [1929, 1932]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1929 | Miss E. W. Telfer | Organizer of Infant and Female Education | Education Department | — | — |
| 1932 | Miss E. W. Telfer | Organizers of Infant and Female Education | Education Department | — | — |

### Deterministic checks: `telfer_elizabeth-wilson_b1895` vs `Telfer, Miss E. W___Gold Coast___1929`

- [PASS] surname_gate: bio 'TELFER' vs stint 'Telfer, Miss E. W' (exact)
- [PASS] initials: bio ['E', 'W'] ~ stint ['M', 'E', 'W']
- [PASS] age_gate: stint starts 1929, birth 1895 (age 34)
- [PASS] colony: 1 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1929-1932
- [FAIL] position_sim: best 35 vs bar 60: 'headmistress, govt. girls' schl., Accra' ~ 'Organizers of Infant and Female Education'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Telfer, W___Gold Coast___1914`

- Staff-list name: **Telfer, W** | colony: **Gold Coast** | listed 1914–1919 | editions [1914, 1915, 1917, 1918, 1919]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1914 | W. Telfer | Medical Officer | Medical Department | — | — |
| 1915 | W. Telfer | Medical Officer | Medical Department | — | — |
| 1917 | W. Telfer | Medical Officer | Medical Department | — | — |
| 1918 | W. Telfer | Medical Officer | Medical Department | — | — |
| 1919 | W. Telfer | Medical Officer | Medical Department | — | — |

### Deterministic checks: `telfer_elizabeth-wilson_b1895` vs `Telfer, W___Gold Coast___1914`

- [PASS] surname_gate: bio 'TELFER' vs stint 'Telfer, W' (exact)
- [PASS] initials: bio ['E', 'W'] ~ stint ['W']
- [PASS] age_gate: stint starts 1914, birth 1895 (age 19)
- [PASS] colony: 1 placed event(s) resolve to 'Gold Coast'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1914-1919
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

