<!-- {"case_id": "case_wohlmann_ward-george_b1872", "bio_ids": ["wohlmann_ward-george_b1872"], "stint_ids": ["Wilmann, G___Mauritius___1922"]} -->
# Dossier case_wohlmann_ward-george_b1872

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `wohlmann_ward-george_b1872`

- Printed name: **WOHLMANN, Ward George**
- Birth year: 1872 (attested in editions [1931, 1932, 1933, 1934, 1935])
- Honours: I.S.O (1934)
- Appears in editions: [1931, 1932, 1933, 1934, 1935]

### Verbatim printed entry text (OCR)

**Version `col1931-L69455.v` — printed in editions [1931, 1932, 1933, 1934, 1935]:**

> WOHLMANN, Ward George, I.S.O. (1934).—B. 1872; ed. N.Z. state schls.; N.Z. permanent arty., 1894-95; N.Z. pol., 1895; sergt., 1906; senr. sergt., 1914; sub-inspr., 1918; inspr., 1921; aspt., 1926; comsnr., 1930; was comsnr. of pol., Samoa, 1920-22.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1894–1895 | N.Z. permanent arty | New Zealand | [1931, 1932, 1933, 1934, 1935] |
| 1 | 1895 | N.Z. pol | New Zealand | [1931, 1932, 1933, 1934, 1935] |
| 2 | 1906 | sergt | New Zealand *(inherited from previous clause)* | [1931, 1932, 1933, 1934, 1935] |
| 3 | 1914 | senr. sergt | New Zealand *(inherited from previous clause)* | [1931, 1932, 1933, 1934, 1935] |
| 4 | 1918 | sub-inspr | New Zealand *(inherited from previous clause)* | [1931, 1932, 1933, 1934, 1935] |
| 5 | 1920–1922 | was comsnr. of pol., Samoa | New Zealand *(inherited from previous clause)* | [1931, 1932, 1933, 1934, 1935] |
| 6 | 1921 | inspr | New Zealand *(inherited from previous clause)* | [1931, 1932, 1933, 1934, 1935] |
| 7 | 1926 | aspt | New Zealand *(inherited from previous clause)* | [1931, 1932, 1933, 1934, 1935] |
| 8 | 1930 | comsnr | New Zealand *(inherited from previous clause)* | [1931, 1932, 1933, 1934, 1935] |

## Candidate stint `Wilmann, G___Mauritius___1922`

- Staff-list name: **Wilmann, G** | colony: **Mauritius** | listed 1922–1931 | editions [1922, 1923, 1925, 1927, 1929, 1931]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | G. Wilmann | Head Inspector | Mare-aux-Vacoas Waterworks | — | — |
| 1923 | G. Wilmann | Head Inspector | MARE-AUX-VACOAS WATERWORKS | — | — |
| 1925 | G. Wilmann | Head Inspector | Mare-aux-Vacoas Waterworks | — | — |
| 1927 | G. Wilmann | Head Inspector | Mare-aux-Vacoas Waterworks | — | — |
| 1929 | G. Wilmann | Head Inspector | MARE-AUX-VACOAS WATERWORKS | — | — |
| 1931 | G. Wilmann | Head Inspector | MARE-AUX-VACOAS WATERWORKS | — | — |

### Deterministic checks: `wohlmann_ward-george_b1872` vs `Wilmann, G___Mauritius___1922`

- [PASS] surname_gate: bio 'WOHLMANN' vs stint 'Wilmann, G' (fuzzy:2)
- [PASS] initials: bio ['W', 'G'] ~ stint ['G']
- [PASS] age_gate: stint starts 1922, birth 1872 (age 50)
- [FAIL] colony: no placed event resolves to 'Mauritius'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1922-1931
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

