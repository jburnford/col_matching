<!-- {"case_id": "case_barney_george-higgins_e1855", "bio_ids": ["barney_george-higgins_e1855"], "stint_ids": ["Barney, G. Higgins___New South Wales___1886"]} -->
# Dossier case_barney_george-higgins_e1855

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `barney_george-higgins_e1855`

- Printed name: **BARNEY, George Higgins**
- Birth year: not printed
- Appears in editions: [1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899]

### Verbatim printed entry text (OCR)

**Version `col1888-L31972.v` — printed in editions [1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899]:**

> BARNEY, George Higgins.—Inspector of distilleries, N. S. Wales, April, 1855; chief inspector of distilleries and sugar refineries, June, 1880.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1855 | Inspector of distilleries, N. S. Wales | Nova Scotia | [1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899] |
| 1 | 1880 | chief inspector of distilleries and sugar refineries | Nova Scotia *(inherited from previous clause)* | [1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899] |

## Candidate stint `Barney, G. Higgins___New South Wales___1886`

- Staff-list name: **Barney, G. Higgins** | colony: **New South Wales** | listed 1886–1889 | editions [1886, 1888, 1889]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1886 | G. H. Barney | Chief Inspector of Distilleries | — | — | — |
| 1888 | G. H. Barney | Chief Inspector of Distilleries | Colonial Architect's Department | — | — |
| 1889 | G. H. Barney | Chief Inspector of Distilleries | Colonial Architect's Department | — | — |

### Deterministic checks: `barney_george-higgins_e1855` vs `Barney, G. Higgins___New South Wales___1886`

- [PASS] surname_gate: bio 'BARNEY' vs stint 'Barney, G. Higgins' (exact)
- [PASS] initials: bio ['G', 'H'] ~ stint ['G', 'H']
- [PASS] age_gate: stint starts 1886; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'New South Wales'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1886-1889
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

