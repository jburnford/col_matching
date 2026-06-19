<!-- {"case_id": "case_keith_j-l_b1895", "bio_ids": ["keith_j-l_b1895"], "stint_ids": ["Keith, J. L___Northern Rhodesia___1929"]} -->
# Dossier case_keith_j-l_b1895

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `keith_j-l_b1895`

- Printed name: **KEITH, J. L**
- Birth year: 1895 (attested in editions [1948, 1950, 1951, 1953, 1954, 1955])
- Honours: C.B.E (1951), O.B.E (1943)
- Appears in editions: [1948, 1950, 1951, 1953, 1954, 1955]

### Verbatim printed entry text (OCR)

**Version `col1948-L33772.v` — printed in editions [1948, 1950, 1951, 1953, 1954, 1955]:**

> KEITH, J. L., C.B.E. (1951), O.B.E. (1943).—b. 1895; ed. Hertford Coll., Oxford; dist. offr., N. Rhod., 1919-37; ag. dir., African educ., 1930-31; African research survey, Chatham House, 1937-39; dir., col. schols. and hd., students dept., C.O., 1941.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1919–1937 | dist. offr. | Northern Rhodesia | [1948, 1950, 1951, 1953, 1954, 1955] |
| 1 | 1930–1931 | ag. dir., African educ | Northern Rhodesia *(inherited from previous clause)* | [1948, 1950, 1951, 1953, 1954, 1955] |
| 2 | 1937–1939 | African research survey, Chatham House | Northern Rhodesia *(inherited from previous clause)* | [1948, 1950, 1951, 1953, 1954, 1955] |
| 3 | 1941 | dir., col. schols. and hd., students dept. | Colonial Office | [1948, 1950, 1951, 1953, 1954, 1955] |

## Candidate stint `Keith, J. L___Northern Rhodesia___1929`

- Staff-list name: **Keith, J. L** | colony: **Northern Rhodesia** | listed 1929–1931 | editions [1929, 1930, 1931]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1929 | J. L. Keith | Native Commissioner (Seconded) | Native Education | — | — |
| 1930 | J. L. Keith | District Officer, Grade III (Seconded) | Native Education | — | — |
| 1931 | J. L. Keith | District Officer, Grade II (Seconded) | Native Education | — | — |

### Deterministic checks: `keith_j-l_b1895` vs `Keith, J. L___Northern Rhodesia___1929`

- [PASS] surname_gate: bio 'KEITH' vs stint 'Keith, J. L' (exact)
- [PASS] initials: bio ['J', 'L'] ~ stint ['J', 'L']
- [PASS] age_gate: stint starts 1929, birth 1895 (age 34)
- [PASS] colony: 3 placed event(s) resolve to 'Northern Rhodesia'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1929-1931
- [FAIL] position_sim: best 42 vs bar 60: 'dist. offr.' ~ 'District Officer, Grade II (Seconded)'
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

