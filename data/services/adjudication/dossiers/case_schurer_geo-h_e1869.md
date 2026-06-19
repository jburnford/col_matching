<!-- {"case_id": "case_schurer_geo-h_e1869", "bio_ids": ["schurer_geo-h_e1869"], "stint_ids": ["Schurer, G. H___British Guiana___1878"]} -->
# Dossier case_schurer_geo-h_e1869

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `schurer_geo-h_e1869`

- Printed name: **SCHURER, Geo. H.**
- Birth year: not printed
- Appears in editions: [1883, 1886]

### Verbatim printed entry text (OCR)

**Version `col1883-L29429.v` — printed in editions [1883, 1886]:**

> SCHURER, Geo. H.—Appointed clerk in the Treasury of British Honduras, July, 1869; keeper of the public cemeteries, September, 1871; private secretary to lieutenant-governor Cairns, July, 1872; performed duty as clerk to the colonial secretary of that colony for a short time, in conjunction with duties in the colonial treasury; justice of the peace, September, 1874; assistant collector of customs of the Gold Coast, November, 1874, to May, 1875; sent on special mission to Quittah, May, 1875; assistant-collector and acting treasurer of Lagos, June, 1875, to January, 1876, also ex-officio registrar of shipping and shipping master; commissary of taxation, British Guiana, Feb., 1876; accountant, registrar's office, May 7, 1877; acting administrator-general from Mar., 1883, to Jan., 1884.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1869 | clerk in the Treasury | British Honduras | [1883, 1886] |
| 1 | 1871 | keeper of the public cemeteries | — | [1883, 1886] |
| 2 | 1872 | private secretary to lieutenant-governor Cairns | — | [1883, 1886] |
| 3 | 1874 | justice of the peace | — | [1883, 1886] |
| 4 | 1874–1875 | assistant collector of customs | Gold Coast | [1883, 1886] |
| 5 | 1875 | sent on special mission | — | [1883, 1886] |
| 6 | 1875–1876 | assistant-collector and acting treasurer, also ex-officio registrar of shipping and shipping master | Lagos | [1883, 1886] |
| 7 | 1876 | commissary of taxation | British Guiana | [1883, 1886] |
| 8 | 1877 | accountant, registrar's office | — | [1883, 1886] |
| 9 | 1883–1884 | acting administrator-general | — | [1883, 1886] |

## Candidate stint `Schurer, G. H___British Guiana___1878`

- Staff-list name: **Schurer, G. H** | colony: **British Guiana** | listed 1878–1886 | editions [1878, 1880, 1883, 1886]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1878 | G. H. Schurer | Accountant | Judicial Establishment | — | — |
| 1880 | G. H. Schurer | Accountant | Judicial Establishment | — | — |
| 1883 | G. H. Schurer | Accountant | Judicial Establishment | — | — |
| 1886 | G. H. Schurer | Accountant | Judicial Establishment | — | — |

### Deterministic checks: `schurer_geo-h_e1869` vs `Schurer, G. H___British Guiana___1878`

- [PASS] surname_gate: bio 'SCHURER' vs stint 'Schurer, G. H' (exact)
- [PASS] initials: bio ['G', 'H'] ~ stint ['G', 'H']
- [PASS] age_gate: stint starts 1878; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'British Guiana'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1878-1886
- [FAIL] position_sim: best 31 vs bar 60: 'commissary of taxation' ~ 'Accountant'
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

