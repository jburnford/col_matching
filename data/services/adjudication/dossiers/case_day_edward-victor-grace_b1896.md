<!-- {"case_id": "case_day_edward-victor-grace_b1896", "bio_ids": ["day_edward-victor-grace_b1896"], "stint_ids": ["Day, E. V. G___Federation of Malaya___1950", "Day, E. V. G___Straits Settlements___1934"]} -->
# Dossier case_day_edward-victor-grace_b1896

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 47 official(s) with this surname in the graph's staff lists; 13 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Day, E. V. G___Federation of Malaya___1950` is also gate-compatible with biography(ies) outside this case: ['day_edward-victor-grave_b1896'] (already linked elsewhere or filtered).
- NOTE: stint `Day, E. V. G___Straits Settlements___1934` is also gate-compatible with biography(ies) outside this case: ['day_edward-victor-grave_b1896'] (already linked elsewhere or filtered).

## Biography `day_edward-victor-grace_b1896`

- Printed name: **DAY, Edward Victor Grace**
- Birth year: 1896 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L32166.v` — printed in editions [1948, 1949, 1950, 1951]:**

> DAY, Edward Victor Grace.—b. 1896; ed. Christ's Coll., Christchurch and Timaru High Sch., N.Z.; on mil serv., 1943-46, col.; cadet, Mal. C.S., 1921; cl. V, 1924; cl. IV, 1928; cl. III, 1933; cl. II, 1938; res. comsnr., Malacca, 1946; staff offr., gr. B, Mal., 1948.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1921 | cadet, Mal. C.S | Malaya | [1948, 1949, 1950, 1951] |
| 1 | 1924 | cl. V | Malaya *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 2 | 1928 | cl. IV | Malaya *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 3 | 1933 | cl. III | Malaya *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 4 | 1938 | cl. II | Malaya *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 5 | 1946 | res. comsnr., Malacca | Malaya *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 6 | 1948 | staff offr., gr. B | Malaya | [1948, 1949, 1950, 1951] |

## Candidate stint `Day, E. V. G___Federation of Malaya___1950`

- Staff-list name: **Day, E. V. G** | colony: **Federation of Malaya** | listed 1950–1952 | editions [1950, 1951, 1952]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | E. V. G. Day | British Adviser, Kedah | Civil Establishment | — | — |
| 1951 | E. V. G. Day | British Adviser, Kedah | ADMINISTRATIVE Secretariat | — | — |
| 1952 | E. V. G. Day | British Adviser, Kedah | Civil Establishment | C.M.G. | — |

### Deterministic checks: `day_edward-victor-grace_b1896` vs `Day, E. V. G___Federation of Malaya___1950`

- [PASS] surname_gate: bio 'DAY' vs stint 'Day, E. V. G' (exact)
- [PASS] initials: bio ['E', 'V', 'G'] ~ stint ['E', 'V', 'G']
- [PASS] age_gate: stint starts 1950, birth 1896 (age 54)
- [PASS] colony: 7 placed event(s) resolve to 'Federation of Malaya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1950-1952
- [FAIL] position_sim: best 28 vs bar 60: 'staff offr., gr. B' ~ 'British Adviser, Kedah'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Day, E. V. G___Straits Settlements___1934`

- Staff-list name: **Day, E. V. G** | colony: **Straits Settlements** | listed 1934–1939 | editions [1934, 1936, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | E. V. G. Day | 2nd Assistant Colonial Secretary (B) | Colonial Secretary's Office | — | — |
| 1936 | E. V. G. Day | Class III Officer | Class III | — | — |
| 1939 | E. V. G. Day | Class II | Civil Establishment | — | — |

### Deterministic checks: `day_edward-victor-grace_b1896` vs `Day, E. V. G___Straits Settlements___1934`

- [PASS] surname_gate: bio 'DAY' vs stint 'Day, E. V. G' (exact)
- [PASS] initials: bio ['E', 'V', 'G'] ~ stint ['E', 'V', 'G']
- [PASS] age_gate: stint starts 1934, birth 1896 (age 38)
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1934-1939
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

