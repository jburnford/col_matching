<!-- {"case_id": "case_bentley_j_b1909", "bio_ids": ["bentley_j_b1909"], "stint_ids": ["Bentley, J. D___Barbados___1936"]} -->
# Dossier case_bentley_j_b1909

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 15 official(s) with this surname in the graph's staff lists; 10 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['bentley_j_b1909'] carry a single initial only — the namesake trap applies.

## Biography `bentley_j_b1909`

- Printed name: **BENTLEY, J**
- Birth year: 1909 (attested in editions [1956, 1957, 1959, 1960, 1961, 1962, 1963])
- Honours: O.B.E (1957)
- Appears in editions: [1956, 1957, 1959, 1960, 1961, 1962, 1963]

### Verbatim printed entry text (OCR)

**Version `col1956-L19754.v` — printed in editions [1956, 1957, 1959, 1960, 1961, 1962, 1963]:**

> BENTLEY, J., O.B.E. (1957).—b. 1909; ed. Whitgift Gram. Sch. and H.M.S. Worcester; police, N. Rhod., 1936; dist. offr., prov. admin., 1947; senr. dist. offr., gr. II, 1957-62.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1936 | police | Northern Rhodesia | [1956, 1957, 1959, 1960, 1961, 1962, 1963] |
| 1 | 1947 | dist. offr., prov. admin | Northern Rhodesia *(inherited from previous clause)* | [1956, 1957, 1959, 1960, 1961, 1962, 1963] |
| 2 | 1957–1962 | senr. dist. offr., gr. II | Northern Rhodesia *(inherited from previous clause)* | [1956, 1957, 1959, 1960, 1961, 1962, 1963] |

## Candidate stint `Bentley, J. D___Barbados___1936`

- Staff-list name: **Bentley, J. D** | colony: **Barbados** | listed 1936–1939 | editions [1936, 1937, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | J. Bentley | Assistant Master | Educational | — | — |
| 1937 | J. Bentley | — | Educational | — | — |
| 1939 | J. Bentley | Assistant Masters | Educational | — | — |

### Deterministic checks: `bentley_j_b1909` vs `Bentley, J. D___Barbados___1936`

- [PASS] surname_gate: bio 'BENTLEY' vs stint 'Bentley, J. D' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J', 'D']
- [PASS] age_gate: stint starts 1936, birth 1909 (age 27)
- [FAIL] colony: no placed event resolves to 'Barbados'
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

