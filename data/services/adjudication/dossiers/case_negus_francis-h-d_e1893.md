<!-- {"case_id": "case_negus_francis-h-d_e1893", "bio_ids": ["negus_francis-h-d_e1893"], "stint_ids": ["Negus, F. H. D___Gold Coast___1894"]} -->
# Dossier case_negus_francis-h-d_e1893

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `negus_francis-h-d_e1893`

- Printed name: **NEGUS, FRANCIS H. D**
- Birth year: not printed
- Appears in editions: [1896, 1897, 1898, 1899, 1900, 1905]

### Verbatim printed entry text (OCR)

**Version `col1896-L40517.v` — printed in editions [1896, 1897, 1898, 1899, 1900, 1905]:**

> NEGUS, FRANCIS H. D.—Local auditor, Lagos, Dec., 1893; ditto., G. Coast, June, 1894.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1893 | Local auditor | Lagos | [1896, 1897, 1898, 1899, 1900, 1905] |
| 1 | 1894 | ditto., G. Coast | Lagos *(inherited from previous clause)* | [1896, 1897, 1898, 1899, 1900, 1905] |

## Candidate stint `Negus, F. H. D___Gold Coast___1894`

- Staff-list name: **Negus, F. H. D** | colony: **Gold Coast** | listed 1894–1899 | editions [1894, 1896, 1898, 1899]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1894 | F. H. D. Negus | Local Auditor | Audit Office | — | — |
| 1896 | F. H. D. Negus | Local Auditor | Audit Office | — | — |
| 1898 | F. H. D. Negus | Local Auditor | Audit Office | — | — |
| 1899 | F. H. D. Negus | Local Auditor | Audit Office | — | — |

### Deterministic checks: `negus_francis-h-d_e1893` vs `Negus, F. H. D___Gold Coast___1894`

- [PASS] surname_gate: bio 'NEGUS' vs stint 'Negus, F. H. D' (exact)
- [PASS] initials: bio ['F', 'H', 'D'] ~ stint ['F', 'H', 'D']
- [PASS] age_gate: stint starts 1894; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Gold Coast'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1894-1899
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

