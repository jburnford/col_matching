<!-- {"case_id": "case_earle_hugh-j-m_b1896", "bio_ids": ["earle_hugh-j-m_b1896"], "stint_ids": ["Earle, H. J. M___British Guiana___1923", "Earle, M___British Guiana___1913"]} -->
# Dossier case_earle_hugh-j-m_b1896

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 17 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `earle_hugh-j-m_b1896`

- Printed name: **EARLE, HUGH J. M**
- Birth year: 1896 (attested in editions [1923, 1924, 1929, 1930, 1931, 1932, 1933, 1935, 1936, 1940])
- Appears in editions: [1923, 1924, 1929, 1930, 1931, 1932, 1933, 1935, 1936, 1940]

### Verbatim printed entry text (OCR)

**Version `col1923-L54136.v` — printed in editions [1923, 1924, 1929, 1930, 1931, 1932, 1933, 1935, 1936, 1940]:**

> EARLE, HUGH J. M.—B. 1896; ed. Cheltenham; on war service, 1914-19; capt., 4th Batt. Essex Regt., 1918; ent. dept. of lands and mines, R. Guiana, 2nd Aug., 1921; 6th cls. clk., secretariat, 1st Mar., 1922; sec. for sp. duty in connexion with Georgetown town disturbances, 1924; ag. A.D.C. to O.A.G., May-Nov., 1925; cadet, admvte. serv., Nigeria, 1927.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1918 | capt., 4th Batt. Essex Regt | — | [1923, 1924, 1929, 1930, 1931, 1932, 1933, 1935, 1936, 1940] |
| 1 | 1921 | ent. dept. of lands and mines, R. Guiana | — | [1923, 1924, 1929, 1930, 1931, 1932, 1933, 1935, 1936, 1940] |
| 2 | 1922 | 6th cls. clk., secretariat | — | [1923, 1924, 1929, 1930, 1931, 1932, 1933, 1935, 1936, 1940] |
| 3 | 1924 | sec. for sp. duty in connexion with Georgetown town disturbances | — | [1923, 1924, 1929, 1930, 1931, 1932, 1933, 1935, 1936, 1940] |
| 4 | 1925 | ag. A.D.C. to O.A.G., May- | — | [1923, 1924, 1929, 1930, 1931, 1932, 1933, 1935, 1936, 1940] |
| 5 | 1927 | cadet, admvte. serv. | Nigeria | [1923, 1924, 1929, 1930, 1931, 1932, 1933, 1935, 1936, 1940] |

## Candidate stint `Earle, H. J. M___British Guiana___1923`

- Staff-list name: **Earle, H. J. M** | colony: **British Guiana** | listed 1923–1925 | editions [1923, 1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1923 | H. J. M. Earle | 6th Clerk | Colonial Secretariat | — | — |
| 1924 | H. J. M. Earle | 6th Clerk | Colonial Secretariat | — | — |
| 1925 | H. J. M. Earle | Clerk | Colonial Secretariat | — | — |

### Deterministic checks: `earle_hugh-j-m_b1896` vs `Earle, H. J. M___British Guiana___1923`

- [PASS] surname_gate: bio 'EARLE' vs stint 'Earle, H. J. M' (exact)
- [PASS] initials: bio ['H', 'J', 'M'] ~ stint ['H', 'J', 'M']
- [PASS] age_gate: stint starts 1923, birth 1896 (age 27)
- [FAIL] colony: no placed event resolves to 'British Guiana'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1923-1925
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Earle, M___British Guiana___1913`

- Staff-list name: **Earle, M** | colony: **British Guiana** | listed 1913–1914 | editions [1913, 1914]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1913 | M. Earle | Clerical Assistant | Education | — | — |
| 1914 | M. Earle | Clerical Assistant | Primary Schools | — | — |

### Deterministic checks: `earle_hugh-j-m_b1896` vs `Earle, M___British Guiana___1913`

- [PASS] surname_gate: bio 'EARLE' vs stint 'Earle, M' (exact)
- [PASS] initials: bio ['H', 'J', 'M'] ~ stint ['M']
- [PASS] age_gate: stint starts 1913, birth 1896 (age 17)
- [FAIL] colony: no placed event resolves to 'British Guiana'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1913-1914
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

