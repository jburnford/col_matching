<!-- {"case_id": "case_pritchard_robert-m-l_e1864", "bio_ids": ["pritchard_robert-m-l_e1864"], "stint_ids": ["Pritchard, R. M___St Helena___1877", "Pritchard, R___Cape of Good Hope___1905"]} -->
# Dossier case_pritchard_robert-m-l_e1864

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 21 official(s) with this surname in the graph's staff lists; 10 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `pritchard_robert-m-l_e1864`

- Printed name: **PRITCHARD, Robert M. L**
- Birth year: not printed
- Appears in editions: [1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1888-L35609.v` — printed in editions [1888, 1889, 1890]:**

> PRITCHARD, Robert M. L.—Locker, customs, St. Helena, July, 1864; 2nd officer of customs and senior gauger, 1873; also harbour master and quarantine officer, Dec., 1878; is also marshal of vice admiralty court.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1864 | Locker, customs | St. Helena | [1888, 1889, 1890] |
| 1 | 1873 | 2nd officer of customs and senior gauger | St. Helena *(inherited from previous clause)* | [1888, 1889, 1890] |
| 2 | 1878 | also harbour master and quarantine officer | St. Helena *(inherited from previous clause)* | [1888, 1889, 1890] |

## Candidate stint `Pritchard, R. M___St Helena___1877`

- Staff-list name: **Pritchard, R. M** | colony: **St Helena** | listed 1877–1883 | editions [1877, 1879, 1880, 1883]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | R. Pritchard | Officer of Customs Branch | Civil Establishment | — | — |
| 1879 | R. Pritchard | Officers of Customs Branch, in Receiver-General's Department | Civil Establishment | — | — |
| 1880 | R. Pritchard | Officers of Customs Branch | Civil Establishment | — | — |
| 1883 | R. Pritchard | Officer of Customs Branch | Receiver-General's Department | — | — |

### Deterministic checks: `pritchard_robert-m-l_e1864` vs `Pritchard, R. M___St Helena___1877`

- [PASS] surname_gate: bio 'PRITCHARD' vs stint 'Pritchard, R. M' (exact)
- [PASS] initials: bio ['R', 'M', 'L'] ~ stint ['R', 'M']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 3 placed event(s) resolve to 'St Helena'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1877-1883
- [PASS] position_sim: best 84 vs bar 60: '2nd officer of customs and senior gauger' ~ 'Officer of Customs Branch'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

## Candidate stint `Pritchard, R___Cape of Good Hope___1905`

- Staff-list name: **Pritchard, R** | colony: **Cape of Good Hope** | listed 1905–1909 | editions [1905, 1906, 1907, 1908, 1909]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | R. Pritchard | Assistant Draftsman | Surveyor-General's Office | — | — |
| 1906 | R. Pritchard | Assistant Draftsman | Surveyor-General's Office | — | — |
| 1907 | R. Pritchard | Assistant Draftsman | Surveyor-General's Office | — | — |
| 1908 | R. Pritchard | Assistant Draughtsman | Surveyor-General's Office | — | — |
| 1909 | R. Pritchard | Draftsman | Surveyor-General's Office | — | — |

### Deterministic checks: `pritchard_robert-m-l_e1864` vs `Pritchard, R___Cape of Good Hope___1905`

- [PASS] surname_gate: bio 'PRITCHARD' vs stint 'Pritchard, R' (exact)
- [PASS] initials: bio ['R', 'M', 'L'] ~ stint ['R']
- [PASS] age_gate: stint starts 1905; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Cape of Good Hope'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1909
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

