<!-- {"case_id": "case_martin_h-g_b1920", "bio_ids": ["martin_h-g_b1920"], "stint_ids": ["Martin, H. G___Nyasaland___1961"]} -->
# Dossier case_martin_h-g_b1920

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 135 official(s) with this surname in the graph's staff lists; 55 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Martin, H. G___Nyasaland___1961` is also gate-compatible with biography(ies) outside this case: ['martin_henry_e1896'] (already linked elsewhere or filtered).

## Biography `martin_h-g_b1920`

- Printed name: **MARTIN, H. G**
- Birth year: 1920 (attested in editions [1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1962-L24286.v` — printed in editions [1962, 1963, 1964, 1965, 1966]:**

> MARTIN, H. G.—b. 1920; ed. Stockport Gram. Sch. and Manchester Univ.; mil. serv., 1940-46, R.A.F.; asst. regsr., N. Rhod., 1953; lands offr., 1958; regr.-gen., Nyas., 1960. (Malawi Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1953 | asst. regsr. | Northern Rhodesia | [1962, 1963, 1964, 1965, 1966] |
| 1 | 1958 | lands offr | Northern Rhodesia *(inherited from previous clause)* | [1962, 1963, 1964, 1965, 1966] |
| 2 | 1960 | regr.-gen., Nyas | Northern Rhodesia *(inherited from previous clause)* | [1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Martin, H. G___Nyasaland___1961`

- Staff-list name: **Martin, H. G** | colony: **Nyasaland** | listed 1961–1964 | editions [1961, 1962, 1963, 1964]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1961 | H. G. Martin | Registrar-General | Civil Establishment | — | — |
| 1962 | H. G. Martin | Registrar General | Ministry of Justice | — | — |
| 1963 | H. G. Martin | Registrar General | Ministry of Justice | — | — |
| 1964 | H. G. Martin | Registrar General | Ministry of Justice | — | — |

### Deterministic checks: `martin_h-g_b1920` vs `Martin, H. G___Nyasaland___1961`

- [PASS] surname_gate: bio 'MARTIN' vs stint 'Martin, H. G' (exact)
- [PASS] initials: bio ['H', 'G'] ~ stint ['H', 'G']
- [PASS] age_gate: stint starts 1961, birth 1920 (age 41)
- [FAIL] colony: no placed event resolves to 'Nyasaland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1961-1964
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

