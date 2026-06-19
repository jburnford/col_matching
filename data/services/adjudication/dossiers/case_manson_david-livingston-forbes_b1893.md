<!-- {"case_id": "case_manson_david-livingston-forbes_b1893", "bio_ids": ["manson_david-livingston-forbes_b1893"], "stint_ids": ["Manson, D. L. F___Nigeria___1927", "Manson, D. L. F___Northern Rhodesia___1939"]} -->
# Dossier case_manson_david-livingston-forbes_b1893

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 14 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `manson_david-livingston-forbes_b1893`

- Printed name: **MANSON, DAVID LIVINGSTON FORBES**
- Birth year: 1893 (attested in editions [1940])
- Appears in editions: [1940]

### Verbatim printed entry text (OCR)

**Version `col1940-L66610.v` — printed in editions [1940]:**

> MANSON, DAVID LIVINGSTON FORBES.—B. 1893; milv. serv., 1914-19; superv., custa., Nigeria, Oct. 1919; collr., cust., 1926; ag. senr. collr., cust. and asst. contr., cust. on various occasions, 1930-37; contr. cust., N. Rhodesia, Sept., 1937.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914–1919 | milv. serv | — | [1940] |
| 1 | 1919 | superv., custa. | Nigeria | [1940] |
| 2 | 1926 | collr., cust | Nigeria *(inherited from previous clause)* | [1940] |
| 3 | 1930–1937 | ag. senr. collr., cust. and asst. contr., cust. on various occasions | Nigeria *(inherited from previous clause)* | [1940] |
| 4 | 1937 | contr. cust., N. Rhodesia | Nigeria *(inherited from previous clause)* | [1940] |

## Candidate stint `Manson, D. L. F___Nigeria___1927`

- Staff-list name: **Manson, D. L. F** | colony: **Nigeria** | listed 1927–1934 | editions [1927, 1929, 1933, 1934]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | D. L. F. Manson | Collector/Supervisor | Customs | — | — |
| 1929 | D. L. F. Manson | Collectors and Supervisors | Customs | — | — |
| 1933 | D. L. F. Manson | Collector/Supervisor | Customs | — | — |
| 1934 | D. L. F. Manson | Collectors and Supervisors | Customs | — | — |

### Deterministic checks: `manson_david-livingston-forbes_b1893` vs `Manson, D. L. F___Nigeria___1927`

- [PASS] surname_gate: bio 'MANSON' vs stint 'Manson, D. L. F' (exact)
- [PASS] initials: bio ['D', 'L', 'F'] ~ stint ['D', 'L', 'F']
- [PASS] age_gate: stint starts 1927, birth 1893 (age 34)
- [PASS] colony: 4 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1927-1934
- [FAIL] position_sim: best 52 vs bar 60: 'superv., custa.' ~ 'Collector/Supervisor'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Manson, D. L. F___Northern Rhodesia___1939`

- Staff-list name: **Manson, D. L. F** | colony: **Northern Rhodesia** | listed 1939–1940 | editions [1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | D. L. F. Manson | Controller of Customs | Customs | — | — |
| 1940 | D. L. F. Manson | Controller of Customs | Customs | — | — |

### Deterministic checks: `manson_david-livingston-forbes_b1893` vs `Manson, D. L. F___Northern Rhodesia___1939`

- [PASS] surname_gate: bio 'MANSON' vs stint 'Manson, D. L. F' (exact)
- [PASS] initials: bio ['D', 'L', 'F'] ~ stint ['D', 'L', 'F']
- [PASS] age_gate: stint starts 1939, birth 1893 (age 46)
- [FAIL] colony: no placed event resolves to 'Northern Rhodesia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1939-1940
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

