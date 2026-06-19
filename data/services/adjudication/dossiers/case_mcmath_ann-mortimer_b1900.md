<!-- {"case_id": "case_mcmath_ann-mortimer_b1900", "bio_ids": ["mcmath_ann-mortimer_b1900"], "stint_ids": ["McMath, A. M___Sierra Leone___1939"]} -->
# Dossier case_mcmath_ann-mortimer_b1900

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mcmath_ann-mortimer_b1900`

- Printed name: **McMATH, Ann Mortimer**
- Birth year: 1900 (attested in editions [1949, 1950])
- Honours: M.A, O.B.E (1949)
- Appears in editions: [1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1949-L34050.v` — printed in editions [1949, 1950]:**

> McMATH, Ann Mortimer, O.B.E. (1949), M.A.; B.Sc., Ph.D.—b. 1900; ed. Morgan Acad., Dundee, and St. Andrews Univ. (Carnegie fellowship); apptd. S.L., 1937; Nig., 1945; senr. woman educ. offr., 1946; mem., slum clearance comsn., Freetown, and nutrition comttee, S.L.; author of various papers in journal of the Chemical Soc.

**Version `col1951-L40526.v` — printed in editions [1951]:**

> MCATH, Ann Mortimer, O.B.E. (1949), M.A., B.Sc., Ph.D.—b. 1900; ed. Morgan Acad., Dundee, and St. Andrews Univ. (Carnegie fellowship); apptd. S.L., 1937; Nig., 1945; senr. woman educ. offr., 1946; mem., slum clearance comsn., Freetown, and nutrition comte, S.L.; author of various papers in journal of the Chemical Soc.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1937 | apptd. S.L | — | [1949, 1950, 1951] |
| 1 | 1945 | apptd. S.L | Nigeria | [1949, 1950, 1951] |
| 2 | 1946 | senr. woman educ. offr | Nigeria *(inherited from previous clause)* | [1949, 1950, 1951] |

## Candidate stint `McMath, A. M___Sierra Leone___1939`

- Staff-list name: **McMath, A. M** | colony: **Sierra Leone** | listed 1939–1940 | editions [1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | Miss A. M. McMath | Lady Education Officer | Education | — | — |
| 1940 | Miss A. M. McMath | Lady Education Officer | Education | — | — |

### Deterministic checks: `mcmath_ann-mortimer_b1900` vs `McMath, A. M___Sierra Leone___1939`

- [PASS] surname_gate: bio 'McMATH' vs stint 'McMath, A. M' (exact)
- [PASS] initials: bio ['A', 'M'] ~ stint ['A', 'M']
- [PASS] age_gate: stint starts 1939, birth 1900 (age 39)
- [FAIL] colony: no placed event resolves to 'Sierra Leone'
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

