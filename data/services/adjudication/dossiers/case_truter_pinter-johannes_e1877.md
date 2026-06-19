<!-- {"case_id": "case_truter_pinter-johannes_e1877", "bio_ids": ["truter_pinter-johannes_e1877"], "stint_ids": ["Truter, P. J. F___Cape of Good Hope___1877"]} -->
# Dossier case_truter_pinter-johannes_e1877

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `truter_pinter-johannes_e1877`

- Printed name: **TRUTER, PINTER JOHANNES**
- Birth year: not printed
- Terminal: died 1888 — “died 1888.”
- Appears in editions: [1888, 1889]

### Verbatim printed entry text (OCR)

**Version `col1888-L36446.v` — printed in editions [1888, 1889]:**

> TRUTER, PINTER JOHANNES.—2nd clerk to R.M., Malmesbury, Oct., 1878; clerk to C.C. and R.M., Namaqualand, Jan., 1877; ditto, Bredasdorp, Mar., 1878; temporarily attached to officer at East London, Oct., 1878, to Feb., 1879 (on special service); chief clerk, East London, Mar., 1880; 1st clerk, native affairs office, June, 1881; chief clerk Aliwal North, April, 1882, and at East London, June, 1882; resigned, 1st Aug., 1882; re-appointed clerk, special court, Kimberley, June, 1883; 2nd clerk to crown prosecutor, Kimberley, Sept., 1883; C.C. and R.M., Vrijburg, British Bechuanaland, April, 1886; died 1888.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1877–1877 | clerk to C.C. and R.M. | — | [1888, 1889] |
| 1 | 1878–1878 | 2nd clerk to R.M. | — | [1888, 1889] |
| 2 | 1878–1879 | temporarily attached to officer | — | [1888, 1889] |
| 3 | 1880–1880 | chief clerk | — | [1888, 1889] |
| 4 | 1881–1881 | 1st clerk | — | [1888, 1889] |
| 5 | 1882–1882 | chief clerk | — | [1888, 1889] |
| 6 | 1882–1882 | — | — | [1888, 1889] |
| 7 | 1883–1883 | clerk, special court | — | [1888, 1889] |
| 8 | 1883–1883 | 2nd clerk to crown prosecutor | — | [1888, 1889] |
| 9 | 1886–1886 | C.C. and R.M. | British Bechuanaland | [1888, 1889] |

## Candidate stint `Truter, P. J. F___Cape of Good Hope___1877`

- Staff-list name: **Truter, P. J. F** | colony: **Cape of Good Hope** | listed 1877–1880 | editions [1877, 1878, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | P. J. Truter | Clerk | Police Branch | — | — |
| 1878 | P. J. Truter | Clerk | Division of Namaqualand | — | — |
| 1880 | P. Truter | Clerk | DIVISION OF BREDASDORP | — | — |

### Deterministic checks: `truter_pinter-johannes_e1877` vs `Truter, P. J. F___Cape of Good Hope___1877`

- [PASS] surname_gate: bio 'TRUTER' vs stint 'Truter, P. J. F' (exact)
- [PASS] initials: bio ['P', 'J'] ~ stint ['P', 'J', 'F']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Cape of Good Hope'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1880
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

