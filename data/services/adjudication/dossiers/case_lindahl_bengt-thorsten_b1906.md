<!-- {"case_id": "case_lindahl_bengt-thorsten_b1906", "bio_ids": ["lindahl_bengt-thorsten_b1906"], "stint_ids": ["Lindahl, B. T___Kenya___1937"]} -->
# Dossier case_lindahl_bengt-thorsten_b1906

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `lindahl_bengt-thorsten_b1906`

- Printed name: **LINDAHL, Bengt Thorsten**
- Birth year: 1906 (attested in editions [1950, 1951])
- Appears in editions: [1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1950-L37318.v` — printed in editions [1950, 1951]:**

> LINDAHL, Bengt Thorsten.—b. 1906; ed. Natal Univ., B.Sc. (Natal); asst. mstr., Ken., 1929; inspr., schs., 1942; senr. educ. offr., 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1929 | asst. mstr. | Kenya | [1950, 1951] |
| 1 | 1942 | inspr., schs | Kenya *(inherited from previous clause)* | [1950, 1951] |
| 2 | 1946 | senr. educ. offr | Kenya *(inherited from previous clause)* | [1950, 1951] |

## Candidate stint `Lindahl, B. T___Kenya___1937`

- Staff-list name: **Lindahl, B. T** | colony: **Kenya** | listed 1937–1940 | editions [1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1937 | B. T. Lindahl | Education Officer—European Education | Education | — | — |
| 1939 | B. T. Lindahl | Education Officer, European Education | Education | — | — |
| 1940 | B. T. Lindahl | Education Officers—European Education | Education | — | — |

### Deterministic checks: `lindahl_bengt-thorsten_b1906` vs `Lindahl, B. T___Kenya___1937`

- [PASS] surname_gate: bio 'LINDAHL' vs stint 'Lindahl, B. T' (exact)
- [PASS] initials: bio ['B', 'T'] ~ stint ['B', 'T']
- [PASS] age_gate: stint starts 1937, birth 1906 (age 31)
- [PASS] colony: 3 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1937-1940
- [FAIL] position_sim: best 29 vs bar 60: 'asst. mstr.' ~ 'Education Officers—European Education'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

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

