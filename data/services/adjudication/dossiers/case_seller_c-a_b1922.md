<!-- {"case_id": "case_seller_c-a_b1922", "bio_ids": ["seller_c-a_b1922"], "stint_ids": ["Seller, C. A___Fiji___1950", "Seller, C. A___Fiji___1962"]} -->
# Dossier case_seller_c-a_b1922

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `seller_c-a_b1922`

- Printed name: **SELLER, C. A**
- Birth year: 1922 (attested in editions [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1959-L27739.v` — printed in editions [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> SELLER, C. A.—b. 1922; ed. Bexhill Sch., and New Coll., Oxford; admin. offr., cl. II, Fiji, 1944; C.O., 1951-53; cl. IIA, 1958; cl. I, 1961; secon. principal, C.O., 1963.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1944 | admin. offr., cl. II | Fiji | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1951–1953 | admin. offr., cl. II | Colonial Office | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1958 | cl. IIA | Colonial Office *(inherited from previous clause)* | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 3 | 1961 | cl. I | Colonial Office *(inherited from previous clause)* | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 4 | 1963 | secon. principal | Colonial Office | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Seller, C. A___Fiji___1950`

- Staff-list name: **Seller, C. A** | colony: **Fiji** | listed 1950–1951 | editions [1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | C. A. Seller | Administrative Officer (Grade II) | District Administration | — | — |
| 1951 | C. A. Seller | Administrative Officer (Grade II) | District Administration | — | — |

### Deterministic checks: `seller_c-a_b1922` vs `Seller, C. A___Fiji___1950`

- [PASS] surname_gate: bio 'SELLER' vs stint 'Seller, C. A' (exact)
- [PASS] initials: bio ['C', 'A'] ~ stint ['C', 'A']
- [PASS] age_gate: stint starts 1950, birth 1922 (age 28)
- [PASS] colony: 1 placed event(s) resolve to 'Fiji'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1950-1951
- [FAIL] position_sim: best 60 vs bar 60: 'admin. offr., cl. II' ~ 'Administrative Officer (Grade II)'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Seller, C. A___Fiji___1962`

- Staff-list name: **Seller, C. A** | colony: **Fiji** | listed 1962–1966 | editions [1962, 1963, 1964, 1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1962 | C. A. Seller | Administrative Officers, Class I. | Civil Establishment | — | — |
| 1963 | C. A. Seller | Administrative Officer Class I | Civil Establishment | — | — |
| 1964 | C. A. Seller | Administrative Officer Class I | Civil Establishment | — | — |
| 1965 | C. A. Seller | Administrative Officers Class I. | Civil Establishment | — | — |
| 1966 | C. A. Seller | Administrative Officers Class I | Civil Establishment | — | — |

### Deterministic checks: `seller_c-a_b1922` vs `Seller, C. A___Fiji___1962`

- [PASS] surname_gate: bio 'SELLER' vs stint 'Seller, C. A' (exact)
- [PASS] initials: bio ['C', 'A'] ~ stint ['C', 'A']
- [PASS] age_gate: stint starts 1962, birth 1922 (age 40)
- [PASS] colony: 1 placed event(s) resolve to 'Fiji'
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

