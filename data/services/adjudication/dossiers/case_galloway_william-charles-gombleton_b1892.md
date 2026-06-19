<!-- {"case_id": "case_galloway_william-charles-gombleton_b1892", "bio_ids": ["galloway_william-charles-gombleton_b1892"], "stint_ids": ["Galloway, W___Gold Coast___1932"]} -->
# Dossier case_galloway_william-charles-gombleton_b1892

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `galloway_william-charles-gombleton_b1892`

- Printed name: **GALLOWAY, WILLIAM CHARLES GOMBLETON**
- Birth year: 1892 (attested in editions [1933, 1934, 1935, 1936, 1937])
- Appears in editions: [1933, 1934, 1935, 1936, 1937]

### Verbatim printed entry text (OCR)

**Version `col1933-L60012.v` — printed in editions [1933, 1934, 1935, 1936, 1937]:**

> GALLOWAY, WILLIAM CHARLES GOMBLETON.—B. 1892; Lond. Institution of City and Guilds bronze medalist, telephony, A.I.E.E.; Br. P., engng. dept., Jan., 1912; on active serv., R.E. (Signals), Nov., 1915; asst. teleg. engr., P. and T. dept., F.M.S., June, 1920; engr., Oct., 1926; ag. sr. engr., P. and T., S.S. and F.M.S., May-July, 1928, and Feb-May, 1929; sr. engr., Dec., 1930; ag. asst. engr.-in-ch., Nov., 1934.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1912 | Br. P., engng. dept. | — | [1933, 1934, 1935, 1936, 1937] |
| 1 | 1915 | on active serv., R.E. (Signals) | — | [1933, 1934, 1935, 1936, 1937] |
| 2 | 1920 | asst. teleg. engr., P. and T. dept. | Federated Malay States | [1933, 1934, 1935, 1936, 1937] |
| 3 | 1926 | engr. | — | [1933, 1934, 1935, 1936, 1937] |
| 4 | 1928–1929 | ag. sr. engr., P. and T. | Straits Settlements and Federated Malay States | [1933, 1934, 1935, 1936, 1937] |
| 5 | 1930 | sr. engr. | — | [1933, 1934, 1935, 1936, 1937] |
| 6 | 1934 | ag. asst. engr.-in-ch. | — | [1933, 1934, 1935, 1936, 1937] |

## Candidate stint `Galloway, W___Gold Coast___1932`

- Staff-list name: **Galloway, W** | colony: **Gold Coast** | listed 1932–1936 | editions [1932, 1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1932 | W. Galloway | Assistant Storekeepers | Railway and Harbour Department | — | — |
| 1934 | W. Galloway | Assistant Storekeeper | Railway and Harbour Department | — | — |
| 1936 | W. Galloway | Assistant Storekeeper | Railway and Harbour Department | — | — |

### Deterministic checks: `galloway_william-charles-gombleton_b1892` vs `Galloway, W___Gold Coast___1932`

- [PASS] surname_gate: bio 'GALLOWAY' vs stint 'Galloway, W' (exact)
- [PASS] initials: bio ['W', 'C', 'G'] ~ stint ['W']
- [PASS] age_gate: stint starts 1932, birth 1892 (age 40)
- [FAIL] colony: no placed event resolves to 'Gold Coast'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1932-1936
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

