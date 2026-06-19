<!-- {"case_id": "case_lewis_w-j_b1917", "bio_ids": ["lewis_w-j_b1917"], "stint_ids": ["Lewis, W. J___Falkland Islands___1939"]} -->
# Dossier case_lewis_w-j_b1917

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 157 official(s) with this surname in the graph's staff lists; 67 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Lewis, W. J___Falkland Islands___1939` is also gate-compatible with biography(ies) outside this case: ['lewis_j_b1924'] (already linked elsewhere or filtered).

## Biography `lewis_w-j_b1917`

- Printed name: **LEWIS, W. J**
- Birth year: 1917 (attested in editions [1960, 1961, 1962])
- Appears in editions: [1960, 1961, 1962]

### Verbatim printed entry text (OCR)

**Version `col1960-L25253.v` — printed in editions [1960, 1961, 1962]:**

> LEWIS, W. J.—b. 1917; ed. Hereford High Sch.; mil. serv., 1939-45; assessment offr., Nig., 1949; senr., 1953; asst. comsnt., income tax, 1954; senr. asst. comsnt., 1955; dep. chmn., fed. bd. of inland rev., 1958-61.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1949 | assessment offr. | Nigeria | [1960, 1961, 1962] |
| 1 | 1953 | senr | Nigeria *(inherited from previous clause)* | [1960, 1961, 1962] |
| 2 | 1954 | asst. comsnt., income tax | Nigeria *(inherited from previous clause)* | [1960, 1961, 1962] |
| 3 | 1955 | senr. asst. comsnt | Nigeria *(inherited from previous clause)* | [1960, 1961, 1962] |
| 4 | 1958–1961 | dep. chmn., fed. bd. of inland rev | Nigeria *(inherited from previous clause)* | [1960, 1961, 1962] |

## Candidate stint `Lewis, W. J___Falkland Islands___1939`

- Staff-list name: **Lewis, W. J** | colony: **Falkland Islands** | listed 1939–1940 | editions [1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | W. J. Lewis | Principal Keeper | Port and Marine | — | — |
| 1940 | W. J. Lewis | Principal Keeper | Cape Pembroke Lighthouse | — | — |

### Deterministic checks: `lewis_w-j_b1917` vs `Lewis, W. J___Falkland Islands___1939`

- [PASS] surname_gate: bio 'LEWIS' vs stint 'Lewis, W. J' (exact)
- [PASS] initials: bio ['W', 'J'] ~ stint ['W', 'J']
- [PASS] age_gate: stint starts 1939, birth 1917 (age 22)
- [FAIL] colony: no placed event resolves to 'Falkland Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1939-1940
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

