<!-- {"case_id": "case_elpstein_alexander_b1886", "bio_ids": ["elpstein_alexander_b1886"], "stint_ids": ["Epstein, A___Palestine___1921"]} -->
# Dossier case_elpstein_alexander_b1886

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['elpstein_alexander_b1886'] carry a single initial only — the namesake trap applies.

## Biography `elpstein_alexander_b1886`

- Printed name: **ELPSTEIN, ALEXANDER**
- Birth year: 1886 (attested in editions [1936])
- Honours: M.B.E (1937)
- Appears in editions: [1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1936-L60522.v` — printed in editions [1936]:**

> ELPSTEIN, ALEXANDER.—B. 1886; ed. Hebrew Inst., Liverpool; Jews Hosp., W. Norwood; inspr., dept. of commerce and industry, Palestine, 1920; dist. offr., Jerusalem-Jaffa dist., 1923; admstv. offr., S. dist., 1925.

**Version `col1937-L60626.v` — printed in editions [1937, 1939, 1940]:**

> EPSTEIN, ALEXANDER, M.B.E. (1937).—B. 1886; ed. Hebrew Inst., Liverpool; Jews Hosp., W. Norwood; inspr., dept. of commerce and industr., Palestine, 1920; dist. offr., Jerusalem-Jaffa dist., 1923; admnstr. offr., S. dist., 1925.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1920 | inspr., dept. of commerce and industry | Palestine | [1936, 1937, 1939, 1940] |
| 1 | 1923 | dist. offr., Jerusalem-Jaffa dist | Palestine *(inherited from previous clause)* | [1936, 1937, 1939, 1940] |
| 2 | 1925 | admstv. offr., S. dist | Palestine *(inherited from previous clause)* | [1936, 1937, 1939, 1940] |

## Candidate stint `Epstein, A___Palestine___1921`

- Staff-list name: **Epstein, A** | colony: **Palestine** | listed 1921–1940 | editions [1921, 1923, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1921 | A. Epstein | Assistant Inspector | DEPARTMENT OF COMMERCE AND INDUSTRY | — | — |
| 1923 | A. Epstein | Assistant Inspector | Department of Commerce and Industry | — | — |
| 1925 | A. Epstein | Assistant District Officer | District Staff | — | — |
| 1927 | A. Epstein | Assistant District Officers | District Staff | — | — |
| 1928 | A. Epstein | Assistant District Officer | District Staff | — | — |
| 1929 | A. Epstein | Assistant District Officer | Civil Establishment | — | — |
| 1930 | A. Epstein | Assistant District Officer | District Staff | — | — |
| 1931 | A. Epstein | Assistant District Officer | District Staff | — | — |
| 1932 | A. Epstein | Assistant District Officer | District Staff | — | — |
| 1940 | A. Epstein | Administrative Officer | District Staff | — | — |

### Deterministic checks: `elpstein_alexander_b1886` vs `Epstein, A___Palestine___1921`

- [PASS] surname_gate: bio 'ELPSTEIN' vs stint 'Epstein, A' (fuzzy:1)
- [PASS] initials: bio ['A'] ~ stint ['A']
- [PASS] age_gate: stint starts 1921, birth 1886 (age 35)
- [PASS] colony: 3 placed event(s) resolve to 'Palestine'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1921-1940
- [PASS] position_sim: best 62 vs bar 60: 'admstv. offr., S. dist' ~ 'Assistant District Officers'
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

