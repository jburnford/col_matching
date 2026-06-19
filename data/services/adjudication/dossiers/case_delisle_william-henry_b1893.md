<!-- {"case_id": "case_delisle_william-henry_b1893", "bio_ids": ["delisle_william-henry_b1893"], "stint_ids": ["Delisle, W. H___Leeward Islands___1927", "Delisle, W. H___Leeward Islands___1949"]} -->
# Dossier case_delisle_william-henry_b1893

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 11 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `delisle_william-henry_b1893`

- Printed name: **DELISLE, William Henry**
- Birth year: 1893 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L32205.v` — printed in editions [1948, 1949, 1950, 1951]:**

> DELISLE, William Henry.—b. 1893 ; ed. St. Kitts-Nevis Gram. Sch. ; copyist, registrar's off., 1911 (St. Kitts) ; clk., admin.'s off., 1915 ; ch. clk., P.O., 1920 ; clk., mag. dist. "C", 1921 ; ass't. tariff clk., treas., 1923 ; elec. comsnr., 1928 ; bacteriologist and inspr. of animals, anthrax campaign, Nevis, 1922.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1911 | copyist, registrar's off | — | [1948, 1949, 1950, 1951] |
| 1 | 1915 | clk., admin.'s off | — | [1948, 1949, 1950, 1951] |
| 2 | 1920 | ch. clk., P.O | — | [1948, 1949, 1950, 1951] |
| 3 | 1921 | clk., mag. dist. "C" | — | [1948, 1949, 1950, 1951] |
| 4 | 1922 | bacteriologist and inspr. of animals, anthrax campaign | Nevis | [1948, 1949, 1950, 1951] |
| 5 | 1923 | ass't. tariff clk., treas | — | [1948, 1949, 1950, 1951] |
| 6 | 1928 | elec. comsnr | — | [1948, 1949, 1950, 1951] |

## Candidate stint `Delisle, W. H___Leeward Islands___1927`

- Staff-list name: **Delisle, W. H** | colony: **Leeward Islands** | listed 1927–1928 | editions [1927, 1928]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | W. H. Delisle | Second Clerk | Treasury and Customs | — | — |
| 1928 | W. H. Delisle | Second Clerk | Treasury and Customs | — | — |

### Deterministic checks: `delisle_william-henry_b1893` vs `Delisle, W. H___Leeward Islands___1927`

- [PASS] surname_gate: bio 'DELISLE' vs stint 'Delisle, W. H' (exact)
- [PASS] initials: bio ['W', 'H'] ~ stint ['W', 'H']
- [PASS] age_gate: stint starts 1927, birth 1893 (age 34)
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1927-1928
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Delisle, W. H___Leeward Islands___1949`

- Staff-list name: **Delisle, W. H** | colony: **Leeward Islands** | listed 1949–1950 | editions [1949, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | W. H. Delisle | Electricity Commissioner | Electricity | — | — |
| 1950 | W. H. Delisle | Electricity Commissioner | ELECTRICITY | — | — |

### Deterministic checks: `delisle_william-henry_b1893` vs `Delisle, W. H___Leeward Islands___1949`

- [PASS] surname_gate: bio 'DELISLE' vs stint 'Delisle, W. H' (exact)
- [PASS] initials: bio ['W', 'H'] ~ stint ['W', 'H']
- [PASS] age_gate: stint starts 1949, birth 1893 (age 56)
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
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

