<!-- {"case_id": "case_credgington_e_b1913", "bio_ids": ["credgington_e_b1913"], "stint_ids": ["Credgington, E___Singapore___1949"]} -->
# Dossier case_credgington_e_b1913

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['credgington_e_b1913'] carry a single initial only — the namesake trap applies.

## Biography `credgington_e_b1913`

- Printed name: **CREDGINGTON, E**
- Birth year: 1913 (attested in editions [1957])
- Appears in editions: [1957]

### Verbatim printed entry text (OCR)

**Version `col1957-L22268.v` — printed in editions [1957]:**

> CREDGINGTON, E.—b. 1913; ed. Fredk. Bird Sch., Coventry, and Coventry Tech. Coll.; B.B.C., 1934-45; senr. engnr. (studios) B.M.A. (Mal.), 1945-46; engnr., b'casting dept., Mal., 1946; ag. dir., engng., S'pore, 1949.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1934–1945 | B.B.C | — | [1957] |
| 1 | 1945–1946 | senr. engnr. (studios) B.M.A. (Mal.) | — | [1957] |
| 2 | 1946 | engnr., b'casting dept. | Malaya | [1957] |
| 3 | 1949 | ag. dir., engng., S'pore | Malaya *(inherited from previous clause)* | [1957] |

## Candidate stint `Credgington, E___Singapore___1949`

- Staff-list name: **Credgington, E** | colony: **Singapore** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | E. Credgington | Engineer | Broadcasting | — | — |
| 1951 | E. Credgington | Engineers | Broadcasting | — | — |

### Deterministic checks: `credgington_e_b1913` vs `Credgington, E___Singapore___1949`

- [PASS] surname_gate: bio 'CREDGINGTON' vs stint 'Credgington, E' (exact)
- [PASS] initials: bio ['E'] ~ stint ['E']
- [PASS] age_gate: stint starts 1949, birth 1913 (age 36)
- [FAIL] colony: no placed event resolves to 'Singapore'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
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

