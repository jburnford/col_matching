<!-- {"case_id": "case_khalidi_ahmad-sameh_b1896", "bio_ids": ["khalidi_ahmad-sameh_b1896"], "stint_ids": ["Khalidi, Ahmed___Palestine___1923"]} -->
# Dossier case_khalidi_ahmad-sameh_b1896

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `khalidi_ahmad-sameh_b1896`

- Printed name: **KHALIDI, Ahmad Sameh**
- Birth year: 1896 (attested in editions [1948, 1949])
- Appears in editions: [1948, 1949]

### Verbatim printed entry text (OCR)

**Version `col1948-L33815.v` — printed in editions [1948, 1949]:**

> KHALIDI, Ahmad Sameh, M.B.E. (Hon.), B.A. (A.U.B.), M.Ph. (A.U.B.).—b. 1896; ed. American Univ., Beirut, and Ottoman Faculty of Med., St. George's Sch., English Coll.; apptd. educ. dept., Pal., 1920; gr. V., 1921; gr. IV., 1922; gr. G., 1932; asst. dir., 1941; author of History of the Government and Administration in Palestine from the 7th Century, A.D., to the 20th Century, Manuscript on the History of Syria and of contributions to medical, scientific and literary magazines.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1920 | apptd. educ. dept. | Palestine | [1948, 1949] |
| 1 | 1921 | gr. V | Palestine *(inherited from previous clause)* | [1948, 1949] |
| 2 | 1922 | gr. IV | Palestine *(inherited from previous clause)* | [1948, 1949] |
| 3 | 1932 | gr. G | Palestine *(inherited from previous clause)* | [1948, 1949] |
| 4 | 1941 | asst. dir | Palestine *(inherited from previous clause)* | [1948, 1949] |

## Candidate stint `Khalidi, Ahmed___Palestine___1923`

- Staff-list name: **Khalidi, Ahmed** | colony: **Palestine** | listed 1923–1932 | editions [1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1923 | Ahmed Khalidi | District Inspectors | Education | — | — |
| 1924 | Ahmed Khalidi | District Inspectors | Education | — | — |
| 1925 | Ahmed Khalidi | Headquarters Inspector | Department of Education | — | — |
| 1927 | Ahmed Khalidi | Principal, Men's Training College | Department of Education | — | — |
| 1928 | Ahmed Khalidi | Principal, Men's Training College | Department of Education | — | — |
| 1929 | Ahmed Khalidi | Principal, Men’s Training College | Department of Education | — | — |
| 1930 | Ahmed Khalidi | Principal, Government Arab College | Department of Education | — | — |
| 1931 | Ahmed Khalidi | Principal, Government Arab College | Department of Education | — | — |
| 1932 | Ahmed Khalidi | Principal, Government Arab College | Department of Education | — | — |

### Deterministic checks: `khalidi_ahmad-sameh_b1896` vs `Khalidi, Ahmed___Palestine___1923`

- [PASS] surname_gate: bio 'KHALIDI' vs stint 'Khalidi, Ahmed' (exact)
- [PASS] initials: bio ['A', 'S'] ~ stint ['A']
- [PASS] age_gate: stint starts 1923, birth 1896 (age 27)
- [PASS] colony: 5 placed event(s) resolve to 'Palestine'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1923-1932
- [FAIL] position_sim: best 25 vs bar 60: 'gr. IV' ~ 'District Inspectors'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

