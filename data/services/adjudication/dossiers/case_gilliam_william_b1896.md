<!-- {"case_id": "case_gilliam_william_b1896", "bio_ids": ["gilliam_william_b1896"], "stint_ids": ["Gilliam, W___Straits Settlements___1922"]} -->
# Dossier case_gilliam_william_b1896

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['gilliam_william_b1896'] carry a single initial only — the namesake trap applies.

## Biography `gilliam_william_b1896`

- Printed name: **GILLIAM, WILLIAM**
- Birth year: 1896 (attested in editions [1937, 1940])
- Appears in editions: [1937, 1940]

### Verbatim printed entry text (OCR)

**Version `col1937-L61197.v` — printed in editions [1937, 1940]:**

> GILLIAM, WILLIAM.—B. 1896; Imp. G.P.O., June, 1911; mily. serv., 1915-19; supt., post surv., S.S., June, 1921; per. asst. to dir. gen., P. and T., Malaya, Sept., 1934; ag. contr., Selangor and Pahang, Aug., 1936; contr., posts, S.S., 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1911 | Imp. G.P.O | — | [1937, 1940] |
| 1 | 1915–1919 | mily. serv | — | [1937, 1940] |
| 2 | 1921 | supt., post surv. | Straits Settlements | [1937, 1940] |
| 3 | 1934 | per. asst. to dir. gen., P. and T. | Malaya | [1937, 1940] |
| 4 | 1936 | ag. contr., Selangor and Pahang | Malaya *(inherited from previous clause)* | [1937, 1940] |
| 5 | 1938 | contr., posts | Straits Settlements | [1937, 1940] |

## Candidate stint `Gilliam, W___Straits Settlements___1922`

- Staff-list name: **Gilliam, W** | colony: **Straits Settlements** | listed 1922–1933 | editions [1922, 1923, 1925, 1931, 1933]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | W. Gilliam | Superintendents | Post Office | — | — |
| 1923 | W. Gilliam | Superintendents | Post Office | — | — |
| 1925 | W. Gilliam | Superintendents | Post Office | — | — |
| 1931 | W. Gilliam | Superintendents | Post Office | — | — |
| 1933 | W. Gilliam | Superintendents | Post Office | — | — |

### Deterministic checks: `gilliam_william_b1896` vs `Gilliam, W___Straits Settlements___1922`

- [PASS] surname_gate: bio 'GILLIAM' vs stint 'Gilliam, W' (exact)
- [PASS] initials: bio ['W'] ~ stint ['W']
- [PASS] age_gate: stint starts 1922, birth 1896 (age 26)
- [PASS] colony: 2 placed event(s) resolve to 'Straits Settlements'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1922-1933
- [FAIL] position_sim: best 34 vs bar 60: 'supt., post surv.' ~ 'Superintendents'
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

