<!-- {"case_id": "calib_gemini_tasmania_0397", "bio_ids": ["barnard_james_e1864"], "stint_ids": ["Barnard, James___Tasmania___1877"]} -->
# Dossier calib_gemini_tasmania_0397

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 62 official(s) with this surname in the graph's staff lists; 13 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['barnard_james_e1864'] carry a single initial only — the namesake trap applies.

## Biography `barnard_james_e1864`

- Printed name: **BARNARD, JAMES**
- Birth year: not printed
- Appears in editions: [1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913]

### Verbatim printed entry text (OCR)

**Version `col1905-L41899.v` — printed in editions [1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913]:**

> BARNARD, JAMES.—Ent. govt. service, 1864; sec. for customs, Tasmania, 1894.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1864 | Ent. govt. service | — | [1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913] |
| 1 | 1894 | sec. for customs | Tasmania | [1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913] |

## Candidate stint `Barnard, James___Tasmania___1877`

- Staff-list name: **Barnard, James** | colony: **Tasmania** | listed 1877–1909 | editions [1877, 1878, 1879, 1880, 1888, 1889, 1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | James Barnard | Government Printer | Miscellaneous Offices | — | — |
| 1877 | J. Barnard | Warehouse-keeper | Customs Department | — | — |
| 1878 | James Barnard | Government Printer | Miscellaneous Offices | — | — |
| 1878 | J. Barnard | Warehouse-keeper | Customs Department | — | — |
| 1879 | James Barnard | Government Printer | Miscellaneous Offices | — | — |
| 1879 | J. Barnard | Warehouse-keeper | Customs Department | — | — |
| 1880 | J. Barnard | Warehouse-keeper | Customs Department | — | — |
| 1888 | James Barnard | Senior Landing Waiter | Customs and Excise Department | — | — |
| 1889 | James Barnard | Senior Landing Waiter | Customs and Excise Department | — | — |
| 1894 | J. Barnard | Collector and Landing Surveyor | Customs and Excise Department | — | — |
| 1896 | J. Barnard | Collector and Inspector of Customs | Customs and Excise Department | — | — |
| 1897 | J. Barnard | Collector and Inspector of Customs | Customs and Excise Department | — | — |
| 1898 | J. Barnard | Collector and Inspector of Customs | Customs and Excise Department | — | — |
| 1899 | J. Barnard | Collector and Inspector of Customs | Customs and Excise Department | — | — |
| 1900 | J. Barnard | Collector and Inspector of Customs | Customs and Excise Department | — | — |
| 1905 | J. Barnard | Collector and Inspector of Customs | Customs and Excise Department (Commonwealth Department) | — | — |
| 1906 | J. Barnard | Collector and Inspector of Customs | Customs and Excise Department (Commonwealth Department) | — | — |
| 1907 | J. Barnard | Collector and Inspector of Customs | Customs and Excise Department (Commonwealth Department) | — | — |
| 1908 | J. Barnard | Collector and Inspector of Customs | Customs and Excise Department (Commonwealth Department) | — | — |
| 1909 | J. Barnard | Collector and Inspector of Customs | Customs and Excise Department | — | — |

### Deterministic checks: `barnard_james_e1864` vs `Barnard, James___Tasmania___1877`

- [PASS] surname_gate: bio 'BARNARD' vs stint 'Barnard, James' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Tasmania'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1909
- [FAIL] position_sim: best 58 vs bar 60: 'sec. for customs' ~ 'Collector and Inspector of Customs'
- [FAIL] honour: no shared honour
- [PASS] edition_cooccurrence: 4 agreeing edition-year(s) [1905, 1906, 1907, 1908] pos~58 (bar: >=2)
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

