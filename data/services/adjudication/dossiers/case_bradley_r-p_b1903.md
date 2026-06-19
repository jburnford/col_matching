<!-- {"case_id": "case_bradley_r-p_b1903", "bio_ids": ["bradley_r-p_b1903"], "stint_ids": ["Bradley, R. P___Straits Settlements___1934"]} -->
# Dossier case_bradley_r-p_b1903

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 29 official(s) with this surname in the graph's staff lists; 15 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `bradley_r-p_b1903`

- Printed name: **BRADLEY, R. P**
- Birth year: 1903 (attested in editions [1956, 1957])
- Appears in editions: [1956, 1957]

### Verbatim printed entry text (OCR)

**Version `col1956-L19977.v` — printed in editions [1956, 1957]:**

> BRADLEY, R. P.—b. 1903; ed. Southall County Sch. and City and Guilds Engng. Coll., London; mil. serv., 1942-45; asst. engrnr., F.M.S., 1927; exec. engrnr., 1936; S'pore, 1938; senr. exec. engrnr., 1950; state engrnr., gr. I, 1952; state engrnr., Johore, 1954.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1927 | asst. engrnr. | Federated Malay States | [1956, 1957] |
| 1 | 1936 | exec. engrnr | Federated Malay States *(inherited from previous clause)* | [1956, 1957] |
| 2 | 1938 | S'pore | Federated Malay States *(inherited from previous clause)* | [1956, 1957] |
| 3 | 1950 | senr. exec. engrnr | Federated Malay States *(inherited from previous clause)* | [1956, 1957] |
| 4 | 1952 | state engrnr., gr. I | Federated Malay States *(inherited from previous clause)* | [1956, 1957] |
| 5 | 1954 | state engrnr. | Johore | [1956, 1957] |

## Candidate stint `Bradley, R. P___Straits Settlements___1934`

- Staff-list name: **Bradley, R. P** | colony: **Straits Settlements** | listed 1934–1939 | editions [1934, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | R. P. Bradley | Assistant Engineer | Public Works | — | — |
| 1939 | R. P. Bradley | Executive Engineers | Public Works | — | — |

### Deterministic checks: `bradley_r-p_b1903` vs `Bradley, R. P___Straits Settlements___1934`

- [PASS] surname_gate: bio 'BRADLEY' vs stint 'Bradley, R. P' (exact)
- [PASS] initials: bio ['R', 'P'] ~ stint ['R', 'P']
- [PASS] age_gate: stint starts 1934, birth 1903 (age 31)
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1934-1939
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

