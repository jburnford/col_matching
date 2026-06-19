<!-- {"case_id": "case_cousins_a-g-w_b1918", "bio_ids": ["cousins_a-g-w_b1918"], "stint_ids": ["Cousins, A. G___Dominica___1963"]} -->
# Dossier case_cousins_a-g-w_b1918

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 11 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `cousins_a-g-w_b1918`

- Printed name: **COUSINS, A. G. W**
- Birth year: 1918 (attested in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1958-L21659.v` — printed in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> COUSINS, A. G. W.—b. 1918; ed. Mico Teachers Train. Coll., J'ca; mil. serv., 1943-47, R.A.F.; J'ca constabulary, 1942; instructor, police train. sch., J'ca, 1947; asst. supt., police, St. V., 1954; dep. supt., Grenada, 1957; supt. Dom., 1960; J'ca, 1964. (J'ca Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1942 | J'ca constabulary | Jamaica | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1947 | instructor, police train. sch. | Jamaica | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1954 | asst. supt., police | St. Vincent | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 3 | 1957 | dep. supt. | Grenada | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 4 | 1960 | supt. Dom | Grenada *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 5 | 1964 | supt. Dom | Jamaica | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Cousins, A. G___Dominica___1963`

- Staff-list name: **Cousins, A. G** | colony: **Dominica** | listed 1963–1964 | editions [1963, 1964]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1963 | A. G. Cousins | Superintendent of Police | Civil Establishment | — | — |
| 1964 | A. G. Cousins | Superintendent of Police | Civil Establishment | — | — |

### Deterministic checks: `cousins_a-g-w_b1918` vs `Cousins, A. G___Dominica___1963`

- [PASS] surname_gate: bio 'COUSINS' vs stint 'Cousins, A. G' (exact)
- [PASS] initials: bio ['A', 'G', 'W'] ~ stint ['A', 'G']
- [PASS] age_gate: stint starts 1963, birth 1918 (age 45)
- [FAIL] colony: no placed event resolves to 'Dominica'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1963-1964
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

