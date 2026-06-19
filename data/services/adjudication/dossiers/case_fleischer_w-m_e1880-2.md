<!-- {"case_id": "case_fleischer_w-m_e1880-2", "bio_ids": ["fleischer_w-m_e1880-2"], "stint_ids": ["Fleischer, W. M___Cape of Good Hope___1877"]} -->
# Dossier case_fleischer_w-m_e1880-2

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Fleischer, W. M___Cape of Good Hope___1877` is also gate-compatible with biography(ies) outside this case: ['fleischer_w-m_e1880'] (already linked elsewhere or filtered).

## Biography `fleischer_w-m_e1880-2`

- Printed name: **FLEISCHER, W. M**
- Birth year: not printed
- Appears in editions: [1898, 1899, 1900]

### Verbatim printed entry text (OCR)

**Version `col1898-L33366.v` — printed in editions [1898, 1899, 1900]:**

> FLEISCHER, W. M.—Civ. comsrr., &c., for E. London, Cape Col., May, 1880.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1880 | Civ. comsrr., &c., for E. London | Cape of Good Hope | [1898, 1899, 1900] |

## Candidate stint `Fleischer, W. M___Cape of Good Hope___1877`

- Staff-list name: **Fleischer, W. M** | colony: **Cape of Good Hope** | listed 1877–1896 | editions [1877, 1878, 1880, 1883, 1888, 1889, 1890, 1894, 1896]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | W. M. Fleischer | Resident Magistrate | Police Branch | — | — |
| 1878 | W. M. Fleischer | Resident Magistrate | DISTRICT OF STEYNSBURG | — | — |
| 1880 | W. M. Fleischer | Civil Commissioner and Resident Magistrate | Division of Wodehouse | — | — |
| 1883 | W. M. Fleischer | Visiting Magistrate | Convict Stations | — | — |
| 1888 | W. M. Fleischer | Visiting Magistrate | Convict Stations | — | — |
| 1889 | W. M. Fleischer | Visiting Magistrate | East London | — | — |
| 1890 | W. M. Fleischer | C.C. and R.M. | DIVISION OF EAST LONDON | — | — |
| 1890 | W. M. Fleischer | Visiting Magistrate | East London | — | — |
| 1894 | W. M. Fleischer | Visiting Magistrate | East London | — | — |
| 1896 | W. M. Fleischer | Visiting Magistrate | East London | — | — |
| 1896 | W. M. Fleischer | R.M. | DIVISION OF PORT ELIZABETH | — | — |

### Deterministic checks: `fleischer_w-m_e1880-2` vs `Fleischer, W. M___Cape of Good Hope___1877`

- [PASS] surname_gate: bio 'FLEISCHER' vs stint 'Fleischer, W. M' (exact)
- [PASS] initials: bio ['W', 'M'] ~ stint ['W', 'M']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Cape of Good Hope'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1896
- [FAIL] position_sim: best 48 vs bar 60: 'Civ. comsrr., &c., for E. London' ~ 'Civil Commissioner and Resident Magistrate'
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

