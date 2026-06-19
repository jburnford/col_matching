<!-- {"case_id": "case_mckinnon_andrew-alexander_b1896", "bio_ids": ["mckinnon_andrew-alexander_b1896"], "stint_ids": ["McKinnon, A. A___British Somaliland___1932"]} -->
# Dossier case_mckinnon_andrew-alexander_b1896

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 12 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mckinnon_andrew-alexander_b1896`

- Printed name: **McKINNON, ANDREW ALEXANDER**
- Birth year: 1896 (attested in editions [1939, 1940])
- Honours: M.B.E (1939)
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L68816.v` — printed in editions [1939, 1940]:**

> McKINNON, ANDREW ALEXANDER, M.B.E. (1939).—B. 1896; Br. postoffice; 1913; milv. serv., 1915-19; postal clk. & telegraphist, Tanganyika Territory, 1921; postmtr., 1926; asst. survr., 1930; postal asst. dir., B. Somaliland, 1931; asst. treas., 1933; ag. treas. and ch. of cust., Apr.-Sept., 1937 and Sept.-Dec., 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1913 | — | — | [1939, 1940] |
| 1 | 1915–1919 | milv. serv | — | [1939, 1940] |
| 2 | 1921 | postal clk. & telegraphist, Tanganyika Territory | Tanganyika | [1939, 1940] |
| 3 | 1926 | postmtr | Tanganyika *(inherited from previous clause)* | [1939, 1940] |
| 4 | 1930 | asst. survr | Tanganyika *(inherited from previous clause)* | [1939, 1940] |
| 5 | 1931 | postal asst. dir., B. Somaliland | Tanganyika *(inherited from previous clause)* | [1939, 1940] |
| 6 | 1933 | asst. treas | Tanganyika *(inherited from previous clause)* | [1939, 1940] |
| 7 | 1937 | ag. treas. and ch. of cust., Apr.- | Tanganyika *(inherited from previous clause)* | [1939, 1940] |
| 8 | 1938 | Sept.- | Tanganyika *(inherited from previous clause)* | [1939, 1940] |

## Candidate stint `McKinnon, A. A___British Somaliland___1932`

- Staff-list name: **McKinnon, A. A** | colony: **British Somaliland** | listed 1932–1940 | editions [1932, 1933, 1934, 1936, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1932 | A. A. McKinnon | Postal Assistant Director | Posts and Telegraphs Department | — | — |
| 1933 | A. A. McKinnon | Postal Assistant Director | Posts and Telegraphs Department | — | — |
| 1934 | A. A. McKinnon | Senior Assistant Treasurer | Treasury and Customs | — | — |
| 1936 | A. A. McKinnon | Senior Assistant Treasurer and Assistant Chief of Customs | Treasury and Customs | — | — |
| 1937 | A. A. McKinnon | Assistant Treasurer | Treasury and Customs | — | — |
| 1939 | A. A. McKinnon | Assistant Treasurers | Treasury and Customs | — | — |
| 1940 | A. A. McKinnon | Assistant Treasurer | Treasury and Customs | — | — |

### Deterministic checks: `mckinnon_andrew-alexander_b1896` vs `McKinnon, A. A___British Somaliland___1932`

- [PASS] surname_gate: bio 'McKINNON' vs stint 'McKinnon, A. A' (exact)
- [PASS] initials: bio ['A', 'A'] ~ stint ['A', 'A']
- [PASS] age_gate: stint starts 1932, birth 1896 (age 36)
- [FAIL] colony: no placed event resolves to 'British Somaliland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1932-1940
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

