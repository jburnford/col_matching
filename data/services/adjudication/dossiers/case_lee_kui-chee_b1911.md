<!-- {"case_id": "case_lee_kui-chee_b1911", "bio_ids": ["lee_kui-chee_b1911"], "stint_ids": ["Lee, K. E___Uganda___1936"]} -->
# Dossier case_lee_kui-chee_b1911

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 45 official(s) with this surname in the graph's staff lists; 30 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['lee_kui-chee_b1911'] carry a single initial only — the namesake trap applies.

## Biography `lee_kui-chee_b1911`

- Printed name: **LEE, Kui-Chee**
- Birth year: 1911 (attested in editions [1965, 1966])
- Appears in editions: [1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1965-L16949.v` — printed in editions [1965, 1966]:**

> LEE, Kui-Chee.—b. 1911; ed. Hong Kong Univ.; master, H.K., 1937; educ. offr., 1954.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1937 | master | Hong Kong | [1965, 1966] |

## Candidate stint `Lee, K. E___Uganda___1936`

- Staff-list name: **Lee, K. E** | colony: **Uganda** | listed 1936–1937 | editions [1936, 1937]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | K. E. Lee | Staff Surveyor | Land and Survey Department | — | — |
| 1937 | K. E. Lee | Staff Surveyor | Land and Survey Department | — | — |

### Deterministic checks: `lee_kui-chee_b1911` vs `Lee, K. E___Uganda___1936`

- [PASS] surname_gate: bio 'LEE' vs stint 'Lee, K. E' (exact)
- [PASS] initials: bio ['K'] ~ stint ['K', 'E']
- [PASS] age_gate: stint starts 1936, birth 1911 (age 25)
- [FAIL] colony: no placed event resolves to 'Uganda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1936-1937
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

