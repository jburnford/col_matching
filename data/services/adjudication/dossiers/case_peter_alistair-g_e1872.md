<!-- {"case_id": "case_peter_alistair-g_e1872", "bio_ids": ["peter_alistair-g_e1872"], "stint_ids": ["Peter, A. G___St Lucia___1880", "Peter, A. G___Windward Islands___1877", "Peter, A. G___Windward Islands___1936"]} -->
# Dossier case_peter_alistair-g_e1872

## Case context

- 1 biography(ies) and 3 candidate stint(s) are entangled in this case.
- Corpus context: 10 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `peter_alistair-g_e1872`

- Printed name: **PETER, ALISTAIR G**
- Birth year: not printed
- Appears in editions: [1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1889-L35102.v` — printed in editions [1889, 1890]:**

> PETER, ALISTAIR G.—Sub.-inspr., rev. pol. and rds., 2nd dist., St. Lucia, 1872; immigr. agent, 1874; harbour master, Aug., 1881.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1872 | Sub.-inspr., rev. pol. and rds., 2nd dist. | St. Lucia | [1889, 1890] |
| 1 | 1874 | immigr. agent | St. Lucia *(inherited from previous clause)* | [1889, 1890] |
| 2 | 1881 | harbour master | St. Lucia *(inherited from previous clause)* | [1889, 1890] |

## Candidate stint `Peter, A. G___St Lucia___1880`

- Staff-list name: **Peter, A. G** | colony: **St Lucia** | listed 1880–1888 | editions [1880, 1888]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1880 | A. G. Peter | Inspector of Revenue and Police, and Sheriff | Judicial and Magisterial | — | — |
| 1888 | A. G. Peter (provisional) | Harbour Master and Officer in charge of Revenue Boats | Harbour Master's Department | — | — |

### Deterministic checks: `peter_alistair-g_e1872` vs `Peter, A. G___St Lucia___1880`

- [PASS] surname_gate: bio 'PETER' vs stint 'Peter, A. G' (exact)
- [PASS] initials: bio ['A', 'G'] ~ stint ['A', 'G']
- [PASS] age_gate: stint starts 1880; no printed birth year — UNCHECKED
- [PASS] colony: 3 placed event(s) resolve to 'St Lucia'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1880-1888
- [PASS] position_sim: best 100 vs bar 60: 'harbour master' ~ 'Harbour Master and Officer in charge of Revenue Boats'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

## Candidate stint `Peter, A. G___Windward Islands___1877`

- Staff-list name: **Peter, A. G** | colony: **Windward Islands** | listed 1877–1889 | editions [1877, 1878, 1880, 1883, 1889]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | A. Peter | Sub-Inspectors | Judicial and Magisterial | — | — |
| 1878 | A. C. Peter | Sub-Inspector | Civil Establishment | — | — |
| 1880 | A. G. Peter | Sub-Inspector | Judicial and Magisterial | — | — |
| 1883 | A. G. Peter | Harbour Master and Officer in charge of Revenue Boats | Harbour Master's Department | — | — |
| 1889 | A. G. Peter | Harbour Master | Harbour Master's Department | — | — |

### Deterministic checks: `peter_alistair-g_e1872` vs `Peter, A. G___Windward Islands___1877`

- [PASS] surname_gate: bio 'PETER' vs stint 'Peter, A. G' (exact)
- [PASS] initials: bio ['A', 'G'] ~ stint ['A', 'G']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Windward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1889
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Peter, A. G___Windward Islands___1936`

- Staff-list name: **Peter, A. G** | colony: **Windward Islands** | listed 1936–1939 | editions [1936, 1937, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | A. G. Peter | Consul (Italy) (Con. Agent) | — | — | — |
| 1937 | A. G. Peter | Consul Agent | Foreign Consuls | — | — |
| 1939 | A. G. Peter | Con. Agent (Italy) | — | — | — |

### Deterministic checks: `peter_alistair-g_e1872` vs `Peter, A. G___Windward Islands___1936`

- [PASS] surname_gate: bio 'PETER' vs stint 'Peter, A. G' (exact)
- [PASS] initials: bio ['A', 'G'] ~ stint ['A', 'G']
- [PASS] age_gate: stint starts 1936; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Windward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1936-1939
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

