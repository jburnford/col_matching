<!-- {"case_id": "case_cromwell_leopold-duncan-godfrey_b1901", "bio_ids": ["cromwell_leopold-duncan-godfrey_b1901"], "stint_ids": ["Cromwell, L. D. G___Windward Islands___1922"]} -->
# Dossier case_cromwell_leopold-duncan-godfrey_b1901

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `cromwell_leopold-duncan-godfrey_b1901`

- Printed name: **CROMWELL, Leopold Duncan Godfrey**
- Birth year: 1901 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L32037.v` — printed in editions [1948, 1949, 1950, 1951]:**

> CROMWELL, Leopold Duncan Godfrey.—b. 1901; ed. Granada Boys' Sch. and London Sch. of Econ.; apptd. Gren.; maths. and sc. mstr., 1923; W.I. overseer, agric. dept., Nig., 1924; senr. agric. asst., 1937; senr. asst. agric. offr., 1942; agric. offr., 1947.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1923 | maths. and sc. mstr | — | [1948, 1949, 1950, 1951] |
| 1 | 1924 | W.I. overseer, agric. dept. | Nigeria | [1948, 1949, 1950, 1951] |
| 2 | 1937 | senr. agric. asst | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 3 | 1942 | senr. asst. agric. offr | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 4 | 1947 | agric. offr | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Cromwell, L. D. G___Windward Islands___1922`

- Staff-list name: **Cromwell, L. D. G** | colony: **Windward Islands** | listed 1922–1923 | editions [1922, 1923]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | L. D. G. Cromwell | Clerk | Carriacou District | — | — |
| 1923 | L. D. G. Cromwell | Clerk | Carriacou District | — | — |

### Deterministic checks: `cromwell_leopold-duncan-godfrey_b1901` vs `Cromwell, L. D. G___Windward Islands___1922`

- [PASS] surname_gate: bio 'CROMWELL' vs stint 'Cromwell, L. D. G' (exact)
- [PASS] initials: bio ['L', 'D', 'G'] ~ stint ['L', 'D', 'G']
- [PASS] age_gate: stint starts 1922, birth 1901 (age 21)
- [FAIL] colony: no placed event resolves to 'Windward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1922-1923
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

