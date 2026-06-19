<!-- {"case_id": "case_trenaman_k-w_b1924", "bio_ids": ["trenaman_k-w_b1924"], "stint_ids": ["Trenaman, K. W___Western Pacific___1957"]} -->
# Dossier case_trenaman_k-w_b1924

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `trenaman_k-w_b1924`

- Printed name: **TRENAMAN, K. W**
- Birth year: 1924 (attested in editions [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Honours: O.B.E (1965)
- Appears in editions: [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1959-L28724.v` — printed in editions [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> TRENAMAN, K. W., O.B.E. (1965).—b. 1924; ed. Okehampton Gram. Sch., and Exeter Coll., Oxford; mil. serv., 1943–46, R.A.F.; asst. consvr., forests, Uga., 1949; chief forest offr., B.S.I.P., 1956.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1949 | asst. consvr., forests | Uganda | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1956 | chief forest offr., B.S.I.P | Uganda *(inherited from previous clause)* | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Trenaman, K. W___Western Pacific___1957`

- Staff-list name: **Trenaman, K. W** | colony: **Western Pacific** | listed 1957–1966 | editions [1957, 1958, 1959, 1960, 1961, 1962, 1964, 1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1957 | K. W. Trenaman | Chief Forestry Officer | Civil Establishment | — | — |
| 1958 | K. W. Trenaman | Chief Forestry Officer | Civil Establishment | — | — |
| 1959 | K. W. Trenaman | Chief Forestry Officer | Civil Establishment | — | — |
| 1960 | K. W. Trenaman | Chief Forestry Officer | Civil Establishment | — | — |
| 1961 | K. W. Trenaman | Chief Forestry Officer | Civil Establishment | — | — |
| 1962 | K. W. Trenaman | Chief Forestry Officer | Civil Establishment | — | — |
| 1964 | K. W. Trenaman | Chief Forestry Officer | Civil Establishment | — | — |
| 1965 | K. W. Trenaman | Chief Forestry Officer | Civil Establishment | — | — |
| 1966 | K. W. Trenaman | Chief Forestry Officer | Civil Establishment | — | — |

### Deterministic checks: `trenaman_k-w_b1924` vs `Trenaman, K. W___Western Pacific___1957`

- [PASS] surname_gate: bio 'TRENAMAN' vs stint 'Trenaman, K. W' (exact)
- [PASS] initials: bio ['K', 'W'] ~ stint ['K', 'W']
- [PASS] age_gate: stint starts 1957, birth 1924 (age 33)
- [FAIL] colony: no placed event resolves to 'Western Pacific'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1957-1966
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

