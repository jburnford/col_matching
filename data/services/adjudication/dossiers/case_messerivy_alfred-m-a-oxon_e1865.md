<!-- {"case_id": "case_messerivy_alfred-m-a-oxon_e1865", "bio_ids": ["messerivy_alfred-m-a-oxon_e1865", "messervy_alfred-m-a-oxon_e1865"], "stint_ids": ["Messervy, Alfred___Mauritius___1898"]} -->
# Dossier case_messerivy_alfred-m-a-oxon_e1865

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Messervy, Alfred___Mauritius___1898'] have more than one claimant biography in this case.
- NOTE: stint `Messervy, Alfred___Mauritius___1898` is also gate-compatible with biography(ies) outside this case: ['messeryy_alfred_e1865'] (already linked elsewhere or filtered).
- NOTE: stint `Messervy, Alfred___Mauritius___1898` is also gate-compatible with biography(ies) outside this case: ['messeryy_alfred_e1865'] (already linked elsewhere or filtered).

## Biography `messerivy_alfred-m-a-oxon_e1865`

- Printed name: **MESSERIVY, ALFRED M.A. (Oxon.)**
- Birth year: not printed
- Appears in editions: [1889]

### Verbatim printed entry text (OCR)

**Version `col1889-L34617.v` — printed in editions [1889]:**

> MESSERIVY, ALFRED M.A. (Oxon.).—Edu. Vic-Coll., Jersey, and Exeter Coll., Ox., scholar in 1865; Taylorian scholar, 1867; rector of the Royal College, Mauritius, Nov., 1879.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1865 | Edu. Vic-Coll., Jersey, and Exeter Coll., Ox., scholar in | — | [1889] |
| 1 | 1867 | Taylorian scholar | — | [1889] |
| 2 | 1879 | rector of the Royal College | Mauritius | [1889] |

## Biography `messervy_alfred-m-a-oxon_e1865`

- Printed name: **MESSERVY, ALFRED M.A. (Oxon)**
- Birth year: not printed
- Appears in editions: [1883, 1886, 1888, 1890, 1894, 1896, 1898, 1899]

### Verbatim printed entry text (OCR)

**Version `col1890-L35671.v` — printed in editions [1890, 1894, 1896, 1898, 1899]:**

> MESSERVY, ALFRED, M.A. (Oxon.).—Ed. Victoria Coll., Jersey, and Exeter Coll., Oxon.; scholar in 1865; Taylorian scholar, 1867; rector of the Roy. Coll., Mauritius, Nov., 1879.

**Version `col1883-L28684.v` — printed in editions [1883, 1886, 1888]:**

> MESSERVY, ALFRED M.A. (Oxon).—Educated at Victoria College, Jersey, and at Exeter College, Oxford, of which he was elected scholar in 1865; Taylorian scholar, 1867; appointed rector of the Royal College, Mauritius, Nov., 1879.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1865 | scholar in | — | [1890, 1894, 1896, 1898, 1899] |
| 1 | 1867 | Taylorian scholar | — | [1883, 1886, 1888, 1890, 1894, 1896, 1898, 1899] |
| 2 | 1879 | rector of the Roy. Coll. | Mauritius | [1883, 1886, 1888, 1890, 1894, 1896, 1898, 1899] |

## Candidate stint `Messervy, Alfred___Mauritius___1898`

- Staff-list name: **Messervy, Alfred** | colony: **Mauritius** | listed 1898–1900 | editions [1898, 1899, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1898 | A. Messervy | Rector, Royal College | Education | — | — |
| 1899 | A. Messervy | Rector, Royal College | Education | — | — |
| 1900 | A. Messervy | Rector, Royal College | Education | — | — |

### Deterministic checks: `messerivy_alfred-m-a-oxon_e1865` vs `Messervy, Alfred___Mauritius___1898`

- [PASS] surname_gate: bio 'MESSERIVY' vs stint 'Messervy, Alfred' (fuzzy:1)
- [PASS] initials: bio ['A', 'M', 'A'] ~ stint ['A']
- [PASS] age_gate: stint starts 1898; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Mauritius'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1898-1900
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `messervy_alfred-m-a-oxon_e1865` vs `Messervy, Alfred___Mauritius___1898`

- [PASS] surname_gate: bio 'MESSERVY' vs stint 'Messervy, Alfred' (exact)
- [PASS] initials: bio ['A', 'M', 'A'] ~ stint ['A']
- [PASS] age_gate: stint starts 1898; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Mauritius'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1898-1900
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

