<!-- {"case_id": "case_collins_kenneth-stephen_b1913", "bio_ids": ["collins_kenneth-stephen_b1913"], "stint_ids": ["Collins, K. S___Gambia___1949"]} -->
# Dossier case_collins_kenneth-stephen_b1913

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 66 official(s) with this surname in the graph's staff lists; 30 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `collins_kenneth-stephen_b1913`

- Printed name: **COLLINS, Kenneth Stephen**
- Birth year: 1913 (attested in editions [1957, 1958, 1959])
- Honours: M.B.E, O.B.E (1957)
- Appears in editions: [1949, 1950, 1951, 1957, 1958, 1959]

### Verbatim printed entry text (OCR)

**Version `col1957-L22070.v` — printed in editions [1957, 1958, 1959]:**

> COLLINS, K. S., O.B.E. (1957), M.B.E.—b. 1913; ed. Taunton's Sch., Southampton, and Merton Coll., Oxford; asst. audr., Tang., 1936; prin. audr., Gam., 1947; Nig., 1951; dep. dir., audit, W. regn., 1951; dir., 1954-58.

**Version `col1949-L31238.v` — printed in editions [1949, 1950, 1951]:**

> COLLINS, Kenneth Stephen, B.A. (Oxon).—b. 1913; asst. audr., T.T., 1936; audr. (later prin. audr.), Gam., 1947.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1936 | asst. audr. | Tanganyika | [1949, 1950, 1951, 1957, 1958, 1959] |
| 1 | 1947 | prin. audr., Gam | Tanganyika *(inherited from previous clause)* | [1949, 1950, 1951, 1957, 1958, 1959] |
| 2 | 1951 | prin. audr., Gam | Nigeria | [1957, 1958, 1959] |
| 3 | 1954–1958 | dir | Nigeria *(inherited from previous clause)* | [1957, 1958, 1959] |

## Candidate stint `Collins, K. S___Gambia___1949`

- Staff-list name: **Collins, K. S** | colony: **Gambia** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | K. S. Collins | Principal Auditor | Audit | — | — |
| 1950 | K. S. Collins | Principal Auditor | Audit | — | — |
| 1951 | K. S. Collins | Principal Auditor | Audit | — | — |

### Deterministic checks: `collins_kenneth-stephen_b1913` vs `Collins, K. S___Gambia___1949`

- [PASS] surname_gate: bio 'COLLINS' vs stint 'Collins, K. S' (exact)
- [PASS] initials: bio ['K', 'S'] ~ stint ['K', 'S']
- [PASS] age_gate: stint starts 1949, birth 1913 (age 36)
- [FAIL] colony: no placed event resolves to 'Gambia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
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

