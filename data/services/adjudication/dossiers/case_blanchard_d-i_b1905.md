<!-- {"case_id": "case_blanchard_d-i_b1905", "bio_ids": ["blanchard_d-i_b1905"], "stint_ids": ["Blanchard, D. I___Leeward Islands___1924"]} -->
# Dossier case_blanchard_d-i_b1905

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 21 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `blanchard_d-i_b1905`

- Printed name: **BLANCHARD, D. I**
- Birth year: 1905 (attested in editions [1955, 1956, 1958])
- Appears in editions: [1955, 1956, 1958]

### Verbatim printed entry text (OCR)

**Version `col1955-L19781.v` — printed in editions [1955, 1956, 1958]:**

> BLANCHARD, D. I.—b. 1905; ed Dominica Gram. Sch.; asst. master Dominica Gram. Sch., 1923; clk., govt. depts., 1929-49; examr., accsts., Dominica, 1949, (later senr. examr.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1923 | asst. master Dominica Gram. Sch | — | [1955, 1956, 1958] |
| 1 | 1929–1949 | clk., govt. depts | — | [1955, 1956, 1958] |
| 2 | 1949 | examr., accsts. | Dominica | [1955, 1956, 1958] |

## Candidate stint `Blanchard, D. I___Leeward Islands___1924`

- Staff-list name: **Blanchard, D. I** | colony: **Leeward Islands** | listed 1924–1925 | editions [1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1924 | D. I. Blanchard | 2nd Assistant Master | Educational Establishment | — | — |
| 1925 | D. I. Blanchard | 2nd Assistant Master, Dominica Grammar School | Educational Establishment | — | — |

### Deterministic checks: `blanchard_d-i_b1905` vs `Blanchard, D. I___Leeward Islands___1924`

- [PASS] surname_gate: bio 'BLANCHARD' vs stint 'Blanchard, D. I' (exact)
- [PASS] initials: bio ['D', 'I'] ~ stint ['D', 'I']
- [PASS] age_gate: stint starts 1924, birth 1905 (age 19)
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1924-1925
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

