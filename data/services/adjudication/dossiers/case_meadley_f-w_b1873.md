<!-- {"case_id": "case_meadley_f-w_b1873", "bio_ids": ["meadley_f-w_b1873"], "stint_ids": ["Meadley, F. W___Transvaal___1906"]} -->
# Dossier case_meadley_f-w_b1873

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `meadley_f-w_b1873`

- Printed name: **MEADLEY, F. W**
- Birth year: 1873 (attested in editions [1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933])
- Appears in editions: [1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933]

### Verbatim printed entry text (OCR)

**Version `col1923-L56614.v` — printed in editions [1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933]:**

> MEADLEY, F. W.—B. 1873; clk., G.P.O., Transvaal, 1902; distributor of stamps, 1903; astt. sec., investment bd., 1908; sec., pub. debt. comm., 1918.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1902 | clk., G.P.O. | Transvaal | [1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933] |
| 1 | 1903 | distributor of stamps | Transvaal *(inherited from previous clause)* | [1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933] |
| 2 | 1908 | astt. sec., investment bd | Transvaal *(inherited from previous clause)* | [1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933] |
| 3 | 1918 | sec., pub. debt. comm | Transvaal *(inherited from previous clause)* | [1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933] |

## Candidate stint `Meadley, F. W___Transvaal___1906`

- Staff-list name: **Meadley, F. W** | colony: **Transvaal** | listed 1906–1907 | editions [1906, 1907]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1906 | F. W. Meadley | Distributor of Stamps | Treasury | — | — |
| 1907 | F. W. Meadley | Distributor of Stamps | Treasury | — | — |

### Deterministic checks: `meadley_f-w_b1873` vs `Meadley, F. W___Transvaal___1906`

- [PASS] surname_gate: bio 'MEADLEY' vs stint 'Meadley, F. W' (exact)
- [PASS] initials: bio ['F', 'W'] ~ stint ['F', 'W']
- [PASS] age_gate: stint starts 1906, birth 1873 (age 33)
- [PASS] colony: 4 placed event(s) resolve to 'Transvaal'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1906-1907
- [PASS] position_sim: best 100 vs bar 60: 'distributor of stamps' ~ 'Distributor of Stamps'
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

