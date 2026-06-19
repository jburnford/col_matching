<!-- {"case_id": "case_conolly_e-t_e1882", "bio_ids": ["conolly_e-t_e1882"], "stint_ids": ["Conolly, E. T___New Zealand___1894"]} -->
# Dossier case_conolly_e-t_e1882

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `conolly_e-t_e1882`

- Printed name: **CONOLLY, E. T**
- Birth year: not printed
- Appears in editions: [1888, 1889, 1890, 1894, 1896]

### Verbatim printed entry text (OCR)

**Version `col1888-L32772.v` — printed in editions [1888, 1889, 1890, 1894, 1896]:**

> CONOLLY, E. T.—Minister of justice, New Zealand, 1882 to 1884; also attorney general, 1883-4.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1882–1884 | Minister of justice | New Zealand | [1888, 1889, 1890, 1894, 1896] |
| 1 | 1883–1884 | also attorney general | New Zealand *(inherited from previous clause)* | [1888, 1889, 1890, 1894, 1896] |

## Candidate stint `Conolly, E. T___New Zealand___1894`

- Staff-list name: **Conolly, E. T** | colony: **New Zealand** | listed 1894–1900 | editions [1894, 1896, 1897, 1898, 1899, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1894 | E. T. Conolly | Puisne Judge | Judicial | — | — |
| 1896 | E. T. Conolly | Puisne Judge | Judicial | — | — |
| 1897 | E. T. Conolly | Judge | Judicial | — | — |
| 1898 | E. T. Conolly | Puisne Judge | Judicial | — | — |
| 1899 | E. T. Conolly | Puisne Judge | Judicial | — | — |
| 1900 | E. T. Conolly | Puisne Judge | Judicial | — | — |

### Deterministic checks: `conolly_e-t_e1882` vs `Conolly, E. T___New Zealand___1894`

- [PASS] surname_gate: bio 'CONOLLY' vs stint 'Conolly, E. T' (exact)
- [PASS] initials: bio ['E', 'T'] ~ stint ['E', 'T']
- [PASS] age_gate: stint starts 1894; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'New Zealand'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1894-1900
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

