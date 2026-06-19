<!-- {"case_id": "case_balderston_benjamin_b1843", "bio_ids": ["balderston_benjamin_b1843"], "stint_ids": ["Balderston, Benjamin___Canada___1897"]} -->
# Dossier case_balderston_benjamin_b1843

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['balderston_benjamin_b1843'] carry a single initial only — the namesake trap applies.

## Biography `balderston_benjamin_b1843`

- Printed name: **BALDERSTON, BENJAMIN**
- Birth year: 1843 (attested in editions [1912, 1913, 1914])
- Appears in editions: [1912, 1913, 1914]

### Verbatim printed entry text (OCR)

**Version `col1912-L42359.v` — printed in editions [1912, 1913, 1914]:**

> BALDERSTON, BENJAMIN.—B. 1843; ed. at Prince of Wales Coll., Prince Edward Island; offl. reporter in the leg. coun. and leg. assem., for many years; apptd. prov. auditor, P.E.I., in 1891, and still holds this office.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1891 | prov. auditor | Prince Edward Island | [1912, 1913, 1914] |
| 1 | ? | offl. reporter | — | [1912, 1913, 1914] |

## Candidate stint `Balderston, Benjamin___Canada___1897`

- Staff-list name: **Balderston, Benjamin** | colony: **Canada** | listed 1897–1912 | editions [1897, 1898, 1899, 1900, 1906, 1907, 1912]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1897 | Benjamin Balderston | Provincial Auditor | Executive Council | — | — |
| 1898 | Benjamin Balderston | Provincial Auditor | Colonial Secretary's Department | — | — |
| 1899 | Benjamin Balderston | Provincial Auditor | Legislative Assembly | — | — |
| 1900 | Benjamin Balderston | Provincial Auditor | Legislative Assembly | — | — |
| 1906 | Benjamin Balderston | Provincial Auditor | Executive Council | — | — |
| 1907 | Benjamin Balderston | Provincial Auditor | Civil Establishment | — | — |
| 1912 | Benjamin Balderston | Provincial Auditor | Legislative Assembly | — | — |

### Deterministic checks: `balderston_benjamin_b1843` vs `Balderston, Benjamin___Canada___1897`

- [PASS] surname_gate: bio 'BALDERSTON' vs stint 'Balderston, Benjamin' (exact)
- [PASS] initials: bio ['B'] ~ stint ['B']
- [PASS] age_gate: stint starts 1897, birth 1843 (age 54)
- [FAIL] colony: no placed event resolves to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1897-1912
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

