<!-- {"case_id": "case_murray-hudson_h-h-b_b1930", "bio_ids": ["murray-hudson_h-h-b_b1930"], "stint_ids": ["Murray-Hudson, H. H. B___Bechuanaland___1965"]} -->
# Dossier case_murray-hudson_h-h-b_b1930

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `murray-hudson_h-h-b_b1930`

- Printed name: **MURRAY-HUDSON, H. H. B**
- Birth year: 1930 (attested in editions [1966])
- Honours: M.B.E
- Appears in editions: [1966]

### Verbatim printed entry text (OCR)

**Version `col1966-L16856.v` — printed in editions [1966]:**

> MURRAY-HUDSON, H. H. B., M.B.E.—b. 1930; ed. Sherborne Sch., Dorset, and Cape Town Univ.; admin. cadet., Bech., 1953; D.O., 1955; perm. sec., min. of labr. and social services, 1965.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1953 | admin. cadet. | Bechuanaland | [1966] |
| 1 | 1955 | admin. cadet. | Dominions Office | [1966] |
| 2 | 1965 | perm. sec., min. of labr. and social services | Dominions Office *(inherited from previous clause)* | [1966] |

## Candidate stint `Murray-Hudson, H. H. B___Bechuanaland___1965`

- Staff-list name: **Murray-Hudson, H. H. B** | colony: **Bechuanaland** | listed 1965–1966 | editions [1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1965 | H. H. B. Murray-Hudson | Permanent Secretary, Ministry of Labour and Social Services | Secretariat | — | — |
| 1966 | H. H. B. Murray-Hudson | Permanent Secretary, Ministry of Labour and Social Services | Secretariat | — | — |

### Deterministic checks: `murray-hudson_h-h-b_b1930` vs `Murray-Hudson, H. H. B___Bechuanaland___1965`

- [PASS] surname_gate: bio 'MURRAY-HUDSON' vs stint 'Murray-Hudson, H. H. B' (exact)
- [PASS] initials: bio ['H', 'H', 'B'] ~ stint ['H', 'H', 'B']
- [PASS] age_gate: stint starts 1965, birth 1930 (age 35)
- [PASS] colony: 1 placed event(s) resolve to 'Bechuanaland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1965-1966
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

