<!-- {"case_id": "case_rees_sr-josiah_e1851", "bio_ids": ["rees_sr-josiah_e1851"], "stint_ids": ["Rees, Josiah___Bermuda___1879"]} -->
# Dossier case_rees_sr-josiah_e1851

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 15 official(s) with this surname in the graph's staff lists; 17 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- Phase 1 found `rees_sr-josiah_e1851` ↔ `Rees, Josiah___Bermuda___1879` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Rees, Josiah___Bermuda___1879` is also gate-compatible with biography(ies) outside this case: ['rees_josiah_e1851'] (already linked elsewhere or filtered).

## Biography `rees_sr-josiah_e1851`

- Printed name: **REES, SR JOSIAH**
- Birth year: not printed
- Honours: F.R.A.S, KT (1891)
- Appears in editions: [1898]

### Verbatim printed entry text (OCR)

**Version `col1898-L35553.v` — printed in editions [1898]:**

> REES, SR JOSIAH, KT.(1891), F.R.A.S.—Called to the bar, Mid. Tem., Nov., 1851; went the S. Wales and Chester circuit; was a revising barrister on that circuit from 1865 to 1877; ch. just., Bermuda, 1878; judge of the V.-A. ct., and pres. of the colln.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1851 | Called to the bar, Mid. Tem | — | [1898] |
| 1 | 1865–1877 | was a revising barrister on that circuit from | — | [1898] |
| 2 | 1878 | ch. just. | Bermuda | [1898] |

## Candidate stint `Rees, Josiah___Bermuda___1879`

- Staff-list name: **Rees, Josiah** | colony: **Bermuda** | listed 1879–1900 | editions [1879, 1880, 1883, 1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1879 | Josiah Rees | Chief Justice (and Judge of Vice-Admiralty Court) | Judicial Establishment | — | — |
| 1880 | Josiah Rees | Chief Justice (and Judge of Vice-Admiralty Court) | Judicial Establishment | — | — |
| 1883 | Josiah Rees | Chief Justice (and Judge of Vice-Admiralty Court) | Judicial Establishment | — | — |
| 1888 | Josiah Rees | Chief Justice (and Judge of Vice-Admiralty Court) | Judicial Establishment | — | — |
| 1889 | Josiah Rees | Chief Justice (and Judge of Vice-Admiralty Court) | Judicial Establishment | — | — |
| 1890 | Josiah Rees | Chief Justice (and Judge of Vice-Admiralty Court) | Judicial Establishment | — | — |
| 1894 | Sir Josiah Rees | Chief Justice (and Judge of Vice-Admiralty Court) | Judicial Establishment | — | — |
| 1896 | Sir Josiah Rees | Chief Justice (and Judge of Vice-Admiralty Court) | Judicial Establishment | — | — |
| 1897 | Sir Josiah Rees | Chief Justice (and Judge of Vice-Admiralty Court) | Judicial Establishment | — | — |
| 1898 | Sir Josiah Rees, Kt. | Chief Justice (and Judge of Vice-Admiralty Court) | Judicial Establishment | — | — |
| 1899 | Sir Josiah Rees | Chief Justice | Judicial Establishment | — | — |
| 1900 | Sir Josiah Rees | Chief Justice | Judicial Establishment | — | — |

### Deterministic checks: `rees_sr-josiah_e1851` vs `Rees, Josiah___Bermuda___1879`

- [PASS] surname_gate: bio 'REES' vs stint 'Rees, Josiah' (exact)
- [PASS] initials: bio ['S', 'J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1879; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Bermuda'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1879-1900
- [PASS] position_sim: best 70 vs bar 60: 'ch. just.' ~ 'Chief Justice'
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

