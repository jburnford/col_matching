<!-- {"case_id": "case_noronha_henrique-lourenco_e1878", "bio_ids": ["noronha_henrique-lourenco_e1878"], "stint_ids": ["Noronha, H. L___Straits Settlements___1880"]} -->
# Dossier case_noronha_henrique-lourenco_e1878

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `noronha_henrique-lourenco_e1878`

- Printed name: **NORONHA, HENRIQUE LOURENCO**
- Birth year: not printed
- Appears in editions: [1888, 1889, 1894, 1896, 1897, 1898, 1899]

### Verbatim printed entry text (OCR)

**Version `col1888-L35270.v` — printed in editions [1888, 1889, 1894, 1896, 1897, 1898, 1899]:**

> NORONHA, HENRIQUE LOURENCO.—Was a member of the government board of examiners for the Hong Kong civil service from 1878 to Sept., 1879; superintendent of the government printing office, Singapore, 2nd Sept., 1879; compiled the "Straits Civil Service List" for 1883 and 1884.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1878 | member of the government board of examiners | Hong Kong | [1888, 1889, 1894, 1896, 1897, 1898, 1899] |
| 1 | 1879 | superintendent of the government printing office | Singapore | [1888, 1889, 1894, 1896, 1897, 1898, 1899] |
| 2 | 1883 | — | Straits Settlements | [1888, 1889, 1894, 1896, 1897, 1898, 1899] |

## Candidate stint `Noronha, H. L___Straits Settlements___1880`

- Staff-list name: **Noronha, H. L** | colony: **Straits Settlements** | listed 1880–1896 | editions [1880, 1888, 1889, 1890, 1896]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1880 | H. L. Noronha | Superintendent | Printing Office | — | — |
| 1888 | H. L. Noronha | Superintendent | Printing Office | — | — |
| 1889 | H. L. Noronha | Superintendent | Printing Office | — | — |
| 1890 | H. L. Noronha | Superintendent | Printing Office | — | — |
| 1896 | H. L. Noronha | Superintendent | Printing Office | — | — |

### Deterministic checks: `noronha_henrique-lourenco_e1878` vs `Noronha, H. L___Straits Settlements___1880`

- [PASS] surname_gate: bio 'NORONHA' vs stint 'Noronha, H. L' (exact)
- [PASS] initials: bio ['H', 'L'] ~ stint ['H', 'L']
- [PASS] age_gate: stint starts 1880; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Straits Settlements'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1880-1896
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

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

