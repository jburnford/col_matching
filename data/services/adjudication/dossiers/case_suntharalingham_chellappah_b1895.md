<!-- {"case_id": "case_suntharalingham_chellappah_b1895", "bio_ids": ["suntharalingham_chellappah_b1895"], "stint_ids": ["Suntharalingam, C___Ceylon___1923"]} -->
# Dossier case_suntharalingham_chellappah_b1895

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['suntharalingham_chellappah_b1895'] carry a single initial only — the namesake trap applies.

## Biography `suntharalingham_chellappah_b1895`

- Printed name: **SUNTHARALINGHAM, CHELLAPPAH**
- Birth year: 1895 (attested in editions [1922])
- Appears in editions: [1922]

### Verbatim printed entry text (OCR)

**Version `col1922-L56431.v` — printed in editions [1922]:**

> SUNTHARALINGHAM, CHELLAPPAH.—B. 1895; cadet, Ceylon civ. serv., Dec., 1920; attd. to Badulla Kach., Jan., 1921.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1920 | cadet, Ceylon civ. serv | Ceylon | [1922] |
| 1 | 1921 | attd. to Badulla Kach | Ceylon *(inherited from previous clause)* | [1922] |

## Candidate stint `Suntharalingam, C___Ceylon___1923`

- Staff-list name: **Suntharalingam, C** | colony: **Ceylon** | listed 1923–1940 | editions [1923, 1925, 1927, 1928, 1929, 1931, 1934, 1936, 1937, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1923 | C. Suntharalingam | Professor of Mathematics | University College | — | — |
| 1925 | C. Suntharalingam | Professor of Mathematics | University College | — | — |
| 1927 | C. Suntharalingam | Professor of Mathematics | University College | — | — |
| 1928 | C. Suntharalingam | Professor of Mathematics | University College | — | — |
| 1929 | C. Suntharalingam | Professor of Mathematics | University College | — | — |
| 1931 | C. Suntharalingam | Professor of Mathematics | University College | — | — |
| 1934 | C. Suntharalingam | Professor of Mathematics | Staff—Ceylon University College | — | — |
| 1936 | C. Suntharalingam | Professor of Mathematics | Ceylon University College | — | — |
| 1937 | C. Suntharalingam | Professor of Mathematics | CEYLON UNIVERSITY COLLEGE | — | — |
| 1940 | C. Suntharalingam | Professor of Mathematics | Ceylon University College | — | — |

### Deterministic checks: `suntharalingham_chellappah_b1895` vs `Suntharalingam, C___Ceylon___1923`

- [PASS] surname_gate: bio 'SUNTHARALINGHAM' vs stint 'Suntharalingam, C' (fuzzy:1)
- [PASS] initials: bio ['C'] ~ stint ['C']
- [PASS] age_gate: stint starts 1923, birth 1895 (age 28)
- [PASS] colony: 2 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1923-1940
- [FAIL] position_sim: best 27 vs bar 60: 'attd. to Badulla Kach' ~ 'Professor of Mathematics'
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

