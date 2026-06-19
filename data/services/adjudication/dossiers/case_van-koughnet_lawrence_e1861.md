<!-- {"case_id": "case_van-koughnet_lawrence_e1861", "bio_ids": ["van-koughnet_lawrence_e1861"], "stint_ids": ["Vankoughnet, Lawrence___Canada___1877"]} -->
# Dossier case_van-koughnet_lawrence_e1861

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['van-koughnet_lawrence_e1861'] carry a single initial only — the namesake trap applies.

## Biography `van-koughnet_lawrence_e1861`

- Printed name: **VAN KOUGHNET, LAWRENCE**
- Birth year: not printed
- Appears in editions: [1886, 1888, 1890]

### Verbatim printed entry text (OCR)

**Version `col1886-L36096.v` — printed in editions [1886, 1888, 1890]:**

> VAN KOUGHNET, LAWRENCE.—4th class clerk, department of Indian affairs, Canada, Feb., 1861; 2nd class, Jan., 1866; 1st class, 1st July, 1873; chief clerk, 1st July, 1870; deputy of superintendent-general of Indian affairs, 1st July, 1880, with rank of deputy minister.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1861 | 4th class clerk, department of Indian affairs | Canada | [1886, 1888, 1890] |
| 1 | 1866 | 2nd class | — | [1886, 1888, 1890] |
| 2 | 1870 | chief clerk | — | [1886, 1888, 1890] |
| 3 | 1873 | 1st class | — | [1886, 1888, 1890] |
| 4 | 1880 | deputy of superintendent-general of Indian affairs | — | [1886, 1888, 1890] |

## Candidate stint `Vankoughnet, Lawrence___Canada___1877`

- Staff-list name: **Vankoughnet, Lawrence** | colony: **Canada** | listed 1877–1896 | editions [1877, 1878, 1879, 1880, 1883, 1888, 1889, 1894, 1896]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | Lawrence Vankoughnet | Deputy Superintendent-General of Indian Affairs | Indian Land Branch | — | — |
| 1878 | Lawrence Vankoughnet | Deputy Superintendent-General of Indian Affairs | Indian Land Branch | — | — |
| 1879 | Lawrence Vankoughnet | Deputy Superintendent-General of Indian Affairs | Indian Land Branch | — | — |
| 1880 | Lawrence Vankoughnet | Deputy Superintendent-General of Indian Affairs | Indian Land Branch | — | — |
| 1883 | Lawrence Vankoughnet | Deputy Superintendent-General | Department of Indian Affairs | — | — |
| 1888 | Lawrence Vankoughnet | Deputy Superintendent-General | Department of Indian Affairs | — | — |
| 1889 | Lawrence Vankoughnet | Deputy Superintendent-General | Department of Indian Affairs | — | — |
| 1894 | Lawrence Vankoughnet | Deputy Superintendent-General | DEPARTMENT OF INDIAN AFFAIRS | — | — |
| 1896 | Lawrence Vankoughnet | Deputy Superintendent-General | Department of Indian Affairs | — | — |

### Deterministic checks: `van-koughnet_lawrence_e1861` vs `Vankoughnet, Lawrence___Canada___1877`

- [PASS] surname_gate: bio 'VAN KOUGHNET' vs stint 'Vankoughnet, Lawrence' (fuzzy:1)
- [PASS] initials: bio ['L'] ~ stint ['L']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1896
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

