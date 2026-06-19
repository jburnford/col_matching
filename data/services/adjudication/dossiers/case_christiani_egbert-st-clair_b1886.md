<!-- {"case_id": "case_christiani_egbert-st-clair_b1886", "bio_ids": ["christiani_egbert-st-clair_b1886"], "stint_ids": ["Christiani, E. S___British Guiana___1910"]} -->
# Dossier case_christiani_egbert-st-clair_b1886

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `christiani_egbert-st-clair_b1886`

- Printed name: **CHRISTIANI, Egbert St. Clair**
- Birth year: 1886 (attested in editions [1940])
- Appears in editions: [1940]

### Verbatim printed entry text (OCR)

**Version `col1940-L63114.v` — printed in editions [1940]:**

> CHRISTIANI, Egbert St. Clair.—B. 1886; cler. asst. botanic gardens, Br. Guiana, 1903; clk., dept. sci. and agr. and sec., bd. of agr., 1911; 2nd cls. clk. local govt. bd., 1918; asst. secy., local govt. bd., 1925; secy., do., 1926; secy., dist. admin., 1932.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1903 | cler. asst. botanic gardens | British Guiana | [1940] |
| 1 | 1911 | clk., dept. sci. and agr. and sec., bd. of agr | British Guiana *(inherited from previous clause)* | [1940] |
| 2 | 1918 | 2nd cls. clk. local govt. bd | British Guiana *(inherited from previous clause)* | [1940] |
| 3 | 1925 | asst. secy., local govt. bd | British Guiana *(inherited from previous clause)* | [1940] |
| 4 | 1926 | secy. | Dominions Office | [1940] |
| 5 | 1932 | secy., dist. admin | Dominions Office *(inherited from previous clause)* | [1940] |

## Candidate stint `Christiani, E. S___British Guiana___1910`

- Staff-list name: **Christiani, E. S** | colony: **British Guiana** | listed 1910–1939 | editions [1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1910 | E. S. Christiani | Clerical and Laboratory Assistants | Science and Agriculture | — | — |
| 1911 | E. S. Christiani | Clerical and Laboratory Assistants | Department of Science and Agriculture | — | — |
| 1912 | E. S Christiani | Clerical and Laboratory Assistants | Department of Science and Agriculture | — | — |
| 1913 | E. S. Christiani | Clerk, and Secretary Board of Agriculture | Department of Science and Agriculture | — | — |
| 1914 | E. S. Christiani | Clerk, and Secretary Board of Agriculture | Department of Science and Agriculture | — | — |
| 1915 | E. S. Christiani | Clerk, and Secretary Board of Agriculture | Science and Agriculture | — | — |
| 1917 | E. S. Christiani | Clerk and Secretary Board of Agriculture | Science and Agriculture | — | — |
| 1918 | E. S. Christiani | Clerk, and Secretary Board of Agriculture | Science and Agriculture | — | — |
| 1919 | E. S. Christiani | Second Class Clerk | Local Government Board | — | — |
| 1920 | E. S. Christiani | Second Class Clerk | Local Government Board | — | — |
| 1921 | E. S. Christiani | Second Class Clerk | Local Government Board | — | — |
| 1922 | E. S. Christiani | Second Class Clerk | Local Government Board | — | — |
| 1923 | E. S. Christiani | Second Class Clerk | Local Government Board | — | — |
| 1924 | E. S. Christiani | Second Class Clerk | Local Government Board | — | — |
| 1925 | E. S. Christiani | Second Class Clerk | Local Government Board | — | — |
| 1927 | E. S. Christiani | Secretary to the Board | Local Government Board | — | — |
| 1928 | E. S. Christiani | Secretary to the Board | Local Government Board | — | — |
| 1929 | E. S. Christiani | Secretary to the Board | Local Government Board | — | — |
| 1930 | E. S. Christiani | Secretary to the Board | Local Government Board | — | — |
| 1939 | E. S. Christiani | Secretary District Administration | Labour and Local Government | — | — |

### Deterministic checks: `christiani_egbert-st-clair_b1886` vs `Christiani, E. S___British Guiana___1910`

- [PASS] surname_gate: bio 'CHRISTIANI' vs stint 'Christiani, E. S' (exact)
- [PASS] initials: bio ['E', 'S', 'C'] ~ stint ['E', 'S']
- [PASS] age_gate: stint starts 1910, birth 1886 (age 24)
- [PASS] colony: 4 placed event(s) resolve to 'British Guiana'
- [PASS] tenure_overlap: 4 event tenure(s) overlap stint years 1910-1939
- [PASS] position_sim: best 60 vs bar 60: 'clk., dept. sci. and agr. and sec., bd. of agr' ~ 'Clerk, and Secretary Board of Agriculture'
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

