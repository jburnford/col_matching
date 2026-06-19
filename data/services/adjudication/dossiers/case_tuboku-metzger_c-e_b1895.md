<!-- {"case_id": "case_tuboku-metzger_c-e_b1895", "bio_ids": ["tuboku-metzger_c-e_b1895"], "stint_ids": ["Tuboku-Metzger, C. E___Sierra Leone___1949"]} -->
# Dossier case_tuboku-metzger_c-e_b1895

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `tuboku-metzger_c-e_b1895`

- Printed name: **TUBOKU-METZGER, C. E**
- Birth year: 1895 (attested in editions [1956, 1957])
- Honours: M.B.E
- Appears in editions: [1956, 1957]

### Verbatim printed entry text (OCR)

**Version `col1956-L24657.v` — printed in editions [1956, 1957]:**

> TUBOKU-METZGER, C. E., M.B.E.—b. 1895; ed. Albert Academy, S.L. and Carnegie Coll. of Tech., U.S.A.; asst. science and tech. master, educ. dept., S.L., 1928; educ. offr., 1945; senr., 1954.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | asst. science and tech. master, educ. dept. | Sierra Leone | [1956, 1957] |
| 1 | 1954 | senr | Sierra Leone *(inherited from previous clause)* | [1956, 1957] |

## Candidate stint `Tuboku-Metzger, C. E___Sierra Leone___1949`

- Staff-list name: **Tuboku-Metzger, C. E** | colony: **Sierra Leone** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | C. E. Tuboku-Metzger | Education Officer | Education | — | — |
| 1951 | C. E. Tuboku-Metzger | Education Officer | EDUCATION | — | — |

### Deterministic checks: `tuboku-metzger_c-e_b1895` vs `Tuboku-Metzger, C. E___Sierra Leone___1949`

- [PASS] surname_gate: bio 'TUBOKU-METZGER' vs stint 'Tuboku-Metzger, C. E' (exact)
- [PASS] initials: bio ['C', 'E'] ~ stint ['C', 'E']
- [PASS] age_gate: stint starts 1949, birth 1895 (age 54)
- [PASS] colony: 2 placed event(s) resolve to 'Sierra Leone'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 36 vs bar 60: 'asst. science and tech. master, educ. dept.' ~ 'Education Officer'
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

