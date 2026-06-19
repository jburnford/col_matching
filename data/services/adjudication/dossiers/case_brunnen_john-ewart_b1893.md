<!-- {"case_id": "case_brunnen_john-ewart_b1893", "bio_ids": ["brunnen_john-ewart_b1893"], "stint_ids": ["Brunnen, J. E___Kenya___1937", "Brunnen, J. E___Tanganyika___1922"]} -->
# Dossier case_brunnen_john-ewart_b1893

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `brunnen_john-ewart_b1893`

- Printed name: **BRUNNEN, JOHN EWART**
- Birth year: 1893 (attested in editions [1929, 1930, 1932, 1933, 1934, 1935, 1936, 1937])
- Appears in editions: [1929, 1930, 1932, 1933, 1934, 1935, 1936, 1937, 1940]

### Verbatim printed entry text (OCR)

**Version `col1929-L58769.v` — printed in editions [1929, 1930, 1932, 1933, 1934, 1935, 1936, 1937]:**

> BRUNNEN, JOHN EWART.—B. 1893; adm'y. and dockyard schls.; H.M. Navy, 1914; adm'y., 1915; engnr., Tanganyika Territory, 1920; ag. asst. elec. engnr., 1922; ag. sen. asst. elec. engnr., 1924.

**Version `col1940-L62761.v` — printed in editions [1940]:**

> BRUNNEN, JOHN EWART.—B. 1893; war serv., H.M. Navy, 1914; admty., 1915; engr., Tanganyika Territory, 1920; asst. elec. engr., 1922; elec. engr., 1931.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914 | H.M. Navy | — | [1929, 1930, 1932, 1933, 1934, 1935, 1936, 1937] |
| 1 | 1915 | adm'y | — | [1929, 1930, 1932, 1933, 1934, 1935, 1936, 1937, 1940] |
| 2 | 1920 | engnr., Tanganyika Territory | Tanganyika | [1929, 1930, 1932, 1933, 1934, 1935, 1936, 1937, 1940] |
| 3 | 1922 | ag. asst. elec. engnr | Tanganyika *(inherited from previous clause)* | [1929, 1930, 1932, 1933, 1934, 1935, 1936, 1937, 1940] |
| 4 | 1924 | ag. sen. asst. elec. engnr | Tanganyika *(inherited from previous clause)* | [1929, 1930, 1932, 1933, 1934, 1935, 1936, 1937] |
| 5 | 1931 | elec. engr | Tanganyika *(inherited from previous clause)* | [1940] |

## Candidate stint `Brunnen, J. E___Kenya___1937`

- Staff-list name: **Brunnen, J. E** | colony: **Kenya** | listed 1937–1940 | editions [1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1937 | J. E. Brunnen | Electrical Engineer | Posts and Telegraphs Department | — | — |
| 1939 | J. E. Brunnen | Electrical Engineer | Posts and Telegraphs Department | — | — |
| 1940 | J. E. Brunnen | Electrical Engineer | Posts and Telegraphs Department | — | — |

### Deterministic checks: `brunnen_john-ewart_b1893` vs `Brunnen, J. E___Kenya___1937`

- [PASS] surname_gate: bio 'BRUNNEN' vs stint 'Brunnen, J. E' (exact)
- [PASS] initials: bio ['J', 'E'] ~ stint ['J', 'E']
- [PASS] age_gate: stint starts 1937, birth 1893 (age 44)
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1937-1940
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Brunnen, J. E___Tanganyika___1922`

- Staff-list name: **Brunnen, J. E** | colony: **Tanganyika** | listed 1922–1925 | editions [1922, 1923, 1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | J. E. Brunnen | Shift Engineers | Electric Power Plant | — | — |
| 1923 | J. E. Brunnen | Shift Engineers | Electric Power Plant | — | — |
| 1924 | J. E. Brunnen | Assistant Electrical Engineers | Electric Power Plant | — | — |
| 1925 | J. E. Brunnen | Assistant Electrical Engineer | Electric Power Plant | — | — |

### Deterministic checks: `brunnen_john-ewart_b1893` vs `Brunnen, J. E___Tanganyika___1922`

- [PASS] surname_gate: bio 'BRUNNEN' vs stint 'Brunnen, J. E' (exact)
- [PASS] initials: bio ['J', 'E'] ~ stint ['J', 'E']
- [PASS] age_gate: stint starts 1922, birth 1893 (age 29)
- [PASS] colony: 4 placed event(s) resolve to 'Tanganyika'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1922-1925
- [PASS] position_sim: best 64 vs bar 60: 'ag. asst. elec. engnr' ~ 'Assistant Electrical Engineer'
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

