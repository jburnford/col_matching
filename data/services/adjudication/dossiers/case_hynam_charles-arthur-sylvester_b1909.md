<!-- {"case_id": "case_hynam_charles-arthur-sylvester_b1909", "bio_ids": ["hynam_charles-arthur-sylvester_b1909"], "stint_ids": ["Hynam, C. A. S___Leeward Islands___1949"]} -->
# Dossier case_hynam_charles-arthur-sylvester_b1909

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hynam_charles-arthur-sylvester_b1909`

- Printed name: **HYNAM, Charles Arthur Sylvester**
- Birth year: 1909 (attested in editions [1948, 1949, 1950, 1951])
- Honours: D.I.C.T.A
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L33544.v` — printed in editions [1948, 1949, 1950, 1951]:**

> HYNAM, Charles Arthur Sylvester, D.I.C.T.A.—b. 1909; ed. Harrison Coll., Barbados and I.C.T.A.; headmstr., Glen Community Sch., St. V., 1933; govt. agric., N.W.I., 1935; agric. asst., Antigua, 1941; asst. agric. supt., 1945; agric. supt., 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1933 | headmstr., Glen Community Sch. | St. Vincent | [1948, 1949, 1950, 1951] |
| 1 | 1935 | govt. agric., N.W.I | St. Vincent *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 2 | 1941 | agric. asst. | Antigua | [1948, 1949, 1950, 1951] |
| 3 | 1945 | asst. agric. supt | Antigua *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 4 | 1946 | agric. supt | Antigua *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Hynam, C. A. S___Leeward Islands___1949`

- Staff-list name: **Hynam, C. A. S** | colony: **Leeward Islands** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | C. A. S. Hynam | Agricultural Superintendent | Agriculture | — | — |
| 1950 | C. A. S. Hynam | Agricultural Superintendent | Agriculture | — | — |
| 1951 | C. A. S. Hynam | Agricultural Superintendent | Agriculture | — | — |

### Deterministic checks: `hynam_charles-arthur-sylvester_b1909` vs `Hynam, C. A. S___Leeward Islands___1949`

- [PASS] surname_gate: bio 'HYNAM' vs stint 'Hynam, C. A. S' (exact)
- [PASS] initials: bio ['C', 'A', 'S'] ~ stint ['C', 'A', 'S']
- [PASS] age_gate: stint starts 1949, birth 1909 (age 40)
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
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

