<!-- {"case_id": "case_tupper_henry-de-beauviore_b1883", "bio_ids": ["tupper_henry-de-beauviore_b1883"], "stint_ids": ["Tupper, H. de B___British Guiana___1927", "Tupper, H. de B___Jamaica___1933"]} -->
# Dossier case_tupper_henry-de-beauviore_b1883

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `tupper_henry-de-beauviore_b1883`

- Printed name: **TUPPER, HENRY DE BEAUVIORE**
- Birth year: 1883 (attested in editions [1935, 1936, 1937, 1939, 1940])
- Honours: A.M, R.N
- Appears in editions: [1935, 1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `dol1935-L62825.v` — printed in editions [1935, 1936, 1937, 1939, 1940]:**

> TUPPER, HENRY DE BEAUVIORE, A.M., R.N., Capt., R.N. (ret.).—B. 1883; naval cadet, 1898; commdr., 1917; capt., 1928; served in Gallipoli, Egypt, Otranto barrage and adm'y.; Legion of Honour (France), Order of Aves (Portugal) and Al Valore (Italy); harmbr., Br. Guiana, 1925; do., Jamaica, Oct., 1931.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1898 | naval cadet | — | [1935, 1936, 1937, 1939, 1940] |
| 1 | 1917 | commdr | — | [1935, 1936, 1937, 1939, 1940] |
| 2 | 1925 | harmbr. | British Guiana | [1935, 1936, 1937, 1939, 1940] |
| 3 | 1928 | capt | — | [1935, 1936, 1937, 1939, 1940] |
| 4 | 1931 | harmbr. | Jamaica | [1935, 1936, 1937, 1939, 1940] |

## Candidate stint `Tupper, H. de B___British Guiana___1927`

- Staff-list name: **Tupper, H. de B** | colony: **British Guiana** | listed 1927–1930 | editions [1927, 1928, 1929, 1930]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | H. de B. Tupper | Harbour Master | Harbour Dept.—Harbour Board | — | — |
| 1928 | H. de B. Tupper | Harbour Master | Harbour Dept.—Harbour Board | — | — |
| 1929 | H. de B. Tupper | Harbour Master | Harbour Department—Harbour Board | — | Captain |
| 1930 | Captain H. de B. Tupper | Harbour Master | Harbour Department | — | Captain |

### Deterministic checks: `tupper_henry-de-beauviore_b1883` vs `Tupper, H. de B___British Guiana___1927`

- [PASS] surname_gate: bio 'TUPPER' vs stint 'Tupper, H. de B' (exact)
- [PASS] initials: bio ['H', 'D', 'B'] ~ stint ['H', 'D', 'B']
- [PASS] age_gate: stint starts 1927, birth 1883 (age 44)
- [PASS] colony: 1 placed event(s) resolve to 'British Guiana'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1927-1930
- [FAIL] position_sim: best 50 vs bar 60: 'harmbr.' ~ 'Harbour Master'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Tupper, H. de B___Jamaica___1933`

- Staff-list name: **Tupper, H. de B** | colony: **Jamaica** | listed 1933–1940 | editions [1933, 1934, 1937, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | H. de B. Tupper | Harbour Master | Harbour Master | — | Captain |
| 1934 | H. de B. Tupper | Commander | Harbour Master | — | Captain |
| 1937 | H. de B. Tupper | Harbour Master | Harbour Master | — | — |
| 1940 | H. de B. Tupper | Harbour Master | Harbour Master | — | — |

### Deterministic checks: `tupper_henry-de-beauviore_b1883` vs `Tupper, H. de B___Jamaica___1933`

- [PASS] surname_gate: bio 'TUPPER' vs stint 'Tupper, H. de B' (exact)
- [PASS] initials: bio ['H', 'D', 'B'] ~ stint ['H', 'D', 'B']
- [PASS] age_gate: stint starts 1933, birth 1883 (age 50)
- [PASS] colony: 1 placed event(s) resolve to 'Jamaica'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1933-1940
- [FAIL] position_sim: best 50 vs bar 60: 'harmbr.' ~ 'Harbour Master'
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

