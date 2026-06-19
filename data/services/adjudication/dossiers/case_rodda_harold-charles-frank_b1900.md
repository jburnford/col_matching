<!-- {"case_id": "case_rodda_harold-charles-frank_b1900", "bio_ids": ["rodda_harold-charles-frank_b1900"], "stint_ids": ["Rodda, H. C. F___Mauritius___1936"]} -->
# Dossier case_rodda_harold-charles-frank_b1900

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `rodda_harold-charles-frank_b1900`

- Printed name: **RODDA, Harold Charles Frank**
- Birth year: 1900 (attested in editions [1950, 1951])
- Appears in editions: [1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1950-L39163.v` — printed in editions [1950, 1951]:**

> RODDA, Harold Charles Frank.—b. 1900; ed. Dulwich Coll.; on war serv., 1917-19; police prbr., F.M.S., 1920; adjt., Johore, 1921; asst. supt., 1924; serv. in Maur. and India, 1941-45; supt., 1944; ch. police offr., Negri Sembilan, 1946; comdt., training sch., S'pore., 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1920 | police prbr. | Federated Malay States | [1950, 1951] |
| 1 | 1921 | adjt. | Johore | [1950, 1951] |
| 2 | 1924 | asst. supt | Johore *(inherited from previous clause)* | [1950, 1951] |
| 3 | 1941–1945 | serv. in Maur. and India | Johore *(inherited from previous clause)* | [1950, 1951] |
| 4 | 1944 | supt | Johore *(inherited from previous clause)* | [1950, 1951] |
| 5 | 1946 | ch. police offr., Negri Sembilan | Johore *(inherited from previous clause)* | [1950, 1951] |

## Candidate stint `Rodda, H. C. F___Mauritius___1936`

- Staff-list name: **Rodda, H. C. F** | colony: **Mauritius** | listed 1936–1939 | editions [1936, 1937, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | H. C. F. Rodda | Inspector | Police Department | — | — |
| 1937 | H. C. F. Rodda | Superintendent | Police Department | — | — |
| 1939 | H. C. F. Rodda | Superintendent | Police Department | — | — |

### Deterministic checks: `rodda_harold-charles-frank_b1900` vs `Rodda, H. C. F___Mauritius___1936`

- [PASS] surname_gate: bio 'RODDA' vs stint 'Rodda, H. C. F' (exact)
- [PASS] initials: bio ['H', 'C', 'F'] ~ stint ['H', 'C', 'F']
- [PASS] age_gate: stint starts 1936, birth 1900 (age 36)
- [FAIL] colony: no placed event resolves to 'Mauritius'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1936-1939
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

