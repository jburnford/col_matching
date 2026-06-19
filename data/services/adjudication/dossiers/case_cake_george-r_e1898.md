<!-- {"case_id": "case_cake_george-r_e1898", "bio_ids": ["cake_george-r_e1898"], "stint_ids": ["Cake, George R___Newfoundland___1906"]} -->
# Dossier case_cake_george-r_e1898

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `cake_george-r_e1898`

- Printed name: **CAKE, GEORGE R**
- Birth year: not printed
- Appears in editions: [1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927]

### Verbatim printed entry text (OCR)

**Version `col1912-L43036.v` — printed in editions [1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927]:**

> CAKE, GEORGE R.—Clik. to atty.-gen., Newfoundland, 1898 to 1900; clk., auditor-gen.'s dept., 1901 to 1904; conf'l. clk., govt. house, 1904.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1898–1900 | Clik. to atty.-gen. | Newfoundland | [1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927] |
| 1 | 1901–1904 | clk., auditor-gen.'s dept | Newfoundland *(inherited from previous clause)* | [1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927] |
| 2 | 1904 | conf'l. clk., govt. house | Newfoundland *(inherited from previous clause)* | [1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927] |

## Candidate stint `Cake, George R___Newfoundland___1906`

- Staff-list name: **Cake, George R** | colony: **Newfoundland** | listed 1906–1927 | editions [1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1927]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1906 | George R. Cake | Clerk | Civil Establishment | — | — |
| 1907 | George R. Cake | Confidential Clerk | Civil Establishment | — | — |
| 1908 | George R. Cake | Confidential Clerk | Civil Establishment | — | — |
| 1909 | George R. Cake | Confidential Clerk | Civil Establishment | — | — |
| 1910 | George R. Cake | Confidential Clerk | Civil Establishment | — | — |
| 1911 | George R. Cake | Confidential Clerk | Civil Establishment | — | — |
| 1912 | George R. Cake | Confidential Clerk | Civil Establishment | — | — |
| 1913 | George R. Cake | Confidential Clerk | Civil Establishment | — | — |
| 1914 | George R. Cake | Confidential Clerk | Civil Establishment | — | — |
| 1915 | George R. Cake | Confidential Clerk | Civil Establishment | — | — |
| 1917 | George R. Cake | Confidential Clerk | Civil Establishment | — | — |
| 1918 | George R. Cake | Confidential Clerk | Civil Establishment | — | — |
| 1919 | George R. Cake | Confidential Clerk | Civil Establishment | — | — |
| 1920 | George R. Cake | Confidential Clerk | Civil Establishment | — | — |
| 1921 | George R. Cake | Confidential Clerk | Civil Establishment | — | — |
| 1927 | George R. Cake | Confidential Clerk | Civil Establishment | — | — |

### Deterministic checks: `cake_george-r_e1898` vs `Cake, George R___Newfoundland___1906`

- [PASS] surname_gate: bio 'CAKE' vs stint 'Cake, George R' (exact)
- [PASS] initials: bio ['G', 'R'] ~ stint ['G', 'R']
- [PASS] age_gate: stint starts 1906; no printed birth year — UNCHECKED
- [PASS] colony: 3 placed event(s) resolve to 'Newfoundland'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1906-1927
- [FAIL] position_sim: best 47 vs bar 60: 'conf'l. clk., govt. house' ~ 'Confidential Clerk'
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

