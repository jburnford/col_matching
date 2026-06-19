<!-- {"case_id": "case_mclean_george_e1871", "bio_ids": ["mclean_george_e1871"], "stint_ids": ["McLean, G. D___Leeward Islands___1933", "McLean, G. G___British Guiana___1913"]} -->
# Dossier case_mclean_george_e1871

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 36 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['mclean_george_e1871'] carry a single initial only — the namesake trap applies.

## Biography `mclean_george_e1871`

- Printed name: **McLEAN, GEORGE**
- Birth year: not printed
- Honours: Kt. Bach.
- Appears in editions: [1914, 1915, 1917, 1918]

### Verbatim printed entry text (OCR)

**Version `col1914-L48292.v` — printed in editions [1914, 1915, 1917, 1918]:**

> McLEAN, HON. SIR GEORGE, Kt. Bach.—Mem. of H. of R., New Zealand, 1871-1872 and 1875-1881; comsnr. of customs, July to Oct., 1877; postmr.-gen., Jan. to Oct., 1877; comsnr. of trade and customs, Aug. to Sept., 1884; M.L.C. since 1881.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1871–1872 | Mem. of H. of R. | New Zealand | [1914, 1915, 1917, 1918] |
| 1 | 1875–1881 | Mem. of H. of R. | New Zealand | [1914, 1915, 1917, 1918] |
| 2 | 1877–1877 | comsnr. of customs | — | [1914, 1915, 1917, 1918] |
| 3 | 1877–1877 | postmr.-gen. | — | [1914, 1915, 1917, 1918] |
| 4 | 1881 | M.L.C. | — | [1914, 1915, 1917, 1918] |
| 5 | 1884–1884 | comsnr. of trade and customs | — | [1914, 1915, 1917, 1918] |

## Candidate stint `McLean, G. D___Leeward Islands___1933`

- Staff-list name: **McLean, G. D** | colony: **Leeward Islands** | listed 1933–1951 | editions [1933, 1936, 1939, 1940, 1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | G. D. McLean | Medical Officer, District "D" | Medical Establishment | — | — |
| 1936 | G. D. McLean | Medical Officer, District No. D | Medical | — | — |
| 1939 | G. D. McLean | Medical Officer, Leper Asylum | Hospitals | — | — |
| 1939 | G. D. McLean | Medical Officer | Medical and Sanitary | — | — |
| 1940 | G. D. McLean | Medical Officer, Leper Asylum | Hospitals | — | — |
| 1940 | G. D. McLean | Medical Officer, District No. 4 | Medical and Sanitary | — | — |
| 1949 | G. D. McLean | Medical Officer, District 4 | Health | — | — |
| 1950 | G. D. McLean | Acting Medical Officer of Health | HEALTH | — | — |
| 1950 | G. D. McLean | Acting Medical Officer of Health | Executive Council | — | — |
| 1951 | G. D. McLean | Medical Officer, District 1 | HEALTH | — | — |

### Deterministic checks: `mclean_george_e1871` vs `McLean, G. D___Leeward Islands___1933`

- [PASS] surname_gate: bio 'McLEAN' vs stint 'McLean, G. D' (exact)
- [PASS] initials: bio ['G'] ~ stint ['G', 'D']
- [PASS] age_gate: stint starts 1933; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1933-1951
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `McLean, G. G___British Guiana___1913`

- Staff-list name: **McLean, G. G** | colony: **British Guiana** | listed 1913–1915 | editions [1913, 1914, 1915]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1913 | G. G. McLean | District Engineers | Public Works | — | — |
| 1914 | G. G. McLean | District Engineers | Public Works | — | — |
| 1915 | G. G. McLean | District Engineer | Public Works | — | — |

### Deterministic checks: `mclean_george_e1871` vs `McLean, G. G___British Guiana___1913`

- [PASS] surname_gate: bio 'McLEAN' vs stint 'McLean, G. G' (exact)
- [PASS] initials: bio ['G'] ~ stint ['G', 'G']
- [PASS] age_gate: stint starts 1913; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'British Guiana'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1913-1915
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

