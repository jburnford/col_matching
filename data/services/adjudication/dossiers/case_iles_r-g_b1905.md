<!-- {"case_id": "case_iles_r-g_b1905", "bio_ids": ["iles_r-g_b1905"], "stint_ids": ["Iles, R G___Straits Settlements___1931", "Iles, R. G___Singapore___1954"]} -->
# Dossier case_iles_r-g_b1905

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `iles_r-g_b1905`

- Printed name: **ILES, R. G**
- Birth year: 1905 (attested in editions [1955, 1956, 1957])
- Appears in editions: [1955, 1956, 1957]

### Verbatim printed entry text (OCR)

**Version `col1955-L21296.v` — printed in editions [1955, 1956, 1957]:**

> ILES, R. G.—b. 1905; ed. Chipping Sodbury Gram. Sch. and Bristol Univ.; mil. serv., 1942-46, maj., garrison engr., Kuantan, 1945–46; asst. engnr., Mal., 1928; res. engnr., new sup. ct., S'pore, 1938; exec. engnr., 1939; senr. exec. engnr., 1947; state engnr., gr. II, 1952; D.D.P.W., S'pore, 1952; D.P.W., 1956.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | asst. engnr. | Malaya | [1955, 1956, 1957] |
| 1 | 1938 | res. engnr., new sup. ct., S'pore | Malaya *(inherited from previous clause)* | [1955, 1956, 1957] |
| 2 | 1939 | exec. engnr | Malaya *(inherited from previous clause)* | [1955, 1956, 1957] |
| 3 | 1947 | senr. exec. engnr | Malaya *(inherited from previous clause)* | [1955, 1956, 1957] |
| 4 | 1952 | state engnr., gr. II | Malaya *(inherited from previous clause)* | [1955, 1956, 1957] |
| 5 | 1956 | D.P.W | Malaya *(inherited from previous clause)* | [1955, 1956, 1957] |

## Candidate stint `Iles, R G___Straits Settlements___1931`

- Staff-list name: **Iles, R G** | colony: **Straits Settlements** | listed 1931–1939 | editions [1931, 1932, 1934, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | R G Iles | Assistant Engineers | PUBLIC WORKS | — | — |
| 1932 | R. G. Iles | Engineer | Government | — | — |
| 1934 | R. G. Iles | Assistant Engineer | Public Works | — | — |
| 1939 | R. G. Iles | Executive Engineers | Public Works | — | — |

### Deterministic checks: `iles_r-g_b1905` vs `Iles, R G___Straits Settlements___1931`

- [PASS] surname_gate: bio 'ILES' vs stint 'Iles, R G' (exact)
- [PASS] initials: bio ['R', 'G'] ~ stint ['R', 'G']
- [PASS] age_gate: stint starts 1931, birth 1905 (age 26)
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1931-1939
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Iles, R. G___Singapore___1954`

- Staff-list name: **Iles, R. G** | colony: **Singapore** | listed 1954–1957 | editions [1954, 1955, 1956, 1957]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1954 | R. G. Iles | Deputy Director of Public Works | Civil Establishment | — | — |
| 1955 | R. G. Iles | Deputy Director of Public Works | Civil Establishment | — | — |
| 1956 | R. G. Iles | Deputy Director of Public Works | Civil Establishment | — | — |
| 1957 | R. G. Iles | Director of Public Works | Civil Establishment | — | — |

### Deterministic checks: `iles_r-g_b1905` vs `Iles, R. G___Singapore___1954`

- [PASS] surname_gate: bio 'ILES' vs stint 'Iles, R. G' (exact)
- [PASS] initials: bio ['R', 'G'] ~ stint ['R', 'G']
- [PASS] age_gate: stint starts 1954, birth 1905 (age 49)
- [FAIL] colony: no placed event resolves to 'Singapore'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1954-1957
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

