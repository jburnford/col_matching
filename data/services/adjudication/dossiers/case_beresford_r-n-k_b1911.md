<!-- {"case_id": "case_beresford_r-n-k_b1911", "bio_ids": ["beresford_r-n-k_b1911"], "stint_ids": ["Beresford, R. N. K___Uganda___1949"]} -->
# Dossier case_beresford_r-n-k_b1911

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 11 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `beresford_r-n-k_b1911`

- Printed name: **BERESFORD, R. N. K.**
- Birth year: 1911 (attested in editions [1961, 1962])
- Honours: M.B.E.
- Appears in editions: [1961, 1962]

### Verbatim printed entry text (OCR)

**Version `col1961-L19758.v` — printed in editions [1961, 1962]:**

> BERESFORD, R. N. K., M.B.E.—b. 1911; ed. Northgate Sch.; mil. serv., 1940–46, major; admin. cadet, Pal., 1946; D.O., Uga., 1948; comsnt., Cyp., 1956; Nicosia, 1957, Paphos, 1958; asst. sec., Uga., 1960–61.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1940–1946 | major | — | [1961, 1962] |
| 1 | 1946–1946 | admin. cadet | Palestine | [1961, 1962] |
| 2 | 1948–1948 | D.O. | Uganda | [1961, 1962] |
| 3 | 1956–1956 | comsnt. | Cyprus | [1961, 1962] |
| 4 | 1957–1957 | — | Cyprus | [1961, 1962] |
| 5 | 1958–1958 | — | Cyprus | [1961, 1962] |
| 6 | 1960–1961 | asst. sec. | Uganda | [1961, 1962] |

## Candidate stint `Beresford, R. N. K___Uganda___1949`

- Staff-list name: **Beresford, R. N. K** | colony: **Uganda** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | R. N. K. Beresford | District Officers and Assistant District Officers | Provincial Administration | — | — |
| 1951 | R. N. K. Beresford | District Officers and Assistant District Officers | Provincial Administration | — | — |

### Deterministic checks: `beresford_r-n-k_b1911` vs `Beresford, R. N. K___Uganda___1949`

- [PASS] surname_gate: bio 'BERESFORD' vs stint 'Beresford, R. N. K' (exact)
- [PASS] initials: bio ['R', 'N', 'K'] ~ stint ['R', 'N', 'K']
- [PASS] age_gate: stint starts 1949, birth 1911 (age 38)
- [PASS] colony: 2 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 12 vs bar 60: 'D.O.' ~ 'District Officers and Assistant District Officers'
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

