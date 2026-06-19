<!-- {"case_id": "case_pilgrim_edward-olivier_b1886", "bio_ids": ["pilgrim_edward-olivier_b1886"], "stint_ids": ["Pilgrim, E. O___British Guiana___1908"]} -->
# Dossier case_pilgrim_edward-olivier_b1886

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 11 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `pilgrim_edward-olivier_b1886`

- Printed name: **PILGRIM, EDWARD OLIVIER**
- Birth year: 1886 (attested in editions [1939, 1940])
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L69810.v` — printed in editions [1939, 1940]:**

> PILGRIM, EDWARD OLIVIER.—B. 1886; ed. Lodge Schl., Barbados; B.Sc. (Lond.), hon. physics; asst. mast., Queen's Coll., Br. Guiana, 1905; ag. prin. various occasions; mem., bd. of land survrs., exams., 1916.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1905 | asst. mast., Queen's Coll. | British Guiana | [1939, 1940] |
| 1 | 1916 | mem., bd. of land survrs., exams | British Guiana *(inherited from previous clause)* | [1939, 1940] |

## Candidate stint `Pilgrim, E. O___British Guiana___1908`

- Staff-list name: **Pilgrim, E. O** | colony: **British Guiana** | listed 1908–1939 | editions [1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1930, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1908 | E. O. Pilgrim | Assistant Master | Education | — | — |
| 1909 | E. O. Pilgrim | Assistant Master | Queen's College | — | — |
| 1910 | E. O. Pilgrim | Assistant Master | Education | — | — |
| 1911 | E. O. Pilgrim | Assistant Master | Education | — | — |
| 1912 | E. O. Pilgrim | Assistant Master | Education | — | — |
| 1913 | E. O. Pilgrim | Assistant Master | Education | — | — |
| 1914 | E. O. Pilgrim | Assistant Master | Queen's College | — | — |
| 1915 | E. O. Pilgrim | Assistant Master | Education | — | — |
| 1917 | E. O. Pilgrim | Assistant Master | Queen's College | — | — |
| 1918 | E. O. Pilgrim | Assistant Master | Queen's College | — | — |
| 1919 | E. O. Pilgrim | Assistant Masters | Education | — | — |
| 1920 | E. O. Pilgrim | 2nd Senior Master | Queen's College | — | — |
| 1921 | E. O. Pilgrim | 2nd Senior Master | Education | — | — |
| 1922 | E. O. Pilgrim | 2nd Senior Master | Education | — | — |
| 1923 | E. O. Pilgrim | 2nd Senior Master | Queen's College | — | — |
| 1924 | E. O. Pilgrim | Mathematical Master | Queen's College | — | — |
| 1925 | E. O. Pilgrim | Senior Masters | Queen's College | — | — |
| 1927 | E. O. Pilgrim | Senior Masters | Education | — | — |
| 1928 | E. O. Pilgrim | Senior Masters | Education | — | — |
| 1930 | E. O. Pilgrim | Assistant Master | Education | — | — |
| 1939 | E. O. Pilgrim | Assistant Master | Queen's College | — | — |

### Deterministic checks: `pilgrim_edward-olivier_b1886` vs `Pilgrim, E. O___British Guiana___1908`

- [PASS] surname_gate: bio 'PILGRIM' vs stint 'Pilgrim, E. O' (exact)
- [PASS] initials: bio ['E', 'O'] ~ stint ['E', 'O']
- [PASS] age_gate: stint starts 1908, birth 1886 (age 22)
- [PASS] colony: 2 placed event(s) resolve to 'British Guiana'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1908-1939
- [FAIL] position_sim: best 58 vs bar 60: 'asst. mast., Queen's Coll.' ~ 'Assistant Masters'
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

