<!-- {"case_id": "case_wharry_charles-john_e1871", "bio_ids": ["wharry_charles-john_e1871"], "stint_ids": ["Wharry, C. J___Hong Kong___1877"]} -->
# Dossier case_wharry_charles-john_e1871

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `wharry_charles-john_e1871`

- Printed name: **WHARRY, CHARLES JOHN**
- Birth year: not printed
- Appears in editions: [1883, 1886]

### Verbatim printed entry text (OCR)

**Version `col1883-L29965.v` — printed in editions [1883, 1886]:**

> WHARRY, CHARLES JOHN, M.D.—Superintendent government Civil Hospital, Hong Kong, Dec., 1872; educated at King's College School, St. Bartholomew's Hospital, London, and University of Aberdeen; graduated M.B., C.M., 1871; M.D., 1873; M.R.C.S.E., L.S.A.L., 1871; formerly house physician to St. Bartholomew's Hospital; visiting surgeon under the C.D. Act in Hong Kong, 1878; placed in charge of temporary Smallpox Hospital in 1878, 1874, and 1879; acting colonial surgeon and inspector of hospitals in 1878 and 1875; is a fellow of the Royal Medical and Chirurgical Society.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1871–1871 | graduated M.B., C.M. | — | [1883, 1886] |
| 1 | 1871–1871 | M.R.C.S.E., L.S.A.L. | — | [1883, 1886] |
| 2 | 1872 | Superintendent government Civil Hospital | Hong Kong | [1883, 1886] |
| 3 | 1873–1873 | M.D. | — | [1883, 1886] |
| 4 | 1874–1879 | placed in charge of temporary Smallpox Hospital | — | [1883, 1886] |
| 5 | 1875–1878 | acting colonial surgeon and inspector of hospitals | — | [1883, 1886] |
| 6 | 1878–1878 | visiting surgeon under the C.D. Act | Hong Kong | [1883, 1886] |

## Candidate stint `Wharry, C. J___Hong Kong___1877`

- Staff-list name: **Wharry, C. J** | colony: **Hong Kong** | listed 1877–1886 | editions [1877, 1878, 1880, 1883, 1886]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | C. J. Wharry | Superintendent of Civil Hospital | Medical Department | — | — |
| 1878 | C. J. Wharry | Superintendent of Civil Hospital | Medical Department | — | — |
| 1880 | C. J. Wharry | Superintendent of Civil Hospital | Medical Department | — | — |
| 1883 | C. J. Wharry | Superintendent of Civil Hospital | Medical Department | — | — |
| 1886 | C. J. Wharry | Superintendent of Civil Hospital | Medical Department | — | — |

### Deterministic checks: `wharry_charles-john_e1871` vs `Wharry, C. J___Hong Kong___1877`

- [PASS] surname_gate: bio 'WHARRY' vs stint 'Wharry, C. J' (exact)
- [PASS] initials: bio ['C', 'J'] ~ stint ['C', 'J']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Hong Kong'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1886
- [FAIL] position_sim: best 43 vs bar 60: 'visiting surgeon under the C.D. Act' ~ 'Superintendent of Civil Hospital'
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

