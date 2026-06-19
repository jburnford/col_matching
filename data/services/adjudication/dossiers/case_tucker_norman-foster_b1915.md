<!-- {"case_id": "case_tucker_norman-foster_b1915", "bio_ids": ["tucker_norman-foster_b1915"], "stint_ids": ["Tucker, N. F___Hong Kong___1949"]} -->
# Dossier case_tucker_norman-foster_b1915

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 53 official(s) with this surname in the graph's staff lists; 15 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `tucker_norman-foster_b1915`

- Printed name: **TUCKER, Norman Foster**
- Birth year: 1915 (attested in editions [1949])
- Appears in editions: [1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1949-L36306.v` — printed in editions [1949]:**

> TUCKER, Norman Foster.—b. 1915; M.A. (Cantab.), dip in educ.; Mstr., educ. dept., H.K., 1939.

**Version `col1950-L40275.v` — printed in editions [1950, 1951]:**

> TUCKER, Norman Foster.—b. 1915; ed. Colfe's Gram Sch., Lewisham, and Queens' Coll., Camb., M.A. (Cantab.), dip. ed. (Cantab.); on mil. serv., 1941-45 (p.o.w.); mstr., educ. dept. H.K., 1939.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1939 | Mstr., educ. dept. | Hong Kong | [1949, 1950, 1951] |

## Candidate stint `Tucker, N. F___Hong Kong___1949`

- Staff-list name: **Tucker, N. F** | colony: **Hong Kong** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | N. F. Tucker | Masters | Education Department | — | — |
| 1950 | N. F. Tucker | Masters | Education | — | — |
| 1951 | N. F. Tucker | Masters | Education | — | — |

### Deterministic checks: `tucker_norman-foster_b1915` vs `Tucker, N. F___Hong Kong___1949`

- [PASS] surname_gate: bio 'TUCKER' vs stint 'Tucker, N. F' (exact)
- [PASS] initials: bio ['N', 'F'] ~ stint ['N', 'F']
- [PASS] age_gate: stint starts 1949, birth 1915 (age 34)
- [PASS] colony: 1 placed event(s) resolve to 'Hong Kong'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 38 vs bar 60: 'Mstr., educ. dept.' ~ 'Masters'
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

