<!-- {"case_id": "case_fernleigh_thomas-ernest_e1908", "bio_ids": ["fernleigh_thomas-ernest_e1908", "fernleigh_thomas-ernest_e1908-2"], "stint_ids": ["Fernleigh, T. E___South Africa___1912"]} -->
# Dossier case_fernleigh_thomas-ernest_e1908

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Fernleigh, T. E___South Africa___1912'] have more than one claimant biography in this case.

## Biography `fernleigh_thomas-ernest_e1908`

- Printed name: **FERNLEIGH, Thomas Ernest**
- Birth year: not printed
- Appears in editions: [1911]

### Verbatim printed entry text (OCR)

**Version `col1911-L44651.v` — printed in editions [1911]:**

> FERNLEIGH, Thomas Ernest—Sub.-inspr., Bech. Prot. police, June, 1908.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1908 | Sub.-inspr., Bech. Prot. police | Bechuanaland | [1911] |

## Biography `fernleigh_thomas-ernest_e1908-2`

- Printed name: **FERNLEIGH, THOMAS ERNEST**
- Birth year: not printed
- Appears in editions: [1912, 1913, 1914]

### Verbatim printed entry text (OCR)

**Version `col1912-L44095.v` — printed in editions [1912, 1913, 1914]:**

> FERNLEIGH, THOMAS ERNEST.—Sub.-inspr., Bech. Prot. police, June, 1908; passed lower civ. serv. law exam.; asst. res. mag., 1911.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1908 | Sub.-inspr., Bech. Prot. police | Bechuanaland | [1912, 1913, 1914] |
| 1 | 1911 | asst. res. mag | Bechuanaland *(inherited from previous clause)* | [1912, 1913, 1914] |

## Candidate stint `Fernleigh, T. E___South Africa___1912`

- Staff-list name: **Fernleigh, T. E** | colony: **South Africa** | listed 1912–1914 | editions [1912, 1914]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | T. E. Fernleigh | Sub-Inspector | Establishment | — | — |
| 1914 | T. E. Fernleigh | Sub-Inspector | Civil Establishment | — | — |

### Deterministic checks: `fernleigh_thomas-ernest_e1908` vs `Fernleigh, T. E___South Africa___1912`

- [PASS] surname_gate: bio 'FERNLEIGH' vs stint 'Fernleigh, T. E' (exact)
- [PASS] initials: bio ['T', 'E'] ~ stint ['T', 'E']
- [PASS] age_gate: stint starts 1912; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'South Africa'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1914
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `fernleigh_thomas-ernest_e1908-2` vs `Fernleigh, T. E___South Africa___1912`

- [PASS] surname_gate: bio 'FERNLEIGH' vs stint 'Fernleigh, T. E' (exact)
- [PASS] initials: bio ['T', 'E'] ~ stint ['T', 'E']
- [PASS] age_gate: stint starts 1912; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'South Africa'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1914
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

