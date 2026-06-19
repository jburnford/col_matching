<!-- {"case_id": "case_lamb_f-m_e1907", "bio_ids": ["lamb_f-m_e1907"], "stint_ids": ["Lamb, F. W. M___Trinidad and Tobago___1949"]} -->
# Dossier case_lamb_f-m_e1907

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 27 official(s) with this surname in the graph's staff lists; 10 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `lamb_f-m_e1907`

- Printed name: **LAMB, F. M**
- Birth year: not printed
- Appears in editions: [1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935]

### Verbatim printed entry text (OCR)

**Version `col1912-L45527.v` — printed in editions [1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935]:**

> LAMB, F. M.—Senior staff surrv., E.A.P., May, 1907; astt. dist. comsnr., Uganda Prot., Feb., 1910; astt. dist. comsnr., E.A.P., Jan., 1911; dist. comsnr., Jan., 1918.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1907 | Senior staff surrv. | East Africa Protectorate | [1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935] |
| 1 | 1910 | astt. dist. comsnr. | Uganda | [1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935] |
| 2 | 1911 | astt. dist. comsnr. | East Africa Protectorate | [1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935] |
| 3 | 1918 | dist. comsnr | East Africa Protectorate *(inherited from previous clause)* | [1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935] |

## Candidate stint `Lamb, F. W. M___Trinidad and Tobago___1949`

- Staff-list name: **Lamb, F. W. M** | colony: **Trinidad and Tobago** | listed 1949–1954 | editions [1949, 1953, 1954]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | F. W. M. Lamb | Senior Pathologist | Bacteriological Laboratory | — | — |
| 1953 | F. W. Lamb | Supervisor of Bacteriological Laboratories | Civil Establishment | — | — |
| 1954 | F. W. Lamb | Supervisor of Bacteriological Laboratories | Civil Establishment | — | — |

### Deterministic checks: `lamb_f-m_e1907` vs `Lamb, F. W. M___Trinidad and Tobago___1949`

- [PASS] surname_gate: bio 'LAMB' vs stint 'Lamb, F. W. M' (exact)
- [PASS] initials: bio ['F', 'M'] ~ stint ['F', 'W', 'M']
- [PASS] age_gate: stint starts 1949; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1954
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

