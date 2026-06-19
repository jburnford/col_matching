<!-- {"case_id": "calib_gemini_ceylon_0074", "bio_ids": ["watt_j_e1866"], "stint_ids": ["Watt, J___Ceylon___1877"]} -->
# Dossier calib_gemini_ceylon_0074

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 88 official(s) with this surname in the graph's staff lists; 20 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['watt_j_e1866'] carry a single initial only — the namesake trap applies.

## Biography `watt_j_e1866`

- Printed name: **WATT, J**
- Birth year: not printed
- Appears in editions: [1883, 1886, 1888]

### Verbatim printed entry text (OCR)

**Version `col1883-L29920.v` — printed in editions [1883, 1886, 1888]:**

> WATT, Rev. J.—Colonial chaplain of the Scot's Kirk, Kandy, Ceylon, 1866.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1866 | Colonial chaplain of the Scot's Kirk, Kandy | Ceylon | [1883, 1886, 1888] |

## Candidate stint `Watt, J___Ceylon___1877`

- Staff-list name: **Watt, J** | colony: **Ceylon** | listed 1877–1900 | editions [1877, 1878, 1879, 1880, 1883, 1886, 1888, 1889, 1890, 1894, 1896, 1898, 1899, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | J. Watt | Colonial Chaplain | Colonial Chaplains | — | — |
| 1878 | J. Watt | — | Ecclesiastical Department | — | — |
| 1879 | J. Watt | Colonial Chaplain | Ecclesiastical Department | — | — |
| 1880 | J. Watt | Colonial Chaplain | Ecclesiastical Department | — | — |
| 1883 | J. Watt | Colonial Chaplain | Ecclesiastical Department | — | — |
| 1886 | J. Watt | Colonial Chaplain | List of Colonial Chaplains | — | — |
| 1888 | J. Watt | Rev. | Presbyterian Church | — | — |
| 1889 | J. Watt | — | Presbyterian Church | — | — |
| 1890 | J. Watt | Chaplain | Ecclesiastical | — | — |
| 1894 | J. Watt | Chaplain | Ecclesiastical | — | — |
| 1896 | J. Watt | Chaplain | Ecclesiastical | — | — |
| 1898 | J. Watt | Chaplain | Ecclesiastical | — | — |
| 1899 | J. Watt | Chaplain | Ecclesiastical | — | — |
| 1900 | J. Watt | Chaplain | Ecclesiastical | — | — |

### Deterministic checks: `watt_j_e1866` vs `Watt, J___Ceylon___1877`

- [PASS] surname_gate: bio 'WATT' vs stint 'Watt, J' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1900
- [PASS] position_sim: best 100 vs bar 60: 'Colonial chaplain of the Scot's Kirk, Kandy' ~ 'Chaplain'
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

