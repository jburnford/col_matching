<!-- {"case_id": "case_reid_harold-wallace_b1897", "bio_ids": ["reid_harold-wallace_b1897"], "stint_ids": ["Reid, H. W___Trinidad and Tobago___1928"]} -->
# Dossier case_reid_harold-wallace_b1897

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 106 official(s) with this surname in the graph's staff lists; 37 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `reid_harold-wallace_b1897`

- Printed name: **REID, HAROLD WALLACE**
- Birth year: 1897 (attested in editions [1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936])
- Appears in editions: [1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936]

### Verbatim printed entry text (OCR)

**Version `col1928-L69387.v` — printed in editions [1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936]:**

> REID, HAROLD WALLACE, B.Sc.—B. 1897; dep. inspr., mines, Trinidad, Sept., 1927.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1927 | dep. inspr., mines | Trinidad | [1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936] |

## Candidate stint `Reid, H. W___Trinidad and Tobago___1928`

- Staff-list name: **Reid, H. W** | colony: **Trinidad and Tobago** | listed 1928–1937 | editions [1928, 1929, 1931, 1933, 1934, 1937]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1928 | H. W. Reid | Deputy Inspector of Mines | Mines Department | — | — |
| 1929 | H. W. Reid | Deputy Inspector of Mines | Mines Department | — | — |
| 1931 | H. W. Reid | Assistant Petroleum Technologist | Mines Department | — | — |
| 1933 | H. W. Reid | Assistant Petroleum Technologist | MINES DEPARTMENT | — | — |
| 1934 | H. W. Reid | Assistant Petroleum Technologist | Mines Department | — | — |
| 1937 | H. W. Reid | Assistant Petroleum Technologist | MINES DEPARTMENT | — | — |

### Deterministic checks: `reid_harold-wallace_b1897` vs `Reid, H. W___Trinidad and Tobago___1928`

- [PASS] surname_gate: bio 'REID' vs stint 'Reid, H. W' (exact)
- [PASS] initials: bio ['H', 'W'] ~ stint ['H', 'W']
- [PASS] age_gate: stint starts 1928, birth 1897 (age 31)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1928-1937
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

