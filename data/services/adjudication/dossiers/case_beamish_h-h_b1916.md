<!-- {"case_id": "case_beamish_h-h_b1916", "bio_ids": ["beamish_h-h_b1916"], "stint_ids": ["Beamish, H. H___Singapore___1958"]} -->
# Dossier case_beamish_h-h_b1916

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `beamish_h-h_b1916`

- Printed name: **BEAMISH, H. H**
- Birth year: 1916 (attested in editions [1958, 1959, 1960, 1961, 1962])
- Appears in editions: [1958, 1959, 1960, 1961, 1962]

### Verbatim printed entry text (OCR)

**Version `col1958-L20417.v` — printed in editions [1958, 1959, 1960, 1961, 1962]:**

> BEAMISH, H. H.—b. 1916; ed. Imp. Service Coll. and Weymouth Coll.; mil. serv., 1939-46, major (desps.); English prog. supvr., b'casting dept., Mal., 1948; dep. dir., b'casting, S'pore, 1957; ag. dir., 1958.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1948 | English prog. supvr., b'casting dept. | Malaya | [1958, 1959, 1960, 1961, 1962] |
| 1 | 1957 | dep. dir., b'casting, S'pore | Malaya *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962] |
| 2 | 1958 | ag. dir | Malaya *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962] |

## Candidate stint `Beamish, H. H___Singapore___1958`

- Staff-list name: **Beamish, H. H** | colony: **Singapore** | listed 1958–1960 | editions [1958, 1959, 1960]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1958 | H. H. Beamish | Deputy Director of Broadcasting | Civil Establishment | — | — |
| 1959 | H. H. Beamish | Director of Broadcasting | Civil Establishment | — | — |
| 1960 | H. H. Beamish | Director of Broadcasting | MINISTRY OF CULTURE | — | — |

### Deterministic checks: `beamish_h-h_b1916` vs `Beamish, H. H___Singapore___1958`

- [PASS] surname_gate: bio 'BEAMISH' vs stint 'Beamish, H. H' (exact)
- [PASS] initials: bio ['H', 'H'] ~ stint ['H', 'H']
- [PASS] age_gate: stint starts 1958, birth 1916 (age 42)
- [FAIL] colony: no placed event resolves to 'Singapore'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1958-1960
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

