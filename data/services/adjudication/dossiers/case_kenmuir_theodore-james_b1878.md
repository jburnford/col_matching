<!-- {"case_id": "case_kenmuir_theodore-james_b1878", "bio_ids": ["kenmuir_theodore-james_b1878"], "stint_ids": ["Kenmuir, T. J___Natal___1905"]} -->
# Dossier case_kenmuir_theodore-james_b1878

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `kenmuir_theodore-james_b1878`

- Printed name: **KENMUIR, THEODORE JAMES**
- Birth year: 1878 (attested in editions [1930, 1931, 1932, 1933])
- Appears in editions: [1930, 1931, 1932, 1933]

### Verbatim printed entry text (OCR)

**Version `col1930-L65941.v` — printed in editions [1930, 1931, 1932, 1933]:**

> KENMUIR, THEODORE JAMES.—B. 1878; apptd. treasy., Natal, Jan., 1896; acotg. offr., Natal treasy., Mar., 1901; acot., July, 1903; senr. clk., July, 1906; ag. ch. acot., July, 1909; prin. clk., May, 1910; transf., Union treasy., Oct., 1910; transf. to head office, inland rev. dept., Pretoria, Apr., 1911; recvr. of rev., Kimberley, July, 1911; head office I.R. dept., Pretoria, Jan., 1915; sp. grade prin. clk. ditto, Apr., 1918; survr., Jan., 1920; ch. clk., income tax, inland rev. dept., Pretoria, Apr., 1920; recvr. of rev., Pretoria, Mar., 1921; ch. clk., gen. admins., I.R. dept., Pretoria, Dec., 1923; ch. rev. offr., ditto, Sept., 1929; recvr., rev., Cape Town, 1930.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1896 | apptd. treasy. | Natal | [1930, 1931, 1932, 1933] |
| 1 | 1901 | acotg. offr., Natal treasy | Natal | [1930, 1931, 1932, 1933] |
| 2 | 1903 | acot | Natal *(inherited from previous clause)* | [1930, 1931, 1932, 1933] |
| 3 | 1906 | senr. clk | Natal *(inherited from previous clause)* | [1930, 1931, 1932, 1933] |
| 4 | 1909 | ag. ch. acot | Natal *(inherited from previous clause)* | [1930, 1931, 1932, 1933] |
| 5 | 1910 | prin. clk | Natal *(inherited from previous clause)* | [1930, 1931, 1932, 1933] |
| 6 | 1911 | transf. to head office, inland rev. dept., Pretoria | Natal *(inherited from previous clause)* | [1930, 1931, 1932, 1933] |
| 7 | 1915 | head office I.R. dept., Pretoria | Natal *(inherited from previous clause)* | [1930, 1931, 1932, 1933] |
| 8 | 1918 | sp. grade prin. clk. ditto | Natal *(inherited from previous clause)* | [1930, 1931, 1932, 1933] |
| 9 | 1920 | survr | Natal *(inherited from previous clause)* | [1930, 1931, 1932, 1933] |
| 10 | 1921 | recvr. of rev., Pretoria | Natal *(inherited from previous clause)* | [1930, 1931, 1932, 1933] |
| 11 | 1923 | ch. clk., gen. admins., I.R. dept., Pretoria | Natal *(inherited from previous clause)* | [1930, 1931, 1932, 1933] |
| 12 | 1929 | ch. rev. offr., ditto | Natal *(inherited from previous clause)* | [1930, 1931, 1932, 1933] |
| 13 | 1930 | recvr., rev., Cape Town | Cape of Good Hope | [1930, 1931, 1932, 1933] |

## Candidate stint `Kenmuir, T. J___Natal___1905`

- Staff-list name: **Kenmuir, T. J** | colony: **Natal** | listed 1905–1927 | editions [1905, 1906, 1907, 1910, 1927]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | T. J. Kenmuir | Accountant | Treasury | — | — |
| 1906 | T. J. Kenmuir | Accountant | Treasury | — | — |
| 1907 | T. J. Kenmuir | Accountant | Treasury | — | — |
| 1910 | T. J. Kenmuir | Accountant | Treasury | — | — |
| 1927 | T. J. Kenmuir | Chief Clerk | Inland Revenue Department | — | — |

### Deterministic checks: `kenmuir_theodore-james_b1878` vs `Kenmuir, T. J___Natal___1905`

- [PASS] surname_gate: bio 'KENMUIR' vs stint 'Kenmuir, T. J' (exact)
- [PASS] initials: bio ['T', 'J'] ~ stint ['T', 'J']
- [PASS] age_gate: stint starts 1905, birth 1878 (age 27)
- [PASS] colony: 13 placed event(s) resolve to 'Natal'
- [PASS] tenure_overlap: 10 event tenure(s) overlap stint years 1905-1927
- [FAIL] position_sim: best 57 vs bar 60: 'acot' ~ 'Accountant'
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

