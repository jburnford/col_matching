<!-- {"case_id": "case_morrison_james-reginald_b1907", "bio_ids": ["morrison_james-reginald_b1907"], "stint_ids": ["Morrison, J___Kenya___1931"]} -->
# Dossier case_morrison_james-reginald_b1907

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 47 official(s) with this surname in the graph's staff lists; 20 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Morrison, J___Kenya___1931` is also gate-compatible with biography(ies) outside this case: ['morrison_j-c_e1877'] (already linked elsewhere or filtered).

## Biography `morrison_james-reginald_b1907`

- Printed name: **MORRISON, JAMES REGINALD**
- Birth year: 1907 (attested in editions [1937])
- Appears in editions: [1937]

### Verbatim printed entry text (OCR)

**Version `col1937-L63267.v` — printed in editions [1937]:**

> MORRISON, JAMES REGINALD.—B. 1907; Northwich Grammar Schl. and Jesus Coll., Cambridge; cadet, Hong Kong, Feb., 1928.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | cadet | Hong Kong | [1937] |

## Candidate stint `Morrison, J___Kenya___1931`

- Staff-list name: **Morrison, J** | colony: **Kenya** | listed 1931–1932 | editions [1931, 1932]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | J. Morrison | Clerk, Storekeeper | Prisons Department | — | — |
| 1932 | J. Morrison | Clerk, Storekeeper | Prisons Department | — | — |

### Deterministic checks: `morrison_james-reginald_b1907` vs `Morrison, J___Kenya___1931`

- [PASS] surname_gate: bio 'MORRISON' vs stint 'Morrison, J' (exact)
- [PASS] initials: bio ['J', 'R'] ~ stint ['J']
- [PASS] age_gate: stint starts 1931, birth 1907 (age 24)
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1931-1932
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

