<!-- {"case_id": "case_mowat_allan-henry_b1900", "bio_ids": ["mowat_allan-henry_b1900"], "stint_ids": ["Mowat, A. H___Uganda___1939"]} -->
# Dossier case_mowat_allan-henry_b1900

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mowat_allan-henry_b1900`

- Printed name: **MOWAT, Allan Henry**
- Birth year: 1900 (attested in editions [1948, 1949, 1950, 1951])
- Honours: F.R.C.S, M.B
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L34812.v` — printed in editions [1948, 1949, 1950, 1951]:**

> MOWAT, Allan Henry, M.B., Ch.B., F.R.C.S., D.T.M. & H. (Edin.).—b. 1900; med. offr., Uga., 1931; specialist, med. dept.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1931 | med. offr. | Uganda | [1948, 1949, 1950, 1951] |

## Candidate stint `Mowat, A. H___Uganda___1939`

- Staff-list name: **Mowat, A. H** | colony: **Uganda** | listed 1939–1951 | editions [1939, 1940, 1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | A. H. Mowat | Specialist (Surgeon) | Medical | — | — |
| 1940 | A. H. Mowat | Specialists (Surgeon) | Medical | — | — |
| 1949 | A. H. Mowat | Surgeons | Medical | — | — |
| 1951 | A. H. Mowat | Surgeons | MEDICAL | — | — |

### Deterministic checks: `mowat_allan-henry_b1900` vs `Mowat, A. H___Uganda___1939`

- [PASS] surname_gate: bio 'MOWAT' vs stint 'Mowat, A. H' (exact)
- [PASS] initials: bio ['A', 'H'] ~ stint ['A', 'H']
- [PASS] age_gate: stint starts 1939, birth 1900 (age 39)
- [PASS] colony: 1 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1939-1951
- [FAIL] position_sim: best 25 vs bar 60: 'med. offr.' ~ 'Surgeons'
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

