<!-- {"case_id": "case_robertson_colin-brown_b1803", "bio_ids": ["robertson_colin-brown_b1803"], "stint_ids": ["Robertson, C. B___Hong Kong___1922"]} -->
# Dossier case_robertson_colin-brown_b1803

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 131 official(s) with this surname in the graph's staff lists; 54 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- Phase 1 found `robertson_colin-brown_b1803` ↔ `Robertson, C. B___Hong Kong___1922` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Robertson, C. B___Hong Kong___1922` is also gate-compatible with biography(ies) outside this case: ['robertson_colin-brown_b1893'] (already linked elsewhere or filtered).

## Biography `robertson_colin-brown_b1803`

- Printed name: **ROBERTSON, COLIN BROWN**
- Birth year: 1803 (attested in editions [1939, 1940])
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L70216.v` — printed in editions [1939, 1940]:**

> ROBERTSON, COLIN BROWN.—B. 1803; ed. Leven higher grade; war serv., 1914-19; exec. engrnr., P.W.D., Hong Kong, 1920.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1920 | exec. engrnr., P.W.D. | Hong Kong | [1939, 1940] |

## Candidate stint `Robertson, C. B___Hong Kong___1922`

- Staff-list name: **Robertson, C. B** | colony: **Hong Kong** | listed 1922–1940 | editions [1922, 1923, 1924, 1925, 1927, 1929, 1930, 1931, 1932, 1933, 1934, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | C. B. Robertson | Engineer | General Staff | — | — |
| 1923 | C. B. Robertson | Engineers | General Staff | — | — |
| 1924 | C. B. Robertson | Engineers | General Staff | — | — |
| 1925 | C. B. Robertson | Engineers | Public Health and Buildings Ordinance | — | — |
| 1927 | C. B. Robertson | Engineers | Public Health and Buildings Ordinance | — | — |
| 1929 | C. B. Robertson | Engineers | Public Health and Buildings Ordinance | — | — |
| 1930 | C. B. Robertson | Engineer | Public Health and Buildings Ordinance | — | — |
| 1931 | C. B. Robertson | Engineer | Public Health and Buildings Ordinance | — | — |
| 1932 | C. B. Robertson | Architect | Public Works Department | — | — |
| 1933 | C. B. Robertson | Architects | Public Works Department | — | — |
| 1934 | C. B. Robertson | Architect | Public Works Department | — | — |
| 1937 | C. B. Robertson | Architect | Public Works Department | — | — |
| 1939 | C. B. Robertson | Executive Engineer | Public Works Department | — | — |
| 1940 | C. B. Robertson | Executive Engineers | Public Works Department | — | — |

### Deterministic checks: `robertson_colin-brown_b1803` vs `Robertson, C. B___Hong Kong___1922`

- [PASS] surname_gate: bio 'ROBERTSON' vs stint 'Robertson, C. B' (exact)
- [PASS] initials: bio ['C', 'B'] ~ stint ['C', 'B']
- [PASS] age_gate: stint starts 1922, birth 1803 (age 119)
- [PASS] colony: 1 placed event(s) resolve to 'Hong Kong'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1922-1940
- [PASS] position_sim: best 61 vs bar 60: 'exec. engrnr., P.W.D.' ~ 'Executive Engineer'
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

