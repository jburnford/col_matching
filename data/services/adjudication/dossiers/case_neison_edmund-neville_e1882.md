<!-- {"case_id": "case_neison_edmund-neville_e1882", "bio_ids": ["neison_edmund-neville_e1882"], "stint_ids": ["Neison, E___Natal___1886"]} -->
# Dossier case_neison_edmund-neville_e1882

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `neison_edmund-neville_e1882`

- Printed name: **NEISON, EDMUND NEVILLE**
- Birth year: not printed
- Honours: F.C.S, F.R.G.S
- Appears in editions: [1888]

### Verbatim printed entry text (OCR)

**Version `col1888-L35085.v` — printed in editions [1888]:**

> NEISON, EDMUND NEVILLE, F.R.G.S., F.C.S.—Government Astronomer, Natal, 1882.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1882 | Government Astronomer | Natal | [1888] |

## Candidate stint `Neison, E___Natal___1886`

- Staff-list name: **Neison, E** | colony: **Natal** | listed 1886–1890 | editions [1886, 1888, 1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1886 | E. Neison | Superintendent | Natal Government Observatory | — | — |
| 1888 | E. Neison | Superintendent | Natal Government Observatory | — | — |
| 1889 | E. Neison | Superintendent | Natal Government Observatory | — | — |
| 1890 | E. Neison | Superintendent | Natal Government Observatory | — | — |

### Deterministic checks: `neison_edmund-neville_e1882` vs `Neison, E___Natal___1886`

- [PASS] surname_gate: bio 'NEISON' vs stint 'Neison, E' (exact)
- [PASS] initials: bio ['E', 'N'] ~ stint ['E']
- [PASS] age_gate: stint starts 1886; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Natal'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1886-1890
- [FAIL] position_sim: best 46 vs bar 60: 'Government Astronomer' ~ 'Superintendent'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

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

