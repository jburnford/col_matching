<!-- {"case_id": "case_blackburn_c-g_e1880", "bio_ids": ["blackburn_c-g_e1880", "blackburn_c-j_e1880"], "stint_ids": ["Blackburn, Charles___Newfoundland___1909"]} -->
# Dossier case_blackburn_c-g_e1880

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 12 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Blackburn, Charles___Newfoundland___1909'] have more than one claimant biography in this case.

## Biography `blackburn_c-g_e1880`

- Printed name: **BLACKBURN, C. G**
- Birth year: not printed
- Appears in editions: [1888]

### Verbatim printed entry text (OCR)

**Version `col1888-L32144.v` — printed in editions [1888]:**

> BLACKBURN, C. G.—Chief clerk and warehouse keeper, Lagos, 1880; district commissioner, July, 1880; acting collector and treasurer, Jan., 1883; collector of customs, Gambia, 1883; acting treasurer and postmaster, April to Dec., 1883; April to Dec. 1884, and since July, 1886; is J.P. and member of Legislative Council and Education Board.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1880 | Chief clerk and warehouse keeper | Lagos | [1888] |
| 1 | 1883 | acting collector and treasurer | Lagos *(inherited from previous clause)* | [1888] |
| 2 | 1883 | collector of customs | Gambia | [1888] |
| 3 | 1884 | acting treasurer and postmaster | Gambia *(inherited from previous clause)* | [1888] |
| 4 | 1886 | since | Gambia *(inherited from previous clause)* | [1888] |

## Biography `blackburn_c-j_e1880`

- Printed name: **BLACKBURN, C. J**
- Birth year: not printed
- Appears in editions: [1886]

### Verbatim printed entry text (OCR)

**Version `col1886-L32206.v` — printed in editions [1886]:**

> BLACKBURN, C. J.—Chief clerk and warehouse keeper, Lagos, 1880; collector of customs, Gambia, 1882.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1880 | Chief clerk and warehouse keeper | Lagos | [1886] |
| 1 | 1882 | collector of customs | Gambia | [1886] |

## Candidate stint `Blackburn, Charles___Newfoundland___1909`

- Staff-list name: **Blackburn, Charles** | colony: **Newfoundland** | listed 1909–1919 | editions [1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1909 | Charles Blackburn | Vice-Consul | Foreign Consuls | — | — |
| 1910 | Charles Blackburn | Vice-Consul | Foreign Consuls | — | — |
| 1911 | Charles Blackburn | Vice-Consul | Foreign Consuls | — | — |
| 1912 | Charles Blackburn | Vice-Consul | Foreign Consuls | — | — |
| 1913 | Charles Blackburn | Consul | Foreign Consuls | — | — |
| 1914 | Charles Blackburn | Consul | Foreign Consuls | — | — |
| 1915 | Charles Blackburn | Consul | Foreign Consuls | — | — |
| 1917 | Charles Blackburn | Consul | Foreign Consuls | — | — |
| 1918 | Charles Blackburn | Consul | Foreign Consuls | — | — |
| 1919 | Charles Blackburn | Consul | Foreign Consuls | — | — |

### Deterministic checks: `blackburn_c-g_e1880` vs `Blackburn, Charles___Newfoundland___1909`

- [PASS] surname_gate: bio 'BLACKBURN' vs stint 'Blackburn, Charles' (exact)
- [PASS] initials: bio ['C', 'G'] ~ stint ['C']
- [PASS] age_gate: stint starts 1909; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Newfoundland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1909-1919
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `blackburn_c-j_e1880` vs `Blackburn, Charles___Newfoundland___1909`

- [PASS] surname_gate: bio 'BLACKBURN' vs stint 'Blackburn, Charles' (exact)
- [PASS] initials: bio ['C', 'J'] ~ stint ['C']
- [PASS] age_gate: stint starts 1909; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Newfoundland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1909-1919
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

