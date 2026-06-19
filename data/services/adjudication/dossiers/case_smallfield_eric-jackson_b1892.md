<!-- {"case_id": "case_smallfield_eric-jackson_b1892", "bio_ids": ["smallfield_eric-jackson_b1892"], "stint_ids": ["Smallfield, E. J___North Borneo___1933"]} -->
# Dossier case_smallfield_eric-jackson_b1892

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `smallfield_eric-jackson_b1892`

- Printed name: **SMALLFIELD, Eric Jackson**
- Birth year: 1892 (attested in editions [1951])
- Honours: O.B.E (1951)
- Appears in editions: [1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1951-L42565.v` — printed in editions [1951]:**

> SMALLFIELD, Eric Jackson, O.B.E. (1951), F.R.I. Chart. Surv. (N.Z.), M.Inst. Surv. (N.Z.).—b. 1892; ed. St. John's Coll., Auckland, N.Z.; on mil. serv., 1917-19; interned, 1942-45; surv. (Chartered Co's. serv.), N. Borneo, 1925; dist. surv., 1936; col. surv. serv., 1946; surv. gen., 1949.

**Version `col1949-L35690.v` — printed in editions [1949, 1950]:**

> SMALLFIELD, Eric Jackson, Member N.Z. Inst. of Surveyors, col. fellow of the royal inst. of chart. surv.—b. 1892; ed. St. John's Coll., Auckland, N.Z.; on mil. serv., 1917-19; surv. (Chartered Co.'s serv.), N. Borneo, 1925; dist. survr., 1936; col. surv. serv., 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1925 | surv. (Chartered Co's. serv.) | North Borneo | [1949, 1950, 1951] |
| 1 | 1936 | dist. surv | North Borneo *(inherited from previous clause)* | [1949, 1950, 1951] |
| 2 | 1942–1945 | interned | — | [1951] |
| 3 | 1946 | col. surv. serv | North Borneo *(inherited from previous clause)* | [1949, 1950, 1951] |
| 4 | 1949 | surv. gen | North Borneo *(inherited from previous clause)* | [1951] |

## Candidate stint `Smallfield, E. J___North Borneo___1933`

- Staff-list name: **Smallfield, E. J** | colony: **North Borneo** | listed 1933–1951 | editions [1933, 1936, 1940, 1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | E. J. Smallfield | Government Surveyor | Other Officers | — | — |
| 1936 | E. J. Smallfield | Government Surveyor | Other Officers | — | — |
| 1940 | E. J. Smallfield | Government Surveyor | Other Officers | — | — |
| 1949 | E. J. Smallfield | Surveyor | Survey | — | — |
| 1950 | E. J. Smallfield | Surveyor-General | Survey | — | — |
| 1951 | E. J. Smallfield | Surveyor-General | Survey | — | — |

### Deterministic checks: `smallfield_eric-jackson_b1892` vs `Smallfield, E. J___North Borneo___1933`

- [PASS] surname_gate: bio 'SMALLFIELD' vs stint 'Smallfield, E. J' (exact)
- [PASS] initials: bio ['E', 'J'] ~ stint ['E', 'J']
- [PASS] age_gate: stint starts 1933, birth 1892 (age 41)
- [PASS] colony: 4 placed event(s) resolve to 'North Borneo'
- [PASS] tenure_overlap: 4 event tenure(s) overlap stint years 1933-1951
- [FAIL] position_sim: best 59 vs bar 60: 'surv. gen' ~ 'Government Surveyor'
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

