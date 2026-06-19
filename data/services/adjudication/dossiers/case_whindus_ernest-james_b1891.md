<!-- {"case_id": "case_whindus_ernest-james_b1891", "bio_ids": ["whindus_ernest-james_b1891"], "stint_ids": ["Whindus, E. J___Cape of Good Hope___1906", "Whindus, E. J___Northern Rhodesia___1936"]} -->
# Dossier case_whindus_ernest-james_b1891

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `whindus_ernest-james_b1891`

- Printed name: **WHINDUS, ERNEST JAMES**
- Birth year: 1891 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1939, 1940, 1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1939-L71720.v` — printed in editions [1939, 1940]:**

> WHINDUS, ERNEST JAMES.—Warserv., S.W. and E. African campaigns, 1914-17; clk., treas., N. Rhodesia, 1917; asst. treas., 1922; senr. asst. treas., 1935; ag. dep. treas., 1935 and 1936; contr., stores and transp., 1937; contr., stores and transp., 1938.

**Version `col1948-L36787.v` — printed in editions [1948, 1949, 1950, 1951]:**

> WHINDUS, Ernest James.—b. 1891; ed. Queen's Coll.; on mil. serv., 1914-17; clk., treas. dept., N. Rhod., 1917; asst. treas., 1922; senr. asst. treas., 1935; contrlr., stores and trans., 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914–1917 | Warserv., S.W. and E. African campaigns | — | [1939, 1940] |
| 1 | 1917–1917 | clk., treas. | Northern Rhodesia | [1939, 1940, 1948, 1949, 1950, 1951] |
| 2 | 1922–1922 | asst. treas. | Northern Rhodesia *(inherited from previous clause)* | [1939, 1940, 1948, 1949, 1950, 1951] |
| 3 | 1935–1935 | senr. asst. treas. | Northern Rhodesia *(inherited from previous clause)* | [1939, 1940, 1948, 1949, 1950, 1951] |
| 4 | 1935–1936 | ag. dep. treas. | — | [1939, 1940] |
| 5 | 1937–1937 | contr., stores and transp. | — | [1939, 1940] |
| 6 | 1938–1938 | contr., stores and transp. | Northern Rhodesia *(inherited from previous clause)* | [1939, 1940, 1948, 1949, 1950, 1951] |

## Candidate stint `Whindus, E. J___Cape of Good Hope___1906`

- Staff-list name: **Whindus, E. J** | colony: **Cape of Good Hope** | listed 1906–1908 | editions [1906, 1908]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1906 | E. J. Whindus | R.M. | — | — | Captain |
| 1908 | Whindus | — | Accounting Branch | — | — |

### Deterministic checks: `whindus_ernest-james_b1891` vs `Whindus, E. J___Cape of Good Hope___1906`

- [PASS] surname_gate: bio 'WHINDUS' vs stint 'Whindus, E. J' (exact)
- [PASS] initials: bio ['E', 'J'] ~ stint ['E', 'J']
- [PASS] age_gate: stint starts 1906, birth 1891 (age 15)
- [FAIL] colony: no placed event resolves to 'Cape of Good Hope'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1906-1908
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Whindus, E. J___Northern Rhodesia___1936`

- Staff-list name: **Whindus, E. J** | colony: **Northern Rhodesia** | listed 1936–1939 | editions [1936, 1937, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | E. J. Whindus | Senior Assistant Treasurer | Public Works Department | — | — |
| 1937 | E. J. Whindus | Senior Assistant Treasurer | Treasury | — | — |
| 1939 | E. J. Whindus | Controller | Stores and Transport | — | — |

### Deterministic checks: `whindus_ernest-james_b1891` vs `Whindus, E. J___Northern Rhodesia___1936`

- [PASS] surname_gate: bio 'WHINDUS' vs stint 'Whindus, E. J' (exact)
- [PASS] initials: bio ['E', 'J'] ~ stint ['E', 'J']
- [PASS] age_gate: stint starts 1936, birth 1891 (age 45)
- [PASS] colony: 4 placed event(s) resolve to 'Northern Rhodesia'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1936-1939
- [PASS] position_sim: best 73 vs bar 60: 'senr. asst. treas.' ~ 'Senior Assistant Treasurer'
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

