<!-- {"case_id": "case_walton_g-a_b1916", "bio_ids": ["walton_g-a_b1916"], "stint_ids": ["Walton, A___Jamaica___1937"]} -->
# Dossier case_walton_g-a_b1916

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 36 official(s) with this surname in the graph's staff lists; 13 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Walton, A___Jamaica___1937` is also gate-compatible with biography(ies) outside this case: ['walton_a-b_b1904', 'walton_arthur-st-george_b1908'] (already linked elsewhere or filtered).

## Biography `walton_g-a_b1916`

- Printed name: **WALTON, G. A**
- Birth year: 1916 (attested in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1957-L28154.v` — printed in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> WALTON, G. A.—b. 1916; ed. Bristol Univ.; med. entom., S.L., 1943; secon. for research into relapsing fever to L.S.H.T.M., 1947; secon., Ken., 1948; secon., E.A.C.S.O., 1950.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1943 | med. entom. | Sierra Leone | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1947 | secon. for research into relapsing fever to L.S.H.T.M | Sierra Leone *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1948 | secon. | Kenya | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 3 | 1950 | secon., E.A.C.S.O | Kenya *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Walton, A___Jamaica___1937`

- Staff-list name: **Walton, A** | colony: **Jamaica** | listed 1937–1940 | editions [1937, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1937 | A. Walton | Matron | Public Hospital, Kingston | — | — |
| 1940 | Miss A. Walton | Matron | Public Hospital, Kingston | — | — |

### Deterministic checks: `walton_g-a_b1916` vs `Walton, A___Jamaica___1937`

- [PASS] surname_gate: bio 'WALTON' vs stint 'Walton, A' (exact)
- [PASS] initials: bio ['G', 'A'] ~ stint ['A']
- [PASS] age_gate: stint starts 1937, birth 1916 (age 21)
- [FAIL] colony: no placed event resolves to 'Jamaica'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1937-1940
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

