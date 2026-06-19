<!-- {"case_id": "case_davson_george-charles-wolsley_b1889", "bio_ids": ["davson_george-charles-wolsley_b1889"], "stint_ids": ["Davson, G. C. W___Straits Settlements___1931"]} -->
# Dossier case_davson_george-charles-wolsley_b1889

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `davson_george-charles-wolsley_b1889`

- Printed name: **DAVSON, George Charles Wolsley**
- Birth year: 1889 (attested in editions [1936, 1937])
- Honours: A.M.I.C.E
- Appears in editions: [1936, 1937]

### Verbatim printed entry text (OCR)

**Version `col1936-L60146.v` — printed in editions [1936, 1937]:**

> DAVSON, George Charles Wolsley, A.M.I.C.E.—B. 1889; ed. Cheltenham Coll., and Birmingham Univ.; asst. engnr., Nigeria, July, 1913; asst. engnr., Nigerian Rly., 1915; cadet as S.M.E., Chatham, 1916; lieut., R.E., 1917; ag. capt., 1919; asst. engnr., S.S., June, 1919; ex. engnr., Nov., 1928; senr. ex. engnr., Sept., 1933.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1913 | asst. engnr. | Nigeria | [1936, 1937] |
| 1 | 1915 | asst. engnr., Nigerian Rly | Nigeria *(inherited from previous clause)* | [1936, 1937] |
| 2 | 1916 | cadet as S.M.E., Chatham | Nigeria *(inherited from previous clause)* | [1936, 1937] |
| 3 | 1917 | lieut., R.E | Nigeria *(inherited from previous clause)* | [1936, 1937] |
| 4 | 1919 | ag. capt | Nigeria *(inherited from previous clause)* | [1936, 1937] |
| 5 | 1919 | asst. engnr. | Straits Settlements | [1936, 1937] |
| 6 | 1928 | ex. engnr | Straits Settlements *(inherited from previous clause)* | [1936, 1937] |
| 7 | 1933 | senr. ex. engnr | Straits Settlements *(inherited from previous clause)* | [1936, 1937] |

## Candidate stint `Davson, G. C. W___Straits Settlements___1931`

- Staff-list name: **Davson, G. C. W** | colony: **Straits Settlements** | listed 1931–1934 | editions [1931, 1933, 1934]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | G. C. W. Davson | Executive Engineer | Public Works | — | — |
| 1933 | G. C. W. Davson | Executive Engineers | Public Works | — | — |
| 1934 | G. C. W. Davson | Executive Engineer | Public Works | — | — |

### Deterministic checks: `davson_george-charles-wolsley_b1889` vs `Davson, G. C. W___Straits Settlements___1931`

- [PASS] surname_gate: bio 'DAVSON' vs stint 'Davson, G. C. W' (exact)
- [PASS] initials: bio ['G', 'C', 'W'] ~ stint ['G', 'C', 'W']
- [PASS] age_gate: stint starts 1931, birth 1889 (age 42)
- [PASS] colony: 3 placed event(s) resolve to 'Straits Settlements'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1931-1934
- [PASS] position_sim: best 62 vs bar 60: 'ex. engnr' ~ 'Executive Engineer'
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

