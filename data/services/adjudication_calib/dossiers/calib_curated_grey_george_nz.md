<!-- {"case_id": "calib_curated_grey_george_nz", "bio_ids": ["grey_george_e1829"], "stint_ids": ["Grey, George___New Zealand___1877"]} -->
# Dossier calib_curated_grey_george_nz

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 66 official(s) with this surname in the graph's staff lists; 12 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['grey_george_e1829'] carry a single initial only — the namesake trap applies.

## Biography `grey_george_e1829`

- Printed name: **GREY, GEORGE**
- Birth year: not printed
- Honours: K.C.B. (Civil.) (1848), P.C. (1894)
- Appears in editions: [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897, 1898]

### Verbatim printed entry text (OCR)

**Version `col1883-L27777.v` — printed in editions [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897, 1898]:**

> GREY, THE Rt. HON. SIR GEORGE, K.C.B. (Civil.), 1848., P.C. (1894).—Ensign in the 83rd regiment, 1829; lieut., 1833; and captain, 1839; left England in 1837 to explore the north-west part of Australia, the account of which will be found in a work published by him, entitled "Journals of Two Expeditions of Discovery in North-west and Western Australia, during 1837-8-9;" was for some time resident magistrate at Albany, West Australia; governor of South Australia, Dec., 1840; of New Zealand, 1846; of the Cape of Good Hope, 1854; re-appointed governor of New Zealand, June, 1861; is author of "Polynesian Mythology;" relieved of the government of New Zealand, end of 1867; retired on a governor's pension in 1872; superintendent of the Province of Auckland, 1875; premier of New Zealand, 1877 to 1879; was one of the representatives of New Zealand at the Australian Federation Convention, 1891.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1829 | Ensign | — | [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897, 1898] |
| 1 | 1833 | lieut. | — | [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897, 1898] |
| 2 | 1837–1839 | — | Australia | [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897, 1898] |
| 3 | 1839 | captain | — | [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897, 1898] |
| 4 | 1840 | governor | South Australia | [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897, 1898] |
| 5 | 1846 | governor | New Zealand | [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897, 1898] |
| 6 | 1854 | governor | Cape of Good Hope | [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897, 1898] |
| 7 | 1861 | governor | New Zealand | [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897, 1898] |
| 8 | 1867 | — | New Zealand | [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897, 1898] |
| 9 | 1872 | — | — | [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897, 1898] |
| 10 | 1875 | superintendent | Auckland | [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897, 1898] |
| 11 | 1877–1879 | premier | New Zealand | [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897, 1898] |
| 12 | 1891 | representative | New Zealand | [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897, 1898] |

## Candidate stint `Grey, George___New Zealand___1877`

- Staff-list name: **Grey, George** | colony: **New Zealand** | listed 1877–1879 | editions [1877, 1878, 1879]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | Sir G. Grey | Superintendent of Auckland | Provincial Governments | K.C.B. | — |
| 1878 | Sir George Grey | Commissioner | Customs Department | K.C.B. | — |
| 1878 | Sir George Grey | Premier and Commissioner of Customs | Executive Council | K.C.B. | — |
| 1879 | Hon. Sir George Grey | Commissioner | Customs Department | K.C.B. | — |
| 1879 | George Grey | Premier and Commissioner of Customs and of Stamps | Executive Council | K.C.B. | — |
| 1879 | G. Grey | Commissioner | STAMP OFFICE | K.C.B. | — |

### Deterministic checks: `grey_george_e1829` vs `Grey, George___New Zealand___1877`

- [PASS] surname_gate: bio 'GREY' vs stint 'Grey, George' (exact)
- [PASS] initials: bio ['G'] ~ stint ['G']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 5 placed event(s) resolve to 'New Zealand'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1879
- [PASS] position_sim: best 100 vs bar 60: 'premier' ~ 'Premier and Commissioner of Customs and of Stamps'
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

