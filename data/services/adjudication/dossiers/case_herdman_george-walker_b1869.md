<!-- {"case_id": "case_herdman_george-walker_b1869", "bio_ids": ["herdman_george-walker_b1869"], "stint_ids": ["Herdman, G. W___South Africa___1912"]} -->
# Dossier case_herdman_george-walker_b1869

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `herdman_george-walker_b1869`

- Printed name: **HERDMAN, GEORGE WALKER**
- Birth year: 1869 (attested in editions [1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924])
- Honours: M.A
- Appears in editions: [1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924]

### Verbatim printed entry text (OCR)

**Version `col1913-L46675.v` — printed in editions [1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924]:**

> HERDMAN, GEORGE WALKER, M.A., B.Sc., M.Inst. C.E.—B. 1869; ed. Edinburgh Univ.; astt. engnr. waterworks, in S. Africa, 1896-1899; engnr. waterworks, England, 1900-1903; astt. engnr., irrigtn. dept., Transvaal, Sept., 1903; exec. engnr., July, 1904; inspecting engnr., P.W.D., Transvaal, Mar., 1907; inspecting engnr., P.W.D., Union of S. Africa, May, 1910; astt. dir. of irrigtn., Union of S. Africa, Sept., 1917.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1896–1899 | astt. engnr. waterworks, in S. Africa | — | [1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924] |
| 1 | 1900–1903 | engnr. waterworks, England | — | [1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924] |
| 2 | 1903 | astt. engnr., irrigtn. dept. | Transvaal | [1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924] |
| 3 | 1904 | exec. engnr | Transvaal *(inherited from previous clause)* | [1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924] |
| 4 | 1907 | inspecting engnr., P.W.D. | Transvaal | [1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924] |
| 5 | 1910 | inspecting engnr., P.W.D., Union of S. Africa | Transvaal *(inherited from previous clause)* | [1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924] |
| 6 | 1917 | astt. dir. of irrigtn., Union of S. Africa | Transvaal *(inherited from previous clause)* | [1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924] |

## Candidate stint `Herdman, G. W___South Africa___1912`

- Staff-list name: **Herdman, G. W** | colony: **South Africa** | listed 1912–1914 | editions [1912, 1914]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | G. W. Herdman | Inspecting Engineer | Province of Transvaal | — | — |
| 1914 | G. W. Herdman | Inspecting Engineer | Public Works Department | — | — |

### Deterministic checks: `herdman_george-walker_b1869` vs `Herdman, G. W___South Africa___1912`

- [PASS] surname_gate: bio 'HERDMAN' vs stint 'Herdman, G. W' (exact)
- [PASS] initials: bio ['G', 'W'] ~ stint ['G', 'W']
- [PASS] age_gate: stint starts 1912, birth 1869 (age 43)
- [FAIL] colony: no placed event resolves to 'South Africa'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1914
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

