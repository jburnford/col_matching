<!-- {"case_id": "case_donnan_j_e1863", "bio_ids": ["donnan_j_e1863"], "stint_ids": ["Donnan, J___Ceylon___1877"]} -->
# Dossier case_donnan_j_e1863

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['donnan_j_e1863'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Donnan, J___Ceylon___1877` is also gate-compatible with biography(ies) outside this case: ['donnan_j_b1837'] (already linked elsewhere or filtered).

## Biography `donnan_j_e1863`

- Printed name: **DONNAN, J**
- Birth year: not printed
- Appears in editions: [1883, 1886]

### Verbatim printed entry text (OCR)

**Version `col1883-L27224.v` — printed in editions [1883, 1886]:**

> DONNAN, J.—Master attendant, Colombo, Ceylon, 1863; was previously commander of government steamer 'Pearl.'

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1863 | Master attendant, Colombo | Ceylon | [1883, 1886] |

## Candidate stint `Donnan, J___Ceylon___1877`

- Staff-list name: **Donnan, J** | colony: **Ceylon** | listed 1877–1900 | editions [1877, 1878, 1879, 1880, 1883, 1886, 1888, 1889, 1890, 1894, 1896, 1898, 1899, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | J. Donnan | Master Attendant | Harbour Department | — | — |
| 1878 | J. Donnan | Master Attendant | Harbour Department | — | — |
| 1879 | J. Donnan | Master Attendant | Harbour Department | — | — |
| 1880 | J. Donnan | Master Attendant | Harbour Department | — | — |
| 1883 | J. Donnan | Master Attendant | Harbour Department | — | — |
| 1886 | J. Donnan | Master Attendants | Harbour Department | — | — |
| 1888 | J. Donnan | Master Attendant | Harbour Department | — | — |
| 1889 | J. Donnan | Muster Attendant | Harbour Department | — | — |
| 1890 | J. Donnan | Master Attendants | Harbour Department | — | — |
| 1894 | J. Donnan | Master Attendants | Harbour Department | — | — |
| 1896 | J. Donnan | Master Attendant | Harbour Department | — | — |
| 1898 | J. Donnan | Master Attendants | Harbour Department | — | — |
| 1899 | J. Donnan | Master Attendant | Harbour Department | — | — |
| 1900 | J. Donnan | Master Attendant | Harbour Department | — | — |

### Deterministic checks: `donnan_j_e1863` vs `Donnan, J___Ceylon___1877`

- [PASS] surname_gate: bio 'DONNAN' vs stint 'Donnan, J' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Ceylon'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1900
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

