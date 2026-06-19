<!-- {"case_id": "case_lamb_william-davis_e1881", "bio_ids": ["lamb_william-davis_e1881"], "stint_ids": ["Lamb, W. D___British Guiana___1886"]} -->
# Dossier case_lamb_william-davis_e1881

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 27 official(s) with this surname in the graph's staff lists; 10 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `lamb_william-davis_e1881`

- Printed name: **LAMB, WILLIAM DAVIS**
- Birth year: not printed
- Appears in editions: [1888, 1889, 1890, 1894]

### Verbatim printed entry text (OCR)

**Version `col1888-L34396.v` — printed in editions [1888, 1889, 1890, 1894]:**

> LAMB, WILLIAM DAVIS.—Entered the civil service, British Guiana, Mar., 1881; 2nd class clerk, secretariat, Sept., 1881; acted as senior clerk from Mar. to Oct., 1882, July, 1883, to Feb., 1884, and Sept., 1884, to May, 1885.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1881–1881 | civil service | British Guiana | [1888, 1889, 1890, 1894] |
| 1 | 1881–1881 | 2nd class clerk, secretariat | — | [1888, 1889, 1890, 1894] |
| 2 | 1882–1885 | acted as senior clerk | — | [1888, 1889, 1890, 1894] |

## Candidate stint `Lamb, W. D___British Guiana___1886`

- Staff-list name: **Lamb, W. D** | colony: **British Guiana** | listed 1886–1890 | editions [1886, 1888, 1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1886 | W. D. Lamb | 2nd Class Senior Clerk | Government Secretariat | — | — |
| 1888 | W. D. Lamb | 2nd Class Senior Clerk | Government Secretariat | — | — |
| 1889 | W. D. Lamb | 2nd Class Senior Clerk | Government Secretariat | — | — |
| 1890 | W. D. Lamb | First Class Clerk | Government Secretariat | — | — |

### Deterministic checks: `lamb_william-davis_e1881` vs `Lamb, W. D___British Guiana___1886`

- [PASS] surname_gate: bio 'LAMB' vs stint 'Lamb, W. D' (exact)
- [PASS] initials: bio ['W', 'D'] ~ stint ['W', 'D']
- [PASS] age_gate: stint starts 1886; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'British Guiana'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1886-1890
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

