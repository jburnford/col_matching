<!-- {"case_id": "case_mabb_victor-leopold_b1889", "bio_ids": ["mabb_victor-leopold_b1889"], "stint_ids": ["Mabb, V. L___Nigeria___1934"]} -->
# Dossier case_mabb_victor-leopold_b1889

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mabb_victor-leopold_b1889`

- Printed name: **MABB, VICTOR LEOPOLD**
- Birth year: 1889 (attested in editions [1930, 1936, 1940])
- Honours: M.C
- Appears in editions: [1930, 1936, 1940]

### Verbatim printed entry text (OCR)

**Version `col1930-L66401.v` — printed in editions [1930, 1936, 1940]:**

> MABB, CAPT. VICTOR LEOPOLD, M.C., Chevalier de la Légion d'Honneur.—B. 1889; joined "Fort Garry" Regt. 18th Canadian Reserves, Aug., 1914; served in France as comsnr. to Tank Corps, Dec., 1916; left Army, July, 1920; ment. in desps.; admstve. serv., N. Provs., Nigeria, 1920; transf. prisons dept., S. Provs. as suplt., prisons, 1924; ag. inspr., prisons, 1925; dep. dir., prisons, 1926; dir., prisons, S. Provs., 1932; dir., prisons, 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914 | joined "Fort Garry" Regt. 18th Canadian Reserves | — | [1930, 1936, 1940] |
| 1 | 1916 | served in France as comsnr. to Tank Corps | — | [1930, 1936, 1940] |
| 2 | 1920 | left Army | — | [1930, 1936, 1940] |
| 3 | 1920 | admstve. serv., N. Provs. | Nigeria | [1930, 1936, 1940] |
| 4 | 1924 | transf. prisons dept., S. Provs. as suplt., prisons | Nigeria *(inherited from previous clause)* | [1930, 1936, 1940] |
| 5 | 1925 | ag. inspr., prisons | Nigeria *(inherited from previous clause)* | [1930, 1936, 1940] |
| 6 | 1926 | dep. dir., prisons | Nigeria *(inherited from previous clause)* | [1930, 1936, 1940] |
| 7 | 1932 | dir., prisons, S. Provs | Nigeria *(inherited from previous clause)* | [1930, 1936, 1940] |
| 8 | 1938 | dir., prisons | Nigeria *(inherited from previous clause)* | [1930, 1936, 1940] |

## Candidate stint `Mabb, V. L___Nigeria___1934`

- Staff-list name: **Mabb, V. L** | colony: **Nigeria** | listed 1934–1939 | editions [1934, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | V. L. Mabb | Deputy Director of Prisons | Prisons, Southern Provinces | — | Captain |
| 1939 | V. L. Mabb | Director | Prisons | — | Captain |

### Deterministic checks: `mabb_victor-leopold_b1889` vs `Mabb, V. L___Nigeria___1934`

- [PASS] surname_gate: bio 'MABB' vs stint 'Mabb, V. L' (exact)
- [PASS] initials: bio ['V', 'L'] ~ stint ['V', 'L']
- [PASS] age_gate: stint starts 1934, birth 1889 (age 45)
- [PASS] colony: 6 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1934-1939
- [PASS] position_sim: best 78 vs bar 60: 'dir., prisons' ~ 'Deputy Director of Prisons'
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

