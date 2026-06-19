<!-- {"case_id": "case_cawthera_alex-bertram_b1897", "bio_ids": ["cawthera_alex-bertram_b1897"], "stint_ids": ["Cawthra, A. B___Gold Coast___1927", "Cawthra, A. B___Gold Coast___1949"]} -->
# Dossier case_cawthera_alex-bertram_b1897

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Cawthra, A. B___Gold Coast___1927` is also gate-compatible with biography(ies) outside this case: ['cawthra_alec-bertram_b1897'] (already linked elsewhere or filtered).
- NOTE: stint `Cawthra, A. B___Gold Coast___1949` is also gate-compatible with biography(ies) outside this case: ['cawthra_alec-bertram_b1897'] (already linked elsewhere or filtered).

## Biography `cawthera_alex-bertram_b1897`

- Printed name: **CAWTHERA, ALEX BERTRAM**
- Birth year: 1897 (attested in editions [1940])
- Appears in editions: [1940]

### Verbatim printed entry text (OCR)

**Version `col1940-L63062.v` — printed in editions [1940]:**

> CAWTHERA, ALEX BERTRAM.—B. 1897; G.P.O., 1912; mily. serv., 1915-21; oh. clk., P. & T., Palestine, 1921; asst. store keeper, P. & T., Gold Coast, 1925; asst. contr., posts, 1935.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1912 | G.P.O | — | [1940] |
| 1 | 1915–1921 | mily. serv | — | [1940] |
| 2 | 1921 | oh. clk., P. & T. | Palestine | [1940] |
| 3 | 1925 | asst. store keeper, P. & T. | Gold Coast | [1940] |
| 4 | 1935 | asst. contr., posts | Gold Coast *(inherited from previous clause)* | [1940] |

## Candidate stint `Cawthra, A. B___Gold Coast___1927`

- Staff-list name: **Cawthra, A. B** | colony: **Gold Coast** | listed 1927–1936 | editions [1927, 1928, 1929, 1930, 1932, 1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | A. B. Cawthra | Assistant Storekeeper | Posts and Telegraphs Department | — | — |
| 1928 | A. B. Cawthra | Assistant Storekeepers | Posts and Telegraphs Department | — | — |
| 1929 | A. B. Cawthra | Assistant Storekeeper | Posts and Telegraphs Department | — | — |
| 1930 | A. B. Cawthra | Assistant Storekeeper | Posts and Telegraphs Department | — | — |
| 1932 | A. B. Cawthra | Assistant Storekeeper | Posts and Telegraphs Department | — | — |
| 1934 | A. B. Cawthra | Assistant Storekeeper | Posts and Telegraphs Department | — | — |
| 1936 | A. B. Cawthra | Surveyor | Posts and Telegraph Department | — | — |

### Deterministic checks: `cawthera_alex-bertram_b1897` vs `Cawthra, A. B___Gold Coast___1927`

- [PASS] surname_gate: bio 'CAWTHERA' vs stint 'Cawthra, A. B' (fuzzy:1)
- [PASS] initials: bio ['A', 'B'] ~ stint ['A', 'B']
- [PASS] age_gate: stint starts 1927, birth 1897 (age 30)
- [PASS] colony: 2 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1927-1936
- [FAIL] position_sim: best 56 vs bar 60: 'asst. store keeper, P. & T.' ~ 'Assistant Storekeepers'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Cawthra, A. B___Gold Coast___1949`

- Staff-list name: **Cawthra, A. B** | colony: **Gold Coast** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | A. B. Cawthra | Senior Assistant Controllers of Posts | Posts and Telegraphs | — | — |
| 1951 | A. B. Cawthra | Controller of Posts | Traffic Branch | — | — |

### Deterministic checks: `cawthera_alex-bertram_b1897` vs `Cawthra, A. B___Gold Coast___1949`

- [PASS] surname_gate: bio 'CAWTHERA' vs stint 'Cawthra, A. B' (fuzzy:1)
- [PASS] initials: bio ['A', 'B'] ~ stint ['A', 'B']
- [PASS] age_gate: stint starts 1949, birth 1897 (age 52)
- [PASS] colony: 2 placed event(s) resolve to 'Gold Coast'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
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

