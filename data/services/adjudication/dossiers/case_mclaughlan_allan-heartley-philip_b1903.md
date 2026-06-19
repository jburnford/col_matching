<!-- {"case_id": "case_mclaughlan_allan-heartley-philip_b1903", "bio_ids": ["mclaughlan_allan-heartley-philip_b1903"], "stint_ids": ["McLaughlan, A. H. P___Cyprus___1930"]} -->
# Dossier case_mclaughlan_allan-heartley-philip_b1903

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mclaughlan_allan-heartley-philip_b1903`

- Printed name: **MCLAUGHLAN, ALLAN HEARTLEY PHILIP**
- Birth year: 1903 (attested in editions [1936, 1940])
- Honours: P.A.S.I
- Appears in editions: [1936, 1940]

### Verbatim printed entry text (OCR)

**Version `col1936-L62804.v` — printed in editions [1936, 1940]:**

> MCLAUGHLAN, ALLAN HEARTLEY PHILIP, A.M.Inst. C.E., P.A.S.I., chartered survr.—B. 1903; ed. English schl., Cyprus, and prte. tuition; tracer, P.W.D., Cyprus, 1920; temp. foreman, P.W.D., 1925; draughtsman and record keeper, P.W.D., 1926; asst. engrn., P.W.D., 1929; ag. divnl. engrn., P.W.D., on various occasions, 1930-35; divnl. engrn., 1938; title changed to exec. engrn., 1939.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1920 | tracer, P.W.D. | Cyprus | [1936, 1940] |
| 1 | 1925 | temp. foreman, P.W.D | Cyprus *(inherited from previous clause)* | [1936, 1940] |
| 2 | 1926 | draughtsman and record keeper, P.W.D | Cyprus *(inherited from previous clause)* | [1936, 1940] |
| 3 | 1929 | asst. engrn., P.W.D | Cyprus *(inherited from previous clause)* | [1936, 1940] |
| 4 | 1930–1935 | ag. divnl. engrn., P.W.D., on various occasions | Cyprus *(inherited from previous clause)* | [1936, 1940] |
| 5 | 1938 | divnl. engrn | Cyprus *(inherited from previous clause)* | [1936, 1940] |
| 6 | 1939 | title changed to exec. engrn | Cyprus *(inherited from previous clause)* | [1936, 1940] |

## Candidate stint `McLaughlan, A. H. P___Cyprus___1930`

- Staff-list name: **McLaughlan, A. H. P** | colony: **Cyprus** | listed 1930–1939 | editions [1930, 1934, 1936, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1930 | A. McLaughlan | Assistant Engineer | Public Works Department | — | — |
| 1934 | A. McLaughlan | Assistant Engineer | Public Works Department | — | — |
| 1936 | A. McLaughlan | Assistant Engineer | Public Works Department | — | — |
| 1939 | A. H. P. McLaughlan | Assistant Engineer | Public Works Department | — | — |

### Deterministic checks: `mclaughlan_allan-heartley-philip_b1903` vs `McLaughlan, A. H. P___Cyprus___1930`

- [PASS] surname_gate: bio 'MCLAUGHLAN' vs stint 'McLaughlan, A. H. P' (exact)
- [PASS] initials: bio ['A', 'H', 'P'] ~ stint ['A', 'H', 'P']
- [PASS] age_gate: stint starts 1930, birth 1903 (age 27)
- [PASS] colony: 7 placed event(s) resolve to 'Cyprus'
- [PASS] tenure_overlap: 5 event tenure(s) overlap stint years 1930-1939
- [FAIL] position_sim: best 56 vs bar 60: 'asst. engrn., P.W.D' ~ 'Assistant Engineer'
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

