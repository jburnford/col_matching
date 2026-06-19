<!-- {"case_id": "case_wylde_alfred-carrington_e1845", "bio_ids": ["wylde_alfred-carrington_e1845"], "stint_ids": ["Wylde, A. C___Cape of Good Hope___1877"]} -->
# Dossier case_wylde_alfred-carrington_e1845

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `wylde_alfred-carrington_e1845`

- Printed name: **WYLDE, ALFRED CARRINGTON**
- Birth year: not printed
- Appears in editions: [1883, 1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1883-L30077.v` — printed in editions [1883, 1888, 1889, 1890]:**

> WYLDE, ALFRED CARRINGTON.—C. C. and R. M. Port Elizabeth division, Cape Colony, September, 1871; was clerk to the chief justice, 1845 to 1861; clerk of the peace for Port Elizabeth, Nitenhage, &c., 1851 to 1864; C. C. and R. M. Morrel Bay, 1864 to 1869; C. C. and R. M. Swellendam, 1869 to 1871.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1845–1861 | was clerk to the chief justice | Cape of Good Hope *(inherited from previous clause)* | [1883, 1888, 1889, 1890] |
| 1 | 1851–1864 | clerk of the peace for Port Elizabeth, Nitenhage, &c | Cape of Good Hope *(inherited from previous clause)* | [1883, 1888, 1889, 1890] |
| 2 | 1864–1869 | C. C. and R. M. Morrel Bay | Cape of Good Hope *(inherited from previous clause)* | [1883, 1888, 1889, 1890] |
| 3 | 1869–1871 | C. C. and R. M. Swellendam | Cape of Good Hope *(inherited from previous clause)* | [1883, 1888, 1889, 1890] |
| 4 | 1871 | C. C. and R. M. Port Elizabeth division | Cape of Good Hope | [1883, 1888, 1889, 1890] |

## Candidate stint `Wylde, A. C___Cape of Good Hope___1877`

- Staff-list name: **Wylde, A. C** | colony: **Cape of Good Hope** | listed 1877–1883 | editions [1877, 1878, 1879, 1880, 1883]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | A. C. Wylde | Surrogate | Vice-Admiralty Court | — | — |
| 1877 | A. C. Wylde | Civil Commissioner and Resident Magistrate | Police Branch | — | — |
| 1878 | A. C. Wylde | Surrogate | Vice-Admiralty Court | — | — |
| 1879 | A. C. Wylde | Surrogate | Vice-Admiralty Court | — | — |
| 1880 | A. C. Wylde | Surrogate | Vice-Admiralty Court | — | — |
| 1883 | A. C. Wylde | — | Vice-Admiralty Court | — | — |

### Deterministic checks: `wylde_alfred-carrington_e1845` vs `Wylde, A. C___Cape of Good Hope___1877`

- [PASS] surname_gate: bio 'WYLDE' vs stint 'Wylde, A. C' (exact)
- [PASS] initials: bio ['A', 'C'] ~ stint ['A', 'C']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 5 placed event(s) resolve to 'Cape of Good Hope'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1883
- [FAIL] position_sim: best 51 vs bar 60: 'C. C. and R. M. Port Elizabeth division' ~ 'Civil Commissioner and Resident Magistrate'
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

