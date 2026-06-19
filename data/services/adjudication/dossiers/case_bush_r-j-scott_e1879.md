<!-- {"case_id": "case_bush_r-j-scott_e1879", "bio_ids": ["bush_r-j-scott_e1879"], "stint_ids": ["Bush, R. S___New Zealand___1880"]} -->
# Dossier case_bush_r-j-scott_e1879

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 11 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `bush_r-j-scott_e1879`

- Printed name: **BUSH, R. J. SCOTT**
- Birth year: not printed
- Appears in editions: [1894]

### Verbatim printed entry text (OCR)

**Version `col1894-L30621.v` — printed in editions [1894]:**

> BUSH, R. J. SCOTT.—Ed. Queen's Roy. Coll., Trinidad, Malvern Coll., and Lancing Coll.; articled pupil to J. E. Tanner, M.I.C.E., 1879-82; ag. and special draftsman, P. W. Dept., Trinidad, various occasions, 1882-6; draftsman light railway, Feb., 1889; surveyor of loan wks., Grenada, Jan., 1890; acgt. director, pub. wks., Mar., 1891.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1879–1882 | articled pupil to J. E. Tanner, M.I.C.E | — | [1894] |
| 1 | 1882–1886 | ag. and special draftsman, P. W. Dept., Trinidad, various occasions | — | [1894] |
| 2 | 1889 | draftsman light railway | — | [1894] |
| 3 | 1890 | surveyor of loan wks. | Grenada | [1894] |
| 4 | 1891 | acgt. director, pub. wks | Grenada *(inherited from previous clause)* | [1894] |

## Candidate stint `Bush, R. S___New Zealand___1880`

- Staff-list name: **Bush, R. S** | colony: **New Zealand** | listed 1880–1888 | editions [1880, 1883, 1886, 1888]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1880 | R. S. Bush | Resident Magistrates | Judicial | — | — |
| 1883 | R. S. Bush | Resident Magistrate | Judicial | — | — |
| 1886 | R. S. Bush | Resident Magistrate | Judicial | — | — |
| 1888 | R. S. Bush | Resident Magistrate | Resident Magistrates | — | — |

### Deterministic checks: `bush_r-j-scott_e1879` vs `Bush, R. S___New Zealand___1880`

- [PASS] surname_gate: bio 'BUSH' vs stint 'Bush, R. S' (exact)
- [PASS] initials: bio ['R', 'J', 'S'] ~ stint ['R', 'S']
- [PASS] age_gate: stint starts 1880; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'New Zealand'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1880-1888
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

