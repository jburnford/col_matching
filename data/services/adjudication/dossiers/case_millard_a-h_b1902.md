<!-- {"case_id": "case_millard_a-h_b1902", "bio_ids": ["millard_a-h_b1902"], "stint_ids": ["Millard, A. H___Straits Settlements___1931"]} -->
# Dossier case_millard_a-h_b1902

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 14 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `millard_a-h_b1902`

- Printed name: **MILLARD, A. H.**
- Birth year: 1902 (attested in editions [1956, 1957])
- Appears in editions: [1956, 1957]

### Verbatim printed entry text (OCR)

**Version `col1956-L23059.v` — printed in editions [1956, 1957]:**

> MILLARD, A. H.—b. 1902; ed. King Edward VI Sch., Bath, and Bath and West of England Coll. of Pharmacy; pharm. chmst., Selangor and N. Sembilan, 1928, suptng. pharm. chmst., K. Lumpur, 1942; chief pharm. chmst., Fed. of Mal., 1949.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | pharm. chmst. | Selangor and Negri Sembilan | [1956, 1957] |
| 1 | 1942 | suptng. pharm. chmst. | Kuala Lumpur | [1956, 1957] |
| 2 | 1949 | chief pharm. chmst. | Federation of Malaya | [1956, 1957] |

## Candidate stint `Millard, A. H___Straits Settlements___1931`

- Staff-list name: **Millard, A. H** | colony: **Straits Settlements** | listed 1931–1933 | editions [1931, 1932, 1933]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | A. H. Millard | Pharmaceutical Chemist | Public Works | — | — |
| 1931 | A. H. Millard | Pharmaceutical Chemist | Medical | — | — |
| 1932 | A. H. Millard | Pharmaceutical Chemist | Medical | — | — |
| 1933 | A. H. Millard | Pharmaceutical Chemist | Medical | — | — |

### Deterministic checks: `millard_a-h_b1902` vs `Millard, A. H___Straits Settlements___1931`

- [PASS] surname_gate: bio 'MILLARD' vs stint 'Millard, A. H' (exact)
- [PASS] initials: bio ['A', 'H'] ~ stint ['A', 'H']
- [PASS] age_gate: stint starts 1931, birth 1902 (age 29)
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1931-1933
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

