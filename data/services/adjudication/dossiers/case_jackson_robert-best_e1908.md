<!-- {"case_id": "case_jackson_robert-best_e1908", "bio_ids": ["jackson_robert-best_e1908"], "stint_ids": ["Jackson, R. B___Hong Kong___1931"]} -->
# Dossier case_jackson_robert-best_e1908

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 144 official(s) with this surname in the graph's staff lists; 60 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Jackson, R. B___Hong Kong___1931` is also gate-compatible with biography(ies) outside this case: ['jackson_robert-brit_e1914'] (already linked elsewhere or filtered).

## Biography `jackson_robert-best_e1908`

- Printed name: **JACKSON, ROBERT BEST**
- Birth year: not printed
- Honours: D.P.H, M.B, T.C.D
- Appears in editions: [1923, 1924, 1925, 1927, 1928, 1930, 1931, 1932]

### Verbatim printed entry text (OCR)

**Version `col1923-L55535.v` — printed in editions [1923, 1924, 1925, 1927, 1928, 1930, 1931, 1932]:**

> JACKSON, ROBERT BEST, M.B., D.P.H., T.C.D., L.M. Rotunda Hospit., Dublin, certif., London Schol. Trop. Med., math. sizar, schl., and junr. modr., Trinity Coll., Dublin, senr. exh. and catechetical prizeman.—Chief med. offr., Indian Mining Assn., Jharia and Katras Coalfields, 1908-14; R.A.M.C., 1914-17; med. offr., Gen. Milly Hosp., Edmonton, 1918; med. offr., F.M.S., 20th Nov., 1920; ag. health offr., Negri Sembilan, 1921.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1908–1914 | Chief med. offr., Indian Mining Assn., Jharia and Katras Coalfields | — | [1923, 1924, 1925, 1927, 1928, 1930, 1931, 1932] |
| 1 | 1914–1917 | R.A.M.C | — | [1923, 1924, 1925, 1927, 1928, 1930, 1931, 1932] |
| 2 | 1918 | med. offr., Gen. Milly Hosp., Edmonton | — | [1923, 1924, 1925, 1927, 1928, 1930, 1931, 1932] |
| 3 | 1920 | med. offr. | Federated Malay States | [1923, 1924, 1925, 1927, 1928, 1930, 1931, 1932] |
| 4 | 1921 | ag. health offr., Negri Sembilan | Federated Malay States *(inherited from previous clause)* | [1923, 1924, 1925, 1927, 1928, 1930, 1931, 1932] |

## Candidate stint `Jackson, R. B___Hong Kong___1931`

- Staff-list name: **Jackson, R. B** | colony: **Hong Kong** | listed 1931–1937 | editions [1931, 1932, 1933, 1934, 1936, 1937]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | R. B. Jackson | Malarialogist | Staff | — | — |
| 1931 | R. B. Jackson | Malarialogist | Medical Departments | — | — |
| 1932 | R. B. Jackson | Malarialogist | Medical Department | — | — |
| 1933 | R. B. Jackson | Malarialogist | Medical Department | — | — |
| 1934 | R. B. Jackson | Malarialogist | Medical Department | — | — |
| 1936 | R. B. Jackson | Malarialogist | Medical Department | — | — |
| 1937 | R. B. Jackson | Malarialogist | Medical Department | — | — |

### Deterministic checks: `jackson_robert-best_e1908` vs `Jackson, R. B___Hong Kong___1931`

- [PASS] surname_gate: bio 'JACKSON' vs stint 'Jackson, R. B' (exact)
- [PASS] initials: bio ['R', 'B'] ~ stint ['R', 'B']
- [PASS] age_gate: stint starts 1931; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Hong Kong'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1931-1937
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

