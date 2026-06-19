<!-- {"case_id": "case_nicolay_hugo-carl-george_e1875", "bio_ids": ["nicolay_hugo-carl-george_e1875"], "stint_ids": ["Nicolay, C. G___Western Australia___1879", "Nicolay, C. G___Western Australia___1889", "Nicolay, H___Cape of Good Hope___1880"]} -->
# Dossier case_nicolay_hugo-carl-george_e1875

## Case context

- 1 biography(ies) and 3 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `nicolay_hugo-carl-george_e1875`

- Printed name: **NICOLAY, HUGO CARL GEORGE**
- Birth year: not printed
- Appears in editions: [1894]

### Verbatim printed entry text (OCR)

**Version `col1894-L33209.v` — printed in editions [1894]:**

> NICOLAY, HUGO CARL GEORGE.—Entered Cape public works dept., 1875; transferred to treasury, Oct., 1876, as assist. accountant; accountant to paymaster-general's office, July, 1881; chief accountant, treas., Aug., 1884; stamping commr., July, 1889; accounting officer of revenue, treasury, July, 1890.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1875–1875 | Entered Cape public works dept. | Cape | [1894] |
| 1 | 1876–1876 | assist. accountant | — | [1894] |
| 2 | 1881–1881 | accountant to paymaster-general's office | — | [1894] |
| 3 | 1884–1884 | chief accountant | — | [1894] |
| 4 | 1889–1889 | stamping commr. | — | [1894] |
| 5 | 1890–1890 | accounting officer of revenue | — | [1894] |

## Candidate stint `Nicolay, C. G___Western Australia___1879`

- Staff-list name: **Nicolay, C. G** | colony: **Western Australia** | listed 1879–1880 | editions [1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1879 | C. G. Nicolay | Chaplain | Convict Department | — | — |
| 1879 | Rev. C. G. Nicolay | Chaplain to Prison | Clergy of the Church of England in the Diocese of Perth, W.A. | — | — |
| 1880 | C. G. Nicolay | Chaplain to Prison, Rev. | Clergy of the Church of England in the Diocese of Perth, W.A. | — | — |

### Deterministic checks: `nicolay_hugo-carl-george_e1875` vs `Nicolay, C. G___Western Australia___1879`

- [PASS] surname_gate: bio 'NICOLAY' vs stint 'Nicolay, C. G' (exact)
- [PASS] initials: bio ['H', 'C', 'G'] ~ stint ['C', 'G']
- [PASS] age_gate: stint starts 1879; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Western Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1879-1880
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Nicolay, C. G___Western Australia___1889`

- Staff-list name: **Nicolay, C. G** | colony: **Western Australia** | listed 1889–1890 | editions [1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1889 | C. G. Nicolay | Rev. | Chief Clergy of the Church of England | — | — |
| 1890 | Rev. C. G. Nicolay | Rev. | Chief Clergy of the Church of England | — | — |

### Deterministic checks: `nicolay_hugo-carl-george_e1875` vs `Nicolay, C. G___Western Australia___1889`

- [PASS] surname_gate: bio 'NICOLAY' vs stint 'Nicolay, C. G' (exact)
- [PASS] initials: bio ['H', 'C', 'G'] ~ stint ['C', 'G']
- [PASS] age_gate: stint starts 1889; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Western Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1889-1890
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Nicolay, H___Cape of Good Hope___1880`

- Staff-list name: **Nicolay, H** | colony: **Cape of Good Hope** | listed 1880–1889 | editions [1880, 1883, 1888, 1889]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1880 | H. Nicolay | Assistant Accountant | Treasury | — | — |
| 1883 | H. Nicolay | Accountant | Paymaster-General's Branch | — | — |
| 1888 | H. Nicolay | Accountant | Paymaster-General's Branch | — | — |
| 1889 | H. Nicolay | Accountant | Paymaster-General's Branch | — | — |

### Deterministic checks: `nicolay_hugo-carl-george_e1875` vs `Nicolay, H___Cape of Good Hope___1880`

- [PASS] surname_gate: bio 'NICOLAY' vs stint 'Nicolay, H' (exact)
- [PASS] initials: bio ['H', 'C', 'G'] ~ stint ['H']
- [PASS] age_gate: stint starts 1880; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Cape of Good Hope'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1880-1889
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

