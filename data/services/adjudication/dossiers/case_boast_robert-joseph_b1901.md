<!-- {"case_id": "case_boast_robert-joseph_b1901", "bio_ids": ["boast_robert-joseph_b1901"], "stint_ids": ["Boast, R. J___Hong Kong___1939", "Boast, R. J___Singapore___1951"]} -->
# Dossier case_boast_robert-joseph_b1901

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 11 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `boast_robert-joseph_b1901`

- Printed name: **BOAST, Robert Joseph**
- Birth year: 1901 (attested in editions [1951])
- Honours: I.R.E
- Appears in editions: [1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1951-L36288.v` — printed in editions [1951]:**

> BOAST, Robert Joseph, A.M. (Brit.), I.R.E.—b. 1901; ed. Sir Joseph Williamson's Math. Sch., Rochester; internee, 1942-45; wireless tech., H.K., 1929; wireless sub. engnr., 1935; asst. contrlr., telecoms., Mal., 1941.

**Version `col1950-L33775.v` — printed in editions [1950]:**

> BOAST, Robert Joseph.—b. 1901; ed. Sir Joseph Williamson's Math. Sch., Rochester, Kent, 1st cl. P.M.G. cert. in radio, A.M. (Brit.), I.R.E.; wireless technician, H.K., 1929; wireless sub-engnr., 1938; asst. contrlr., telecoms., S'pore, 1941.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1929 | wireless tech. | Hong Kong | [1950, 1951] |
| 1 | 1935 | wireless sub. engnr | Hong Kong *(inherited from previous clause)* | [1951] |
| 2 | 1938 | wireless sub-engnr | Hong Kong *(inherited from previous clause)* | [1950] |
| 3 | 1941 | asst. contrlr., telecoms. | Malaya | [1950, 1951] |
| 4 | 1942–1945 | internee | — | [1951] |

## Candidate stint `Boast, R. J___Hong Kong___1939`

- Staff-list name: **Boast, R. J** | colony: **Hong Kong** | listed 1939–1940 | editions [1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | R. J. Boast | Wireless Sub-Engineer | Wireless | — | — |
| 1940 | R. J. Boast | Wireless Sub-Engineer | Post Office | — | — |

### Deterministic checks: `boast_robert-joseph_b1901` vs `Boast, R. J___Hong Kong___1939`

- [PASS] surname_gate: bio 'BOAST' vs stint 'Boast, R. J' (exact)
- [PASS] initials: bio ['R', 'J'] ~ stint ['R', 'J']
- [PASS] age_gate: stint starts 1939, birth 1901 (age 38)
- [PASS] colony: 3 placed event(s) resolve to 'Hong Kong'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1939-1940
- [PASS] position_sim: best 92 vs bar 60: 'wireless sub-engnr' ~ 'Wireless Sub-Engineer'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

## Candidate stint `Boast, R. J___Singapore___1951`

- Staff-list name: **Boast, R. J** | colony: **Singapore** | listed 1951–1953 | editions [1951, 1953]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1951 | R. J. Boast | Assistant Controller of Telecommunications | Telecommunications | — | — |
| 1953 | R. J. Boast | Controller of Telecommunications | Civil Establishment | — | — |

### Deterministic checks: `boast_robert-joseph_b1901` vs `Boast, R. J___Singapore___1951`

- [PASS] surname_gate: bio 'BOAST' vs stint 'Boast, R. J' (exact)
- [PASS] initials: bio ['R', 'J'] ~ stint ['R', 'J']
- [PASS] age_gate: stint starts 1951, birth 1901 (age 50)
- [FAIL] colony: no placed event resolves to 'Singapore'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1951-1953
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

