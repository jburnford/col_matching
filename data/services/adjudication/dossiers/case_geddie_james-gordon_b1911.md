<!-- {"case_id": "case_geddie_james-gordon_b1911", "bio_ids": ["geddie_james-gordon_b1911"], "stint_ids": ["Geddie, J. G___Northern Rhodesia___1949"]} -->
# Dossier case_geddie_james-gordon_b1911

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `geddie_james-gordon_b1911`

- Printed name: **GEDDIE, James Gordon**
- Birth year: 1911 (attested in editions [1951])
- Appears in editions: [1951]

### Verbatim printed entry text (OCR)

**Version `col1951-L38315.v` — printed in editions [1951]:**

> GEDDIE, James Gordon, B.Sc. (S.A. Univ.)—b. 1911; ed. Cambridge High Sch. (Cape Prov.) and Rhodes Univ. Coll. (U.S. Africa); high. educ. dip.; on mil. serv., 1939-44, capt.; mstr., European educ. dept., N. Rhod., 1935.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1935 | mstr., European educ. dept. | Northern Rhodesia | [1951] |

## Candidate stint `Geddie, J. G___Northern Rhodesia___1949`

- Staff-list name: **Geddie, J. G** | colony: **Northern Rhodesia** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | J. G. Geddie | Master | Education | — | — |
| 1951 | J. G. Geddie | Master | Education | — | — |

### Deterministic checks: `geddie_james-gordon_b1911` vs `Geddie, J. G___Northern Rhodesia___1949`

- [PASS] surname_gate: bio 'GEDDIE' vs stint 'Geddie, J. G' (exact)
- [PASS] initials: bio ['J', 'G'] ~ stint ['J', 'G']
- [PASS] age_gate: stint starts 1949, birth 1911 (age 38)
- [PASS] colony: 1 placed event(s) resolve to 'Northern Rhodesia'
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

