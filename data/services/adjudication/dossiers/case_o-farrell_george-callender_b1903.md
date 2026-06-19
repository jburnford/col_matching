<!-- {"case_id": "case_o-farrell_george-callender_b1903", "bio_ids": ["o-farrell_george-callender_b1903"], "stint_ids": ["O'Farrell, G. C___Singapore___1951"]} -->
# Dossier case_o-farrell_george-callender_b1903

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 15 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `o-farrell_george-callender_b1903`

- Printed name: **O'FARRELL, George Callender**
- Birth year: 1903 (attested in editions [1950, 1951])
- Honours: A.M.I.E.E
- Appears in editions: [1950, 1951, 1953]

### Verbatim printed entry text (OCR)

**Version `col1950-L38413.v` — printed in editions [1950, 1951]:**

> O'FARRELL, George Callender, B.Sc. (eng.), A.M.I.E.E.—b. 1903; ed. Wandsworth Tech. Inst. and Battersea Poly., Lond.; on mil. serv., 1942 and 1945; prob. engnr., B.P.O. engnr. dept., 1926; engnr., post. and tels., S.S. & F.M.S., 1928; asst. contrlr., telecoms. (change of title), 1939; engnr., posts and tels., Nig. (secondment), 1942-44; contrlr., telecoms., Mal., 1946; ag. dir., telecoms., S'pore., 1949.

**Version `col1953-L18620.v` — printed in editions [1953]:**

> O'FARRELL, G. C.—b. 1903; ed. Wandsworth Tech. Inst. and Battersea Poly., Lond.; mil. serv., 1942 and 1945; prob. engrn., B.P.O. engrg. dept., 1926; engrn., post. and tels., S.S. & F.M.S., 1928; asst.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1926 | prob. engnr., B.P.O. engnr. dept | — | [1950, 1951, 1953] |
| 1 | 1928 | engnr., post. and tels., S.S. & F.M.S | Straits Settlements | [1950, 1951, 1953] |
| 2 | 1939 | asst. contrlr., telecoms. (change of title) | Straits Settlements *(inherited from previous clause)* | [1950, 1951] |
| 3 | 1942–1944 | engnr., posts and tels., Nig. (secondment) | Nigeria | [1950, 1951] |
| 4 | 1946 | contrlr., telecoms. | Malaya | [1950, 1951] |
| 5 | 1949 | ag. dir., telecoms., S'pore | Malaya *(inherited from previous clause)* | [1950, 1951] |

## Candidate stint `O'Farrell, G. C___Singapore___1951`

- Staff-list name: **O'Farrell, G. C** | colony: **Singapore** | listed 1951–1953 | editions [1951, 1952, 1953]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1951 | G. C. O'Farrell | Director of Telecommunications | Telecommunications | — | — |
| 1952 | G. C. O'Farrell | Director of Telecommunications (Acting) | Civil Establishment | — | — |
| 1953 | G. C. O'Farrell | Director of Telecommunications | Civil Establishment | — | — |

### Deterministic checks: `o-farrell_george-callender_b1903` vs `O'Farrell, G. C___Singapore___1951`

- [PASS] surname_gate: bio 'O'FARRELL' vs stint 'O'Farrell, G. C' (exact)
- [PASS] initials: bio ['G', 'C'] ~ stint ['G', 'C']
- [PASS] age_gate: stint starts 1951, birth 1903 (age 48)
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

