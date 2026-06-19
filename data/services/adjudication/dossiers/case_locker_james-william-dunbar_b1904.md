<!-- {"case_id": "case_locker_james-william-dunbar_b1904", "bio_ids": ["locker_james-william-dunbar_b1904"], "stint_ids": ["Locker, J. W. D___Nyasaland___1930"]} -->
# Dossier case_locker_james-william-dunbar_b1904

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `locker_james-william-dunbar_b1904`

- Printed name: **LOCKER, James William Dunbar**
- Birth year: 1904 (attested in editions [1949, 1950, 1951])
- Honours: O.B.E
- Appears in editions: [1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1949-L33742.v` — printed in editions [1949, 1950, 1951]:**

> LOCKER, James William Dunbar, O.B.E.—b. 1904 ; ed. Repton Sch., Derby ; admin. offr., Nyasa, 1926 ; seconded to C.O., 1936 ; p.s. to lt.-gov., Malta, 1939 ; gov. sec., St. H., 1943.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1926 | admin. offr. | Nyasaland | [1949, 1950, 1951] |
| 1 | 1936 | seconded to C.O | Nyasaland *(inherited from previous clause)* | [1949, 1950, 1951] |
| 2 | 1939 | p.s. to lt.-gov. | Malta | [1949, 1950, 1951] |
| 3 | 1943 | gov. sec., St. H | Malta *(inherited from previous clause)* | [1949, 1950, 1951] |

## Candidate stint `Locker, J. W. D___Nyasaland___1930`

- Staff-list name: **Locker, J. W. D** | colony: **Nyasaland** | listed 1930–1939 | editions [1930, 1931, 1932, 1934, 1937, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1930 | J. W. D. Locker | Assistant District Officers | District Staff | — | — |
| 1931 | J. W. D. Locker | Assistant District Officer | District Staff | — | — |
| 1932 | J. W. D. Locker | Assistant District Officer | District Staff | — | — |
| 1934 | J. W. D. Locker | Assistant District Officer | District Staff | — | — |
| 1937 | J. W. D. Locker | Assistant District Officer | District Staff | — | — |
| 1939 | J. W. D. Locker | District Officer | District Staff | — | — |

### Deterministic checks: `locker_james-william-dunbar_b1904` vs `Locker, J. W. D___Nyasaland___1930`

- [PASS] surname_gate: bio 'LOCKER' vs stint 'Locker, J. W. D' (exact)
- [PASS] initials: bio ['J', 'W', 'D'] ~ stint ['J', 'W', 'D']
- [PASS] age_gate: stint starts 1930, birth 1904 (age 26)
- [PASS] colony: 2 placed event(s) resolve to 'Nyasaland'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1930-1939
- [FAIL] position_sim: best 54 vs bar 60: 'admin. offr.' ~ 'District Officer'
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

