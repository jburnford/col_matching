<!-- {"case_id": "case_mein_charles-stuart_e1876", "bio_ids": ["mein_charles-stuart_e1876", "mein_charles-stuart_e1884"], "stint_ids": ["Mein, Charles Stuart___Queensland___1878"]} -->
# Dossier case_mein_charles-stuart_e1876

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Mein, Charles Stuart___Queensland___1878'] have more than one claimant biography in this case.
- Phase 1 found `mein_charles-stuart_e1876` ↔ `Mein, Charles Stuart___Queensland___1878` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- Phase 1 found `mein_charles-stuart_e1884` ↔ `Mein, Charles Stuart___Queensland___1878` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).

## Biography `mein_charles-stuart_e1876`

- Printed name: **MEIN, CHARLES STUART**
- Birth year: not printed
- Appears in editions: [1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1888-L34871.v` — printed in editions [1888, 1889, 1890]:**

> MEIN, CHARLES STUART, M.A.—Postmaster-general of Queensland, and leader of the government in the legislative council, July, 1876, to Jan., 1879; again leader of the government in the council, with office of postmaster-general, afterwards of minister for public instruction, from June, 1884, to April, 1885, when he was raised to the bench of the supreme court; he has for many years commanded the 1st regt. of the defence force, with the rank of lieut.-col.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1876–1879 | Postmaster-general, and leader of the government in the legislative council | Queensland | [1888, 1889, 1890] |
| 1 | 1884–1885 | leader of the government in the council, with office of postmaster-general, afterwards of minister for public instruction | — | [1888, 1889, 1890] |
| 2 | 1885 | bench of the supreme court | — | [1888, 1889, 1890] |

## Biography `mein_charles-stuart_e1884`

- Printed name: **MEIN, CHARLES STUART**
- Birth year: not printed
- Appears in editions: [1886]

### Verbatim printed entry text (OCR)

**Version `col1886-L34796.v` — printed in editions [1886]:**

> MEIN, CHARLES STUART.—Postmaster-general, Queensland, July, 1884; minister for public instruction, March, 1885; puisne judge, April, 1885.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1884 | Postmaster-general | Queensland | [1886] |
| 1 | 1885 | minister for public instruction | Queensland *(inherited from previous clause)* | [1886] |

## Candidate stint `Mein, Charles Stuart___Queensland___1878`

- Staff-list name: **Mein, Charles Stuart** | colony: **Queensland** | listed 1878–1890 | editions [1878, 1879, 1880, 1883, 1886, 1888, 1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1878 | Charles Stuart Mein | Postmaster-General | Executive Council | — | — |
| 1878 | C. S. Mein | Member | Legislative Council | — | — |
| 1879 | C. S. Mein | Member of Legislative Council | Legislative Council | — | — |
| 1879 | Charles Stuart Mein | Postmaster-General | Executive Council | — | — |
| 1880 | C. S. Mein | Member | Legislative Council | — | — |
| 1883 | C. S. Mein | Member | Legislative Council | — | — |
| 1886 | Hon. Charles Stuart Mein | 2nd Puisne Judge | Attorney-General's Department | — | — |
| 1888 | Charles Stuart Mein | 2nd puisne Judge | Attorney-General's Department | — | — |
| 1889 | Hon. Charles Stuart Mein | 2nd puisne Judge | Department of Justice | — | — |
| 1890 | Charles Stuart Mein | 2nd puisne Judge | Department of Justice | — | — |

### Deterministic checks: `mein_charles-stuart_e1876` vs `Mein, Charles Stuart___Queensland___1878`

- [PASS] surname_gate: bio 'MEIN' vs stint 'Mein, Charles Stuart' (exact)
- [PASS] initials: bio ['C', 'S'] ~ stint ['C', 'S']
- [PASS] age_gate: stint starts 1878; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Queensland'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1878-1890
- [PASS] position_sim: best 100 vs bar 60: 'Postmaster-general, and leader of the government in the legislative council' ~ 'Postmaster-General'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

### Deterministic checks: `mein_charles-stuart_e1884` vs `Mein, Charles Stuart___Queensland___1878`

- [PASS] surname_gate: bio 'MEIN' vs stint 'Mein, Charles Stuart' (exact)
- [PASS] initials: bio ['C', 'S'] ~ stint ['C', 'S']
- [PASS] age_gate: stint starts 1878; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Queensland'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1878-1890
- [PASS] position_sim: best 100 vs bar 60: 'Postmaster-general' ~ 'Postmaster-General'
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

