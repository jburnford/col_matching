<!-- {"case_id": "case_browning_sydney_e1893", "bio_ids": ["browning_sydney_e1893"], "stint_ids": ["Browning, J. S___New Zealand___1894", "Browning, S___Uganda___1906"]} -->
# Dossier case_browning_sydney_e1893

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 17 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['browning_sydney_e1893'] carry a single initial only — the namesake trap applies.

## Biography `browning_sydney_e1893`

- Printed name: **BROWNING, SYDNEY**
- Birth year: not printed
- Appears in editions: [1914, 1915, 1917, 1918, 1919, 1920, 1921]

### Verbatim printed entry text (OCR)

**Version `col1914-L44986.v` — printed in editions [1914, 1915, 1917, 1918, 1919, 1920, 1921]:**

> BROWNING, SYDNEY.—Asst. collr. and commissariat offr., Fort Johnston, Nyassaland, 1893-1895; asst. collr., Uganda Prot., 1900; dist. comsrs., 1905; ag. prov. comsrs., 1911 to 1913.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1893–1895 | Asst. collr. and commissariat offr., Fort Johnston, Nyassaland | — | [1914, 1915, 1917, 1918, 1919, 1920, 1921] |
| 1 | 1900 | asst. collr. | Uganda | [1914, 1915, 1917, 1918, 1919, 1920, 1921] |
| 2 | 1905 | dist. comsrs | Uganda *(inherited from previous clause)* | [1914, 1915, 1917, 1918, 1919, 1920, 1921] |
| 3 | 1911–1913 | ag. prov. comsrs | Uganda *(inherited from previous clause)* | [1914, 1915, 1917, 1918, 1919, 1920, 1921] |

## Candidate stint `Browning, J. S___New Zealand___1894`

- Staff-list name: **Browning, J. S** | colony: **New Zealand** | listed 1894–1897 | editions [1894, 1896, 1897]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1894 | J. S. Browning | Commissioner of Crown Lands | Crown Lands Office | — | — |
| 1896 | J. S. Browning | Commissioner of Crown Lands | Lands and Survey Department | — | — |
| 1897 | J. S. Browning | Commissioner of Crown Lands | Lands and Survey Department | — | — |

### Deterministic checks: `browning_sydney_e1893` vs `Browning, J. S___New Zealand___1894`

- [PASS] surname_gate: bio 'BROWNING' vs stint 'Browning, J. S' (exact)
- [PASS] initials: bio ['S'] ~ stint ['J', 'S']
- [PASS] age_gate: stint starts 1894; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'New Zealand'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1894-1897
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Browning, S___Uganda___1906`

- Staff-list name: **Browning, S** | colony: **Uganda** | listed 1906–1920 | editions [1906, 1907, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1919, 1920]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1906 | S. Browning | Collector | Administration | — | — |
| 1907 | S. Browning | Collector | Administration | — | — |
| 1910 | S. Browning | District Commissioner | Administration | — | — |
| 1911 | S. Browning | District Commissioner | Administration | — | — |
| 1912 | S. Browning | District Commissioner | Administration | — | — |
| 1913 | S. Browning | District Commissioner | Administration | — | — |
| 1914 | S. Browning | District Commissioner | Administration | — | — |
| 1915 | S. Browning | District Commissioner | Administration | — | — |
| 1917 | S. Browning | Provincial Commissioner | Administration | — | — |
| 1919 | S. Browning | Provincial Commissioner | Civil Establishment | — | — |
| 1920 | S. Browning | Provincial Commissioner | Administration | — | — |

### Deterministic checks: `browning_sydney_e1893` vs `Browning, S___Uganda___1906`

- [PASS] surname_gate: bio 'BROWNING' vs stint 'Browning, S' (exact)
- [PASS] initials: bio ['S'] ~ stint ['S']
- [PASS] age_gate: stint starts 1906; no printed birth year — UNCHECKED
- [PASS] colony: 3 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1906-1920
- [PASS] position_sim: best 62 vs bar 60: 'dist. comsrs' ~ 'District Commissioner'
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

