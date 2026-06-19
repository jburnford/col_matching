<!-- {"case_id": "case_may_w-b_b1917", "bio_ids": ["may_w-b_b1917"], "stint_ids": ["May, Barry___Aden___1964"]} -->
# Dossier case_may_w-b_b1917

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 53 official(s) with this surname in the graph's staff lists; 24 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `May, Barry___Aden___1964` is also gate-compatible with biography(ies) outside this case: ['may_b-f_b1913', 'may_barry_b1869'] (already linked elsewhere or filtered).

## Biography `may_w-b_b1917`

- Printed name: **MAY, W. B**
- Birth year: 1917 (attested in editions [1958, 1959, 1960, 1961, 1962, 1963])
- Appears in editions: [1958, 1959, 1960, 1961, 1962, 1963]

### Verbatim printed entry text (OCR)

**Version `col1958-L25207.v` — printed in editions [1958, 1959, 1960, 1961, 1962, 1963]:**

> MAY, W. B.—b. 1917; ed. Oswald-twistle Secondary Sch., Lancs., Hort. Station, Harris Inst., Preston, Univ. Botanic Garden, Camb.; mil. serv., 1939–43; L.A.C.; agric. supt., N. Rhod., 1943; supt., plantations, E.A.A.R.I., Tang., 1946; scientific asst., clove research, Zanz., 1948; field experimentalist, E.A.A.F.R.O., 1951–62.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1943 | agric. supt. | Northern Rhodesia | [1958, 1959, 1960, 1961, 1962, 1963] |
| 1 | 1946 | supt., plantations, E.A.A.R.I. | Tanganyika | [1958, 1959, 1960, 1961, 1962, 1963] |
| 2 | 1948 | scientific asst., clove research | Zanzibar | [1958, 1959, 1960, 1961, 1962, 1963] |
| 3 | 1951–1962 | field experimentalist, E.A.A.F.R.O | Zanzibar *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963] |

## Candidate stint `May, Barry___Aden___1964`

- Staff-list name: **May, Barry** | colony: **Aden** | listed 1964–1966 | editions [1964, 1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1964 | B. F. May | Chief Accountant | CIVIL ESTABLISHMENT | — | — |
| 1965 | B. F. May | Chief Accountant | Civil Establishment | — | — |
| 1966 | B. F. May | Chief Accountant | Civil Establishment | — | — |

### Deterministic checks: `may_w-b_b1917` vs `May, Barry___Aden___1964`

- [PASS] surname_gate: bio 'MAY' vs stint 'May, Barry' (exact)
- [PASS] initials: bio ['W', 'B'] ~ stint ['B']
- [PASS] age_gate: stint starts 1964, birth 1917 (age 47)
- [FAIL] colony: no placed event resolves to 'Aden'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1964-1966
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

