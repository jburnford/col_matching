<!-- {"case_id": "case_mettam_richard-william-morison_b1893", "bio_ids": ["mettam_richard-william-morison_b1893"], "stint_ids": ["Mettam, R. W. M___Kenya___1928", "Mettam, R. W___Uganda___1933"]} -->
# Dossier case_mettam_richard-william-morison_b1893

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Mettam, R. W. M___Kenya___1928` is also gate-compatible with biography(ies) outside this case: ['mettam_richard-william-morison_b1895'] (already linked elsewhere or filtered).
- NOTE: stint `Mettam, R. W___Uganda___1933` is also gate-compatible with biography(ies) outside this case: ['mettam_richard-william-morison_b1895'] (already linked elsewhere or filtered).

## Biography `mettam_richard-william-morison_b1893`

- Printed name: **METTAM, RICHARD WILLIAM MORISON**
- Birth year: 1893 (attested in editions [1939, 1940])
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L69080.v` — printed in editions [1939, 1940]:**

> METTAM, RICHARD WILLIAM MORISON.—B. 1893; prof. of bacteriology, Royal Vety. Coll., Dublin, Ireland; M.R.C.V.S., 1917; lieut., R.A.V.C., Aug., 1917; served in France and Flanders, 1917-1918; capt., 1918; Rhine Army, 1919; vety. research offr., dept. of agr., Onderstepoort, Pretoria, Jan., 1920; prof. of anatomy and embryology, Univ. of Witwatersrand, 1922-26; prof. of anatomy and embryology, Transvaal Univ. Coll., Pretoria, 1926-27; ag. asst., ch. vety. research lab., Kabeta, Kenya, 1927-28; vety. pathologist, Nigeria, 1937.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1917 | M.R.C.V.S | — | [1939, 1940] |
| 1 | 1917 | lieut., R.A.V.C | — | [1939, 1940] |
| 2 | 1917–1918 | served in France and Flanders | — | [1939, 1940] |
| 3 | 1918 | capt | — | [1939, 1940] |
| 4 | 1919 | Rhine Army | — | [1939, 1940] |
| 5 | 1920 | vety. research offr., dept. of agr., Onderstepoort, Pretoria | — | [1939, 1940] |
| 6 | 1922–1926 | prof. of anatomy and embryology, Univ. of Witwatersrand | — | [1939, 1940] |
| 7 | 1926–1927 | prof. of anatomy and embryology, Transvaal Univ. Coll., Pretoria | — | [1939, 1940] |
| 8 | 1927–1928 | ag. asst., ch. vety. research lab., Kabeta | Kenya | [1939, 1940] |
| 9 | 1937 | vety. pathologist | Nigeria | [1939, 1940] |

## Candidate stint `Mettam, R. W. M___Kenya___1928`

- Staff-list name: **Mettam, R. W. M** | colony: **Kenya** | listed 1928–1930 | editions [1928, 1929, 1930]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1928 | R. W. M. Mettam | Veterinary Research Officer | Veterinary Research | — | — |
| 1929 | R. W. M. Mettam | Veterinary Research Officers | Veterinary Research | — | — |
| 1930 | R. W. M. Mettam | Veterinary Research Officers | Veterinary Research | — | — |

### Deterministic checks: `mettam_richard-william-morison_b1893` vs `Mettam, R. W. M___Kenya___1928`

- [PASS] surname_gate: bio 'METTAM' vs stint 'Mettam, R. W. M' (exact)
- [PASS] initials: bio ['R', 'W', 'M'] ~ stint ['R', 'W', 'M']
- [PASS] age_gate: stint starts 1928, birth 1893 (age 35)
- [PASS] colony: 1 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1928-1930
- [FAIL] position_sim: best 52 vs bar 60: 'ag. asst., ch. vety. research lab., Kabeta' ~ 'Veterinary Research Officer'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Mettam, R. W___Uganda___1933`

- Staff-list name: **Mettam, R. W** | colony: **Uganda** | listed 1933–1937 | editions [1933, 1937]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | R. W. Mettam | Veterinary Pathologist | Veterinary Department | — | — |
| 1937 | R. W. Mettam | Veterinary Pathologist | Veterinary Department | — | — |

### Deterministic checks: `mettam_richard-william-morison_b1893` vs `Mettam, R. W___Uganda___1933`

- [PASS] surname_gate: bio 'METTAM' vs stint 'Mettam, R. W' (exact)
- [PASS] initials: bio ['R', 'W', 'M'] ~ stint ['R', 'W']
- [PASS] age_gate: stint starts 1933, birth 1893 (age 40)
- [FAIL] colony: no placed event resolves to 'Uganda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1933-1937
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

