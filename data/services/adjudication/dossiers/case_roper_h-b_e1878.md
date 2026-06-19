<!-- {"case_id": "case_roper_h-b_e1878", "bio_ids": ["roper_h-b_e1878"], "stint_ids": ["Roper, H. B___Cape of Good Hope___1888", "Roper, H. B___Griqualand West___1877"]} -->
# Dossier case_roper_h-b_e1878

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 22 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `roper_h-b_e1878`

- Printed name: **ROPER, H. B**
- Birth year: not printed
- Appears in editions: [1883, 1886]

### Verbatim printed entry text (OCR)

**Version `col1883-L29318.v` — printed in editions [1883, 1886]:**

> ROPER, H. B.—Civil commissioner and resident magistrate for Herbert, Cape Colony, Nov., 1878.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1878 | Civil commissioner and resident magistrate for Herbert | Cape of Good Hope | [1883, 1886] |

## Candidate stint `Roper, H. B___Cape of Good Hope___1888`

- Staff-list name: **Roper, H. B** | colony: **Cape of Good Hope** | listed 1888–1900 | editions [1888, 1889, 1894, 1896, 1897, 1898, 1899, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | H. B. Roper | Chief of Department | Detective Department | — | — |
| 1889 | H. B. Roper | Chief of Department | Detective Department | — | — |
| 1894 | H. B. Roper | Inspector of Prisons | Convict and Prisons Branch | — | — |
| 1896 | H. B. Roper | Inspector of Prisons | Convict and Prisons Branch | — | — |
| 1897 | H. B. Roper | Inspector of Prisons | Convict and Prisons Branch | — | — |
| 1898 | H. B. Roper | Inspector of Prisons | Convict and Prisons Branch | — | — |
| 1899 | H. B. Roper | Inspector of Prisons | Convict and Prisons Branch. | — | — |
| 1900 | H. B. Roper | Inspector of Prisons | Convict and Prisons Branch | — | — |

### Deterministic checks: `roper_h-b_e1878` vs `Roper, H. B___Cape of Good Hope___1888`

- [PASS] surname_gate: bio 'ROPER' vs stint 'Roper, H. B' (exact)
- [PASS] initials: bio ['H', 'B'] ~ stint ['H', 'B']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Cape of Good Hope'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1888-1900
- [FAIL] position_sim: best 33 vs bar 60: 'Civil commissioner and resident magistrate for Herbert' ~ 'Chief of Department'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Roper, H. B___Griqualand West___1877`

- Staff-list name: **Roper, H. B** | colony: **Griqualand West** | listed 1877–1880 | editions [1877, 1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | H. B. Roper | Civil Commissioner and Resident Magistrate | Civil Commissioner's Department | — | — |
| 1879 | H. B. Roper | Civil Commissioner and Resident Magistrate | Civil Commissioner, District of Hay | — | — |
| 1880 | H. B. Roper | Civil Commissioner and Resident Magistrate | District of Herbert | — | — |

### Deterministic checks: `roper_h-b_e1878` vs `Roper, H. B___Griqualand West___1877`

- [PASS] surname_gate: bio 'ROPER' vs stint 'Roper, H. B' (exact)
- [PASS] initials: bio ['H', 'B'] ~ stint ['H', 'B']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Griqualand West'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1880
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

