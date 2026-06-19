<!-- {"case_id": "case_kuperman_joseph_b1898", "bio_ids": ["kuperman_joseph_b1898"], "stint_ids": ["Kupperman, J___Palestine___1923"]} -->
# Dossier case_kuperman_joseph_b1898

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['kuperman_joseph_b1898'] carry a single initial only — the namesake trap applies.

## Biography `kuperman_joseph_b1898`

- Printed name: **KUPERMAN, Joseph**
- Birth year: 1898 (attested in editions [1948, 1949])
- Honours: M.B.E (1942)
- Appears in editions: [1948, 1949]

### Verbatim printed entry text (OCR)

**Version `col1948-L33889.v` — printed in editions [1948, 1949]:**

> KUPERMAN, Joseph, M.B.E. (1942).—b. 1898; ed. Zicron Jacob Sch. and Ecole Professionne le de L'Alliance Isralite Universelle, Jerusalem; apptd. police dept., O.E.T.A.(S), 1918; asst. inspr., Pal. civ. admin., 1920; dist. offr., 1922; dist. offr., grade H, 1940; asst. dist. comsnr., 1946; mem. of comtes. conn. w. Village Admin. Ordce., and Land Transfers Regs.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1918 | apptd. police dept., O.E.T.A.(S) | — | [1948, 1949] |
| 1 | 1920 | asst. inspr., Pal. civ. admin | Palestine | [1948, 1949] |
| 2 | 1922 | dist. offr | Palestine *(inherited from previous clause)* | [1948, 1949] |
| 3 | 1940 | dist. offr., grade H | Palestine *(inherited from previous clause)* | [1948, 1949] |
| 4 | 1946 | asst. dist. comsnr | Palestine *(inherited from previous clause)* | [1948, 1949] |

## Candidate stint `Kupperman, J___Palestine___1923`

- Staff-list name: **Kupperman, J** | colony: **Palestine** | listed 1923–1932 | editions [1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1923 | J. Kupperman | Assistant District Officer | Administrative Staff | — | — |
| 1924 | J. Kupperman | Assistant District Officer | Administrative Staff | — | — |
| 1925 | J. Kupperman | Assistant District Officer | District Staff | — | — |
| 1927 | J. Kupperman | Assistant District Officers | District Staff | — | — |
| 1928 | J. Kupperman | Assistant District Officer | District Staff | — | — |
| 1929 | J. Kupperman | Assistant District Officer | Civil Establishment | — | — |
| 1930 | J. Kupperman | Assistant District Officer | District Staff | — | — |
| 1931 | J. Kupperman | Assistant District Officer | District Staff | — | — |
| 1932 | J. Kupperman | Assistant District Officer | District Staff | — | — |

### Deterministic checks: `kuperman_joseph_b1898` vs `Kupperman, J___Palestine___1923`

- [PASS] surname_gate: bio 'KUPERMAN' vs stint 'Kupperman, J' (fuzzy:1)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1923, birth 1898 (age 25)
- [PASS] colony: 4 placed event(s) resolve to 'Palestine'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1923-1932
- [FAIL] position_sim: best 51 vs bar 60: 'dist. offr' ~ 'Assistant District Officer'
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

