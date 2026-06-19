<!-- {"case_id": "case_burbeau_jaques_b1860", "bio_ids": ["burbeau_jaques_b1860"], "stint_ids": ["Bureau, Jacques O___Canada___1877", "Bureau, Jacques O___Canada___1905", "Bureau, Jacques O___Canada___1919"]} -->
# Dossier case_burbeau_jaques_b1860

## Case context

- 1 biography(ies) and 3 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['burbeau_jaques_b1860'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Bureau, Jacques O___Canada___1877` is also gate-compatible with biography(ies) outside this case: ['bureau_jacques_b1860'] (already linked elsewhere or filtered).
- NOTE: stint `Bureau, Jacques O___Canada___1905` is also gate-compatible with biography(ies) outside this case: ['bureau_jacques_b1860'] (already linked elsewhere or filtered).
- NOTE: stint `Bureau, Jacques O___Canada___1919` is also gate-compatible with biography(ies) outside this case: ['bureau_jacques_b1860'] (already linked elsewhere or filtered).

## Biography `burbeau_jaques_b1860`

- Printed name: **BURBEAU, JAQUES**
- Birth year: 1860 (attested in editions [1910])
- Appears in editions: [1910]

### Verbatim printed entry text (OCR)

**Version `col1910-L44642.v` — printed in editions [1910]:**

> BURBEAU, HON. JAQUES, K.C., LL.B.—B. 1860; ed. Nicolet Coll. and Laval Univ.; elec. to H. of C., Canada, 1900; re-elected, 1904, 1907, 1908; solr.-gen., 1907.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1900 | elec. to H. of C. | Canada | [1910] |
| 1 | 1904–1908 | re-elected | — | [1910] |
| 2 | 1907 | solr.-gen. | — | [1910] |

## Candidate stint `Bureau, Jacques O___Canada___1877`

- Staff-list name: **Bureau, Jacques O** | colony: **Canada** | listed 1877–1883 | editions [1877, 1878, 1879, 1880, 1883]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | Jacques O. Bureau | Senator | Senate of Canada | — | — |
| 1878 | Jacques O. Bureau | Senator | Senate of Canada | — | — |
| 1879 | Jacques O. Bureau | Senator | Senate of Canada | — | — |
| 1880 | Jacques O. Bureau | Senator | Senators | — | — |
| 1883 | Jacques O. Bureau | Senator | Senators | — | — |

### Deterministic checks: `burbeau_jaques_b1860` vs `Bureau, Jacques O___Canada___1877`

- [PASS] surname_gate: bio 'BURBEAU' vs stint 'Bureau, Jacques O' (fuzzy:1)
- [PASS] initials: bio ['J'] ~ stint ['J', 'O']
- [PASS] age_gate: stint starts 1877, birth 1860 (age 17)
- [PASS] colony: 1 placed event(s) resolve to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1883
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Bureau, Jacques O___Canada___1905`

- Staff-list name: **Bureau, Jacques O** | colony: **Canada** | listed 1905–1908 | editions [1905, 1906, 1908]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | Jacques Bureau | — | — | — | — |
| 1906 | Jacques Bureau | — | — | — | — |
| 1908 | Hon. Jacques Bureau | Solicitor-General | Department of Justice | — | — |
| 1908 | Jacques Bureau | — | Province of Quebec | — | — |
| 1908 | Hon. Jacques Bureau | Solicitor-General | The Cabinet | — | — |

### Deterministic checks: `burbeau_jaques_b1860` vs `Bureau, Jacques O___Canada___1905`

- [PASS] surname_gate: bio 'BURBEAU' vs stint 'Bureau, Jacques O' (fuzzy:1)
- [PASS] initials: bio ['J'] ~ stint ['J', 'O']
- [PASS] age_gate: stint starts 1905, birth 1860 (age 45)
- [PASS] colony: 1 placed event(s) resolve to 'Canada'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1905-1908
- [FAIL] position_sim: best 27 vs bar 60: 'elec. to H. of C.' ~ 'Solicitor-General'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Bureau, Jacques O___Canada___1919`

- Staff-list name: **Bureau, Jacques O** | colony: **Canada** | listed 1919–1922 | editions [1919, 1922]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1919 | J. Bureau | Member of Parliament | House of Commons | — | — |
| 1922 | Jacques Bureau | Minister of Customs and Excise | Customs and Inland Revenue | — | — |
| 1922 | Jacques Bureau | Minister of Customs and Excise | THE MINISTRY | — | — |

### Deterministic checks: `burbeau_jaques_b1860` vs `Bureau, Jacques O___Canada___1919`

- [PASS] surname_gate: bio 'BURBEAU' vs stint 'Bureau, Jacques O' (fuzzy:1)
- [PASS] initials: bio ['J'] ~ stint ['J', 'O']
- [PASS] age_gate: stint starts 1919, birth 1860 (age 59)
- [PASS] colony: 1 placed event(s) resolve to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1919-1922
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

