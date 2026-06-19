<!-- {"case_id": "case_branday_w-j_b1901", "bio_ids": ["branday_w-j_b1901"], "stint_ids": ["Branday, W. J___Trinidad and Tobago___1949"]} -->
# Dossier case_branday_w-j_b1901

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `branday_w-j_b1901`

- Printed name: **BRANDAY, W. J**
- Birth year: 1901 (attested in editions [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964])
- Honours: O.B.E (1957)
- Appears in editions: [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1953-L16666.v` — printed in editions [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]:**

> BRANDAY, W. J., O.B.E. (1957).—b. 1901; ed. St. George's Coll., J'ca, Univ. of Birmingham and Johns Hopkins Univ.; M.O.H., J'ca, 1932; M.O.H. (T.B. clinic), 1939; T.B. offr., 1942; chief T.B. offr., Trin., 1947; later suptg. M.O., spec., T.B. sanatorium and clinics; author of articles in various med. journals.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1932 | M.O.H. | Jamaica | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 1 | 1939 | M.O.H. (T.B. clinic) | Jamaica *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 2 | 1942 | T.B. offr | Jamaica *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 3 | 1947 | chief T.B. offr. | Trinidad | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |

## Candidate stint `Branday, W. J___Trinidad and Tobago___1949`

- Staff-list name: **Branday, W. J** | colony: **Trinidad and Tobago** | listed 1949–1954 | editions [1949, 1953, 1954]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | W. J. Branday | Medical Superintendent and Chief Tuberculosis Officer | Sanatorium and Clinics | — | — |
| 1953 | W. J. Branday | Chief Tuberculosis Officer and Medical Superintendent, Sanatorium and Clinics | Civil Establishment | — | — |
| 1954 | W. J. Branday | Chief Tuberculosis Officer and Medical Superintendent, Sanatorium and Clinics | Civil Establishment | — | — |

### Deterministic checks: `branday_w-j_b1901` vs `Branday, W. J___Trinidad and Tobago___1949`

- [PASS] surname_gate: bio 'BRANDAY' vs stint 'Branday, W. J' (exact)
- [PASS] initials: bio ['W', 'J'] ~ stint ['W', 'J']
- [PASS] age_gate: stint starts 1949, birth 1901 (age 48)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1954
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

