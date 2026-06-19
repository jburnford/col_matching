<!-- {"case_id": "case_beaton_i-w_b1909", "bio_ids": ["beaton_i-w_b1909"], "stint_ids": ["Beaton, I. W___Uganda___1939"]} -->
# Dossier case_beaton_i-w_b1909

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `beaton_i-w_b1909`

- Printed name: **BEATON, I. W.**
- Birth year: 1909 (attested in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965])
- Appears in editions: [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965]

### Verbatim printed entry text (OCR)

**Version `col1957-L20998.v` — printed in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965]:**

> BEATON, I. W.—b. 1909; ed. Greenock High Sch. and Royal Tech. Coll., Glasgow; mil. serv., 1939-45, capt.; health inspr., Uga., 1935; labour offr., 1949; organized (i/c 1946-48) Mbale rehabilitation centre for African ex-servicemen; ret., re-app. labr. offr., Nyasa., 1960. (Malawi Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1935–1935 | health inspr. | Uganda | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 1 | 1939–1945 | capt. | — | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 2 | 1946–1948 | i/c Mbale rehabilitation centre for African ex-servicemen | — | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 3 | 1949–1949 | labour offr. | — | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 4 | 1960–1960 | labr. offr. | Nyasaland | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |

## Candidate stint `Beaton, I. W___Uganda___1939`

- Staff-list name: **Beaton, I. W** | colony: **Uganda** | listed 1939–1949 | editions [1939, 1940, 1949]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | I. W. Beaton | Sanitary Inspector | Medical | — | — |
| 1940 | I. W. Beaton | Health Inspector | Medical | — | — |
| 1949 | I. W. Beaton | Health Inspectors | Medical | — | — |

### Deterministic checks: `beaton_i-w_b1909` vs `Beaton, I. W___Uganda___1939`

- [PASS] surname_gate: bio 'BEATON' vs stint 'Beaton, I. W' (exact)
- [PASS] initials: bio ['I', 'W'] ~ stint ['I', 'W']
- [PASS] age_gate: stint starts 1939, birth 1909 (age 30)
- [PASS] colony: 1 placed event(s) resolve to 'Uganda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1939-1949
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

