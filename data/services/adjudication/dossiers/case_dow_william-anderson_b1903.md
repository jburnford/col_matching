<!-- {"case_id": "case_dow_william-anderson_b1903", "bio_ids": ["dow_william-anderson_b1903"], "stint_ids": ["Dow, A___Nyasaland___1950"]} -->
# Dossier case_dow_william-anderson_b1903

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `dow_william-anderson_b1903`

- Printed name: **DOW, William Anderson**
- Birth year: 1903 (attested in editions [1953, 1954, 1955])
- Honours: A.C.G.I, A.M.I.C.E
- Appears in editions: [1948, 1949, 1950, 1951, 1953, 1954, 1955]

### Verbatim printed entry text (OCR)

**Version `col1953-L17180.v` — printed in editions [1953, 1954, 1955]:**

> DOW, W. A.—b. 1903 ; ed. Sir Joseph Williamson's Mathematical Sch., Rochester, and Imp. Coll. of Sci. and Tech. ; C.A., 1925 ; civ. engr., chief's dept., adm'y., 1926 ; P.W.D., Nig., 1930 ; senr. exec. engr., 1945 ; asst. D.P.W., 1949 ; D.P.W., E. reg'n., 1951.

**Version `col1948-L32289.v` — printed in editions [1948, 1949, 1950, 1951]:**

> DOW, William Anderson, B.Sc. (eng.) (Lond.), A.C.G.I., A.M.I.C.E.—b. 1903; ed. Sir Joseph Williamson's Mathematical Sch., Rochester and Imp. Coll. of Sc. and Tech. (schol); C.A., 1925; civ. engrnr., chief's dept., admy., 1926; P.W.D., Nig., 1930; senr. exec. engrnr., 1945; asst. D.P.W., 1949.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1925 | C.A | — | [1948, 1949, 1950, 1951, 1953, 1954, 1955] |
| 1 | 1926 | civ. engr., chief's dept., adm'y | — | [1948, 1949, 1950, 1951, 1953, 1954, 1955] |
| 2 | 1930 | P.W.D. | Nigeria | [1948, 1949, 1950, 1951, 1953, 1954, 1955] |
| 3 | 1945 | senr. exec. engr | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1953, 1954, 1955] |
| 4 | 1949 | asst. D.P.W | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1953, 1954, 1955] |
| 5 | 1951 | D.P.W., E. reg'n | Nigeria *(inherited from previous clause)* | [1953, 1954, 1955] |

## Candidate stint `Dow, A___Nyasaland___1950`

- Staff-list name: **Dow, A** | colony: **Nyasaland** | listed 1950–1951 | editions [1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | A. Dow | Assistant Establishment Officers | Secretariat | — | — |
| 1951 | A. Dow | Assistant Establishment Officer | Secretariat | — | — |

### Deterministic checks: `dow_william-anderson_b1903` vs `Dow, A___Nyasaland___1950`

- [PASS] surname_gate: bio 'DOW' vs stint 'Dow, A' (exact)
- [PASS] initials: bio ['W', 'A'] ~ stint ['A']
- [PASS] age_gate: stint starts 1950, birth 1903 (age 47)
- [FAIL] colony: no placed event resolves to 'Nyasaland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1950-1951
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

