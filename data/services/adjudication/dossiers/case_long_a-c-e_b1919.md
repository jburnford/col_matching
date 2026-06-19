<!-- {"case_id": "case_long_a-c-e_b1919", "bio_ids": ["long_a-c-e_b1919"], "stint_ids": ["Long, A. C. E___High Commission Territories___1963", "Long, A. C. E___Swaziland___1962"]} -->
# Dossier case_long_a-c-e_b1919

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 38 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `long_a-c-e_b1919`

- Printed name: **LONG, A. C. E**
- Birth year: 1919 (attested in editions [1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Honours: C.B.E (1964), M.B.E (1956)
- Appears in editions: [1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1960-L25363.v` — printed in editions [1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> LONG, A. C. E., C.B.E. (1964), M.B.E. (1956).—b. 1919; ed. Westminster Sch., and Brasenose Coll., Oxford; mil. serv., 1939-45, capt., p.o.w. 1942-45; Burma civil serv., 1946-47; admin. offr., N. Nig., 1948; senr. D.O., 1956; resdt., 1959; dep. resdt. comsnr. and govt. sec., Swaz., 1961; ch. sec.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946–1947 | Burma civil serv | — | [1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1948 | admin. offr. | Northern Nigeria | [1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1956 | senr. D.O | Northern Nigeria *(inherited from previous clause)* | [1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 3 | 1959 | resdt | Northern Nigeria *(inherited from previous clause)* | [1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 4 | 1961 | dep. resdt. comsnr. and govt. sec., Swaz | Northern Nigeria *(inherited from previous clause)* | [1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Long, A. C. E___High Commission Territories___1963`

- Staff-list name: **Long, A. C. E** | colony: **High Commission Territories** | listed 1963–1964 | editions [1963, 1964]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1963 | A. C. E. Long | Deputy Resident Commissioner and Government Secretary | SECRETARIAT | M.B.E. | — |
| 1964 | A. C. E. Long | Chief Secretary | Civil Establishment | — | — |

### Deterministic checks: `long_a-c-e_b1919` vs `Long, A. C. E___High Commission Territories___1963`

- [PASS] surname_gate: bio 'LONG' vs stint 'Long, A. C. E' (exact)
- [PASS] initials: bio ['A', 'C', 'E'] ~ stint ['A', 'C', 'E']
- [PASS] age_gate: stint starts 1963, birth 1919 (age 44)
- [FAIL] colony: no placed event resolves to 'High Commission Territories'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1963-1964
- [FAIL] position_sim: no overlapping placed event to compare
- [PASS] honour: shared: M.B.E
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Long, A. C. E___Swaziland___1962`

- Staff-list name: **Long, A. C. E** | colony: **Swaziland** | listed 1962–1966 | editions [1962, 1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1962 | A. C. E. Long | Deputy Resident Commissioner and Government Secretary | Secretariat | — | — |
| 1965 | A. C. E. Long | Chief Secretary | Secretariat | — | — |
| 1966 | A. C. E. Long | Chief Secretary | Civil Establishment | — | — |

### Deterministic checks: `long_a-c-e_b1919` vs `Long, A. C. E___Swaziland___1962`

- [PASS] surname_gate: bio 'LONG' vs stint 'Long, A. C. E' (exact)
- [PASS] initials: bio ['A', 'C', 'E'] ~ stint ['A', 'C', 'E']
- [PASS] age_gate: stint starts 1962, birth 1919 (age 43)
- [FAIL] colony: no placed event resolves to 'Swaziland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1962-1966
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

