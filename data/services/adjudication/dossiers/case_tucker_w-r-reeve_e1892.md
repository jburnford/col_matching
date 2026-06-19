<!-- {"case_id": "case_tucker_w-r-reeve_e1892", "bio_ids": ["tucker_w-r-reeve_e1892"], "stint_ids": ["Tucker, R___Gold Coast___1899"]} -->
# Dossier case_tucker_w-r-reeve_e1892

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 53 official(s) with this surname in the graph's staff lists; 15 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `tucker_w-r-reeve_e1892`

- Printed name: **TUCKER, W. R. REEVE**
- Birth year: not printed
- Appears in editions: [1900]

### Verbatim printed entry text (OCR)

**Version `col1900-L37577.v` — printed in editions [1900]:**

> TUCKER, W. R. REEVE.—Asst. inspr., Lagos Hausas, 1892; commanded Hausas in Ashanti expdn., 1895-6; wing officer, Malay States Guides, 1898; travelling consmr., Lagos, 1899.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1892 | Asst. inspr., Lagos Hausas | Lagos | [1900] |
| 1 | 1895–1896 | commanded Hausas in Ashanti expdn | Lagos *(inherited from previous clause)* | [1900] |
| 2 | 1898 | wing officer, Malay States Guides | Lagos *(inherited from previous clause)* | [1900] |
| 3 | 1899 | travelling consmr. | Lagos | [1900] |

## Candidate stint `Tucker, R___Gold Coast___1899`

- Staff-list name: **Tucker, R** | colony: **Gold Coast** | listed 1899–1900 | editions [1899, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1899 | R. Tucker | Telegraph Foremen | Telegraph Department | — | — |
| 1900 | R. Tucker | Telegraph Foremen | Telegraph Department | — | — |

### Deterministic checks: `tucker_w-r-reeve_e1892` vs `Tucker, R___Gold Coast___1899`

- [PASS] surname_gate: bio 'TUCKER' vs stint 'Tucker, R' (exact)
- [PASS] initials: bio ['W', 'R', 'R'] ~ stint ['R']
- [PASS] age_gate: stint starts 1899; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Gold Coast'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1899-1900
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

