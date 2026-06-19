<!-- {"case_id": "case_argeant_edward-lewis_b1901", "bio_ids": ["argeant_edward-lewis_b1901"], "stint_ids": ["Sargeant, E___Barbados___1924"]} -->
# Dossier case_argeant_edward-lewis_b1901

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `argeant_edward-lewis_b1901`

- Printed name: **ARGEANT, Edward Lewis**
- Birth year: 1901 (attested in editions [1951])
- Appears in editions: [1951]

### Verbatim printed entry text (OCR)

**Version `col1951-L42278.v` — printed in editions [1951]:**

> ARGEANT, Edward Lewis.—b. 1901; ed. Pamphylia High Sch.; clk., rlwy., Trin., 1918; treasury, 1931; prin. offr., 1947; asst. acctnt.-gen., 1948.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1918 | clk., rlwy. | Trinidad | [1951] |
| 1 | 1931 | treasury | Trinidad *(inherited from previous clause)* | [1951] |
| 2 | 1947 | prin. offr | Trinidad *(inherited from previous clause)* | [1951] |
| 3 | 1948 | asst. acctnt.-gen | Trinidad *(inherited from previous clause)* | [1951] |

## Candidate stint `Sargeant, E___Barbados___1924`

- Staff-list name: **Sargeant, E** | colony: **Barbados** | listed 1924–1925 | editions [1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1924 | Miss E. Sargeant | Clerk | Post Office | — | — |
| 1925 | Miss E. Sargeant | 6th Grade Clerk | Post Office | — | — |

### Deterministic checks: `argeant_edward-lewis_b1901` vs `Sargeant, E___Barbados___1924`

- [PASS] surname_gate: bio 'ARGEANT' vs stint 'Sargeant, E' (fuzzy:1)
- [PASS] initials: bio ['E', 'L'] ~ stint ['E']
- [PASS] age_gate: stint starts 1924, birth 1901 (age 23)
- [FAIL] colony: no placed event resolves to 'Barbados'
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

