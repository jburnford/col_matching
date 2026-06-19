<!-- {"case_id": "case_nettelton_clement-ridgway_e1901", "bio_ids": ["nettelton_clement-ridgway_e1901"], "stint_ids": ["Nettelton, C. R___Bechuanaland___1905", "Nettelton, C. R___South Africa___1912"]} -->
# Dossier case_nettelton_clement-ridgway_e1901

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Nettelton, C. R___Bechuanaland___1905` is also gate-compatible with biography(ies) outside this case: ['nettelton_clement-ringway_e1901', 'nettetton_clement-ridgway_e1901'] (already linked elsewhere or filtered).
- NOTE: stint `Nettelton, C. R___South Africa___1912` is also gate-compatible with biography(ies) outside this case: ['nettelton_clement-ringway_e1901', 'nettetton_clement-ridgway_e1901'] (already linked elsewhere or filtered).

## Biography `nettelton_clement-ridgway_e1901`

- Printed name: **NETTELTON, CLEMENT RIDGWAY**
- Birth year: not printed
- Appears in editions: [1910, 1912, 1913, 1915, 1919, 1922]

### Verbatim printed entry text (OCR)

**Version `col1910-L47767.v` — printed in editions [1910, 1912, 1913, 1915, 1919, 1922]:**

> NETTELTON, CLEMENT RIDGWAY.—Inspr., Bechuana Land Prot. pol., May, 1901; seconded from Basutoland service.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1901 | Inspr., Bechuana Land Prot. pol | Bechuana Land | [1910, 1912, 1913, 1915, 1919, 1922] |

## Candidate stint `Nettelton, C. R___Bechuanaland___1905`

- Staff-list name: **Nettelton, C. R** | colony: **Bechuanaland** | listed 1905–1917 | editions [1905, 1906, 1909, 1911, 1917]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | C. R. Nettelton | Inspector | Establishment | — | — |
| 1906 | C. R. Nettelton | Inspector | Civil Establishment | — | — |
| 1909 | C. R. Nettelton | Inspector | Establishment | — | — |
| 1911 | C. R. Nettelton | Inspector | Establishment | — | — |
| 1917 | C. R. Nettelton | Inspector | Establishment | — | — |

### Deterministic checks: `nettelton_clement-ridgway_e1901` vs `Nettelton, C. R___Bechuanaland___1905`

- [PASS] surname_gate: bio 'NETTELTON' vs stint 'Nettelton, C. R' (exact)
- [PASS] initials: bio ['C', 'R'] ~ stint ['C', 'R']
- [PASS] age_gate: stint starts 1905; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Bechuanaland'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1905-1917
- [FAIL] position_sim: best 32 vs bar 60: 'Inspr., Bechuana Land Prot. pol' ~ 'Inspector'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Nettelton, C. R___South Africa___1912`

- Staff-list name: **Nettelton, C. R** | colony: **South Africa** | listed 1912–1914 | editions [1912, 1914]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | C. R. Nettelton | Inspector | Establishment | — | — |
| 1914 | C. R. Nettelton | Inspector | Civil Establishment | — | — |

### Deterministic checks: `nettelton_clement-ridgway_e1901` vs `Nettelton, C. R___South Africa___1912`

- [PASS] surname_gate: bio 'NETTELTON' vs stint 'Nettelton, C. R' (exact)
- [PASS] initials: bio ['C', 'R'] ~ stint ['C', 'R']
- [PASS] age_gate: stint starts 1912; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'South Africa'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1914
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

