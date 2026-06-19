<!-- {"case_id": "case_salter_david_b1893", "bio_ids": ["salter_david_b1893"], "stint_ids": ["Salter, David___Bahamas___1922"]} -->
# Dossier case_salter_david_b1893

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['salter_david_b1893'] carry a single initial only — the namesake trap applies.

## Biography `salter_david_b1893`

- Printed name: **SALTER, DAVID**
- Birth year: 1893 (attested in editions [1939, 1940])
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L70387.v` — printed in editions [1939, 1940]:**

> SALTER, DAVID, Assoc. M.I.B.E.—B. 1893; served during the Great War, 1914-19; British mercantile marine, 1914-15; Royal Navy, 1915-19; tel. dept., Bahamas, 1920 (on contract); established, 1921; asst. supt., tels., 1928; supt., 1932.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914–1919 | served during the Great War | — | [1939, 1940] |
| 1 | 1914–1915 | British mercantile marine | — | [1939, 1940] |
| 2 | 1915–1919 | Royal Navy | — | [1939, 1940] |
| 3 | 1920 | tel. dept. | Bahamas | [1939, 1940] |
| 4 | 1921 | established | Bahamas *(inherited from previous clause)* | [1939, 1940] |
| 5 | 1928 | asst. supt., tels | Bahamas *(inherited from previous clause)* | [1939, 1940] |
| 6 | 1932 | supt | Bahamas *(inherited from previous clause)* | [1939, 1940] |

## Candidate stint `Salter, David___Bahamas___1922`

- Staff-list name: **Salter, David** | colony: **Bahamas** | listed 1922–1937 | editions [1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1936, 1937]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | David Salter | First Operator | Telegraph Department | — | — |
| 1923 | David Salter | First Operator | Telegraph Department | — | — |
| 1924 | David Salter | First Operator | Telegraph Department | — | — |
| 1925 | David Salter | First Telegraphist | Telegraph Department | — | — |
| 1927 | D. Salter | Telegraphist, Grade I | Telegraph Department | — | — |
| 1928 | D. Salter | Telegraphist, Grade I. | Telegraph Department | — | — |
| 1929 | D. Salter | Assistant Superintendent | Telegraph Department | — | — |
| 1930 | D. Salter | Assistant Superintendent | Telegraph Department | — | — |
| 1931 | D. Salter | Assistant Superintendent | Telegraph Department | — | — |
| 1932 | D. Salter | Assistant Superintendent | Telegraph Department | — | — |
| 1933 | D. Salter | Superintendent of Telegraphs | Telegraph Department | — | — |
| 1934 | D. Salter | Superintendent of Telegraphs | Telegraph Department | — | — |
| 1936 | D. Salter | Superintendent of Telegraphs | Telegraph Department | — | — |
| 1937 | D. Salter | Superintendent of Telegraphs | Telegraph Department | — | — |

### Deterministic checks: `salter_david_b1893` vs `Salter, David___Bahamas___1922`

- [PASS] surname_gate: bio 'SALTER' vs stint 'Salter, David' (exact)
- [PASS] initials: bio ['D'] ~ stint ['D']
- [PASS] age_gate: stint starts 1922, birth 1893 (age 29)
- [PASS] colony: 4 placed event(s) resolve to 'Bahamas'
- [PASS] tenure_overlap: 4 event tenure(s) overlap stint years 1922-1937
- [FAIL] position_sim: best 53 vs bar 60: 'asst. supt., tels' ~ 'Assistant Superintendent'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

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

