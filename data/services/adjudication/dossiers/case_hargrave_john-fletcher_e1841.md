<!-- {"case_id": "case_hargrave_john-fletcher_e1841", "bio_ids": ["hargrave_john-fletcher_e1841"], "stint_ids": ["Hargrave, J. F___New South Wales___1877"]} -->
# Dossier case_hargrave_john-fletcher_e1841

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hargrave_john-fletcher_e1841`

- Printed name: **HARGRAVE, JOHN FLETCHER**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L27860.v` — printed in editions [1883]:**

> HARGRAVE, JOHN FLETCHER.—Called to the bar, Lincoln's Inn, Jan. 1841, Q.C. and solicitor-general of New South Wales, M.L.C., representing the Cowper government in the legislative council, May 27th, 1862; attorney-general, New South Wales, 1864; 3rd puisne judge, 1865; senior puisne judge.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1841–1841 | Called to the bar | — | [1883] |
| 1 | 1862–1862 | Q.C. and solicitor-general, M.L.C. | New South Wales | [1883] |
| 2 | 1864–1864 | attorney-general | New South Wales | [1883] |
| 3 | 1865–1865 | 3rd puisne judge | — | [1883] |

## Candidate stint `Hargrave, J. F___New South Wales___1877`

- Staff-list name: **Hargrave, J. F** | colony: **New South Wales** | listed 1877–1880 | editions [1877, 1878, 1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | J. F. Hargrave | Senior Puisne Judge and Judge in Matrimonial Causes | Judicial and Legal Departments | — | — |
| 1878 | J. F. Hargrave | First puisne Judge and Judge in Matrimonial Causes | Judicial and Legal Departments | — | — |
| 1879 | J. F. Hargrave | First Puisne Judge and Judge in Matrimonial Causes | Judicial and Legal Departments | — | — |
| 1880 | J. F. Hargrave | First Puisne Judge and Judge in Matrimonial Causes | Judicial and Legal Departments | — | — |

### Deterministic checks: `hargrave_john-fletcher_e1841` vs `Hargrave, J. F___New South Wales___1877`

- [PASS] surname_gate: bio 'HARGRAVE' vs stint 'Hargrave, J. F' (exact)
- [PASS] initials: bio ['J', 'F'] ~ stint ['J', 'F']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'New South Wales'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1880
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

