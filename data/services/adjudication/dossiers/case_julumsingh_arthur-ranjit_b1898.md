<!-- {"case_id": "case_julumsingh_arthur-ranjit_b1898", "bio_ids": ["julumsingh_arthur-ranjit_b1898"], "stint_ids": ["Julumsingh, A. R___Trinidad and Tobago___1928"]} -->
# Dossier case_julumsingh_arthur-ranjit_b1898

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `julumsingh_arthur-ranjit_b1898`

- Printed name: **JULUMSINGH, Arthur Ranjit**
- Birth year: 1898 (attested in editions [1951])
- Appears in editions: [1951]

### Verbatim printed entry text (OCR)

**Version `col1951-L39660.v` — printed in editions [1951]:**

> JULUMSINGH, Arthur Ranjit.—b. 1898; ed. Queen's Royal Coll., Trin.; clk., magistracy, Trin., 1917; prin. offr., clerk II, 1943; clerk I, 1944; pay and Q.M., police, 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1917 | clk., magistracy | Trinidad | [1951] |
| 1 | 1943 | prin. offr., clerk II | Trinidad *(inherited from previous clause)* | [1951] |
| 2 | 1944 | clerk I | Trinidad *(inherited from previous clause)* | [1951] |
| 3 | 1946 | pay and Q.M., police | Trinidad *(inherited from previous clause)* | [1951] |

## Candidate stint `Julumsingh, A. R___Trinidad and Tobago___1928`

- Staff-list name: **Julumsingh, A. R** | colony: **Trinidad and Tobago** | listed 1928–1929 | editions [1928, 1929]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1928 | A. R. Julumsingh | Assistant Clerk of the Peace | Clerks of the Peace | — | — |
| 1929 | A. R. Julumsingh | Assistant Clerk of the Peace | Clerks of the Peace | — | — |

### Deterministic checks: `julumsingh_arthur-ranjit_b1898` vs `Julumsingh, A. R___Trinidad and Tobago___1928`

- [PASS] surname_gate: bio 'JULUMSINGH' vs stint 'Julumsingh, A. R' (exact)
- [PASS] initials: bio ['A', 'R'] ~ stint ['A', 'R']
- [PASS] age_gate: stint starts 1928, birth 1898 (age 30)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1928-1929
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

