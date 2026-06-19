<!-- {"case_id": "case_spencer-churchill_j_e1854", "bio_ids": ["spencer-churchill_j_e1854"], "stint_ids": ["Spencer-Churchill, J. K. G. T___Bahamas___1899", "Spencer-Churchill, J. M___Leeward Islands___1880"]} -->
# Dossier case_spencer-churchill_j_e1854

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['spencer-churchill_j_e1854'] carry a single initial only — the namesake trap applies.

## Biography `spencer-churchill_j_e1854`

- Printed name: **SPENCER-CHURCHILL, J.**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L29573.v` — printed in editions [1883]:**

> SPENCER-CHURCHILL, J.—Educated at Winchester; ensign 46th regt., 1854; served at siege of Sebastopol (medal and clasp); A.D.C. to Lord Lisgar, when lord high commissioner of the Ionian Islands, 1857; captain 46th regt., 1866. Appointed president of Virgin Islands, Mar., 1879; acting president of Nevis, April, 1879, to Jan., 1881.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1854 | ensign 46th regt. | — | [1883] |
| 1 | 1857 | A.D.C. to Lord Lisgar | Ionian Islands | [1883] |
| 2 | 1866 | captain 46th regt. | — | [1883] |
| 3 | 1879 | president | Virgin Islands | [1883] |

## Candidate stint `Spencer-Churchill, J. K. G. T___Bahamas___1899`

- Staff-list name: **Spencer-Churchill, J. K. G. T** | colony: **Bahamas** | listed 1899–1905 | editions [1899, 1900, 1905]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1899 | J. K. G. T. Spencer-Churchill | Colonial Secretary | Colonial Secretary's Office | — | — |
| 1900 | J. K. G. T. Spencer-Churchill | Colonial Secretary | Colonial Secretary's Department | — | — |
| 1905 | J. K. G. T. Spencer-Churchill | Colonial Secretary | Colonial Secretary's Office | C.M.G. | — |

### Deterministic checks: `spencer-churchill_j_e1854` vs `Spencer-Churchill, J. K. G. T___Bahamas___1899`

- [PASS] surname_gate: bio 'SPENCER-CHURCHILL' vs stint 'Spencer-Churchill, J. K. G. T' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J', 'K', 'G', 'T']
- [PASS] age_gate: stint starts 1899; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Bahamas'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1899-1905
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Spencer-Churchill, J. M___Leeward Islands___1880`

- Staff-list name: **Spencer-Churchill, J. M** | colony: **Leeward Islands** | listed 1880–1889 | editions [1880, 1883, 1889]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1880 | J. Spencer-Churchill | President and Colonial Treasurer | Civil Establishment | — | — |
| 1883 | J. Spencer-Churchill | President and Magistrate | Civil Establishment | — | — |
| 1889 | J. M. Spencer-Churchill | Commissioner | Civil Establishment | — | Captain |

### Deterministic checks: `spencer-churchill_j_e1854` vs `Spencer-Churchill, J. M___Leeward Islands___1880`

- [PASS] surname_gate: bio 'SPENCER-CHURCHILL' vs stint 'Spencer-Churchill, J. M' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J', 'M']
- [PASS] age_gate: stint starts 1880; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1880-1889
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

