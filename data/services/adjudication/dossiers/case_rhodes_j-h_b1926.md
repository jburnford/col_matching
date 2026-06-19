<!-- {"case_id": "case_rhodes_j-h_b1926", "bio_ids": ["rhodes_j-h_b1926"], "stint_ids": ["Rhodes, J. H___High Commission Territories___1959"]} -->
# Dossier case_rhodes_j-h_b1926

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 16 official(s) with this surname in the graph's staff lists; 17 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `rhodes_j-h_b1926`

- Printed name: **RHODES, J. H**
- Birth year: 1926 (attested in editions [1961, 1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1961-L26638.v` — printed in editions [1961, 1962, 1963, 1964, 1965, 1966]:**

> RHODES, J. H.—b. 1926; ed. Haileybury Coll., Reading and Camb. Univs.; agric. offr., N. Rhod., 1949; secon., Basuto., as prin. agric. offr., 1959.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1949 | agric. offr. | Northern Rhodesia | [1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1959 | secon., Basuto., as prin. agric. offr | Northern Rhodesia *(inherited from previous clause)* | [1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Rhodes, J. H___High Commission Territories___1959`

- Staff-list name: **Rhodes, J. H** | colony: **High Commission Territories** | listed 1959–1960 | editions [1959, 1960]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1959 | J. H. Rhodes | Principal Agricultural Officer | BASUTOLAND | — | — |
| 1960 | J. H. Rhodes | Principal Agricultural Officer | BASUTOLAND | — | — |

### Deterministic checks: `rhodes_j-h_b1926` vs `Rhodes, J. H___High Commission Territories___1959`

- [PASS] surname_gate: bio 'RHODES' vs stint 'Rhodes, J. H' (exact)
- [PASS] initials: bio ['J', 'H'] ~ stint ['J', 'H']
- [PASS] age_gate: stint starts 1959, birth 1926 (age 33)
- [FAIL] colony: no placed event resolves to 'High Commission Territories'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1959-1960
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

