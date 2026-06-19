<!-- {"case_id": "case_jensen_j-a_e1903", "bio_ids": ["jensen_j-a_e1903"], "stint_ids": ["Jensen, J. A___Tasmania___1906", "Jensen, Johannes___Australia___1918"]} -->
# Dossier case_jensen_j-a_e1903

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `jensen_j-a_e1903`

- Printed name: **JENSEN, J. A.**
- Birth year: not printed
- Appears in editions: [1917, 1918, 1919]

### Verbatim printed entry text (OCR)

**Version `col1917-L50780.v` — printed in editions [1917, 1918, 1919]:**

> JENSEN, HON. J. A.—M.H.A., Tasmania, 1903; chief sec., 20th to 27th Oct., 1909; resig., Feb., 1910; mem. H. of R., C. of A., general elections, 1910, 1913, 1914; chmn. of select comte., on Tasmanian customs leakage, 1910; asst. min., C. of A., 17th Sept., 1914; min. for the navy, 1915; min. for trade and customs, Feb., 1917, to Dec., 1918.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1903–1903 | M.H.A. | Tasmania | [1917, 1918, 1919] |
| 1 | 1909–1909 | chief sec. | — | [1917, 1918, 1919] |
| 2 | 1910–1910 | — | — | [1917, 1918, 1919] |
| 3 | 1910–1914 | mem. H. of R. | Commonwealth of Australia | [1917, 1918, 1919] |
| 4 | 1910–1910 | chmn. of select comte. | Tasmania | [1917, 1918, 1919] |
| 5 | 1914–1914 | asst. min. | Commonwealth of Australia | [1917, 1918, 1919] |
| 6 | 1915–1915 | min. for the navy | — | [1917, 1918, 1919] |
| 7 | 1917–1918 | min. for trade and customs | — | [1917, 1918, 1919] |

## Candidate stint `Jensen, J. A___Tasmania___1906`

- Staff-list name: **Jensen, J. A** | colony: **Tasmania** | listed 1906–1909 | editions [1906, 1907, 1908, 1909]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1906 | J. A. Jensen | — | House of Assembly | — | — |
| 1907 | J. A. Jensen | — | House of Assembly | — | — |
| 1908 | J. A. Jensen | — | House of Assembly | — | — |
| 1909 | J. A. Jensen | Member | House of Assembly | — | — |

### Deterministic checks: `jensen_j-a_e1903` vs `Jensen, J. A___Tasmania___1906`

- [PASS] surname_gate: bio 'JENSEN' vs stint 'Jensen, J. A' (exact)
- [PASS] initials: bio ['J', 'A'] ~ stint ['J', 'A']
- [PASS] age_gate: stint starts 1906; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Tasmania'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1906-1909
- [FAIL] position_sim: best 23 vs bar 60: 'chmn. of select comte.' ~ 'Member'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Jensen, Johannes___Australia___1918`

- Staff-list name: **Jensen, Johannes** | colony: **Australia** | listed 1918–1927 | editions [1918, 1927]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1918 | J. C. Jensen | Accountant | Department of Education | — | — |
| 1918 | Johannes Jensen | Vice-Consul | Foreign Consuls | — | — |
| 1927 | J. C. Jensen | Accountant | Department of Education | — | — |

### Deterministic checks: `jensen_j-a_e1903` vs `Jensen, Johannes___Australia___1918`

- [PASS] surname_gate: bio 'JENSEN' vs stint 'Jensen, Johannes' (exact)
- [PASS] initials: bio ['J', 'A'] ~ stint ['J']
- [PASS] age_gate: stint starts 1918; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1918-1927
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

