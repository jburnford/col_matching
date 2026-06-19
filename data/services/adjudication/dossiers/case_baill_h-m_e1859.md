<!-- {"case_id": "case_baill_h-m_e1859", "bio_ids": ["baill_h-m_e1859", "ball_h-m_e1859"], "stint_ids": ["Ball, H. M___Canada___1877"]} -->
# Dossier case_baill_h-m_e1859

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 19 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Ball, H. M___Canada___1877'] have more than one claimant biography in this case.

## Biography `baill_h-m_e1859`

- Printed name: **BAILL, H. M**
- Birth year: not printed
- Appears in editions: [1889]

### Verbatim printed entry text (OCR)

**Version `col1889-L31640.v` — printed in editions [1889]:**

> BAILL, H. M.—Formerly in the army; stipendiary magistrate at Lytton, British Columbia, 1859; magistrate and gold commissioner of the Cariboo district, April, 1867; also magistrate of New Westminster, October, 1867; is a county court judge.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1859 | stipendiary magistrate at Lytton | British Columbia | [1889] |
| 1 | 1867 | magistrate and gold commissioner of the Cariboo district | British Columbia *(inherited from previous clause)* | [1889] |

## Biography `ball_h-m_e1859`

- Printed name: **BALL, H. M**
- Birth year: not printed
- Appears in editions: [1883, 1886, 1888, 1890]

### Verbatim printed entry text (OCR)

**Version `col1883-L26307.v` — printed in editions [1883, 1886, 1888, 1890]:**

> BALL, H. M.—Formerly in the army; stipendiary magistrate at Lytton, British Columbia, 1859; magistrate and gold commissioner of the Cariboo district, April, 1867; also magistrate of New Westminster, October, 1867; is a county court judge.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1859 | stipendiary magistrate at Lytton | British Columbia | [1883, 1886, 1888, 1890] |
| 1 | 1867 | magistrate and gold commissioner of the Cariboo district | British Columbia *(inherited from previous clause)* | [1883, 1886, 1888, 1890] |

## Candidate stint `Ball, H. M___Canada___1877`

- Staff-list name: **Ball, H. M** | colony: **Canada** | listed 1877–1880 | editions [1877, 1878, 1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | H. M. Ball | County Court Judge | County Court Judges | — | — |
| 1878 | H. M. Ball | County Court Judge | Judicial Establishment | — | — |
| 1879 | H. M. Ball | County Court Judge | Judicial Establishment | — | — |
| 1880 | H. M. Ball | County Court Judge | Judicial Establishment | — | — |

### Deterministic checks: `baill_h-m_e1859` vs `Ball, H. M___Canada___1877`

- [PASS] surname_gate: bio 'BAILL' vs stint 'Ball, H. M' (fuzzy:1)
- [PASS] initials: bio ['H', 'M'] ~ stint ['H', 'M']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1880
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `ball_h-m_e1859` vs `Ball, H. M___Canada___1877`

- [PASS] surname_gate: bio 'BALL' vs stint 'Ball, H. M' (exact)
- [PASS] initials: bio ['H', 'M'] ~ stint ['H', 'M']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Canada'
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

