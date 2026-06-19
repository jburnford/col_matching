<!-- {"case_id": "case_coote_j-m_e1915", "bio_ids": ["coote_j-m_e1915"], "stint_ids": ["Coote, J. M___Uganda___1907"]} -->
# Dossier case_coote_j-m_e1915

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `coote_j-m_e1915`

- Printed name: **COOTE, J. M**
- Birth year: not printed
- Appears in editions: [1918, 1919]

### Verbatim printed entry text (OCR)

**Version `col1918-L49566.v` — printed in editions [1918, 1919]:**

> COOTE, J. M.—Special service offr., E.A.P., Aug., 1915; formerly dist. comsnr., Uganda Prot.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1915 | Special service offr. | East Africa Protectorate | [1918, 1919] |

## Candidate stint `Coote, J. M___Uganda___1907`

- Staff-list name: **Coote, J. M** | colony: **Uganda** | listed 1907–1912 | editions [1907, 1910, 1911, 1912]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1907 | J. M. Coote | Assistant Collector | Administration | — | — |
| 1910 | J. M. Coote | District Commissioner | Administration | — | — |
| 1911 | J. M. Coote | District Commissioner | Administration | — | — |
| 1912 | J. M. Coote | District Commissioner | Administration | — | — |

### Deterministic checks: `coote_j-m_e1915` vs `Coote, J. M___Uganda___1907`

- [PASS] surname_gate: bio 'COOTE' vs stint 'Coote, J. M' (exact)
- [PASS] initials: bio ['J', 'M'] ~ stint ['J', 'M']
- [PASS] age_gate: stint starts 1907; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Uganda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1907-1912
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

