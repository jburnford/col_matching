<!-- {"case_id": "case_malan_hendrick-jacobus_b1879", "bio_ids": ["malan_hendrick-jacobus_b1879"], "stint_ids": ["Malan, H. J___Cape of Good Hope___1905"]} -->
# Dossier case_malan_hendrick-jacobus_b1879

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `malan_hendrick-jacobus_b1879`

- Printed name: **MALAN, HENDRICK JACOBUS**
- Birth year: 1879 (attested in editions [1934, 1935, 1936, 1937, 1939, 1940])
- Appears in editions: [1934, 1935, 1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1934-L61471.v` — printed in editions [1934, 1935, 1936, 1937, 1939, 1940]:**

> MALAN, HENDRICK JACOBUS, B.A. (Cape).—B. 1879; Cape civ. serv., 1900; war serv., capt., Pretoria Rgt., S.W.A., 1914-15; astt. mag., Johannesburg, 1918; mag. Britstown, 1919; Ladysmith, 1922; Johannesburg, 1927; Senekal, 1930; Potchefstroom, 1933; Pietermaritzburg, 1936; Port Elizabeth, Oct., 1936.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1900 | Cape civ. serv | Cape of Good Hope | [1934, 1935, 1936, 1937, 1939, 1940] |
| 1 | 1918 | astt. mag., Johannesburg | Cape of Good Hope *(inherited from previous clause)* | [1934, 1935, 1936, 1937, 1939, 1940] |
| 2 | 1919 | mag. Britstown | Cape of Good Hope *(inherited from previous clause)* | [1934, 1935, 1936, 1937, 1939, 1940] |
| 3 | 1922 | Ladysmith | Cape of Good Hope *(inherited from previous clause)* | [1934, 1935, 1936, 1937, 1939, 1940] |
| 4 | 1927 | Johannesburg | Cape of Good Hope *(inherited from previous clause)* | [1934, 1935, 1936, 1937, 1939, 1940] |
| 5 | 1930 | Senekal | Cape of Good Hope *(inherited from previous clause)* | [1934, 1935, 1936, 1937, 1939, 1940] |
| 6 | 1933 | Potchefstroom | Cape of Good Hope *(inherited from previous clause)* | [1934, 1935, 1936, 1937, 1939, 1940] |
| 7 | 1936 | Pietermaritzburg | Cape of Good Hope *(inherited from previous clause)* | [1934, 1935, 1936, 1937, 1939, 1940] |

## Candidate stint `Malan, H. J___Cape of Good Hope___1905`

- Staff-list name: **Malan, H. J** | colony: **Cape of Good Hope** | listed 1905–1909 | editions [1905, 1906, 1907, 1908, 1909]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | H. J. Malan | Clerk | Administrative Branch | — | — |
| 1906 | H. J. Malan | Clerk | Administrative Branch | — | — |
| 1907 | H. J. Malan | Clerk | Administrative Branch | — | — |
| 1908 | H. J. Malan | Clerk | Administrative Branch | — | — |
| 1909 | H. J. Malan | Clerk | Divisional Courts Branch | — | — |

### Deterministic checks: `malan_hendrick-jacobus_b1879` vs `Malan, H. J___Cape of Good Hope___1905`

- [PASS] surname_gate: bio 'MALAN' vs stint 'Malan, H. J' (exact)
- [PASS] initials: bio ['H', 'J'] ~ stint ['H', 'J']
- [PASS] age_gate: stint starts 1905, birth 1879 (age 26)
- [PASS] colony: 8 placed event(s) resolve to 'Cape of Good Hope'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1905-1909
- [FAIL] position_sim: best 33 vs bar 60: 'Cape civ. serv' ~ 'Clerk'
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

