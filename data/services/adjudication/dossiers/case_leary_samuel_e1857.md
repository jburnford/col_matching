<!-- {"case_id": "case_leary_samuel_e1857", "bio_ids": ["leary_samuel_e1857"], "stint_ids": ["Leary, S___British Guiana___1878"]} -->
# Dossier case_leary_samuel_e1857

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 11 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['leary_samuel_e1857'] carry a single initial only — the namesake trap applies.

## Biography `leary_samuel_e1857`

- Printed name: **LEARY, SAMUEL**
- Birth year: not printed
- Appears in editions: [1883, 1886, 1888, 1889]

### Verbatim printed entry text (OCR)

**Version `col1883-L28339.v` — printed in editions [1883, 1886, 1888, 1889]:**

> LEARY, SAMUEL.—New Amsterdam, British Guiana; diploma of the College of Physicians, Dublin, 1860; diploma of the Faculty of Physicians and Surgeons, Glasgow, 1855; diploma in Midwifery, Andersonian University, 1852, and Faculty Hall, Glasgow, 1855; J.P. and coroner, British Guiana; medical officer East Canje District, Berbice; surgeon, New Amsterdam jail and police health officer, Port of New Amsterdam; entered government service, 1st July, 1873; late medical officer, Skeldon District, Coventyne, Co., Berbice, 1867 to 1873; Philadelphia District, West Coast, Demerara, 1873 to 1875; and medical superintendent, public hospital, Berbice; surgeon, Pettijo and Clonelly Dispensary Districts, Co. Donegal, Ireland, 1857 to 1867.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1857–1867 | surgeon | Ireland | [1883, 1886, 1888, 1889] |
| 1 | 1867–1873 | late medical officer | Berbice | [1883, 1886, 1888, 1889] |
| 2 | 1873 | entered government service | — | [1883, 1886, 1888, 1889] |
| 3 | 1873–1875 | — | Demerara | [1883, 1886, 1888, 1889] |
| 4 | ? | — | British Guiana | [1883, 1886, 1888, 1889] |

## Candidate stint `Leary, S___British Guiana___1878`

- Staff-list name: **Leary, S** | colony: **British Guiana** | listed 1878–1889 | editions [1878, 1879, 1880, 1883, 1886, 1888, 1889]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1878 | S. Leary | Medical Officer | Medical Officers of Immigration Districts | — | — |
| 1879 | S. Leary | Medical Officer | Medical Officers of Immigration Districts | — | — |
| 1880 | S. Leary | East Canje | Immigration Department | — | — |
| 1880 | S. Leary | Visiting Physician | Hospital, Berbice | — | — |
| 1883 | S. Leary | Medical Superintendent | Hospital, Berbice | — | — |
| 1883 | S. Leary | — | Immigration Department | — | — |
| 1886 | S. Leary | Health Officer | Harbours | — | — |
| 1886 | S. Leary | Medical Superintendent | Hospital, Berbice | — | — |
| 1886 | S. Leary | Medical Officer | Immigration Department | — | — |
| 1888 | S. Leary | Health Officer | Harbours | — | — |
| 1888 | S. Leary | Medical Officer | Medical Department | — | — |
| 1889 | S. Leary | Health Officer | Harbours | — | — |
| 1889 | S. Leary | Medical Officer | Medical Department | — | — |

### Deterministic checks: `leary_samuel_e1857` vs `Leary, S___British Guiana___1878`

- [PASS] surname_gate: bio 'LEARY' vs stint 'Leary, S' (exact)
- [PASS] initials: bio ['S'] ~ stint ['S']
- [PASS] age_gate: stint starts 1878; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'British Guiana'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1878-1889
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

