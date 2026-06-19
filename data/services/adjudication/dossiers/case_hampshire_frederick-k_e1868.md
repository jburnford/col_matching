<!-- {"case_id": "case_hampshire_frederick-k_e1868", "bio_ids": ["hampshire_frederick-k_e1868"], "stint_ids": ["Hampshire, F. K___Straits Settlements___1877"]} -->
# Dossier case_hampshire_frederick-k_e1868

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hampshire_frederick-k_e1868`

- Printed name: **HAMPSHIRE, FREDERICK K.**
- Birth year: not printed
- Appears in editions: [1883, 1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1888-L33854.v` — printed in editions [1888, 1889, 1890]:**

> HAMPSHIRE, FREDERICK K., M.B., M.R.C.S.—Colonial surgeon, Malacca, 1868; transferred to Singapore in 1872; to Penang in Mar., 1875, to June, 1876; again at Singapore, 1877; transferred to Penang in 1879, with charge of all the civil medical establishments at that settlement; is health officer and visiting surgeon under C.D.O.; registrar of births and deaths, 1881, and registrar of Mahomedan marriages, 1882; deputy superintendent of vaccination; is a justice of the peace, S.S.

**Version `col1883-L27850.v` — printed in editions [1883]:**

> HAMPSHIRE, FREDERICK K., M.B., M.R.C.S., London.—Colonial surgeon, S.S., July 14th, 1868; resident surgeon at Malacca, with medical charge of native troops in garrison there, 1868. Was transferred to Singapore in May, 1872. Is in charge of general hospital, in medical charge of civil and criminal gaols. Police surgeon and deputy superintendent of vaccination. Is also government analyst for the Straits Settlements.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1868 | Colonial surgeon | Malacca | [1883, 1888, 1889, 1890] |
| 1 | 1872 | — | Singapore | [1883, 1888, 1889, 1890] |
| 2 | 1875–1876 | — | Penang | [1888, 1889, 1890] |
| 3 | 1877 | — | Singapore | [1888, 1889, 1890] |
| 4 | 1879 | charge of all the civil medical establishments | Penang | [1888, 1889, 1890] |
| 5 | 1881 | registrar of births and deaths | — | [1888, 1889, 1890] |
| 6 | 1882 | registrar of Mahomedan marriages | — | [1888, 1889, 1890] |

## Candidate stint `Hampshire, F. K___Straits Settlements___1877`

- Staff-list name: **Hampshire, F. K** | colony: **Straits Settlements** | listed 1877–1888 | editions [1877, 1879, 1880, 1888]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | F. K. Hampshire | Colonial Surgeon | Medical | — | — |
| 1879 | F. K. Hampshire | Surgeon Lock Hospital | Medical | — | — |
| 1880 | F. K. Hampshire | Colonial Surgeon | Medical | — | — |
| 1888 | F. K. Hampshire | Colonial Surgeon | Penang | — | — |

### Deterministic checks: `hampshire_frederick-k_e1868` vs `Hampshire, F. K___Straits Settlements___1877`

- [PASS] surname_gate: bio 'HAMPSHIRE' vs stint 'Hampshire, F. K' (exact)
- [PASS] initials: bio ['F', 'K'] ~ stint ['F', 'K']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1888
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

