<!-- {"case_id": "case_reere_aubrey-temple_e1886", "bio_ids": ["reere_aubrey-temple_e1886"], "stint_ids": ["Reeve, A. T___Ceylon___1922"]} -->
# Dossier case_reere_aubrey-temple_e1886

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 15 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `reere_aubrey-temple_e1886`

- Printed name: **REERE, AUBREY TEMPLE**
- Birth year: not printed
- Appears in editions: [1897]

### Verbatim printed entry text (OCR)

**Version `col1897-L32064.v` — printed in editions [1897]:**

> REERE, AUBREY TEMPLE.—Cadet, Sarawak army, Oct., 1886; asst. resdt., May, 1890; resdt., 1891; 4th div., Jan., 1894.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1886 | Cadet, Sarawak army | Sarawak | [1897] |
| 1 | 1890 | asst. resdt | Sarawak *(inherited from previous clause)* | [1897] |
| 2 | 1891 | resdt | Sarawak *(inherited from previous clause)* | [1897] |
| 3 | 1894 | 4th div | Sarawak *(inherited from previous clause)* | [1897] |

## Candidate stint `Reeve, A. T___Ceylon___1922`

- Staff-list name: **Reeve, A. T** | colony: **Ceylon** | listed 1922–1925 | editions [1922, 1923, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | A. T. Reeve | Inspector for Plant Pests and Diseases (Mycological) | Inspectorette Branch | — | — |
| 1923 | A. T. Reeve | Inspector for Plant Pests and Diseases (Southern) | Inspectorate Branch | — | — |
| 1925 | A. T. Reeve | Inspector for Plant Pests and Diseases (Southern) | Department of Agriculture | — | — |

### Deterministic checks: `reere_aubrey-temple_e1886` vs `Reeve, A. T___Ceylon___1922`

- [PASS] surname_gate: bio 'REERE' vs stint 'Reeve, A. T' (fuzzy:1)
- [PASS] initials: bio ['A', 'T'] ~ stint ['A', 'T']
- [PASS] age_gate: stint starts 1922; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Ceylon'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1922-1925
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

