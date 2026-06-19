<!-- {"case_id": "case_de-veuex_george-william_e1861", "bio_ids": ["de-veuex_george-william_e1861"], "stint_ids": ["De Veer, G___British Guiana___1888"]} -->
# Dossier case_de-veuex_george-william_e1861

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `de-veuex_george-william_e1861`

- Printed name: **DE VEUEx, GEORGE WILLIAM**
- Birth year: not printed
- Honours: C.M.G. (1877), K.C.M.G. (1883)
- Appears in editions: [1889]

### Verbatim printed entry text (OCR)

**Version `col1889-L32742.v` — printed in editions [1889]:**

> DE VEUEx, SIR GEORGE WILLIAM, K.C.M.G. (1883), (C.M.G. 1877).—Educated at Charter House and Balliol College, Oxford. Called to the bar of Upper Canada, 1861; stipendiary magistrate, British Guiana, 1863; administrator of the government, St. Lucia, 1869; act. gov. of Trinidad, Jan., 1877, to Jan., 1878; acting governor of Fiji, June, 1878, to Sept., 1879; nominated governor of the Bahamas, 1880; governor of Fiji, 1880-6; Assistant High Commissioner of the Western Pacific, 1880, and High Commissioner, 1882-5; governor of Newfoundland, 1886; of Hong Kong, 1887.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1861 | Called to the bar | Upper Canada | [1889] |
| 1 | 1863 | stipendiary magistrate | British Guiana | [1889] |
| 2 | 1869 | administrator of the government | St. Lucia | [1889] |
| 3 | 1877–1878 | act. gov. | Trinidad | [1889] |
| 4 | 1878–1879 | acting governor | Fiji | [1889] |
| 5 | 1880 | nominated governor | Bahamas | [1889] |
| 6 | 1880 | Assistant High Commissioner | Western Pacific | [1889] |
| 7 | 1882–1885 | High Commissioner | — | [1889] |
| 8 | 1886 | governor | Newfoundland | [1889] |
| 9 | 1887 | governor | Hong Kong | [1889] |

## Candidate stint `De Veer, G___British Guiana___1888`

- Staff-list name: **De Veer, G** | colony: **British Guiana** | listed 1888–1894 | editions [1888, 1889, 1890, 1894]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | G. De Veer | Dispenser | Institutions | — | — |
| 1889 | G. De Veer | Dispenser | Institutions | — | — |
| 1890 | G. De Veer | Dispenser | Medical Institutions | — | — |
| 1894 | G. De Veer | Dispenser | Medical Institutions | — | — |

### Deterministic checks: `de-veuex_george-william_e1861` vs `De Veer, G___British Guiana___1888`

- [PASS] surname_gate: bio 'DE VEUEx' vs stint 'De Veer, G' (fuzzy:2)
- [PASS] initials: bio ['G', 'W'] ~ stint ['G']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'British Guiana'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1888-1894
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

