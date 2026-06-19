<!-- {"case_id": "case_samuel_lionel-l_e1878", "bio_ids": ["samuel_lionel-l_e1878"], "stint_ids": ["Samuel, L. L___Jamaica___1880", "Samuel, L. L___Jamaica___1894"]} -->
# Dossier case_samuel_lionel-l_e1878

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 17 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `samuel_lionel-l_e1878`

- Printed name: **SAMUEL, LIONEL L.**
- Birth year: not printed
- Appears in editions: [1888, 1889, 1890, 1894, 1896, 1897]

### Verbatim printed entry text (OCR)

**Version `col1890-L36540.v` — printed in editions [1890, 1894, 1896, 1897]:**

> SAMUEL, LIONEL L.—Admitted solicitor, Supreme Court, Jamaica, June, 1878, acted as clerk of petty sessions, clerk of St. Ann's circuit court, 1879; assistant clerk Port Antonio (now eastern) district court, and clerk of Bath circuit court, Oct., 1879; now clk. of cts., St. Ann's; is a J.P.

**Version `col1888-L35892.v` — printed in editions [1888, 1889]:**

> SAMUEL, LIONEL L.—Admitted solicitor, Supreme Court, Jamaica, June, 1878; acted as clerk of petty sessions for parish of St. Ann, and clerk of St. Ann's circuit court, April to Aug., 1879; acted as clerk of petty sessions for parish of St. Thomas, assistant clerk Port Antonio (now eastern) district court, and clerk of Bath circuit court, Oct., 1879; is a J.P.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1878–1878 | Admitted solicitor | Jamaica | [1888, 1889, 1890, 1894, 1896, 1897] |
| 1 | 1879–1879 | clerk of petty sessions, clerk of St. Ann's circuit court | Jamaica *(inherited from previous clause)* | [1888, 1889, 1890, 1894, 1896, 1897] |
| 2 | 1879–1879 | assistant clerk Port Antonio (now eastern) district court, and clerk of Bath circuit court | — | [1890, 1894, 1896, 1897] |
| 3 | ? | clk. of cts. | — | [1890, 1894, 1896, 1897] |

## Candidate stint `Samuel, L. L___Jamaica___1880`

- Staff-list name: **Samuel, L. L** | colony: **Jamaica** | listed 1880–1888 | editions [1880, 1883, 1886, 1888]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1880 | L. L. Samuel | Clerk of Petty Sessions | Clerks of Petty Sessions | — | — |
| 1883 | L. L. Samuel | Clerk of Petty Sessions | Clerks of Petty Sessions | — | — |
| 1886 | L. L. Samuel | Clerk of Petty Sessions | Petty Sessions | — | — |
| 1888 | L. L. Samuel | Clerk of Petty Sessions | Judicial Establishment | — | — |

### Deterministic checks: `samuel_lionel-l_e1878` vs `Samuel, L. L___Jamaica___1880`

- [PASS] surname_gate: bio 'SAMUEL' vs stint 'Samuel, L. L' (exact)
- [PASS] initials: bio ['L', 'L'] ~ stint ['L', 'L']
- [PASS] age_gate: stint starts 1880; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Jamaica'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1880-1888
- [PASS] position_sim: best 100 vs bar 60: 'clerk of petty sessions, clerk of St. Ann's circuit court' ~ 'Clerk of Petty Sessions'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

## Candidate stint `Samuel, L. L___Jamaica___1894`

- Staff-list name: **Samuel, L. L** | colony: **Jamaica** | listed 1894–1896 | editions [1894, 1896]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1894 | L. L. Samuel | Clerk | Clerks of the Courts | — | — |
| 1896 | L. L. Samuel | Clerk | Judicial Establishment | — | — |

### Deterministic checks: `samuel_lionel-l_e1878` vs `Samuel, L. L___Jamaica___1894`

- [PASS] surname_gate: bio 'SAMUEL' vs stint 'Samuel, L. L' (exact)
- [PASS] initials: bio ['L', 'L'] ~ stint ['L', 'L']
- [PASS] age_gate: stint starts 1894; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Jamaica'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1894-1896
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

