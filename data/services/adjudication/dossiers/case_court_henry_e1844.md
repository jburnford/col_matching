<!-- {"case_id": "case_court_henry_e1844", "bio_ids": ["court_henry_e1844"], "stint_ids": ["Court, H___Trinidad___1877"]} -->
# Dossier case_court_henry_e1844

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['court_henry_e1844'] carry a single initial only — the namesake trap applies.

## Biography `court_henry_e1844`

- Printed name: **COURT, HENRY**
- Birth year: not printed
- Appears in editions: [1883, 1888]

### Verbatim printed entry text (OCR)

**Version `col1883-L26971.v` — printed in editions [1883]:**

> COURT, HENRY.—Member of the Middle Temple; called to the English bar in 1844; a graduate of the Law University of Paris; member of the legislative council, Trinidad, 1866; second puisne judge of the supreme civil and criminal court of the island in 1870.

**Version `col1888-L32809.v` — printed in editions [1888]:**

> COURT, HENRY.—Called to the bar, Middle Temple, in 1844; a graduate of the Law University of Paris; member of the legislative council, Trinidad, 1866; second civil and criminal supreme court, 1870.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1844 | called to the English bar in | — | [1883, 1888] |
| 1 | 1866 | member of the legislative council | Trinidad | [1883, 1888] |
| 2 | 1870 | second puisne judge of the supreme civil and criminal court of the island in | Trinidad *(inherited from previous clause)* | [1883, 1888] |

## Candidate stint `Court, H___Trinidad___1877`

- Staff-list name: **Court, H** | colony: **Trinidad** | listed 1877–1886 | editions [1877, 1879, 1880, 1886]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | H. Court | Judge | Judicial Department | — | — |
| 1879 | H. Court | — | Judicial Department | — | — |
| 1880 | H. Court | H. Court 1 | Judicial Department | — | — |
| 1886 | H. Court | — | Judicial Department | — | — |

### Deterministic checks: `court_henry_e1844` vs `Court, H___Trinidad___1877`

- [PASS] surname_gate: bio 'COURT' vs stint 'Court, H' (exact)
- [PASS] initials: bio ['H'] ~ stint ['H']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Trinidad'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1886
- [PASS] position_sim: best 100 vs bar 60: 'second puisne judge of the supreme civil and criminal court of the island in' ~ 'Judge'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

