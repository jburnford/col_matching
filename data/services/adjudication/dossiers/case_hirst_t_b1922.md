<!-- {"case_id": "case_hirst_t_b1922", "bio_ids": ["hirst_t_b1922"], "stint_ids": ["Hirst, T___Gold Coast___1949"]} -->
# Dossier case_hirst_t_b1922

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 14 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['hirst_t_b1922'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Hirst, T___Gold Coast___1949` is also gate-compatible with biography(ies) outside this case: ['hirst_tom_b1899'] (already linked elsewhere or filtered).

## Biography `hirst_t_b1922`

- Printed name: **HIRST, T**
- Birth year: 1922 (attested in editions [1959, 1960, 1961])
- Appears in editions: [1959, 1960, 1961]

### Verbatim printed entry text (OCR)

**Version `col1959-L24165.v` — printed in editions [1959, 1960, 1961]:**

> HIRST, T.—b. 1922; mil. serv., 1942-44, R.N.; tech. instr. (mech. engrng.), Nig., 1947; senr. tech. instr., N. Nig., 1955-60.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1947 | tech. instr. (mech. engrng.) | Nigeria | [1959, 1960, 1961] |
| 1 | 1955–1960 | senr. tech. instr. | Northern Nigeria | [1959, 1960, 1961] |

## Candidate stint `Hirst, T___Gold Coast___1949`

- Staff-list name: **Hirst, T** | colony: **Gold Coast** | listed 1949–1950 | editions [1949, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | T. Hirst | Director | Geological Survey | — | — |
| 1950 | T. Hirst | Director | Geological Survey | — | — |

### Deterministic checks: `hirst_t_b1922` vs `Hirst, T___Gold Coast___1949`

- [PASS] surname_gate: bio 'HIRST' vs stint 'Hirst, T' (exact)
- [PASS] initials: bio ['T'] ~ stint ['T']
- [PASS] age_gate: stint starts 1949, birth 1922 (age 27)
- [FAIL] colony: no placed event resolves to 'Gold Coast'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1950
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

