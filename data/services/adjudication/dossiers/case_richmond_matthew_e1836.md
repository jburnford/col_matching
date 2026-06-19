<!-- {"case_id": "case_richmond_matthew_e1836", "bio_ids": ["richmond_matthew_e1836"], "stint_ids": ["Richmond, M. L___Cape of Good Hope___1905"]} -->
# Dossier case_richmond_matthew_e1836

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 16 official(s) with this surname in the graph's staff lists; 11 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['richmond_matthew_e1836'] carry a single initial only — the namesake trap applies.

## Biography `richmond_matthew_e1836`

- Printed name: **RICHMOND, MATTHEW**
- Birth year: not printed
- Honours: C.B. (1860)
- Appears in editions: [1883, 1886, 1888, 1889, 1890, 1894]

### Verbatim printed entry text (OCR)

**Version `col1883-L29246.v` — printed in editions [1883, 1886, 1888, 1889, 1890, 1894]:**

> RICHMOND, MATTHEW, C.B. (1360)—Resident of Paxo, Ionian Islands, 1836; on departure from the Island was presented with a gold medal and a farewell address from the Regent, bishop, judges, and inhabitants; deputy judge advocate at St. John's, New Brunswick, 1838; commissioner for examining and reporting on claims to grants of land in New Zealand, 1840; while engaged on this duty, the "Wairau massacre" occurred; was despatched to establish order and confidence; chief police magistrate of the southern division of New Ulster (now called North Island) and Cook Straits, 1843; superintendent of the southern division of New Zealand, 1844; superintendent and resident magistrate at Nelson, 1846; member of the legislative council by governor Sir George Grey, 25th June, 1853, &c.; received the honour of Companion of the Bath, with an expression of Her Majesty's approbation of the services rendered by him under the crown, conveyed by his grace the Duke of Newcastle, then secretary of state, in despatch dated 18th May, 1860; elected chairman of committees of the legislative council, 28th July, 1865.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1836–1836 | Resident | Ionian Islands | [1883, 1886, 1888, 1889, 1890, 1894] |
| 1 | 1838–1838 | deputy judge advocate | New Brunswick | [1883, 1886, 1888, 1889, 1890, 1894] |
| 2 | 1840–1840 | commissioner for examining and reporting on claims to grants of land | New Zealand | [1883, 1886, 1888, 1889, 1890, 1894] |
| 3 | 1843–1843 | chief police magistrate of the southern division of New Ulster (now called North Island) and Cook Straits | New Ulster | [1883, 1886, 1888, 1889, 1890, 1894] |
| 4 | 1844–1844 | superintendent of the southern division | New Zealand | [1883, 1886, 1888, 1889, 1890, 1894] |
| 5 | 1846–1846 | superintendent and resident magistrate | — | [1883, 1886, 1888, 1889, 1890, 1894] |
| 6 | 1853 | member of the legislative council | — | [1883, 1886, 1888, 1889, 1890, 1894] |
| 7 | 1860–1860 | Companion of the Bath | — | [1883, 1886, 1888, 1889, 1890, 1894] |
| 8 | 1865–1865 | chairman of committees of the legislative council | — | [1883, 1886, 1888, 1889, 1890, 1894] |

## Candidate stint `Richmond, M. L___Cape of Good Hope___1905`

- Staff-list name: **Richmond, M. L** | colony: **Cape of Good Hope** | listed 1905–1909 | editions [1905, 1907, 1909]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | Miss M. L. Richmond | Typist | Educational Department | — | — |
| 1907 | Miss M. L. Richmond | Typist | Educational Department | — | — |
| 1909 | M. L. Richmond | Typists | Educational Department | — | — |

### Deterministic checks: `richmond_matthew_e1836` vs `Richmond, M. L___Cape of Good Hope___1905`

- [PASS] surname_gate: bio 'RICHMOND' vs stint 'Richmond, M. L' (exact)
- [PASS] initials: bio ['M'] ~ stint ['M', 'L']
- [PASS] age_gate: stint starts 1905; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Cape of Good Hope'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1909
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

