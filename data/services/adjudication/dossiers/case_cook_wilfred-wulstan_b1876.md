<!-- {"case_id": "case_cook_wilfred-wulstan_b1876", "bio_ids": ["cook_wilfred-wulstan_b1876"], "stint_ids": ["Cook, W. W___New Zealand___1918"]} -->
# Dossier case_cook_wilfred-wulstan_b1876

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 55 official(s) with this surname in the graph's staff lists; 21 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `cook_wilfred-wulstan_b1876`

- Printed name: **COOK, WILFRED WULSTAN**
- Birth year: 1876 (attested in editions [1928, 1930, 1931, 1932])
- Appears in editions: [1928, 1930, 1931, 1932]

### Verbatim printed entry text (OCR)

**Version `col1928-L65180.v` — printed in editions [1928, 1930, 1931, 1932]:**

> COOK, WILFRED WULSTAN.—B. 1876; est. reglar.-gen.'s dept., New Zealand, 1895; ch. clk. and dep. reglar.-gen., 1906; reglar.-gen., 1916.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1895 | est. reglar.-gen.'s dept. | New Zealand | [1928, 1930, 1931, 1932] |
| 1 | 1906 | ch. clk. and dep. reglar.-gen | New Zealand *(inherited from previous clause)* | [1928, 1930, 1931, 1932] |
| 2 | 1916 | reglar.-gen | New Zealand *(inherited from previous clause)* | [1928, 1930, 1931, 1932] |

## Candidate stint `Cook, W. W___New Zealand___1918`

- Staff-list name: **Cook, W. W** | colony: **New Zealand** | listed 1918–1922 | editions [1918, 1920, 1922]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1918 | W. W. Cook | Registrar-General of Births, Deaths, and Marriages | Registrar-General's Office | — | — |
| 1920 | W. W. Cook | Registrar-General of Births, Deaths, and Marriages | Registrar-General's Office | — | — |
| 1922 | W. W. Cook | Registrar-General of Births, Deaths, and Marriages | Registrar-General's Office | — | — |

### Deterministic checks: `cook_wilfred-wulstan_b1876` vs `Cook, W. W___New Zealand___1918`

- [PASS] surname_gate: bio 'COOK' vs stint 'Cook, W. W' (exact)
- [PASS] initials: bio ['W', 'W'] ~ stint ['W', 'W']
- [PASS] age_gate: stint starts 1918, birth 1876 (age 42)
- [PASS] colony: 3 placed event(s) resolve to 'New Zealand'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1918-1922
- [FAIL] position_sim: best 29 vs bar 60: 'reglar.-gen' ~ 'Registrar-General of Births, Deaths, and Marriages'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

