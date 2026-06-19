<!-- {"case_id": "case_south_francis-wilton_b1886", "bio_ids": ["south_francis-wilton_b1886"], "stint_ids": ["South, F. W___Barbados___1910", "South___Canada___1918"]} -->
# Dossier case_south_francis-wilton_b1886

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `south_francis-wilton_b1886`

- Printed name: **SOUTH, FRANCIS WILTON**
- Birth year: 1886 (attested in editions [1932, 1933, 1934, 1935, 1936, 1937])
- Appears in editions: [1932, 1933, 1934, 1935, 1936, 1937]

### Verbatim printed entry text (OCR)

**Version `col1932-L64108.v` — printed in editions [1932, 1933, 1934, 1935, 1936, 1937]:**

> SOUTH, FRANCIS WILTON, M.A. (Cantab.).—B. 1886; ed. Marlborough Coll., and Emmanuel Coll., Cambridge; mycologist and lect. in agrl. sci., Imp. dept. of agr. for W. Indies, Mar., 1909; chg. agrl. inspr., agrl. dept., F.M.S., May, 1913; chg. agrl. field offr., Nov., 1924; ag. sec. for agr., S.S. and F.M.S., for various periods 1927-31; rep. of Malaya at mycological confce. in Lond., Sept., 1929; ag. dir., agr., S.S. and F.M.S. for various periods, 1929 and 1931-32.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1909 | mycologist and lect. in agrl. sci., Imp. dept. of agr. | West Indies | [1932, 1933, 1934, 1935, 1936, 1937] |
| 1 | 1913 | chg. agrl. inspr., agrl. dept. | Federated Malay States | [1932, 1933, 1934, 1935, 1936, 1937] |
| 2 | 1924 | chg. agrl. field offr. | — | [1932, 1933, 1934, 1935, 1936, 1937] |
| 3 | 1927–1931 | ag. sec. for agr. | Straits Settlements and Federated Malay States | [1932, 1933, 1934, 1935, 1936, 1937] |
| 4 | 1929 | rep. of Malaya at mycological confce. | London | [1932, 1933, 1934, 1935, 1936, 1937] |
| 5 | 1929–1932 | ag. dir., agr. | Straits Settlements and Federated Malay States | [1932, 1933, 1934, 1935, 1936, 1937] |

## Candidate stint `South, F. W___Barbados___1910`

- Staff-list name: **South, F. W** | colony: **Barbados** | listed 1910–1914 | editions [1910, 1911, 1912, 1914]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1910 | F. W. South | Mycologist and Lecturer in Agricultural Science | Imperial Department of Agriculture for the West Indies | — | — |
| 1911 | F. W. South | Mycologist and Lecturer in Agricultural Science | Imperial Department of Agriculture for the West Indies | — | — |
| 1912 | F. W. South | Mycologist and Lecturer in Agricultural Science | Imperial Department of Agriculture | — | — |
| 1914 | F. W. South | Mycologist and Lecturer in Agricultural Science | Imperial Department of Agriculture for the West Indies | — | — |

### Deterministic checks: `south_francis-wilton_b1886` vs `South, F. W___Barbados___1910`

- [PASS] surname_gate: bio 'SOUTH' vs stint 'South, F. W' (exact)
- [PASS] initials: bio ['F', 'W'] ~ stint ['F', 'W']
- [PASS] age_gate: stint starts 1910, birth 1886 (age 24)
- [FAIL] colony: no placed event resolves to 'Barbados'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1910-1914
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `South___Canada___1918`

- Staff-list name: **South** | colony: **Canada** | listed 1918–1919 | editions [1918, 1919]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1918 | South, | Member of Parliament | House of Commons | — | — |
| 1919 | South | Cape Breton | House of Commons | — | — |

### Deterministic checks: `south_francis-wilton_b1886` vs `South___Canada___1918`

- [PASS] surname_gate: bio 'SOUTH' vs stint 'South' (exact)
- [PASS] initials: bio ['F', 'W'] ~ stint ['?']
- [PASS] age_gate: stint starts 1918, birth 1886 (age 32)
- [FAIL] colony: no placed event resolves to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1918-1919
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

