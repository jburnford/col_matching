<!-- {"case_id": "case_marnan_j-f_b1908", "bio_ids": ["marnan_j-f_b1908"], "stint_ids": ["Marnan, J. F___West Indies Federation___1961"]} -->
# Dossier case_marnan_j-f_b1908

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `marnan_j-f_b1908`

- Printed name: **MARNAN, J. F**
- Birth year: 1908 (attested in editions [1960, 1961, 1962, 1963])
- Honours: M.B.E
- Appears in editions: [1960, 1961, 1962, 1963]

### Verbatim printed entry text (OCR)

**Version `col1960-L25849.v` — printed in editions [1960, 1961, 1962, 1963]:**

> MARNAN, J. F., M.B.E., Q.C.—b. 1908; ed. Ampleforth Coll., and Trinity Coll., Oxford; barrister-at-law, Inner Temple; mil. serv., 1939-45; dep. recorder, Chester and Birkenhead, 1947; metrop. mag., 1956; govt. serv., Ken., 1958; fed. justice, T.W.I., 1959-62.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1947 | dep. recorder, Chester and Birkenhead | — | [1960, 1961, 1962, 1963] |
| 1 | 1956 | metrop. mag | — | [1960, 1961, 1962, 1963] |
| 2 | 1958 | govt. serv. | Kenya | [1960, 1961, 1962, 1963] |
| 3 | 1959–1962 | fed. justice, T.W.I | Kenya *(inherited from previous clause)* | [1960, 1961, 1962, 1963] |

## Candidate stint `Marnan, J. F___West Indies Federation___1961`

- Staff-list name: **Marnan, J. F** | colony: **West Indies Federation** | listed 1961–1962 | editions [1961, 1962]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1961 | J. F. Marnan | Federal Justice | JUDICIARY | M.B.E. | — |
| 1962 | J. F. Marnan | Federal Justices | Judiciary | — | — |

### Deterministic checks: `marnan_j-f_b1908` vs `Marnan, J. F___West Indies Federation___1961`

- [PASS] surname_gate: bio 'MARNAN' vs stint 'Marnan, J. F' (exact)
- [PASS] initials: bio ['J', 'F'] ~ stint ['J', 'F']
- [PASS] age_gate: stint starts 1961, birth 1908 (age 53)
- [FAIL] colony: no placed event resolves to 'West Indies Federation'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1961-1962
- [FAIL] position_sim: no overlapping placed event to compare
- [PASS] honour: shared: M.B.E
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

