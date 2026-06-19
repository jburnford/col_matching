<!-- {"case_id": "case_grason_william_b1909", "bio_ids": ["grason_william_b1909"], "stint_ids": ["Grason, W___Gold Coast___1949"]} -->
# Dossier case_grason_william_b1909

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['grason_william_b1909'] carry a single initial only — the namesake trap applies.

## Biography `grason_william_b1909`

- Printed name: **GRASON, William**
- Birth year: 1909 (attested in editions [1950, 1951])
- Appears in editions: [1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1950-L35854.v` — printed in editions [1950, 1951]:**

> GRASON, William, B.Sc. (hons.) (Durham).—b. 1909; ed. Wheelwright Gram. Sch., Dewsbury, and Durham Univ.; senr. mstr. and hdmstr., Gram. Sch., Dominica, 1939; educ. offr., G.C., 1947.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1939 | senr. mstr. and hdmstr., Gram. Sch. | Dominica | [1950, 1951] |

## Candidate stint `Grason, W___Gold Coast___1949`

- Staff-list name: **Grason, W** | colony: **Gold Coast** | listed 1949–1950 | editions [1949, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | W. Grason | Education Officer | Education | — | — |
| 1950 | W. Grason | Education Officers | Education | — | — |

### Deterministic checks: `grason_william_b1909` vs `Grason, W___Gold Coast___1949`

- [PASS] surname_gate: bio 'GRASON' vs stint 'Grason, W' (exact)
- [PASS] initials: bio ['W'] ~ stint ['W']
- [PASS] age_gate: stint starts 1949, birth 1909 (age 40)
- [FAIL] colony: no placed event resolves to 'Gold Coast'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1950
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

