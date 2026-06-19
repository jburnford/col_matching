<!-- {"case_id": "case_davy_john-bernard_e1900", "bio_ids": ["davy_john-bernard_e1900"], "stint_ids": ["Davy, J. Burt___Transvaal___1906"]} -->
# Dossier case_davy_john-bernard_e1900

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `davy_john-bernard_e1900`

- Printed name: **DAVY, JOHN BERNARD**
- Birth year: not printed
- Appears in editions: [1911]

### Verbatim printed entry text (OCR)

**Version `col1911-L44172.v` — printed in editions [1911]:**

> DAVY, JOHN BERNARD.—M.B.(Lond.) 1900; M.R.C.S. (Eng.), L.R.C.P. (Lond.) 1899; D.T.M. (Liverpool); entrance exhibn. and Freeman schlr., Middx. Hosp.; civ. surg., S. African War, 1900-1 (medal and clasp), med. offr., Nyasaland Prot., 1902.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1900–1901 | civ. surg. | South Africa | [1911] |
| 1 | 1902 | med. offr. | Nyasaland Protectorate | [1911] |

## Candidate stint `Davy, J. Burt___Transvaal___1906`

- Staff-list name: **Davy, J. Burt** | colony: **Transvaal** | listed 1906–1907 | editions [1906, 1907]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1906 | J. Burt Davy | Division of Botany | Agricultural Department | — | — |
| 1907 | J. Burt Davy | Division of Botany | Agricultural Department | — | — |

### Deterministic checks: `davy_john-bernard_e1900` vs `Davy, J. Burt___Transvaal___1906`

- [PASS] surname_gate: bio 'DAVY' vs stint 'Davy, J. Burt' (exact)
- [PASS] initials: bio ['J', 'B'] ~ stint ['J', 'B']
- [PASS] age_gate: stint starts 1906; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Transvaal'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1906-1907
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

