<!-- {"case_id": "case_simmins_godfrey-butler_b1901", "bio_ids": ["simmins_godfrey-butler_b1901"], "stint_ids": ["Simmins, G. B___Palestine___1931"]} -->
# Dossier case_simmins_godfrey-butler_b1901

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `simmins_godfrey-butler_b1901`

- Printed name: **SIMMINS, Godfrey Butler**
- Birth year: 1901 (attested in editions [1948])
- Honours: D.V.S.M, M.R.C.V.S, O.B.E
- Appears in editions: [1948]

### Verbatim printed entry text (OCR)

**Version `col1948-L35899.v` — printed in editions [1948]:**

> SIMMINS, Godfrey Butler, O.B.E., M.R.C.V.S., D.V.S.M.—b. 1901; ed. Glasgow Vet. Coll., Royal (Dick) Vet. Coll., Edinburgh, and Edinburgh Univ.; asst. senr. vet. offr., 1930; senr. vet. research offr., 1937; ch. vet. offr. trans to Jer., 1940; dir. of vet. servs., Pal., 1947.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1930 | asst. senr. vet. offr | — | [1948] |
| 1 | 1937 | senr. vet. research offr | — | [1948] |
| 2 | 1940 | ch. vet. offr. trans to Jer | — | [1948] |
| 3 | 1947 | dir. of vet. servs. | Palestine | [1948] |

## Candidate stint `Simmins, G. B___Palestine___1931`

- Staff-list name: **Simmins, G. B** | colony: **Palestine** | listed 1931–1940 | editions [1931, 1932, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | G. B. Simmins | Asst. Senior Vety. Officer | Department of Agriculture and Forests | — | — |
| 1932 | G. B. Simmins | Ass. Senior Vety. Officer | Department of Agriculture and Forests | — | — |
| 1940 | G. B. Simmins | Senior Veterinary Research Officer | Department of Agriculture and Fisheries | — | — |

### Deterministic checks: `simmins_godfrey-butler_b1901` vs `Simmins, G. B___Palestine___1931`

- [PASS] surname_gate: bio 'SIMMINS' vs stint 'Simmins, G. B' (exact)
- [PASS] initials: bio ['G', 'B'] ~ stint ['G', 'B']
- [PASS] age_gate: stint starts 1931, birth 1901 (age 30)
- [PASS] colony: 1 placed event(s) resolve to 'Palestine'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1931-1940
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

