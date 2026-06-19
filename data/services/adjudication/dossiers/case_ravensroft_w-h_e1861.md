<!-- {"case_id": "case_ravensroft_w-h_e1861", "bio_ids": ["ravensroft_w-h_e1861"], "stint_ids": ["Ravenscroft, W. H___Ceylon___1878"]} -->
# Dossier case_ravensroft_w-h_e1861

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- Phase 1 found `ravensroft_w-h_e1861` ↔ `Ravenscroft, W. H___Ceylon___1878` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Ravenscroft, W. H___Ceylon___1878` is also gate-compatible with biography(ies) outside this case: ['ravenscroft_w-h_e1861'] (already linked elsewhere or filtered).

## Biography `ravensroft_w-h_e1861`

- Printed name: **RAVENSROFT, W. H.**
- Birth year: not printed
- Appears in editions: [1883, 1888]

### Verbatim printed entry text (OCR)

**Version `col1883-L29201.v` — printed in editions [1883]:**

> RAVENSROFT, W. H.—Joined Her Majesty's Commissariat in April, 1861; served in England and Ireland, the West Indies, and Canada; accompanied Sir Garnet Wolseley, to the Gold Coast in September, 1878, and served throughout the Ashanti war of 1878-4, including the battles of Amoafu, and capture of Coomassie; mentioned in despatches, promoted, medal and clasp; in May, 1876, obtained leave without pay for two years to proceed to Griqualand West, on special service under the Colonial Office; served as auditor-general, Griqualand West, from 6 June, 1876, and also as acting colonial secretary, from 20 Nov., 1876, to 22 May, 1877; appointed on 28 May, 1877, auditor-general, accountant-general, and controller of revenue of Ceylon; acted as colonial secretary in conjunction with his own duties, from 1 Feb. to 25 Aug., 1878, and again from 7 March to 20 July, 1879; and as colonial secretary alone, from 28 Feb. to 11 Sept., 1881.

**Version `col1888-L35648.v` — printed in editions [1888]:**

> RAVENSROFT, W. H.—Joined Her Majesty's commissariat in April, 1861; served in England and Ireland, the West Indies, and Canada; and served throughout the Ashanti war of 1873-4, including the battles of Amoatful, and capture of Coomassie; mentioned in despatches; promoted, medal and clasp; in May, 1876, proceeded to Griqualand West, on special service under the colonial office; served as auditor-general, Griqualand West, from 6 June, 1876, and also as acting colonial secretary, from 20 Nov., 1876, to 22 May, 1877; 23 May, 1877, auditor-general, accountant-general, and controller of revenue of Ceylon; acted as colonial secretary on several occasions.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1861 | Her Majesty's Commissariat | — | [1883, 1888] |
| 1 | 1873–1874 | — | Gold Coast | [1883] |
| 2 | 1873–1874 | — | — | [1888] |
| 3 | 1876–1878 | special service | Griqualand West | [1883, 1888] |
| 4 | 1876–1877 | acting colonial secretary | — | [1888] |
| 5 | 1877 | auditor-general, accountant-general, and controller of revenue | Ceylon | [1883, 1888] |
| 6 | 1878–1878 | colonial secretary | Ceylon | [1883] |
| 7 | 1879–1879 | colonial secretary | Ceylon | [1883] |
| 8 | 1881–1881 | colonial secretary alone | Ceylon | [1883] |

## Candidate stint `Ravenscroft, W. H___Ceylon___1878`

- Staff-list name: **Ravenscroft, W. H** | colony: **Ceylon** | listed 1878–1890 | editions [1878, 1879, 1880, 1883, 1886, 1888, 1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1878 | W. H. Ravenscroft | Auditor-General | Audit Office | — | — |
| 1879 | W. H. Ravenscroft | Auditor-General | Audit Office | — | — |
| 1880 | W. H. Ravenscroft | Auditor-General | Audit Office | — | — |
| 1883 | W. H. Ravenscroft | Auditor-General | Audit Office | — | — |
| 1886 | W. H. Ravenscroft | Auditor-General | Audit Office | — | — |
| 1888 | W. H. Ravenscroft | Auditor-General | Executive Council | — | — |
| 1888 | W. H. Ravenscroft | Auditor-General | Civil Establishment | — | — |
| 1889 | W. H. Ravenscroft | Auditor-General | Civil Establishment | C.M.G. | — |
| 1890 | W. H. Ravenscroft | Auditor-General | Civil Establishment | C.M.G. | — |

### Deterministic checks: `ravensroft_w-h_e1861` vs `Ravenscroft, W. H___Ceylon___1878`

- [PASS] surname_gate: bio 'RAVENSROFT' vs stint 'Ravenscroft, W. H' (fuzzy:1)
- [PASS] initials: bio ['W', 'H'] ~ stint ['W', 'H']
- [PASS] age_gate: stint starts 1878; no printed birth year — UNCHECKED
- [PASS] colony: 4 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 4 event tenure(s) overlap stint years 1878-1890
- [PASS] position_sim: best 100 vs bar 60: 'auditor-general, accountant-general, and controller of revenue' ~ 'Auditor-General'
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

