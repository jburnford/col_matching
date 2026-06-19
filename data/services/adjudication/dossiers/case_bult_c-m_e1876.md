<!-- {"case_id": "case_bult_c-m_e1876", "bio_ids": ["bult_c-m_e1876"], "stint_ids": ["Bult, C. M___Griqualand West___1877"]} -->
# Dossier case_bult_c-m_e1876

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `bult_c-m_e1876`

- Printed name: **BULT, C. M**
- Birth year: not printed
- Appears in editions: [1883, 1886]

### Verbatim printed entry text (OCR)

**Version `col1883-L26646.v` — printed in editions [1883, 1886]:**

> BULT, C. M.—Registrar of Natives at Du Toits Pan, Cape Colony, 30th June, 1876.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1876 | Registrar of Natives at Du Toits Pan | Cape of Good Hope | [1883, 1886] |

## Candidate stint `Bult, C. M___Griqualand West___1877`

- Staff-list name: **Bult, C. M** | colony: **Griqualand West** | listed 1877–1880 | editions [1877, 1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | C. M. Bult | Postmaster | Postal Department | — | — |
| 1879 | C. M. Bult | Postmaster | Postal Department | — | — |
| 1879 | C. M. Bult | Registrar | Registry of Natives, Du Toits Pan | — | — |
| 1880 | C. M. Bult | Postmaster | Postal Department | — | — |
| 1880 | C. M. Bult | Registrar | Registry of Natives, Du Toits Pan | — | — |

### Deterministic checks: `bult_c-m_e1876` vs `Bult, C. M___Griqualand West___1877`

- [PASS] surname_gate: bio 'BULT' vs stint 'Bult, C. M' (exact)
- [PASS] initials: bio ['C', 'M'] ~ stint ['C', 'M']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Griqualand West'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1880
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

