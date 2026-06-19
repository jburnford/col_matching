<!-- {"case_id": "case_hutchinson_m-p_b1918", "bio_ids": ["hutchinson_m-p_b1918"], "stint_ids": ["Hutchinson, P___Nyasaland___1939"]} -->
# Dossier case_hutchinson_m-p_b1918

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 44 official(s) with this surname in the graph's staff lists; 14 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hutchinson_m-p_b1918`

- Printed name: **HUTCHINSON, M. P**
- Birth year: 1918 (attested in editions [1956, 1957, 1958, 1959])
- Appears in editions: [1956, 1957, 1958, 1959]

### Verbatim printed entry text (OCR)

**Version `col1956-L22093.v` — printed in editions [1956, 1957, 1958, 1959]:**

> HUTCHINSON, M. P.—b. 1918; ed. Eastbourne Coll. and Guy's Hosp., London; M.O., S. Leone, 1943; sleeping sickness M.O., Nig., 1947; secon. to W.A. inst. for trypanosomiasis research as research epidemiologist, 1949; dep. dir., W.A.I.T.R., 1956-58; author Epidemiology of Human Trypanosomiasis in British W. Africa.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1943 | M.O., S. Leone | — | [1956, 1957, 1958, 1959] |
| 1 | 1947 | sleeping sickness M.O. | Nigeria | [1956, 1957, 1958, 1959] |
| 2 | 1949 | secon. to W.A. inst. for trypanosomiasis research as research epidemiologist | Nigeria *(inherited from previous clause)* | [1956, 1957, 1958, 1959] |
| 3 | 1956–1958 | dep. dir., W.A.I.T.R | Nigeria *(inherited from previous clause)* | [1956, 1957, 1958, 1959] |

## Candidate stint `Hutchinson, P___Nyasaland___1939`

- Staff-list name: **Hutchinson, P** | colony: **Nyasaland** | listed 1939–1940 | editions [1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | P. Hutchinson | Nurses | Medical | — | — |
| 1940 | P. Hutchinson | Nurse | Medical | — | — |

### Deterministic checks: `hutchinson_m-p_b1918` vs `Hutchinson, P___Nyasaland___1939`

- [PASS] surname_gate: bio 'HUTCHINSON' vs stint 'Hutchinson, P' (exact)
- [PASS] initials: bio ['M', 'P'] ~ stint ['P']
- [PASS] age_gate: stint starts 1939, birth 1918 (age 21)
- [FAIL] colony: no placed event resolves to 'Nyasaland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1939-1940
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

