<!-- {"case_id": "case_rock_alfred-milton_b1888", "bio_ids": ["rock_alfred-milton_b1888"], "stint_ids": ["Rock, A. M___Leeward Islands___1917"]} -->
# Dossier case_rock_alfred-milton_b1888

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `rock_alfred-milton_b1888`

- Printed name: **ROCK, ALFRED MILTON**
- Birth year: 1888 (attested in editions [1930, 1931, 1932, 1934, 1935, 1936, 1937, 1939, 1940])
- Appears in editions: [1930, 1931, 1932, 1934, 1935, 1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1930-L67863.v` — printed in editions [1930, 1931, 1932, 1934, 1935, 1936, 1937, 1939, 1940]:**

> ROCK, ALFRED MILTON.—B. 1888; ag. 3rd outdoor offr. and harbour., treas., Dominica, 1913-15; clk. and interpreter to mag., dist. "E," Mar., 1915; clk., mag., registr. and provost marshal "A," comanr. of oaths, dep. coroner, Montserrat, Sept., 1915; clk. to mag., dist. "A" and "B," dep. coroner, Antigua, Nov., 1920; senr.-clk., registr.'s office, clk., sup. ct. law libry., "A" comanr. of oaths, dep. coroner, Dominica, May, 1927; prin. for duty as registr. and provost marshal, registr. of titles, admr. of estates and registr.-gen. of births, marriages and deaths, Dominica, Apr., 1929.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1913–1915 | ag. 3rd outdoor offr. and harbour., treas. | Dominica | [1930, 1931, 1932, 1934, 1935, 1936, 1937, 1939, 1940] |
| 1 | 1915 | clk. and interpreter to mag., dist. "E," | Dominica *(inherited from previous clause)* | [1930, 1931, 1932, 1934, 1935, 1936, 1937, 1939, 1940] |
| 2 | 1915 | clk., mag., registr. and provost marshal "A, " comanr. of oaths, dep. coroner | Montserrat | [1930, 1931, 1932, 1934, 1935, 1936, 1937, 1939, 1940] |
| 3 | 1920 | clk. to mag., dist. "A" and "B, " dep. coroner | Antigua | [1930, 1931, 1932, 1934, 1935, 1936, 1937, 1939, 1940] |
| 4 | 1927 | senr.-clk., registr.'s office, clk., sup. ct. law libry., "A" comanr. of oaths, dep. coroner | Dominica | [1930, 1931, 1932, 1934, 1935, 1936, 1937, 1939, 1940] |
| 5 | 1929 | prin. for duty as registr. and provost marshal, registr. of titles, admr. of estates and registr.-gen. of births, marriages and deaths | Dominica | [1930, 1931, 1932, 1934, 1935, 1936, 1937, 1939, 1940] |

## Candidate stint `Rock, A. M___Leeward Islands___1917`

- Staff-list name: **Rock, A. M** | colony: **Leeward Islands** | listed 1917–1928 | editions [1917, 1919, 1920, 1922, 1923, 1924, 1925, 1927, 1928]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1917 | A. M. Rock | Clerk to Magistrate | Judicial Department | — | — |
| 1919 | A. M. Rock | Clerk to Magistrate | Judicial Department | — | — |
| 1920 | A. M. Rock | Clerk to Magistrate | Judicial Department | — | — |
| 1922 | A. M. Rock | Clerk of Police Magistrate | Magistracy and Police | — | — |
| 1923 | A. M. Rock | Clerk of Police Magistrate | Magistracy and Police | — | — |
| 1924 | A. M. Rock | Clerk of Police Magistrate | Magistracy and Police | — | — |
| 1925 | A. M. Rock | Clerk to Magistrate, District A | Magistracy and Police | — | — |
| 1927 | A. M. Rock | Clerk to Magistrate, District "A" | Magistracy and Police | — | — |
| 1928 | A. M. Rock | First Clerk and French Interpreter | Judicial Establishment | — | — |

### Deterministic checks: `rock_alfred-milton_b1888` vs `Rock, A. M___Leeward Islands___1917`

- [PASS] surname_gate: bio 'ROCK' vs stint 'Rock, A. M' (exact)
- [PASS] initials: bio ['A', 'M'] ~ stint ['A', 'M']
- [PASS] age_gate: stint starts 1917, birth 1888 (age 29)
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1917-1928
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

