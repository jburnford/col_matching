<!-- {"case_id": "case_rayner_william-alfonso_e1872", "bio_ids": ["rayner_william-alfonso_e1872"], "stint_ids": ["Rayner, William A___Mauritius___1877"]} -->
# Dossier case_rayner_william-alfonso_e1872

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `rayner_william-alfonso_e1872`

- Printed name: **RAYNER, William Alfonso**
- Birth year: not printed
- Appears in editions: [1886]

### Verbatim printed entry text (OCR)

**Version `col1886-L35398.v` — printed in editions [1886]:**

> RAYNER, William Alfonso.—16th June, 1872, acting tide waiter, Mauritius; 23rd Sept., 1874, tug clerk, customs; 5th Mar., 1875, first clerk and cashier, Seychelles; April, 1876, shipping master; 24th April to 19th Sept., 1877, acting collector of dues and taxes, and secretary to board of civil commissioners; Oct., 1877, was appointed clerk in charge of accounts, political department; Nov., 1877, secretary to board of civil commissioners, board of health, and board of education; Dec., 1877, audit examiner; 21st June, 1880, district cashier, Mauritius.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1872 | acting tide waiter | Mauritius | [1886] |
| 1 | 1874 | tug clerk, customs | — | [1886] |
| 2 | 1875 | first clerk and cashier | Seychelles | [1886] |
| 3 | 1876 | shipping master | — | [1886] |
| 4 | 1877–1877 | acting collector of dues and taxes, and secretary to board of civil commissioners | — | [1886] |
| 5 | 1877 | clerk in charge of accounts, political department | — | [1886] |
| 6 | 1877 | audit examiner | — | [1886] |
| 7 | 1880 | district cashier | Mauritius | [1886] |

## Candidate stint `Rayner, William A___Mauritius___1877`

- Staff-list name: **Rayner, William A** | colony: **Mauritius** | listed 1877–1880 | editions [1877, 1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | W. A. Rayner | Clerk, Internal Revenue and Registration Offices | Revenue Department | — | — |
| 1879 | W. A. Rayner | Audit Examiner | Audit Department | — | — |
| 1879 | William A. Rayner | Honorary Secretary | Board of Health | — | — |
| 1879 | William A. Rayner | Honorary Secretary | Board of Education | — | — |
| 1879 | W. A. Rayner | Secretary | Board of Civil Commissioners | — | — |
| 1880 | W. A. Rayner | Auditor | Revenue Department | — | — |
| 1880 | W. A. Rayner | Honorary Secretary | Board of Health | — | — |
| 1880 | W. A. Rayner | Honorary Secretary | Board of Education | — | — |
| 1880 | W. A. Rayner | Secretary | Board of Civil Commissioners | — | — |

### Deterministic checks: `rayner_william-alfonso_e1872` vs `Rayner, William A___Mauritius___1877`

- [PASS] surname_gate: bio 'RAYNER' vs stint 'Rayner, William A' (exact)
- [PASS] initials: bio ['W', 'A'] ~ stint ['W', 'A']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Mauritius'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1880
- [FAIL] position_sim: best 43 vs bar 60: 'district cashier' ~ 'Auditor'
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

