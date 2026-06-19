<!-- {"case_id": "case_hannay_w-m_e1876", "bio_ids": ["hannay_w-m_e1876"], "stint_ids": ["Hannay, W. M___New Zealand___1883"]} -->
# Dossier case_hannay_w-m_e1876

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hannay_w-m_e1876`

- Printed name: **HANNAY, W. M.**
- Birth year: not printed
- Appears in editions: [1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900]

### Verbatim printed entry text (OCR)

**Version `col1888-L33856.v` — printed in editions [1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900]:**

> HANNAY, W. M.—For ten years in Glasgow and S. W. Rly.; entered N. Zealand Govt. Rly. service May, 1876; asst. traffic manager, June, 1878; traffic manager, 1879; asst. gen. manager, 1880; rly. commer. under Govt. Rlys. Act, 1887, June, 1889.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1876 | entered N. Zealand Govt. Rly. service | New Zealand | [1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900] |
| 1 | 1878 | asst. traffic manager | — | [1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900] |
| 2 | 1879 | traffic manager | — | [1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900] |
| 3 | 1880 | asst. gen. manager | — | [1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900] |
| 4 | 1889 | rly. commer. under Govt. Rlys. Act, 1887 | — | [1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900] |

## Candidate stint `Hannay, W. M___New Zealand___1883`

- Staff-list name: **Hannay, W. M** | colony: **New Zealand** | listed 1883–1894 | editions [1883, 1886, 1888, 1889, 1894]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1883 | W. M. Hannay | Assistant General Manager | Working Railways Branch | — | — |
| 1886 | W. M. Hannay | Assistant General Manager | WORKING RAILWAYS BRANCH | — | — |
| 1888 | W. M. Hannay | Assistant General Manager | WORKING RAILWAYS BRANCH | — | — |
| 1889 | W. M. Hannay | Assistant General Manager | WORKING RAILWAYS BRANCH | — | — |
| 1894 | W. M. Hannay | Railway Commissioner | Working Railways Department | — | — |

### Deterministic checks: `hannay_w-m_e1876` vs `Hannay, W. M___New Zealand___1883`

- [PASS] surname_gate: bio 'HANNAY' vs stint 'Hannay, W. M' (exact)
- [PASS] initials: bio ['W', 'M'] ~ stint ['W', 'M']
- [PASS] age_gate: stint starts 1883; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'New Zealand'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1883-1894
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

