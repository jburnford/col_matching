<!-- {"case_id": "case_blanchard_r-l_b1907", "bio_ids": ["blanchard_r-l_b1907"], "stint_ids": ["Blanchard, R. L___Windward Islands___1950"]} -->
# Dossier case_blanchard_r-l_b1907

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 21 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `blanchard_r-l_b1907`

- Printed name: **BLANCHARD, R. L**
- Birth year: 1907 (attested in editions [1949, 1950, 1951, 1953, 1954, 1955, 1956, 1958, 1959, 1960, 1961, 1962])
- Appears in editions: [1949, 1950, 1951, 1953, 1954, 1955, 1956, 1958, 1959, 1960, 1961, 1962]

### Verbatim printed entry text (OCR)

**Version `col1949-L30523.v` — printed in editions [1949, 1950, 1951, 1953, 1954, 1955, 1956, 1958, 1959, 1960, 1961, 1962]:**

> BLANCHARD, R. L.—b. 1907 ; ed. Dominica Gram. Sch.; asst. clk., treas., Dominica, 1928 ; clk., various depts., 1928–45 ; labour offr., 1945.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | asst. clk., treas. | Dominica | [1949, 1950, 1951, 1953, 1954, 1955, 1956, 1958, 1959, 1960, 1961, 1962] |
| 1 | 1945 | labour offr | Dominica *(inherited from previous clause)* | [1949, 1950, 1951, 1953, 1954, 1955, 1956, 1958, 1959, 1960, 1961, 1962] |

## Candidate stint `Blanchard, R. L___Windward Islands___1950`

- Staff-list name: **Blanchard, R. L** | colony: **Windward Islands** | listed 1950–1952 | editions [1950, 1952]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | R. L. Blanchard | Labour Officer | LABOUR | — | — |
| 1952 | R. L. Blanchard | Labour Officer | Civil Establishment | — | — |

### Deterministic checks: `blanchard_r-l_b1907` vs `Blanchard, R. L___Windward Islands___1950`

- [PASS] surname_gate: bio 'BLANCHARD' vs stint 'Blanchard, R. L' (exact)
- [PASS] initials: bio ['R', 'L'] ~ stint ['R', 'L']
- [PASS] age_gate: stint starts 1950, birth 1907 (age 43)
- [FAIL] colony: no placed event resolves to 'Windward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1950-1952
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

