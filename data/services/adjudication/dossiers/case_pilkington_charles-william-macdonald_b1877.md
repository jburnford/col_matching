<!-- {"case_id": "case_pilkington_charles-william-macdonald_b1877", "bio_ids": ["pilkington_charles-william-macdonald_b1877"], "stint_ids": ["Pilkington, C. W. M___Cape of Good Hope___1898"]} -->
# Dossier case_pilkington_charles-william-macdonald_b1877

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `pilkington_charles-william-macdonald_b1877`

- Printed name: **PILKINGTON, Charles William MacDonald**
- Birth year: 1877 (attested in editions [1936, 1937, 1939])
- Appears in editions: [1936, 1937, 1939]

### Verbatim printed entry text (OCR)

**Version `col1936-L63726.v` — printed in editions [1936, 1937, 1939]:**

> PILKINGTON, Charles William MacDonald.—B. 1877; clk., cust., Cape Town, 1895; oh. clk., Port Elizabeth, 1930; do., Pretoria, 1933; collr., cust., Johannesburg, 1934.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1895 | clk., cust., Cape Town | Cape of Good Hope | [1936, 1937, 1939] |
| 1 | 1930 | oh. clk., Port Elizabeth | Cape of Good Hope *(inherited from previous clause)* | [1936, 1937, 1939] |
| 2 | 1933 | do., Pretoria | Cape of Good Hope *(inherited from previous clause)* | [1936, 1937, 1939] |
| 3 | 1934 | collr., cust., Johannesburg | Cape of Good Hope *(inherited from previous clause)* | [1936, 1937, 1939] |

## Candidate stint `Pilkington, C. W. M___Cape of Good Hope___1898`

- Staff-list name: **Pilkington, C. W. M** | colony: **Cape of Good Hope** | listed 1898–1900 | editions [1898, 1899, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1898 | C. W. M. Pilkington | Clerk and Assistant Examining Officer | Port of Mossel Bay | — | — |
| 1899 | C. W. M. Pilkington | Clerk and Examining Officer | Port of Knysna | — | — |
| 1900 | C. W. M. Pilkington | Clerk and Examining Officer | Executive Section | — | — |

### Deterministic checks: `pilkington_charles-william-macdonald_b1877` vs `Pilkington, C. W. M___Cape of Good Hope___1898`

- [PASS] surname_gate: bio 'PILKINGTON' vs stint 'Pilkington, C. W. M' (exact)
- [PASS] initials: bio ['C', 'W', 'M'] ~ stint ['C', 'W', 'M']
- [PASS] age_gate: stint starts 1898, birth 1877 (age 21)
- [PASS] colony: 4 placed event(s) resolve to 'Cape of Good Hope'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1898-1900
- [FAIL] position_sim: best 36 vs bar 60: 'clk., cust., Cape Town' ~ 'Clerk and Examining Officer'
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

