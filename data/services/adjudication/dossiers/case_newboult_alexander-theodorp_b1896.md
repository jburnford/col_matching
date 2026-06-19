<!-- {"case_id": "case_newboult_alexander-theodorp_b1896", "bio_ids": ["newboult_alexander-theodorp_b1896"], "stint_ids": ["Newboult, Alec T___Federation of Malaya___1949"]} -->
# Dossier case_newboult_alexander-theodorp_b1896

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Newboult, Alec T___Federation of Malaya___1949` is also gate-compatible with biography(ies) outside this case: ['newboult_alexander-theodore_b1896'] (already linked elsewhere or filtered).

## Biography `newboult_alexander-theodorp_b1896`

- Printed name: **NEWBOULT, Alexander Theodorp**
- Birth year: 1896 (attested in editions [1936])
- Appears in editions: [1936]

### Verbatim printed entry text (OCR)

**Version `col1936-L63326.v` — printed in editions [1936]:**

> NEWBOULT, Alexander Theodorp, M.C.—B. 1896; ed. Kingswood and Exeter Coll., Oxford; cadet, F.M.S., Nov., 1920; attd. Perak

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1920 | cadet | Federated Malay States | [1936] |

## Candidate stint `Newboult, Alec T___Federation of Malaya___1949`

- Staff-list name: **Newboult, Alec T** | colony: **Federation of Malaya** | listed 1949–1950 | editions [1949, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | Alec T. Newboult | Chief Secretary | Civil Establishment | C.M.G. | — |
| 1950 | Sir Alec T. Newboult | Chief Secretary | Civil Establishment | K.B.E., C.M.G., M.C., E.D. | — |

### Deterministic checks: `newboult_alexander-theodorp_b1896` vs `Newboult, Alec T___Federation of Malaya___1949`

- [PASS] surname_gate: bio 'NEWBOULT' vs stint 'Newboult, Alec T' (exact)
- [PASS] initials: bio ['A', 'T'] ~ stint ['A', 'T']
- [PASS] age_gate: stint starts 1949, birth 1896 (age 53)
- [FAIL] colony: no placed event resolves to 'Federation of Malaya'
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

