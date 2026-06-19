<!-- {"case_id": "case_gregory_richard-ernest_b1907", "bio_ids": ["gregory_richard-ernest_b1907"], "stint_ids": ["Gregory, R. E___Northern Rhodesia___1949"]} -->
# Dossier case_gregory_richard-ernest_b1907

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 34 official(s) with this surname in the graph's staff lists; 16 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `gregory_richard-ernest_b1907`

- Printed name: **GREGORY, Richard Ernest**
- Birth year: 1907 (attested in editions [1951])
- Appears in editions: [1951]

### Verbatim printed entry text (OCR)

**Version `col1951-L38617.v` — printed in editions [1951]:**

> GREGORY, Richard Ernest.—b. 1907 ; ed. Hindley and Abram Gram. Sch., Goldsmiths' Coll., Lond. Univ., and cent. sch. of arts and crafts, teach. cert., art mstrs. cert. ; on mil. serv., 1939-42 ; mstr., European educ. dept., N. Rhod., 1931 ; prim., 1948.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1931 | mstr., European educ. dept. | Northern Rhodesia | [1951] |
| 1 | 1948 | prim | Northern Rhodesia *(inherited from previous clause)* | [1951] |

## Candidate stint `Gregory, R. E___Northern Rhodesia___1949`

- Staff-list name: **Gregory, R. E** | colony: **Northern Rhodesia** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | R. E. Gregory | Master | Education | — | — |
| 1951 | R. E. Gregory | Principal | Education | — | — |

### Deterministic checks: `gregory_richard-ernest_b1907` vs `Gregory, R. E___Northern Rhodesia___1949`

- [PASS] surname_gate: bio 'GREGORY' vs stint 'Gregory, R. E' (exact)
- [PASS] initials: bio ['R', 'E'] ~ stint ['R', 'E']
- [PASS] age_gate: stint starts 1949, birth 1907 (age 42)
- [PASS] colony: 2 placed event(s) resolve to 'Northern Rhodesia'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 46 vs bar 60: 'prim' ~ 'Principal'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

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

