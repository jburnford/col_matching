<!-- {"case_id": "case_altson_ralph-abby_b1894", "bio_ids": ["altson_ralph-abby_b1894"], "stint_ids": ["Altson, R. A___British Guiana___1925"]} -->
# Dossier case_altson_ralph-abby_b1894

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `altson_ralph-abby_b1894`

- Printed name: **ALTSON, RALPH ABBY**
- Birth year: 1894 (attested in editions [1939, 1940])
- Honours: A.R.C.S
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L64282.v` — printed in editions [1939, 1940]:**

> ALTSON, RALPH ABBY, B.Sc., A.R.C.S.—B. 1894; Bedford Sch. and Royal Coll. of Sci., London; asst. botanist and mycologist, dept. of agr., B. Guiana, Feb., 1923; botanist and mycologist, Jan., 1928; asst. mycologist, agrl. dept., F.M.S., Apr., 1928; del. to 2nd Internat. Congr. for Microbiology, Lond., July, 1936; ag. mycologist, July, 1937; title changed, plant pathologist, Jan., 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1923 | asst. botanist and mycologist, dept. of agr., B. Guiana | — | [1939, 1940] |
| 1 | 1928 | botanist and mycologist | — | [1939, 1940] |
| 2 | 1928 | asst. mycologist, agrl. dept. | Federated Malay States | [1939, 1940] |
| 3 | 1936 | del. to 2nd Internat. Congr. for Microbiology, Lond | Federated Malay States *(inherited from previous clause)* | [1939, 1940] |
| 4 | 1937 | ag. mycologist | Federated Malay States *(inherited from previous clause)* | [1939, 1940] |
| 5 | 1938 | title changed, plant pathologist | Federated Malay States *(inherited from previous clause)* | [1939, 1940] |

## Candidate stint `Altson, R. A___British Guiana___1925`

- Staff-list name: **Altson, R. A** | colony: **British Guiana** | listed 1925–1928 | editions [1925, 1927, 1928]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1925 | R. A. Altson | Assistant Botanist and Mycologist | Department of Science and Agriculture | — | — |
| 1927 | R. A. Altson | Assistant Botanist and Mycologist | Science and Agriculture | — | — |
| 1928 | R. A. Altson | Assistant Botanist and Mycologist | Department of Science and Agriculture | — | — |

### Deterministic checks: `altson_ralph-abby_b1894` vs `Altson, R. A___British Guiana___1925`

- [PASS] surname_gate: bio 'ALTSON' vs stint 'Altson, R. A' (exact)
- [PASS] initials: bio ['R', 'A'] ~ stint ['R', 'A']
- [PASS] age_gate: stint starts 1925, birth 1894 (age 31)
- [FAIL] colony: no placed event resolves to 'British Guiana'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1925-1928
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

