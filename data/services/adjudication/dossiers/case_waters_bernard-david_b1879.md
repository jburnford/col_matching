<!-- {"case_id": "case_waters_bernard-david_b1879", "bio_ids": ["waters_bernard-david_b1879"], "stint_ids": ["Waters, B. D___Northern Rhodesia___1925"]} -->
# Dossier case_waters_bernard-david_b1879

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 21 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `waters_bernard-david_b1879`

- Printed name: **WATERS, BERNARD DAVID**
- Birth year: 1879 (attested in editions [1927, 1928, 1929, 1930, 1931, 1932])
- Appears in editions: [1927, 1928, 1929, 1930, 1931, 1932]

### Verbatim printed entry text (OCR)

**Version `col1927-L63651.v` — printed in editions [1927, 1928, 1929, 1930, 1931, 1932]:**

> WATERS, BERNARD DAVID.—B. 1879; telegraphist, Cape Colony, May, 1902 to Aug., 1905; postal asst., N. Rhodesia, Aug., 1905; ch. asst., Apr., 1912; sec., post office, May, 1913; ag. P.M.G., Jan., 1926 to May, 1926; dep. P.M.G., Nov., 1926.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1902–1905 | telegraphist | Cape of Good Hope | [1927, 1928, 1929, 1930, 1931, 1932] |
| 1 | 1905 | postal asst., N. Rhodesia | Cape of Good Hope *(inherited from previous clause)* | [1927, 1928, 1929, 1930, 1931, 1932] |
| 2 | 1912 | ch. asst | Cape of Good Hope *(inherited from previous clause)* | [1927, 1928, 1929, 1930, 1931, 1932] |
| 3 | 1913 | sec., post office | Cape of Good Hope *(inherited from previous clause)* | [1927, 1928, 1929, 1930, 1931, 1932] |
| 4 | 1926–1926 | ag. P.M.G | Cape of Good Hope *(inherited from previous clause)* | [1927, 1928, 1929, 1930, 1931, 1932] |

## Candidate stint `Waters, B. D___Northern Rhodesia___1925`

- Staff-list name: **Waters, B. D** | colony: **Northern Rhodesia** | listed 1925–1927 | editions [1925, 1927]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1925 | B. D. Waters | Secretary to Post Office | Posts and Telegraphs | — | — |
| 1927 | B. D. Waters | Secretary to Post Office | Posts and Telegraphs | — | — |

### Deterministic checks: `waters_bernard-david_b1879` vs `Waters, B. D___Northern Rhodesia___1925`

- [PASS] surname_gate: bio 'WATERS' vs stint 'Waters, B. D' (exact)
- [PASS] initials: bio ['B', 'D'] ~ stint ['B', 'D']
- [PASS] age_gate: stint starts 1925, birth 1879 (age 46)
- [FAIL] colony: no placed event resolves to 'Northern Rhodesia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1925-1927
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

