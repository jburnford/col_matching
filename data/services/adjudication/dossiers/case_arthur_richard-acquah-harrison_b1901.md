<!-- {"case_id": "case_arthur_richard-acquah-harrison_b1901", "bio_ids": ["arthur_richard-acquah-harrison_b1901"], "stint_ids": ["Arthur, Raynor___Bahamas___1957"]} -->
# Dossier case_arthur_richard-acquah-harrison_b1901

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 22 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Arthur, Raynor___Bahamas___1957` is also gate-compatible with biography(ies) outside this case: ['arthur_oswald-ratnoh_b1905', 'arthur_raynor_b1903'] (already linked elsewhere or filtered).

## Biography `arthur_richard-acquah-harrison_b1901`

- Printed name: **ARTHUR, Richard Acquah Harrison**
- Birth year: 1901 (attested in editions [1950, 1951])
- Appears in editions: [1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1950-L33289.v` — printed in editions [1950, 1951]:**

> ARTHUR, Richard Acquah Harrison.—b. 1901; ed. Baptist Sch. and Training Coll., Accra; probr., G.C., 1917; 3rd cl. clk., 1918; 4th cl., 1920; 2nd div. clk., 1922; 1st div. offr., 1940; senr. div. offr., 1947; asst. contrlr., posts, 1948.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1917 | probr. | Gold Coast | [1950, 1951] |
| 1 | 1918 | 3rd cl. clk | Gold Coast *(inherited from previous clause)* | [1950, 1951] |
| 2 | 1920 | 4th cl | Gold Coast *(inherited from previous clause)* | [1950, 1951] |
| 3 | 1922 | 2nd div. clk | Gold Coast *(inherited from previous clause)* | [1950, 1951] |
| 4 | 1940 | 1st div. offr | Gold Coast *(inherited from previous clause)* | [1950, 1951] |
| 5 | 1947 | senr. div. offr | Gold Coast *(inherited from previous clause)* | [1950, 1951] |
| 6 | 1948 | asst. contrlr., posts | Gold Coast *(inherited from previous clause)* | [1950, 1951] |

## Candidate stint `Arthur, Raynor___Bahamas___1957`

- Staff-list name: **Arthur, Raynor** | colony: **Bahamas** | listed 1957–1960 | editions [1957, 1958, 1959, 1960]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1957 | Sir Raynor Arthur | Governor and Commander-in-Chief | Civil Establishment | K.C.M.G. | — |
| 1958 | Sir Raynor Arthur | Governor and Commander-in-Chief | Civil Establishment | K.C.M.G. | — |
| 1959 | Sir Raynor Arthur | Governor and Commander-in-Chief | Civil Establishment | K.C.M.G. | — |

### Deterministic checks: `arthur_richard-acquah-harrison_b1901` vs `Arthur, Raynor___Bahamas___1957`

- [PASS] surname_gate: bio 'ARTHUR' vs stint 'Arthur, Raynor' (exact)
- [PASS] initials: bio ['R', 'A', 'H'] ~ stint ['R']
- [PASS] age_gate: stint starts 1957, birth 1901 (age 56)
- [FAIL] colony: no placed event resolves to 'Bahamas'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1957-1960
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

