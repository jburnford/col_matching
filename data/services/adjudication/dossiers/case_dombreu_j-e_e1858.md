<!-- {"case_id": "case_dombreu_j-e_e1858", "bio_ids": ["dombreu_j-e_e1858"], "stint_ids": ["Dombreux, J. E___Mauritius___1879", "Dombreux, J. E___Mauritius___1889"]} -->
# Dossier case_dombreu_j-e_e1858

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `dombreu_j-e_e1858`

- Printed name: **DOMBREU, J. E.**
- Birth year: not printed
- Appears in editions: [1883, 1888]

### Verbatim printed entry text (OCR)

**Version `col1888-L33125.v` — printed in editions [1888]:**

> DOMBREU, J. E.—Was clerk to the procureur-general, Mauritius, from Feb. 1858 to 1863; district clerk at Pamplemousses, 1863, at Plaines Wilhelms, 18th April, 1876, now at Black River.

**Version `col1883-L27220.v` — printed in editions [1883]:**

> DOMBREU, J. E.—Was clerk to the procureur-general, Mauritius, from Feb. 1858 to 1863; district clerk at Pamplemousses, 1863.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1858–1863 | clerk to the procureur-general | Mauritius | [1883, 1888] |
| 1 | 1863–1863 | district clerk | Pamplemousses | [1883, 1888] |
| 2 | 1876–1876 | district clerk | Plaines Wilhelms | [1888] |
| 3 | ? | district clerk | Black River | [1888] |

## Candidate stint `Dombreux, J. E___Mauritius___1879`

- Staff-list name: **Dombreux, J. E** | colony: **Mauritius** | listed 1879–1883 | editions [1879, 1883]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1879 | J. E. Dombreux | District Clerk | District Magistracy | — | — |
| 1883 | J. E. Dombreux | District Clerk | District Magistracy | — | — |

### Deterministic checks: `dombreu_j-e_e1858` vs `Dombreux, J. E___Mauritius___1879`

- [PASS] surname_gate: bio 'DOMBREU' vs stint 'Dombreux, J. E' (fuzzy:1)
- [PASS] initials: bio ['J', 'E'] ~ stint ['J', 'E']
- [PASS] age_gate: stint starts 1879; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Mauritius'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1879-1883
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Dombreux, J. E___Mauritius___1889`

- Staff-list name: **Dombreux, J. E** | colony: **Mauritius** | listed 1889–1890 | editions [1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1889 | J. Dombreux | 2nd Class Master | Royal College School | — | — |
| 1890 | J. Dombreux | 2nd Class Masters | Royal College School | — | — |

### Deterministic checks: `dombreu_j-e_e1858` vs `Dombreux, J. E___Mauritius___1889`

- [PASS] surname_gate: bio 'DOMBREU' vs stint 'Dombreux, J. E' (fuzzy:1)
- [PASS] initials: bio ['J', 'E'] ~ stint ['J', 'E']
- [PASS] age_gate: stint starts 1889; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Mauritius'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1889-1890
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

