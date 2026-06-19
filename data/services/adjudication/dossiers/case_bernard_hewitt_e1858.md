<!-- {"case_id": "case_bernard_hewitt_e1858", "bio_ids": ["bernard_hewitt_e1858"], "stint_ids": ["Bernard, H. L. C___Tasmania___1888"]} -->
# Dossier case_bernard_hewitt_e1858

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 12 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['bernard_hewitt_e1858'] carry a single initial only — the namesake trap applies.

## Biography `bernard_hewitt_e1858`

- Printed name: **BERNARD, HEWITT**
- Birth year: not printed
- Honours: C.M.G. (1872)
- Appears in editions: [1886, 1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1886-L32156.v` — printed in editions [1886, 1888, 1889, 1890]:**

> BERNARD, HEWITT, LIEUT.-COL., C.M.G. (1872).—Called to the bar, Upper Canada, 1866; secretary to attorney-general, Upper Canada, 25th February, 1858; chief clerk, crown law department, Upper Canada, 5th March, 1859; was secretary to conference of delegates on the subject of confederation of British North American Provinces, held in Quebec, 1st October, 1864, and also secretary to the conference of delegates on same subject held in London, England, November, 1866; appointed deputy to the minister of justice, 30th May, 1868, an office he resigned in October, 1876, retiring on a pension; and served in 1878-9 as assistant commissioner with Sir Alexander Galt, C.C.M.G., in negotiations with the courts of France and Spain for commercial relations with Canada, appointed by H.M. the King of Spain a Knight Commander of the Order of Isabel la Católica, 1872; created a Q.C., December, 1872; is an extra aide-de-camp to the governor-general of Canada.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1858–1858 | secretary to attorney-general | Upper Canada | [1886, 1888, 1889, 1890] |
| 1 | 1859–1859 | chief clerk, crown law department | Upper Canada | [1886, 1888, 1889, 1890] |
| 2 | 1864–1864 | secretary to conference of delegates on the subject of confederation of British North American Provinces | Quebec | [1886, 1888, 1889, 1890] |
| 3 | 1866–1866 | Called to the bar | Upper Canada | [1886, 1888, 1889, 1890] |
| 4 | 1866–1866 | secretary to the conference of delegates on same subject | London, England | [1886, 1888, 1889, 1890] |
| 5 | 1868–1876 | deputy to the minister of justice | — | [1886, 1888, 1889, 1890] |
| 6 | 1872–1872 | Knight Commander of the Order of Isabel la Católica | — | [1886, 1888, 1889, 1890] |
| 7 | 1872–1872 | created a Q.C. | — | [1886, 1888, 1889, 1890] |
| 8 | 1878–1879 | assistant commissioner | Canada | [1886, 1888, 1889, 1890] |

## Candidate stint `Bernard, H. L. C___Tasmania___1888`

- Staff-list name: **Bernard, H. L. C** | colony: **Tasmania** | listed 1888–1889 | editions [1888, 1889]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | H. L. C. Bernard | Col. Commanding Reserves | Defences | — | Colonel |
| 1889 | Colonel H. L. C. Bernard | Superintendent Country Rifle Clubs | Defences | — | Colonel |

### Deterministic checks: `bernard_hewitt_e1858` vs `Bernard, H. L. C___Tasmania___1888`

- [PASS] surname_gate: bio 'BERNARD' vs stint 'Bernard, H. L. C' (exact)
- [PASS] initials: bio ['H'] ~ stint ['H', 'L', 'C']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Tasmania'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1888-1889
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

