<!-- {"case_id": "case_barbados_x_e1825-2", "bio_ids": ["barbados_x_e1825-2"], "stint_ids": ["Barbaro, Crispo___Malta___1898"]} -->
# Dossier case_barbados_x_e1825-2

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['barbados_x_e1825-2'] carry a single initial only — the namesake trap applies.

## Biography `barbados_x_e1825-2`

- Printed name: **BARBADOS, (no given names printed)**
- Birth year: not printed
- Appears in editions: [1900, 1913]

### Verbatim printed entry text (OCR)

**Version `col1900-L33778.v` — printed in editions [1900, 1913]:**

> BARBADOS, BISHOP OF (founded 1825).—RIGHT REV.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1825 | BISHOP | Barbados | [1900, 1913] |

## Candidate stint `Barbaro, Crispo___Malta___1898`

- Staff-list name: **Barbaro, Crispo** | colony: **Malta** | listed 1898–1905 | editions [1898, 1899, 1905]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1898 | Crispo Barbaro, Marquis of St George | Superintendent of Corradino Prison | Corradino Prison | — | — |
| 1899 | Crispo Barbaro, Marquis of St. George | Superintendent of Corradino Prison | Corradino Prison | — | — |
| 1905 | Crispo Barbaro | Superintendent of Corradino Prison | Corradino Prison | — | — |

### Deterministic checks: `barbados_x_e1825-2` vs `Barbaro, Crispo___Malta___1898`

- [PASS] surname_gate: bio 'BARBADOS' vs stint 'Barbaro, Crispo' (fuzzy:2)
- [PASS] initials: bio ['?'] ~ stint ['C']
- [PASS] age_gate: stint starts 1898; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Malta'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1898-1905
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

