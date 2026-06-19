<!-- {"case_id": "case_pound_albert-edward_b1915", "bio_ids": ["pound_albert-edward_b1915"], "stint_ids": ["Pound, A. E___Kenya___1950"]} -->
# Dossier case_pound_albert-edward_b1915

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `pound_albert-edward_b1915`

- Printed name: **POUND, Albert Edward**
- Birth year: 1915 (attested in editions [1950, 1951])
- Appears in editions: [1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1950-L38814.v` — printed in editions [1950, 1951]:**

> POUND, Albert Edward, B.Sc. (hons) agric. bot.—b. 1915; ed. Sexey's Sch., Bruton, and Reading Univ.; produce inspr., G.C., 1939; Nig., 1939; agric. offr., Ken., 1942; dir., agric., Seychelles (secondment), 1946; resumed duty, Ken., 1947.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1939 | produce inspr. | Gold Coast | [1950, 1951] |
| 1 | 1942 | agric. offr. | Kenya | [1950, 1951] |
| 2 | 1946 | dir., agric., Seychelles (secondment) | Seychelles | [1950, 1951] |
| 3 | 1947 | resumed duty | Kenya | [1950, 1951] |

## Candidate stint `Pound, A. E___Kenya___1950`

- Staff-list name: **Pound, A. E** | colony: **Kenya** | listed 1950–1951 | editions [1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | A. E. Pound | Agricultural Officer | AGRICULTURE | — | — |
| 1951 | A. E. Pound | Agricultural Officer | Agriculture | — | — |

### Deterministic checks: `pound_albert-edward_b1915` vs `Pound, A. E___Kenya___1950`

- [PASS] surname_gate: bio 'POUND' vs stint 'Pound, A. E' (exact)
- [PASS] initials: bio ['A', 'E'] ~ stint ['A', 'E']
- [PASS] age_gate: stint starts 1950, birth 1915 (age 35)
- [PASS] colony: 2 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1950-1951
- [FAIL] position_sim: best 25 vs bar 60: 'resumed duty' ~ 'Agricultural Officer'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

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

