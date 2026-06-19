<!-- {"case_id": "calib_gemini_jamaica_0150", "bio_ids": ["mossey_charles-benjamin_e1866"], "stint_ids": ["Mosse, C. B___Jamaica___1878"]} -->
# Dossier calib_gemini_jamaica_0150

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mossey_charles-benjamin_e1866`

- Printed name: **MOSSEY, CHARLES BENJAMIN**
- Birth year: not printed
- Honours: C.B. (1874)
- Terminal: retired 1892 — “retired 1892.”
- Appears in editions: [1897]

### Verbatim printed entry text (OCR)

**Version `col1897-L33482.v` — printed in editions [1897]:**

> MOSSEY, CHARLES BENJAMIN, C.B. (1874), L.R.C.P., M.R.C.S., L.R. and Q.C., Ph.D., M.R.Z.S., Deputy Surgeon-General, A.M.D., served in medical charge of expeditionary force to the river Gambia, West Africa, June, 1866; present at the assault and capture of the stockaded village town of Tubarlong (mentioned in despatches); staff surgeon (1867) for "valuable services" during epidemic of yellow fever at Freetown; held the acting appointments of surgeon's advocate (member of council), chief magistrate, colonial surgeon, and inspector of prisons, when serving at Gambia and on the Gold Coast; served throughout the Ashantee war, 1873-74; present at the action of Essaman, at the battles of Amoafu and Ordahsu, and capture of Coomassie (mentioned in despatches, C.B., and medal with clasp); superintending medical officer for Jamaica, June, 1876; retired 1892.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1866–1866 | medical charge of expeditionary force | Gambia | [1897] |
| 1 | 1867–1867 | staff surgeon | — | [1897] |
| 2 | 1873–1874 | — | — | [1897] |
| 3 | 1876 | superintending medical officer | Jamaica | [1897] |

## Candidate stint `Mosse, C. B___Jamaica___1878`

- Staff-list name: **Mosse, C. B** | colony: **Jamaica** | listed 1878–1890 | editions [1878, 1879, 1880, 1883, 1886, 1888, 1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1878 | C. B. Mosse | Superintending Medical Officer, Deputy Surgeon-General | Medical Department | C.B. | — |
| 1879 | C. B. Mosse | Superintending Medical Officer, Deputy Surgeon-General | Medical Department | C.B. | — |
| 1880 | C. B. Mosse | Chief Medical Officer and Director | Public Hospital | C.B. | — |
| 1880 | C. B. Mosse | Superintending Medical Officer, Deputy Surgeon-General | Medical Department | C.B. | — |
| 1883 | C. B. Mosse | Chief Medical Officer and Director | Public Hospital | C.B. | — |
| 1883 | C. B. Mosse | Superintending Medical Officer, Deputy Surgeon-General | Medical Department | C.B. | — |
| 1886 | C. B. Mosse | Superintending Medical Officer | Legislative Council | C.B. | Deputy Surgeon-General |
| 1888 | C. B. Mosse | Deputy Surgeon-General; Superintendent Medical Officer | Legislative Council | C.B. | — |
| 1889 | C. B. Mosse | Deputy Surgeon-General, Superintendent Medical Officer | Legislative Council | C.B. | — |
| 1889 | C. B. Mosse | Superintendent Medical Officer, Deputy Surgeon-General | Medical Department | C.B. | — |
| 1890 | C. B. Mosse | Deputy Surgeon-General; Superintending Medical Officer | Legislative Council | C.B. | — |
| 1890 | C. B. Mosse | Superintending Medical Officer, Deputy Surgeon-General | Medical Department | C.B. | — |

### Deterministic checks: `mossey_charles-benjamin_e1866` vs `Mosse, C. B___Jamaica___1878`

- [PASS] surname_gate: bio 'MOSSEY' vs stint 'Mosse, C. B' (fuzzy:1)
- [PASS] initials: bio ['C', 'B'] ~ stint ['C', 'B']
- [PASS] age_gate: stint starts 1878; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Jamaica'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1878-1890
- [PASS] position_sim: best 100 vs bar 60: 'superintending medical officer' ~ 'Superintending Medical Officer, Deputy Surgeon-General'
- [PASS] honour: shared: C.B.
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

