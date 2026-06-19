<!-- {"case_id": "case_nichols_e-h_b1925", "bio_ids": ["nichols_e-h_b1925"], "stint_ids": ["Nichols, E. H___Sierra Leone___1949"]} -->
# Dossier case_nichols_e-h_b1925

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 23 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `nichols_e-h_b1925`

- Printed name: **NICHOLS, E. H**
- Birth year: 1925 (attested in editions [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1959-L26385.v` — printed in editions [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> NICHOLS, E. H.—b. 1925; ed. Royal Gram. Sch., Newcastle-on-Tyne, King's Coll., Durham Univ., Queen's Coll., Camb., and I.C.T.A.; agric. offr., S. Leone, 1947; senr., 1954; prin. agric. offr., 1957; asst. dir., agric., fish. and forestry, H.K., 1959.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1947 | agric. offr., S. Leone | — | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1954 | senr | — | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1957 | prin. agric. offr | — | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 3 | 1959 | asst. dir., agric., fish. and forestry | Hong Kong | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Nichols, E. H___Sierra Leone___1949`

- Staff-list name: **Nichols, E. H** | colony: **Sierra Leone** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | E. H. Nichols | Agricultural Officer | Agricultural | — | — |
| 1950 | E. H. Nichols | Agricultural Officers | Agricultural | — | — |
| 1951 | E. H. Nichols | Agricultural Officers | AGRICULTURE | — | — |

### Deterministic checks: `nichols_e-h_b1925` vs `Nichols, E. H___Sierra Leone___1949`

- [PASS] surname_gate: bio 'NICHOLS' vs stint 'Nichols, E. H' (exact)
- [PASS] initials: bio ['E', 'H'] ~ stint ['E', 'H']
- [PASS] age_gate: stint starts 1949, birth 1925 (age 24)
- [FAIL] colony: no placed event resolves to 'Sierra Leone'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
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

