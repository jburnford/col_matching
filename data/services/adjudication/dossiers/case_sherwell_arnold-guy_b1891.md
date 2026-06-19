<!-- {"case_id": "case_sherwell_arnold-guy_b1891", "bio_ids": ["sherwell_arnold-guy_b1891"], "stint_ids": ["Sherwell, A. G___Nyasaland___1915"]} -->
# Dossier case_sherwell_arnold-guy_b1891

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `sherwell_arnold-guy_b1891`

- Printed name: **SHERWELL, ARNOLD GUY**
- Birth year: 1891 (attested in editions [1934, 1935, 1937, 1939, 1940])
- Appears in editions: [1934, 1935, 1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1934-L62973.v` — printed in editions [1934, 1935, 1937, 1939, 1940]:**

> SHERWELL, ARNOLD GUY.—B. 1891; ed. St. Edward's Schl. and Brasenose Coll., Oxford; M.A. (schl. of jurisprudence, hons. cls. III); called to bar (Inner Temple), 1914; asst. res., Nyasaland, 1914; mily. serv. in Africa, ment. in desps., 1915; practised at bar, 1920-25; dist. judge, Sudan, 1925; asst. advoc. gen. and legal advr. to Sudan govt., rlys. and steamers, 1928; govt. advoc., Palestine, Apr., 1929; relieving pres. of dist. cts., 1930; pres., dist. ct., 1935.

**Version `col1936-L64560.v` — printed in editions [1936]:**

> SHRREWELL, ARNOLD GUY.—B. 1891; ed. St. Edward's Schl. and Brasenose Coll., Oxford; M.A. (schl. of jurisprudence, hons. cls. III); called to bar (Inner Temple), 1914; asst. res., Nyasaland, 1914; mily. serv. in Africa, ment. in desps., 1915; practised at bar, 1920-25; dist. judge, Sudan, 1925; asst. advoc. gen. and legal advr. to Sudan govt., rlys. and steamers, 1928; govt. advoc., Palestine, Apr., 1929; relieving pres. of dist. cts., 1930; pres. dist. ct., 1936.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914 | called to bar (Inner Temple) | — | [1934, 1935, 1936, 1937, 1939, 1940] |
| 1 | 1914 | asst. res. | Nyasaland | [1934, 1935, 1936, 1937, 1939, 1940] |
| 2 | 1915 | mily. serv. in Africa, ment. in desps | Nyasaland *(inherited from previous clause)* | [1934, 1935, 1936, 1937, 1939, 1940] |
| 3 | 1920–1925 | practised at bar | Nyasaland *(inherited from previous clause)* | [1934, 1935, 1936, 1937, 1939, 1940] |
| 4 | 1925 | dist. judge, Sudan | Nyasaland *(inherited from previous clause)* | [1934, 1935, 1936, 1937, 1939, 1940] |
| 5 | 1928 | asst. advoc. gen. and legal advr. to Sudan govt., rlys. and steamers | Nyasaland *(inherited from previous clause)* | [1934, 1935, 1936, 1937, 1939, 1940] |
| 6 | 1929 | govt. advoc. | Palestine | [1934, 1935, 1936, 1937, 1939, 1940] |
| 7 | 1930 | relieving pres. of dist. cts | Palestine *(inherited from previous clause)* | [1934, 1935, 1936, 1937, 1939, 1940] |
| 8 | 1935 | pres., dist. ct | Palestine *(inherited from previous clause)* | [1934, 1935, 1937, 1939, 1940] |
| 9 | 1936 | pres. dist. ct | Palestine *(inherited from previous clause)* | [1936] |

## Candidate stint `Sherwell, A. G___Nyasaland___1915`

- Staff-list name: **Sherwell, A. G** | colony: **Nyasaland** | listed 1915–1919 | editions [1915, 1917, 1918, 1919]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1915 | A. G. Sherwell | Assistant | District Residents | — | — |
| 1917 | A. G. Sherwell | Assistant | District Residents | — | — |
| 1918 | A. G. Sherwell | Twenty-four Assistants | District Residents | — | — |
| 1919 | A. G. Sherwell | Twenty-four Assistants | District Residents | — | — |

### Deterministic checks: `sherwell_arnold-guy_b1891` vs `Sherwell, A. G___Nyasaland___1915`

- [PASS] surname_gate: bio 'SHERWELL' vs stint 'Sherwell, A. G' (exact)
- [PASS] initials: bio ['A', 'G'] ~ stint ['A', 'G']
- [PASS] age_gate: stint starts 1915, birth 1891 (age 24)
- [PASS] colony: 5 placed event(s) resolve to 'Nyasaland'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1915-1919
- [FAIL] position_sim: best 47 vs bar 60: 'asst. res.' ~ 'Assistant'
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

