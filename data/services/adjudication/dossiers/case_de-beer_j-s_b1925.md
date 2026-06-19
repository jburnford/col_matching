<!-- {"case_id": "case_de-beer_j-s_b1925", "bio_ids": ["de-beer_j-s_b1925"], "stint_ids": ["de Beer, J. S___High Commission Territories___1960"]} -->
# Dossier case_de-beer_j-s_b1925

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `de-beer_j-s_b1925`

- Printed name: **DE BEER, J. S**
- Birth year: 1925 (attested in editions [1961, 1962, 1963])
- Appears in editions: [1961, 1962, 1963]

### Verbatim printed entry text (OCR)

**Version `col1961-L21326.v` — printed in editions [1961, 1962, 1963]:**

> DE BEER, J. S.—b. 1925; ed. Grey Coll. Sch., Bloemfontein, and Univ. of Stellenbosch; agric. offr., pasture res., Bech. Prot., 1950; agric. extension offr., Union dept. of agric., 1952; agric. offr., Bech. Prot., 1954; dir., agric., 1959.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1950 | agric. offr., pasture res. | Bechuanaland | [1961, 1962, 1963] |
| 1 | 1952 | agric. extension offr., Union dept. of agric | Bechuanaland *(inherited from previous clause)* | [1961, 1962, 1963] |
| 2 | 1954 | agric. offr. | Bechuanaland | [1961, 1962, 1963] |
| 3 | 1959 | dir., agric | Bechuanaland *(inherited from previous clause)* | [1961, 1962, 1963] |

## Candidate stint `de Beer, J. S___High Commission Territories___1960`

- Staff-list name: **de Beer, J. S** | colony: **High Commission Territories** | listed 1960–1963 | editions [1960, 1963]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1960 | J. de Beer | Director of Agriculture | BECHUANALAND PROTECTORATE | — | — |
| 1963 | J. S. de Beer | Director of Agriculture | Secretariat | — | — |

### Deterministic checks: `de-beer_j-s_b1925` vs `de Beer, J. S___High Commission Territories___1960`

- [PASS] surname_gate: bio 'DE BEER' vs stint 'de Beer, J. S' (exact)
- [PASS] initials: bio ['J', 'S'] ~ stint ['J', 'S']
- [PASS] age_gate: stint starts 1960, birth 1925 (age 35)
- [FAIL] colony: no placed event resolves to 'High Commission Territories'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1960-1963
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

