<!-- {"case_id": "case_schouten_s-a_b1911", "bio_ids": ["schouten_s-a_b1911"], "stint_ids": ["Schouten, S. A___Windward Islands___1950"]} -->
# Dossier case_schouten_s-a_b1911

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `schouten_s-a_b1911`

- Printed name: **SCHOUTEN, S. A**
- Birth year: 1911 (attested in editions [1956, 1957, 1958, 1959])
- Honours: M.B.E (1950)
- Appears in editions: [1956, 1957, 1958, 1959]

### Verbatim printed entry text (OCR)

**Version `col1956-L23995.v` — printed in editions [1956, 1957, 1958, 1959]:**

> SCHOUTEN, S. A., M.B.E. (1950).—b. 1911; ed. St. Kitts-Nevis Gram. Sch., I.C.T.A. and Cornell Univ., U.S.A.; asst. agric. offr., Dominica, 1933; agric. asst., Montserrat, 1935; senr. staff., I.C.T.A., for econ. surveys, 1938-42; senr. agric. asst., St. V., 1942; agric. supt., St. L., 1946-58; mem., cotton industry comsn. of enq., Montserrat.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1933 | asst. agric. offr. | Dominica | [1956, 1957, 1958, 1959] |
| 1 | 1935 | agric. asst. | Montserrat | [1956, 1957, 1958, 1959] |
| 2 | 1938–1942 | senr. staff., I.C.T.A., for econ. surveys | Montserrat *(inherited from previous clause)* | [1956, 1957, 1958, 1959] |
| 3 | 1942 | senr. agric. asst. | St. Vincent | [1956, 1957, 1958, 1959] |
| 4 | 1946–1958 | agric. supt. | St. Lucia | [1956, 1957, 1958, 1959] |

## Candidate stint `Schouten, S. A___Windward Islands___1950`

- Staff-list name: **Schouten, S. A** | colony: **Windward Islands** | listed 1950–1952 | editions [1950, 1952]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | S. A. Schouten | Agricultural Superintendent | Agricultural Department | — | — |
| 1952 | S. A. Schouten | Agricultural Superintendent | Civil Establishment | — | — |

### Deterministic checks: `schouten_s-a_b1911` vs `Schouten, S. A___Windward Islands___1950`

- [PASS] surname_gate: bio 'SCHOUTEN' vs stint 'Schouten, S. A' (exact)
- [PASS] initials: bio ['S', 'A'] ~ stint ['S', 'A']
- [PASS] age_gate: stint starts 1950, birth 1911 (age 39)
- [FAIL] colony: no placed event resolves to 'Windward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1950-1952
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

