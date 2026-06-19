<!-- {"case_id": "case_curle_alexander-tanered_b1900", "bio_ids": ["curle_alexander-tanered_b1900"], "stint_ids": ["Curle, A. T___British Somaliland___1930"]} -->
# Dossier case_curle_alexander-tanered_b1900

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `curle_alexander-tanered_b1900`

- Printed name: **CURLE, Alexander Tanered**
- Birth year: 1900 (attested in editions [1950, 1951])
- Honours: M.B.E.
- Appears in editions: [1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1950-L34760.v` — printed in editions [1950, 1951]:**

> CURLE, Alexander Tanered, M.B.E.—b. 1900; ed. Repton and R.M.C., Sandhurst; army, 1918-29; comsnr. 3rd grade and asst. dist. offr., Som., 1929-37; ag. Br. Vice-Consul, Jijiga, 1932, Harar, 1933-35; seconded pol. offr., British Somaliland-Ethiopia Boundary comm., 1935-36; seconded pol. offr., attd. S.C.C. (K.A.R.), 1940; seconded F.O.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1918–1929 | army | — | [1950, 1951] |
| 1 | 1929–1937 | comsnr. 3rd grade and asst. dist. offr. | Somaliland | [1950, 1951] |
| 2 | 1932–1932 | ag. Br. Vice-Consul | Jijiga | [1950, 1951] |
| 3 | 1933–1935 | ag. Br. Vice-Consul | Harar | [1950, 1951] |
| 4 | 1935–1936 | seconded pol. offr. | — | [1950, 1951] |
| 5 | 1940–1940 | seconded pol. offr. | — | [1950, 1951] |

## Candidate stint `Curle, A. T___British Somaliland___1930`

- Staff-list name: **Curle, A. T** | colony: **British Somaliland** | listed 1930–1937 | editions [1930, 1932, 1933, 1934, 1936, 1937]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1930 | A. T. Curle | Commissioner | Administration | — | — |
| 1932 | A. T. Curle | Commissioner | Administration | — | — |
| 1933 | A. T. Curle | Assistant District Officer | Administration | — | — |
| 1934 | A. T. Curle | Assistant District Officer | Administration | — | — |
| 1936 | A. T. Curle | Assistant District Officer | Administration | — | — |
| 1937 | A. T. Curle | Assistant District Officer | Administration | — | — |

### Deterministic checks: `curle_alexander-tanered_b1900` vs `Curle, A. T___British Somaliland___1930`

- [PASS] surname_gate: bio 'CURLE' vs stint 'Curle, A. T' (exact)
- [PASS] initials: bio ['A', 'T'] ~ stint ['A', 'T']
- [PASS] age_gate: stint starts 1930, birth 1900 (age 30)
- [PASS] colony: 1 placed event(s) resolve to 'British Somaliland'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1930-1937
- [FAIL] position_sim: best 52 vs bar 60: 'comsnr. 3rd grade and asst. dist. offr.' ~ 'Assistant District Officer'
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

