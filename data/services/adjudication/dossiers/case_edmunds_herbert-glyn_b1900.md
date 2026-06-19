<!-- {"case_id": "case_edmunds_herbert-glyn_b1900", "bio_ids": ["edmunds_herbert-glyn_b1900"], "stint_ids": ["Edmunds, H. G___Falkland Islands___1932"]} -->
# Dossier case_edmunds_herbert-glyn_b1900

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 10 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Edmunds, H. G___Falkland Islands___1932` is also gate-compatible with biography(ies) outside this case: ['edmunds_harry_b1907'] (already linked elsewhere or filtered).

## Biography `edmunds_herbert-glyn_b1900`

- Printed name: **EDMUNDS, HERBERT GLYN**
- Birth year: 1900 (attested in editions [1937, 1940])
- Appears in editions: [1932, 1933, 1934, 1936, 1937, 1940]

### Verbatim printed entry text (OCR)

**Version `col1937-L60560.v` — printed in editions [1937, 1940]:**

> EDMUNDS, HERBERT GLYN.—B.1900; ed. Swansea and Univ. Coll., London; med. offr., Falkland Is., June, 1931; lieut., Falkland Is. Def. Force, July, 1931; ag. prin. med. offr., Mar. to Oct., 1932; M.S.A. (Lond.), 1932; ag. senr. med. offr., Dec., 1934 to Feb., 1935; med. offr., Nigeria, 1936.

**Version `col1936-L60456.v` — printed in editions [1936]:**

> EDMONDS, HERBERT GLYN.—B.1900; ed. Swansea and Univ. Coll., London; med. offr., Falkland Is., June, 1931; lieut., Falkland Is. Def. Force, July, 1931; ag. prin. med. offr., Mar. to Oct., 1932; M.S.A. (Lond.), 1932; ag. senr. med. offr., Dec., 1934 to Feb., 1935.

**Version `col1933-L59449.v` — printed in editions [1933, 1934]:**

> EDMUNDS, HERBERT GLYN.—B.1900; ed. Swansea and Univ. Coll., London; L.M.S.S.A. (Lond.) 1930; med. offr., Falkland Is., June, 1931; lieut., Falkland Is. Def. Force, July, 1931; ag. prin. med. offr., Mar. to Oct., 1932.

**Version `col1932-L59946.v` — printed in editions [1932]:**

> EDMONDS, HERBERT GLYN.—B.1900; ed. Swansea and Univ. Coll., London; L.M.S.S.A. (Lond.) 1930; med. offr., Falkland Is., June, 1931; lieut., Falkland Is. Def. Force, July, 1931.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1930 | L.M.S.S.A. (Lond.) | — | [1932, 1933, 1934] |
| 1 | 1931 | med. offr., Falkland Is | — | [1932, 1933, 1934, 1936, 1937, 1940] |
| 2 | 1931 | lieut., Falkland Is. Def. Force | — | [1932, 1933, 1934, 1936, 1937, 1940] |
| 3 | 1932 | ag. prin. med. offr | — | [1933, 1934, 1936, 1937, 1940] |
| 4 | 1932 | M.S.A. (Lond.) | — | [1936, 1937, 1940] |
| 5 | 1934–1935 | ag. senr. med. offr | — | [1936, 1937, 1940] |
| 6 | 1936 | med. offr. | Nigeria | [1937, 1940] |

## Candidate stint `Edmunds, H. G___Falkland Islands___1932`

- Staff-list name: **Edmunds, H. G** | colony: **Falkland Islands** | listed 1932–1936 | editions [1932, 1933, 1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1932 | H. G. Edmunds | Lieutenants | Military Department | — | — |
| 1932 | H. G. Edmunds | Medical Officer | Medical | — | — |
| 1933 | H. G. Edmunds | Medical Officer | Medical | — | — |
| 1933 | H. G. Edmunds | Lieutenants | Military Department | — | — |
| 1934 | H. G. Edmunds | Medical Officer | Medical | — | — |
| 1936 | H. G. Edmunds | Lieutenant | Military Department | — | Lieutenant |
| 1936 | H. G. Edmunds | Medical Officer | Medical | — | — |

### Deterministic checks: `edmunds_herbert-glyn_b1900` vs `Edmunds, H. G___Falkland Islands___1932`

- [PASS] surname_gate: bio 'EDMUNDS' vs stint 'Edmunds, H. G' (exact)
- [PASS] initials: bio ['H', 'G'] ~ stint ['H', 'G']
- [PASS] age_gate: stint starts 1932, birth 1900 (age 32)
- [FAIL] colony: no placed event resolves to 'Falkland Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1932-1936
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

