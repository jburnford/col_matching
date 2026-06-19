<!-- {"case_id": "case_peaker_a-j_b1911", "bio_ids": ["peaker_a-j_b1911"], "stint_ids": ["Peaker, A. J___Hong Kong___1961"]} -->
# Dossier case_peaker_a-j_b1911

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `peaker_a-j_b1911`

- Printed name: **PEAKER, A. J**
- Birth year: 1911 (attested in editions [1961, 1962, 1963, 1964, 1965, 1966])
- Honours: M.B.E
- Appears in editions: [1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1961-L26085.v` — printed in editions [1961, 1962, 1963, 1964, 1965, 1966]:**

> PEAKER, A. J., M.B.E.—b. 1911; ed. Leeds Gram. Sch. and Coll. of Technology; mil. serv., 1941–45; asst. instr. in building, tech. coll., H.K., 1938; supt., furniture and equipment, 1947; asst. contrlr. of stores, 1957; dep. contrlr., 1959; contrlr., 1960–65.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1938 | asst. instr. in building, tech. coll. | Hong Kong | [1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1947 | supt., furniture and equipment | Hong Kong *(inherited from previous clause)* | [1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1957 | asst. contrlr. of stores | Hong Kong *(inherited from previous clause)* | [1961, 1962, 1963, 1964, 1965, 1966] |
| 3 | 1959 | dep. contrlr | Hong Kong *(inherited from previous clause)* | [1961, 1962, 1963, 1964, 1965, 1966] |
| 4 | 1960–1965 | contrlr | Hong Kong *(inherited from previous clause)* | [1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Peaker, A. J___Hong Kong___1961`

- Staff-list name: **Peaker, A. J** | colony: **Hong Kong** | listed 1961–1965 | editions [1961, 1962, 1963, 1964, 1965]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1961 | A. J. Peaker | Controller of Stores | Civil Establishment | — | — |
| 1962 | A. J. Peaker | Controller of Stores | Civil Establishment | — | — |
| 1963 | A. J. Peaker | Controller of Stores | Civil Establishment | — | — |
| 1964 | A. J. Peaker | Controller of Stores | Civil Establishment | — | — |
| 1965 | A. J. Peaker | Controller of Stores | Civil Establishment | M.B.E. | — |

### Deterministic checks: `peaker_a-j_b1911` vs `Peaker, A. J___Hong Kong___1961`

- [PASS] surname_gate: bio 'PEAKER' vs stint 'Peaker, A. J' (exact)
- [PASS] initials: bio ['A', 'J'] ~ stint ['A', 'J']
- [PASS] age_gate: stint starts 1961, birth 1911 (age 50)
- [PASS] colony: 5 placed event(s) resolve to 'Hong Kong'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1961-1965
- [FAIL] position_sim: best 58 vs bar 60: 'dep. contrlr' ~ 'Controller of Stores'
- [PASS] honour: shared: M.B.E
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

