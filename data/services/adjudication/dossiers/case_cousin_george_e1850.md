<!-- {"case_id": "case_cousin_george_e1850", "bio_ids": ["cousin_george_e1850"], "stint_ids": ["Cousin, Geo___Malta___1877"]} -->
# Dossier case_cousin_george_e1850

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['cousin_george_e1850'] carry a single initial only — the namesake trap applies.

## Biography `cousin_george_e1850`

- Printed name: **COUSIN, GEORGE**
- Birth year: not printed
- Appears in editions: [1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1888-L32817.v` — printed in editions [1888, 1889, 1890]:**

> COUSIN, GEORGE.—M.D., Malta University, 1850; physician and surgeon of Hospital of Incurables and Orphan Asylum, 16th February, 1851; clerk charitable institution, 18th March, 1853; chief clerk of police, 24th March, 1875; commissary of Monte de Pieta and Savings Bank, 7th May, 1884; auditor-general and director of contracts, 20th May, 1885; ex officio member of council of government, and is a member of executive council. He has also rendered the following special services: commissioned as surgeon to the Malta Artillery Militia, 4th February, 1854; at the time of the Crimean War served as surgeon to the 3rd Corps of Reserve of the British Army; from Dec., 1856, to April, 1857, discharged duties of British Vice-Consul at Naples; from Sept. to Dec., 1858, acted as deputy-comptroller of contracts, Gozo; compiled the last census taken in April, 1881.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1850–1850 | M.D. | Malta | [1888, 1889, 1890] |
| 1 | 1851–1851 | physician and surgeon | — | [1888, 1889, 1890] |
| 2 | 1853–1853 | clerk charitable institution | — | [1888, 1889, 1890] |
| 3 | 1854–1854 | surgeon | Malta | [1888, 1889, 1890] |
| 4 | 1856–1857 | British Vice-Consul | Naples | [1888, 1889, 1890] |
| 5 | 1858–1858 | deputy-comptroller of contracts | Gozo | [1888, 1889, 1890] |
| 6 | 1875–1875 | chief clerk of police | — | [1888, 1889, 1890] |
| 7 | 1881–1881 | — | — | [1888, 1889, 1890] |
| 8 | 1884–1884 | commissary | — | [1888, 1889, 1890] |
| 9 | 1885–1885 | auditor-general and director of contracts | — | [1888, 1889, 1890] |

## Candidate stint `Cousin, Geo___Malta___1877`

- Staff-list name: **Cousin, Geo** | colony: **Malta** | listed 1877–1889 | editions [1877, 1878, 1880, 1883, 1886, 1889]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | G. Cousin | Chief Clerk | Judicial Establishment | — | — |
| 1878 | G. Cousin | Chief Clerk | Police Department | — | — |
| 1880 | G. Cousin | Chief Clerk | Police Department | — | — |
| 1883 | G. Cousin | First Class Clerk | Police Department | — | — |
| 1886 | Geo. Cousin | Auditor-General and Director of Contracts | Audit and Contract Office | — | — |
| 1889 | Geo. Cousin | Auditor-General and Director of Contracts | Audit and Contract Office | — | — |

### Deterministic checks: `cousin_george_e1850` vs `Cousin, Geo___Malta___1877`

- [PASS] surname_gate: bio 'COUSIN' vs stint 'Cousin, Geo' (exact)
- [PASS] initials: bio ['G'] ~ stint ['G']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Malta'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1889
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

