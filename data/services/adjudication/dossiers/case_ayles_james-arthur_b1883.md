<!-- {"case_id": "case_ayles_james-arthur_b1883", "bio_ids": ["ayles_james-arthur_b1883"], "stint_ids": ["Ayles, J. A___Trinidad and Tobago___1931"]} -->
# Dossier case_ayles_james-arthur_b1883

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `ayles_james-arthur_b1883`

- Printed name: **AYLES, JAMES ARTHUR**
- Birth year: 1883 (attested in editions [1937, 1939, 1940])
- Appears in editions: [1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1937-L58556.v` — printed in editions [1937, 1939, 1940]:**

> AYLES, JAMES ARTHUR, M.C.—B. 1883; Cape Col. post and tel. serv., 1898-1906; Union of S. Africa post and tel. serv., 1911-13; Beaufortland post and tel. serv., 1913; asst. P.M.G., Trinidad, 1930; P.M.G., 1936.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1898–1906 | Cape Col. post and tel. serv | Cape of Good Hope | [1937, 1939, 1940] |
| 1 | 1911–1913 | Union of S. Africa post and tel. serv | Cape of Good Hope *(inherited from previous clause)* | [1937, 1939, 1940] |
| 2 | 1913 | Beaufortland post and tel. serv | Cape of Good Hope *(inherited from previous clause)* | [1937, 1939, 1940] |
| 3 | 1930 | asst. P.M.G. | Trinidad | [1937, 1939, 1940] |
| 4 | 1936 | P.M.G | Trinidad *(inherited from previous clause)* | [1937, 1939, 1940] |

## Candidate stint `Ayles, J. A___Trinidad and Tobago___1931`

- Staff-list name: **Ayles, J. A** | colony: **Trinidad and Tobago** | listed 1931–1939 | editions [1931, 1933, 1934, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | J. A. Ayles | Assistant Postmaster-General | Post Office Department | — | — |
| 1933 | J. A. Ayles | Assistant Postmaster-General | Post Office Department | — | — |
| 1934 | J. A. Ayles | Assistant Postmaster-General | POST OFFICE DEPARTMENT | — | — |
| 1939 | J. A. Ayles | Postmaster-General and Manager of Savings Bank | Post Office and Savings Bank | — | — |

### Deterministic checks: `ayles_james-arthur_b1883` vs `Ayles, J. A___Trinidad and Tobago___1931`

- [PASS] surname_gate: bio 'AYLES' vs stint 'Ayles, J. A' (exact)
- [PASS] initials: bio ['J', 'A'] ~ stint ['J', 'A']
- [PASS] age_gate: stint starts 1931, birth 1883 (age 48)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1931-1939
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

