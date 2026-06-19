<!-- {"case_id": "case_knott_alexander-john_b1905", "bio_ids": ["knott_alexander-john_b1905"], "stint_ids": ["Knott, A. J___Gambia___1936"]} -->
# Dossier case_knott_alexander-john_b1905

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `knott_alexander-john_b1905`

- Printed name: **KNOTT, Alexander John**
- Birth year: 1905 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L33873.v` — printed in editions [1948, 1949, 1950, 1951]:**

> KNOTT, Alexander John.—b. 1905; ed. Perse Sch. and Peterhouse, Camb., M.A. (Cantab.); cadet, Nig., 1928; admin. offr., cl. II, 1946; cl. I, 1948; temp. trans. to Gambia, 1935-40.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | cadet | Nigeria | [1948, 1949, 1950, 1951] |
| 1 | 1935–1940 | temp. trans. to Gambia | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 2 | 1946 | admin. offr., cl. II | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 3 | 1948 | cl. I | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Knott, A. J___Gambia___1936`

- Staff-list name: **Knott, A. J** | colony: **Gambia** | listed 1936–1940 | editions [1936, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | A. J. Knott | Commissioners and Assistant Commissioners | Provincial Administration | — | — |
| 1937 | A. J. Knott | Commissioner | Provincial Administration | — | — |
| 1939 | A. J. Knott | Commissioners and Assistant Commissioners | Provincial Administration | — | — |
| 1940 | A. J. Knott | Commissioner/Assistant Commissioner | Provincial Administration | — | — |

### Deterministic checks: `knott_alexander-john_b1905` vs `Knott, A. J___Gambia___1936`

- [PASS] surname_gate: bio 'KNOTT' vs stint 'Knott, A. J' (exact)
- [PASS] initials: bio ['A', 'J'] ~ stint ['A', 'J']
- [PASS] age_gate: stint starts 1936, birth 1905 (age 31)
- [FAIL] colony: no placed event resolves to 'Gambia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1936-1940
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

