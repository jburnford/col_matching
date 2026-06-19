<!-- {"case_id": "case_turner_percival-elisha_b1898", "bio_ids": ["turner_percival-elisha_b1898"], "stint_ids": ["Turner, P. E___Trinidad and Tobago___1937"]} -->
# Dossier case_turner_percival-elisha_b1898

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 107 official(s) with this surname in the graph's staff lists; 43 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `turner_percival-elisha_b1898`

- Printed name: **TURNER, Percival Elisha**
- Birth year: 1898 (attested in editions [1949, 1950, 1951])
- Honours: F.I.C, O.B.E (1949)
- Appears in editions: [1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1949-L36322.v` — printed in editions [1949, 1950, 1951]:**

> TURNER, Percival Elisha, O.B.E. (1949), M.Sc., F.I.C.—b. 1898; ed. Gram. Sch., Cowbridge, Glam., Royal Gram. Sch., Worcester, and Univ. Coll., Reading (West exhibn.); on mil. serv., 1918-19; lect., I.C.T.A., 1923; soil chem., sugar cane invest. comttee., Trin. (secondment), 1926; advsr. in sugar cane, I.C.T.A., 1933-43; sugar agron. and exec. offr., sugar cane invest. comttee., Trin., 1934-43; sugar agron., dev. and welf. organ in W.I., 1943; reg. vice-chmn. for B.W.I. at 6th cong. of internat. soc. of sugar cane tech., Louisiana, 1938; mem., Soulbury sugar comsn., 1948; author of various publns. on sugar cultivation.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1923 | lect., I.C.T.A | — | [1949, 1950, 1951] |
| 1 | 1926 | soil chem., sugar cane invest. comttee., Trin. (secondment) | Trinidad | [1949, 1950, 1951] |
| 2 | 1933–1943 | advsr. in sugar cane, I.C.T.A | Trinidad *(inherited from previous clause)* | [1949, 1950, 1951] |
| 3 | 1934–1943 | sugar agron. and exec. offr., sugar cane invest. comttee. | Trinidad | [1949, 1950, 1951] |
| 4 | 1938 | reg. vice-chmn. for B.W.I. at 6th cong. of internat. soc. of sugar cane tech., Louisiana | Trinidad *(inherited from previous clause)* | [1949, 1950, 1951] |
| 5 | 1943 | sugar agron., dev. and welf. organ in W.I | Trinidad *(inherited from previous clause)* | [1949, 1950, 1951] |
| 6 | 1948 | mem., Soulbury sugar comsn | Trinidad *(inherited from previous clause)* | [1949, 1950, 1951] |

## Candidate stint `Turner, P. E___Trinidad and Tobago___1937`

- Staff-list name: **Turner, P. E** | colony: **Trinidad and Tobago** | listed 1937–1949 | editions [1937, 1940, 1949]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1937 | P. E. Turner | Sugar Agronomist | Scientific and Technical Staff | — | — |
| 1940 | P. E. Turner | Sugar Agronomist | Department of Agriculture | — | — |
| 1949 | P. E. Turner | Sugar Agronomist | Agriculture | — | — |

### Deterministic checks: `turner_percival-elisha_b1898` vs `Turner, P. E___Trinidad and Tobago___1937`

- [PASS] surname_gate: bio 'TURNER' vs stint 'Turner, P. E' (exact)
- [PASS] initials: bio ['P', 'E'] ~ stint ['P', 'E']
- [PASS] age_gate: stint starts 1937, birth 1898 (age 39)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1937-1949
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

