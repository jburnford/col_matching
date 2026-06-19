<!-- {"case_id": "case_watson_h-c_b1882", "bio_ids": ["watson_h-c_b1882"], "stint_ids": ["Watson, Harrison___Canada___1907"]} -->
# Dossier case_watson_h-c_b1882

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 119 official(s) with this surname in the graph's staff lists; 67 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Watson, Harrison___Canada___1907` is also gate-compatible with biography(ies) outside this case: ['watson_a-h_e1900', 'watson_edwin-henry_e1899', 'watson_herbert-gordon_e1895'] (already linked elsewhere or filtered).

## Biography `watson_h-c_b1882`

- Printed name: **WATSON, H.C**
- Birth year: 1882 (attested in editions [1939, 1940])
- Honours: B.A.O, M.B, R.U
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L71626.v` — printed in editions [1939, 1940]:**

> WATSON, H.C., M.B., B.Ch., B.A.O., R.U., Ireland.—B. 1882; ed. Campbell Coll. and Queen's Coll., Belfast; Transvaal civ. serv., July, 1909; physn. supt., Fort Beaufort ment. hosp., 1919; Alexandra instn., Cape Town, 1921; Bloemfontein ment. hosp., 1923.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1909 | Transvaal civ. serv | Transvaal | [1939, 1940] |
| 1 | 1919 | physn. supt., Fort Beaufort ment. hosp | Transvaal *(inherited from previous clause)* | [1939, 1940] |
| 2 | 1921 | Alexandra instn., Cape Town | Cape of Good Hope | [1939, 1940] |
| 3 | 1923 | Bloemfontein ment. hosp | Cape of Good Hope *(inherited from previous clause)* | [1939, 1940] |

## Candidate stint `Watson, Harrison___Canada___1907`

- Staff-list name: **Watson, Harrison** | colony: **Canada** | listed 1907–1918 | editions [1907, 1912, 1913, 1914, 1915, 1917, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1907 | Harrison Watson | Agent-General | Civil Establishment | — | — |
| 1912 | Harrison Watson | Agent-General | Legislative Assembly | — | — |
| 1913 | Harrison Watson | Agent-General | — | — | — |
| 1914 | Harrison Watson | Agent-General in London | Executive Council | — | — |
| 1915 | Harrison Watson | Agent-General in London | Civil Establishment | — | — |
| 1917 | Harrison Watson | Agent-General | Civil Establishment | — | — |
| 1918 | Harrison Watson | Agent-General | Executive Council | — | — |

### Deterministic checks: `watson_h-c_b1882` vs `Watson, Harrison___Canada___1907`

- [PASS] surname_gate: bio 'WATSON' vs stint 'Watson, Harrison' (exact)
- [PASS] initials: bio ['H', 'C'] ~ stint ['H']
- [PASS] age_gate: stint starts 1907, birth 1882 (age 25)
- [FAIL] colony: no placed event resolves to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1907-1918
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

