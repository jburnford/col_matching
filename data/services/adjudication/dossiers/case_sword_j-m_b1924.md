<!-- {"case_id": "case_sword_j-m_b1924", "bio_ids": ["sword_j-m_b1924"], "stint_ids": ["Sword, J. M___Nyasaland___1949"]} -->
# Dossier case_sword_j-m_b1924

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `sword_j-m_b1924`

- Printed name: **SWORD, J. M**
- Birth year: 1924 (attested in editions [1960, 1961, 1962])
- Appears in editions: [1960, 1961, 1962]

### Verbatim printed entry text (OCR)

**Version `col1960-L28527.v` — printed in editions [1960, 1961, 1962]:**

> SWORD, J. M.—b. 1924; ed. Charterhouse, and Gonville and Caius Coll., Camb.; mil. serv., 1944-47, capt.; cadet, Tang., 1949; dist. offr., 1951.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1949 | cadet | Tanganyika | [1960, 1961, 1962] |
| 1 | 1951 | dist. offr | Tanganyika *(inherited from previous clause)* | [1960, 1961, 1962] |

## Candidate stint `Sword, J. M___Nyasaland___1949`

- Staff-list name: **Sword, J. M** | colony: **Nyasaland** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | J. M. Sword | Medical Officer | Medical | — | — |
| 1950 | J. M. Sword | Medical Officers | Medical | — | — |
| 1951 | J. M. Sword | Medical Officer | MEDICAL | — | — |

### Deterministic checks: `sword_j-m_b1924` vs `Sword, J. M___Nyasaland___1949`

- [PASS] surname_gate: bio 'SWORD' vs stint 'Sword, J. M' (exact)
- [PASS] initials: bio ['J', 'M'] ~ stint ['J', 'M']
- [PASS] age_gate: stint starts 1949, birth 1924 (age 25)
- [FAIL] colony: no placed event resolves to 'Nyasaland'
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

