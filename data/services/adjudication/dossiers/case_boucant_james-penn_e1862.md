<!-- {"case_id": "case_boucant_james-penn_e1862", "bio_ids": ["boucant_james-penn_e1862"], "stint_ids": ["Boucant, James Penn___South Australia___1879"]} -->
# Dossier case_boucant_james-penn_e1862

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `boucant_james-penn_e1862`

- Printed name: **BOUCANT, JAMES PENN**
- Birth year: not printed
- Appears in editions: [1886, 1888]

### Verbatim printed entry text (OCR)

**Version `col1886-L32271.v` — printed in editions [1886, 1888]:**

> BOUCANT, JAMES PENN.—Entered Parliament, South Australia, 1862. Held office in several ministries, as attorney-general, October, 1865, to March, 1866, and thence to May, 1867; as attorney-general and premier, and again as attorney-general, in 1862; as premier and commissioner of crown lands and public works, from June, 1875, to June, 1876; as premier and treasurer, from 26th October, 1877, to 25th September, 1878, when he accepted a seat on the bench of the Supreme Court.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1862 | Member of Parliament | South Australia | [1886, 1888] |
| 1 | 1862–1862 | attorney-general and premier, and again as attorney-general | — | [1886, 1888] |
| 2 | 1865–1867 | attorney-general | — | [1886, 1888] |
| 3 | 1875–1876 | premier and commissioner of crown lands and public works | — | [1886, 1888] |
| 4 | 1877–1878 | premier and treasurer | — | [1886, 1888] |
| 5 | 1878 | seat on the bench of the Supreme Court | — | [1886, 1888] |

## Candidate stint `Boucant, James Penn___South Australia___1879`

- Staff-list name: **Boucant, James Penn** | colony: **South Australia** | listed 1879–1880 | editions [1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1879 | James Penn Boucant | Third Judge | JUDGES OF THE SUPREME COURT | — | — |
| 1880 | James Penn Boucant | Third Judge | Judges of the Supreme Court | — | — |

### Deterministic checks: `boucant_james-penn_e1862` vs `Boucant, James Penn___South Australia___1879`

- [PASS] surname_gate: bio 'BOUCANT' vs stint 'Boucant, James Penn' (exact)
- [PASS] initials: bio ['J', 'P'] ~ stint ['J', 'P']
- [PASS] age_gate: stint starts 1879; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'South Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1879-1880
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

