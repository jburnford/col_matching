<!-- {"case_id": "case_coveney_william-augustine_b1893", "bio_ids": ["coveney_william-augustine_b1893"], "stint_ids": ["Coveney, W. A___North Borneo___1920"]} -->
# Dossier case_coveney_william-augustine_b1893

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `coveney_william-augustine_b1893`

- Printed name: **COVENEY, William Augustine**
- Birth year: 1893 (attested in editions [1948])
- Honours: A.M.I.C.E
- Appears in editions: [1948]

### Verbatim printed entry text (OCR)

**Version `col1948-L31955.v` — printed in editions [1948]:**

> COVENEY, William Augustine, R.E. (N.U.I.), A.M.I.C.E., M.I.M.Cy.E.—b. 1893; ed. National Sch. and Christian Coll., Cork, National Univ., Cork; exec. engrn., P.W.D., N. Born.; G.C., 1924; senr. exec. engrn., 1940; D.D.P.W., 1944.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1924 | — | Gold Coast | [1948] |
| 1 | 1940 | senr. exec. engrn | Gold Coast *(inherited from previous clause)* | [1948] |
| 2 | 1944 | D.D.P.W | Gold Coast *(inherited from previous clause)* | [1948] |

## Candidate stint `Coveney, W. A___North Borneo___1920`

- Staff-list name: **Coveney, W. A** | colony: **North Borneo** | listed 1920–1921 | editions [1920, 1921]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1920 | W. A. Coveney | Assistant Engineer, Public Works Department | Other Officers | — | — |
| 1921 | W. A. Coveney | Assistant Engineer | Other Officers | — | — |

### Deterministic checks: `coveney_william-augustine_b1893` vs `Coveney, W. A___North Borneo___1920`

- [PASS] surname_gate: bio 'COVENEY' vs stint 'Coveney, W. A' (exact)
- [PASS] initials: bio ['W', 'A'] ~ stint ['W', 'A']
- [PASS] age_gate: stint starts 1920, birth 1893 (age 27)
- [FAIL] colony: no placed event resolves to 'North Borneo'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1920-1921
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

