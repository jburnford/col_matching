<!-- {"case_id": "case_kerr_a-e_b1912", "bio_ids": ["kerr_a-e_b1912"], "stint_ids": ["Kerr, A. E___Trinidad and Tobago___1953"]} -->
# Dossier case_kerr_a-e_b1912

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 68 official(s) with this surname in the graph's staff lists; 23 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `kerr_a-e_b1912`

- Printed name: **KERR, A. E**
- Birth year: 1912 (attested in editions [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962])
- Appears in editions: [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962]

### Verbatim printed entry text (OCR)

**Version `col1953-L18024.v` — printed in editions [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962]:**

> KERR, A. E.—b. 1912; ed. Queen’s Royal Coll., Trin., and Lond. Univ.; asst. govt. chmst., Trin., 1941; dep. govt. chmst., 1950; govt. chmst., 1957.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1941 | asst. govt. chmst. | Trinidad | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962] |
| 1 | 1950 | dep. govt. chmst | Trinidad *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962] |
| 2 | 1957 | govt. chmst | Trinidad *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962] |

## Candidate stint `Kerr, A. E___Trinidad and Tobago___1953`

- Staff-list name: **Kerr, A. E** | colony: **Trinidad and Tobago** | listed 1953–1962 | editions [1953, 1954, 1962]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1953 | A. E. Kerr | Deputy Government Chemist | Civil Establishment | — | — |
| 1954 | A. E. Kerr | Deputy Government Chemist | Civil Establishment | — | — |
| 1962 | A. E. Kerr | Government Chemist | Civil Establishment | — | — |

### Deterministic checks: `kerr_a-e_b1912` vs `Kerr, A. E___Trinidad and Tobago___1953`

- [PASS] surname_gate: bio 'KERR' vs stint 'Kerr, A. E' (exact)
- [PASS] initials: bio ['A', 'E'] ~ stint ['A', 'E']
- [PASS] age_gate: stint starts 1953, birth 1912 (age 41)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1953-1962
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

