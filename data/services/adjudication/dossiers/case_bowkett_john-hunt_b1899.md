<!-- {"case_id": "case_bowkett_john-hunt_b1899", "bio_ids": ["bowkett_john-hunt_b1899"], "stint_ids": ["Bowkett, J. H___Uganda___1937"]} -->
# Dossier case_bowkett_john-hunt_b1899

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `bowkett_john-hunt_b1899`

- Printed name: **BOWKETT, John Hunt**
- Birth year: 1899 (attested in editions [1949, 1950, 1951])
- Appears in editions: [1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1949-L30591.v` — printed in editions [1949, 1950, 1951]:**

> BOWKETT, John Hunt.—b. 1899; on mil. serv., 1916-23; apptd. T.T., 1928; Uga., 1934; govt. printer, Maur., 1940; Zanz., 1947; Aden, 1950.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | apptd. T.T | — | [1949, 1950, 1951] |
| 1 | 1934 | apptd. T.T | Uganda | [1949, 1950, 1951] |
| 2 | 1940 | govt. printer | Mauritius | [1949, 1950, 1951] |
| 3 | 1947 | govt. printer | Zanzibar | [1949, 1950, 1951] |
| 4 | 1950 | govt. printer | Aden | [1949, 1950, 1951] |

## Candidate stint `Bowkett, J. H___Uganda___1937`

- Staff-list name: **Bowkett, J. H** | colony: **Uganda** | listed 1937–1939 | editions [1937, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1937 | J. H. Bowkett | Second Assistant Printer | Printing and Stationery Department | — | — |
| 1939 | J. H. Bowkett | Second Assistant Printer | Printing and Stationery Department | — | — |

### Deterministic checks: `bowkett_john-hunt_b1899` vs `Bowkett, J. H___Uganda___1937`

- [PASS] surname_gate: bio 'BOWKETT' vs stint 'Bowkett, J. H' (exact)
- [PASS] initials: bio ['J', 'H'] ~ stint ['J', 'H']
- [PASS] age_gate: stint starts 1937, birth 1899 (age 38)
- [PASS] colony: 1 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1937-1939
- [FAIL] position_sim: best 25 vs bar 60: 'apptd. T.T' ~ 'Second Assistant Printer'
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

