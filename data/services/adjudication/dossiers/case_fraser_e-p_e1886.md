<!-- {"case_id": "case_fraser_e-p_e1886", "bio_ids": ["fraser_e-p_e1886"], "stint_ids": ["Fraser, E. P___British Guiana___1888"]} -->
# Dossier case_fraser_e-p_e1886

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 140 official(s) with this surname in the graph's staff lists; 69 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `fraser_e-p_e1886`

- Printed name: **FRASER, E. P**
- Birth year: not printed
- Appears in editions: [1894]

### Verbatim printed entry text (OCR)

**Version `col1894-L31601.v` — printed in editions [1894]:**

> FRASER, E. P.—Copyist regtr's. office B. Guiana, Nov., 1886; transferred to customs dept., Aug., 1887; supervisor of customs, Gold Coast, Oct., 1892; has acted as dist. commr.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1886 | Copyist regtr's. office B. Guiana | — | [1894] |
| 1 | 1887 | transferred to customs dept | — | [1894] |
| 2 | 1892 | supervisor of customs | Gold Coast | [1894] |

## Candidate stint `Fraser, E. P___British Guiana___1888`

- Staff-list name: **Fraser, E. P** | colony: **British Guiana** | listed 1888–1890 | editions [1888, 1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | E. P. Fraser | 6th Class | Customs | — | — |
| 1889 | E. P. Fraser | 6th Class | Customs | — | — |
| 1890 | E. P. Fraser | 5th Class | Customs | — | — |

### Deterministic checks: `fraser_e-p_e1886` vs `Fraser, E. P___British Guiana___1888`

- [PASS] surname_gate: bio 'FRASER' vs stint 'Fraser, E. P' (exact)
- [PASS] initials: bio ['E', 'P'] ~ stint ['E', 'P']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'British Guiana'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1888-1890
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

