<!-- {"case_id": "case_wylde_john-f_e1862", "bio_ids": ["wylde_john-f_e1862"], "stint_ids": ["Wylde, J. F___Antigua___1888", "Wylde, J. F___Leeward Islands___1883"]} -->
# Dossier case_wylde_john-f_e1862

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `wylde_john-f_e1862`

- Printed name: **WYLDE, JOHN F**
- Birth year: not printed
- Appears in editions: [1883, 1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1883-L30081.v` — printed in editions [1883, 1888, 1889, 1890]:**

> WYLDE, JOHN F.—Treasurer, Dominica, and member of legislative assembly, 1873; casual receiver and ordnance commissioner, 1873; acted as president, Aug. to Dec., 1876; member of executive council, 1877; treasurer and protector of immigrants, Nevis, March, 1878; member of executive and legislative councils, June, 1878; treasurer and registrar of shipping, Antigua, June, 1879; member of the executive and legislative councils; acting auditor, Leeward Islands, July to Nov., 1862, and April to Sept., 1885.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1862 | acting auditor | Leeward Islands | [1883, 1888, 1889, 1890] |
| 1 | 1873 | Treasurer, Dominica, and member of legislative assembly | — | [1883, 1888, 1889, 1890] |
| 2 | 1873 | casual receiver and ordnance commissioner | — | [1883, 1888, 1889, 1890] |
| 3 | 1876 | acted as president | — | [1883, 1888, 1889, 1890] |
| 4 | 1877 | member of executive council | — | [1883, 1888, 1889, 1890] |
| 5 | 1878 | treasurer and protector of immigrants | Nevis | [1883, 1888, 1889, 1890] |
| 6 | 1879 | treasurer and registrar of shipping | Antigua | [1883, 1888, 1889, 1890] |
| 7 | 1885 | acting auditor | Leeward Islands *(inherited from previous clause)* | [1883, 1888, 1889, 1890] |

## Candidate stint `Wylde, J. F___Antigua___1888`

- Staff-list name: **Wylde, J. F** | colony: **Antigua** | listed 1888–1890 | editions [1888, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | J. F. Wylde | Treasurer and Comptroller of Customs and Navigation Laws | Civil Establishment | — | — |
| 1890 | J. F. Wylde | Treasurer and Comptroller of Customs and Navigation Laws | Civil Establishment | — | — |

### Deterministic checks: `wylde_john-f_e1862` vs `Wylde, J. F___Antigua___1888`

- [PASS] surname_gate: bio 'WYLDE' vs stint 'Wylde, J. F' (exact)
- [PASS] initials: bio ['J', 'F'] ~ stint ['J', 'F']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Antigua'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1888-1890
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Wylde, J. F___Leeward Islands___1883`

- Staff-list name: **Wylde, J. F** | colony: **Leeward Islands** | listed 1883–1889 | editions [1883, 1886, 1889]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1883 | J. F. Wylde | Treasurer and Comptroller of Customs and Navigation Laws | Civil Establishment | — | — |
| 1886 | J. F. Wylde | Treasurer and Comptroller of Customs and Navigation Laws | Civil Establishment | — | — |
| 1889 | J. F. Wylde | Treasurer and Comptroller of Customs and Navigation Loans | Civil Establishment | — | — |

### Deterministic checks: `wylde_john-f_e1862` vs `Wylde, J. F___Leeward Islands___1883`

- [PASS] surname_gate: bio 'WYLDE' vs stint 'Wylde, J. F' (exact)
- [PASS] initials: bio ['J', 'F'] ~ stint ['J', 'F']
- [PASS] age_gate: stint starts 1883; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Leeward Islands'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1883-1889
- [FAIL] position_sim: best 30 vs bar 60: 'acting auditor' ~ 'Treasurer and Comptroller of Customs and Navigation Loans'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

