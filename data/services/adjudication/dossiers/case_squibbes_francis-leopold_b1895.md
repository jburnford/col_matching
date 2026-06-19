<!-- {"case_id": "case_squibbes_francis-leopold_b1895", "bio_ids": ["squibbes_francis-leopold_b1895"], "stint_ids": ["Squibbs, F. L___Leeward Islands___1927", "Squibbs, F. L___Seychelles___1936"]} -->
# Dossier case_squibbes_francis-leopold_b1895

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Squibbs, F. L___Leeward Islands___1927` is also gate-compatible with biography(ies) outside this case: ['squibb_francis-leopold_b1895'] (already linked elsewhere or filtered).
- NOTE: stint `Squibbs, F. L___Seychelles___1936` is also gate-compatible with biography(ies) outside this case: ['squibb_francis-leopold_b1895'] (already linked elsewhere or filtered).

## Biography `squibbes_francis-leopold_b1895`

- Printed name: **SQUIBBES, Francis Leopold**
- Birth year: 1895 (attested in editions [1940])
- Appears in editions: [1940]

### Verbatim printed entry text (OCR)

**Version `col1940-L68616.v` — printed in editions [1940]:**

> SQUIBBES, Francis Leopold.—B. 1895; ed. Towcester Schil.; served Manchester Rgt., 1914-19; Imp. war graves comm., 1920-22; entd. R. botanic gardens, Kew, 1922; asst. supt., botanical and forest dept., Hong Kong, 1924; asst. curator and agrl. offr., Dominica, 1926; ag. agrl. supt., Apr. to Nov., 1931; asst. dir., agr., Seychelles, 1932; dir., Mar., 1934; mem., ex. and lex. couns., Apr., 1934; agric. offr., Gold Coast, 1939.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914–1919 | served Manchester Rgt | — | [1940] |
| 1 | 1920–1922 | Imp. war graves comm | — | [1940] |
| 2 | 1922 | entd. R. botanic gardens, Kew | — | [1940] |
| 3 | 1924 | asst. supt., botanical and forest dept. | Hong Kong | [1940] |
| 4 | 1926 | asst. curator and agrl. offr. | Dominica | [1940] |
| 5 | 1931 | ag. agrl. supt | Dominica *(inherited from previous clause)* | [1940] |
| 6 | 1932 | asst. dir., agr. | Seychelles | [1940] |
| 7 | 1934 | dir | Seychelles *(inherited from previous clause)* | [1940] |
| 8 | 1939 | agric. offr. | Gold Coast | [1940] |

## Candidate stint `Squibbs, F. L___Leeward Islands___1927`

- Staff-list name: **Squibbs, F. L** | colony: **Leeward Islands** | listed 1927–1928 | editions [1927, 1928]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | F. L. Squibbs | 2nd Assistant Curator | Botanical | — | — |
| 1928 | F. L. Squibbs | 2nd Assistant Curator | Botanical | — | — |

### Deterministic checks: `squibbes_francis-leopold_b1895` vs `Squibbs, F. L___Leeward Islands___1927`

- [PASS] surname_gate: bio 'SQUIBBES' vs stint 'Squibbs, F. L' (fuzzy:1)
- [PASS] initials: bio ['F', 'L'] ~ stint ['F', 'L']
- [PASS] age_gate: stint starts 1927, birth 1895 (age 32)
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1927-1928
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Squibbs, F. L___Seychelles___1936`

- Staff-list name: **Squibbs, F. L** | colony: **Seychelles** | listed 1936–1939 | editions [1936, 1937, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | F. L. Squibbs | Director of Agriculture | Department of Agriculture | — | — |
| 1937 | F. L. Squibbs | Director of Agriculture | Department of Agriculture | — | — |
| 1939 | F. L. Squibbs | Director of Agriculture | Department of Agriculture | — | — |

### Deterministic checks: `squibbes_francis-leopold_b1895` vs `Squibbs, F. L___Seychelles___1936`

- [PASS] surname_gate: bio 'SQUIBBES' vs stint 'Squibbs, F. L' (fuzzy:1)
- [PASS] initials: bio ['F', 'L'] ~ stint ['F', 'L']
- [PASS] age_gate: stint starts 1936, birth 1895 (age 41)
- [PASS] colony: 2 placed event(s) resolve to 'Seychelles'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1936-1939
- [FAIL] position_sim: best 23 vs bar 60: 'dir' ~ 'Director of Agriculture'
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

