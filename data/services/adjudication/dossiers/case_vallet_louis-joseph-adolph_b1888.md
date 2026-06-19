<!-- {"case_id": "case_vallet_louis-joseph-adolph_b1888", "bio_ids": ["vallet_louis-joseph-adolph_b1888"], "stint_ids": ["Vallet, A___Mauritius___1915"]} -->
# Dossier case_vallet_louis-joseph-adolph_b1888

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `vallet_louis-joseph-adolph_b1888`

- Printed name: **VALLET, Louis Joseph Adolph**
- Birth year: 1888 (attested in editions [1950])
- Honours: M.I.C.E
- Appears in editions: [1950]

### Verbatim printed entry text (OCR)

**Version `col1950-L40345.v` — printed in editions [1950]:**

> VALLET, Louis Joseph Adolph, M.I.C.E.—b. 1888; ed. Royal Coll., Maur., and Cent. Tech. Coll., Lond. (assoc. city & guilds inst.); asst. engrnr., Maur., 1911; inspr. way. and bridges, 1914; engrnr., 1915; asst. gen. man., rlwys., 1921; D.D.P.W., 1928; D.P.W., 1944.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1911 | asst. engrnr. | Mauritius | [1950] |
| 1 | 1914 | inspr. way. and bridges | Mauritius *(inherited from previous clause)* | [1950] |
| 2 | 1915 | engrnr | Mauritius *(inherited from previous clause)* | [1950] |
| 3 | 1921 | asst. gen. man., rlwys | Mauritius *(inherited from previous clause)* | [1950] |
| 4 | 1928 | D.D.P.W | Mauritius *(inherited from previous clause)* | [1950] |
| 5 | 1944 | D.P.W | Mauritius *(inherited from previous clause)* | [1950] |

## Candidate stint `Vallet, A___Mauritius___1915`

- Staff-list name: **Vallet, A** | colony: **Mauritius** | listed 1915–1939 | editions [1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1925, 1927, 1928, 1929, 1931, 1932, 1936, 1937, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1915 | A. Vallet | Inspector, Permanent Way and Bridges | Railway Department | — | — |
| 1917 | A. Vallet | Engineer | Railway Department | — | — |
| 1918 | A. Vallet | Engineer | Railway Department | — | — |
| 1919 | A. Vallet | Engineer | Railway Department | — | — |
| 1920 | A. Vallet | Engineer | Railway Department | — | — |
| 1921 | A. Vallet | Engineer | Railway Department | — | — |
| 1922 | A. Vallet | Engineer | Railway Department | — | — |
| 1923 | A. Vallet | Engineer | Railway Department | — | — |
| 1925 | A. Vallet | Assistant General Manager and Permanent Way Engineer | Railway Department | — | — |
| 1927 | A. Vallet | Assistant General Manager and Permanent Way Engineer | Railway Department | — | — |
| 1928 | A. Vallet | Permanent Way Engineer | Railway Department | — | — |
| 1929 | A. Vallet | Permanent Way Engineer | Railway Department | — | — |
| 1931 | A. Vallet | Deputy Director | Public Works and Surveys | — | — |
| 1932 | A. Vallet | Deputy Director | Public Works and Surveys | — | — |
| 1936 | A. Vallet | Deputy Director | Public Works and Surveys | — | — |
| 1937 | A. Vallet | Deputy Director | Public Works and Surveys | — | — |
| 1939 | A. Vallet | Deputy Director | Public Works and Surveys | — | — |

### Deterministic checks: `vallet_louis-joseph-adolph_b1888` vs `Vallet, A___Mauritius___1915`

- [PASS] surname_gate: bio 'VALLET' vs stint 'Vallet, A' (exact)
- [PASS] initials: bio ['L', 'J', 'A'] ~ stint ['A']
- [PASS] age_gate: stint starts 1915, birth 1888 (age 27)
- [PASS] colony: 6 placed event(s) resolve to 'Mauritius'
- [PASS] tenure_overlap: 5 event tenure(s) overlap stint years 1915-1939
- [PASS] position_sim: best 83 vs bar 60: 'inspr. way. and bridges' ~ 'Inspector, Permanent Way and Bridges'
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

