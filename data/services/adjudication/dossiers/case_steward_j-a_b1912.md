<!-- {"case_id": "case_steward_j-a_b1912", "bio_ids": ["steward_j-a_b1912"], "stint_ids": ["Steward, J. A___High Commission Territories___1959"]} -->
# Dossier case_steward_j-a_b1912

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 10 official(s) with this surname in the graph's staff lists; 13 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `steward_j-a_b1912`

- Printed name: **STEWARD, J. A.**
- Birth year: 1912 (attested in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965])
- Honours: C.B.E. (1960), M.B.E.
- Appears in editions: [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965]

### Verbatim printed entry text (OCR)

**Version `col1957-L27508.v` — printed in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965]:**

> STEWARD, J. A., C.B.E. (1960), M.B.E.—b. 1912; ed. Haileybury Coll. and R.M.C., Sandhurst; Indian army and political serv., 1936-47, maj.; D.O., Basuto, 1947; secon. high comsnr's. off., 1953; secon. C.O., 1955; admin. sec., high comsnr's. off., B.B. and S., 1956-64.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1936–1947 | Indian army and political serv., maj. | — | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 1 | 1947 | D.O. | Basutoland | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 2 | 1953 | secon. high comsnr's. off. | — | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 3 | 1955 | secon. C.O. | — | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 4 | 1956–1964 | admin. sec., high comsnr's. off. | Basutoland, Bechuanaland and Swaziland | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |

## Candidate stint `Steward, J. A___High Commission Territories___1959`

- Staff-list name: **Steward, J. A** | colony: **High Commission Territories** | listed 1959–1962 | editions [1959, 1960, 1962]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1959 | J. A. Steward | Administrative Secretary | HIGH COMMISSIONER'S OFFICE | M.B.E. | — |
| 1960 | J. A. Steward | Administrative Secretary | HIGH COMMISSIONER'S OFFICE | C.B.E. | — |
| 1962 | J. A. Steward | Administrative Secretary | HIGH COMMISSIONER'S OFFICE | C.B.E. | — |

### Deterministic checks: `steward_j-a_b1912` vs `Steward, J. A___High Commission Territories___1959`

- [PASS] surname_gate: bio 'STEWARD' vs stint 'Steward, J. A' (exact)
- [PASS] initials: bio ['J', 'A'] ~ stint ['J', 'A']
- [PASS] age_gate: stint starts 1959, birth 1912 (age 47)
- [FAIL] colony: no placed event resolves to 'High Commission Territories'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1959-1962
- [FAIL] position_sim: no overlapping placed event to compare
- [PASS] honour: shared: C.B.E., M.B.E.
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

