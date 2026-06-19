<!-- {"case_id": "case_dalziel_enrico_b1892", "bio_ids": ["dalziel_enrico_b1892"], "stint_ids": ["Dalziel, K. E___Uganda___1949"]} -->
# Dossier case_dalziel_enrico_b1892

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['dalziel_enrico_b1892'] carry a single initial only — the namesake trap applies.

## Biography `dalziel_enrico_b1892`

- Printed name: **DALZIEL, ENRICO**
- Birth year: 1892 (attested in editions [1932])
- Honours: D.D
- Appears in editions: [1932]

### Verbatim printed entry text (OCR)

**Version `col1932-L59502.v` — printed in editions [1932]:**

> DALZIEL, HON. REV. ENRICO, B.L.Can., D.D., Ph.D.—B. 1892; ed. St. Paul's Inst., Valletta; matric. Malta Univ., 1906; B.L Can., D.D., 1913; awarded govt. prize as first student of academical course; Ph.D., Gregorian Univ., Rome, 1915; teacher of philosophy and English lit. and prefect of studies in Archiepiscopal Seminary, Malta, 1916-19; elec. for 2nd divn. in Maltese parlmt., Oct., 1921; min. for pub. instrn., 10th July, 1923; resigned, June, 1927; re-el. Aug., 1927.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1906 | matric. Malta Univ | — | [1932] |
| 1 | 1913 | B.L Can., D.D | — | [1932] |
| 2 | 1915 | Ph.D., Gregorian Univ., Rome | — | [1932] |
| 3 | 1916–1919 | teacher of philosophy and English lit. and prefect of studies in Archiepiscopal Seminary | Malta | [1932] |
| 4 | 1921 | elec. for 2nd divn. in Maltese parlmt | Malta *(inherited from previous clause)* | [1932] |
| 5 | 1923 | min. for pub. instrn | Malta *(inherited from previous clause)* | [1932] |
| 6 | 1927 | resigned | Malta *(inherited from previous clause)* | [1932] |

## Candidate stint `Dalziel, K. E___Uganda___1949`

- Staff-list name: **Dalziel, K. E** | colony: **Uganda** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | K. E. Dalziel | District Officers and Assistant District Officers | Provincial Administration | — | — |
| 1951 | K. E. Dalziel | District Officers and Assistant District Officers | Provincial Administration | — | — |

### Deterministic checks: `dalziel_enrico_b1892` vs `Dalziel, K. E___Uganda___1949`

- [PASS] surname_gate: bio 'DALZIEL' vs stint 'Dalziel, K. E' (exact)
- [PASS] initials: bio ['E'] ~ stint ['K', 'E']
- [PASS] age_gate: stint starts 1949, birth 1892 (age 57)
- [FAIL] colony: no placed event resolves to 'Uganda'
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

