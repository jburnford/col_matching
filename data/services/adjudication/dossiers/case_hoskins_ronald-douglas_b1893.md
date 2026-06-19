<!-- {"case_id": "case_hoskins_ronald-douglas_b1893", "bio_ids": ["hoskins_ronald-douglas_b1893"], "stint_ids": ["Hoskins, R. D___Kenya___1924", "Hoskins___Nyasaland___1914"]} -->
# Dossier case_hoskins_ronald-douglas_b1893

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Hoskins___Nyasaland___1914` is also gate-compatible with biography(ies) outside this case: ['hoskins_james_e1878'] (already linked elsewhere or filtered).

## Biography `hoskins_ronald-douglas_b1893`

- Printed name: **HOSKINS, RONALD DOUGLAS**
- Birth year: 1893 (attested in editions [1939, 1940])
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L67676.v` — printed in editions [1939, 1940]:**

> HOSKINS, RONALD DOUGLAS.—B. 1893; mero. marine, 1913-20; Kenya pol., 1922; 2nd ch. and ch. offr., K.U.R. & H., 1922; commdr., K.U.R. & H., 1929.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1913–1920 | mero. marine | — | [1939, 1940] |
| 1 | 1922 | Kenya pol | Kenya | [1939, 1940] |
| 2 | 1929 | commdr., K.U.R. & H | Kenya *(inherited from previous clause)* | [1939, 1940] |

## Candidate stint `Hoskins, R. D___Kenya___1924`

- Staff-list name: **Hoskins, R. D** | colony: **Kenya** | listed 1924–1925 | editions [1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1924 | R. D. Hoskins | Second Officer | Marine | — | — |
| 1925 | R. D. Hoskins | Second Officers | Marine Department | — | — |

### Deterministic checks: `hoskins_ronald-douglas_b1893` vs `Hoskins, R. D___Kenya___1924`

- [PASS] surname_gate: bio 'HOSKINS' vs stint 'Hoskins, R. D' (exact)
- [PASS] initials: bio ['R', 'D'] ~ stint ['R', 'D']
- [PASS] age_gate: stint starts 1924, birth 1893 (age 31)
- [PASS] colony: 2 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1924-1925
- [FAIL] position_sim: best 26 vs bar 60: 'Kenya pol' ~ 'Second Officer'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Hoskins___Nyasaland___1914`

- Staff-list name: **Hoskins** | colony: **Nyasaland** | listed 1914–1915 | editions [1914, 1915]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1914 | Hoskins | Inspector-General, K.A.R. | King's African Rifles | — | Colonel |
| 1915 | Hoskins | Inspector-General, K.A.R. | King's African Rifles | — | Colonel |

### Deterministic checks: `hoskins_ronald-douglas_b1893` vs `Hoskins___Nyasaland___1914`

- [PASS] surname_gate: bio 'HOSKINS' vs stint 'Hoskins' (exact)
- [PASS] initials: bio ['R', 'D'] ~ stint ['?']
- [PASS] age_gate: stint starts 1914, birth 1893 (age 21)
- [FAIL] colony: no placed event resolves to 'Nyasaland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1914-1915
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

