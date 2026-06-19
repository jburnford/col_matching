<!-- {"case_id": "case_brownlee_charles_e1846-2", "bio_ids": ["brownlee_charles_e1846-2"], "stint_ids": ["Brownlee, C___Cape of Good Hope___1877"]} -->
# Dossier case_brownlee_charles_e1846-2

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['brownlee_charles_e1846-2'] carry a single initial only — the namesake trap applies.

## Biography `brownlee_charles_e1846-2`

- Printed name: **BROWNLEE, CHARLES**
- Birth year: not printed
- Honours: C.M.G. (1883)
- Terminal: retired 1884 — “retired on pension equal to full pay, 1884, by unanimous resolution of both houses of parliament, in consideration of important services.”
- Appears in editions: [1890]

### Verbatim printed entry text (OCR)

**Version `col1890-L32890.v` — printed in editions [1890]:**

> BROWNLEE, CHARLES, C.M.G. (1883).—Entered Cape govt. service, 1846; Gaika commissioner, 1848; served on personal staff of Sir H. Smith in war of 1851, and was wounded; comm. native contingent, 1852, under Sir G. Cathcart; keeping open communications; entrusted with negotiations for peace, 1863, receiving thanks of govt.; acted as first minister of native affairs on introduction of responsible govt. in 1873, retired 1878, and was appointed to chief magistracy in East Griqualand; raised force in 1880 for defence of East Griqualand; retired on pension equal to full pay, 1884, by unanimous resolution of both houses of parliament, in consideration of important services.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1846 | govt. service | Cape Colony | [1890] |
| 1 | 1848 | Gaika commissioner | — | [1890] |
| 2 | 1851 | personal staff | — | [1890] |
| 3 | 1852 | comm. native contingent | — | [1890] |
| 4 | 1863 | — | — | [1890] |
| 5 | 1873–1878 | first minister of native affairs | East Griqualand | [1890] |
| 6 | 1880 | — | East Griqualand | [1890] |

## Candidate stint `Brownlee, C___Cape of Good Hope___1877`

- Staff-list name: **Brownlee, C** | colony: **Cape of Good Hope** | listed 1877–1879 | editions [1877, 1879]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | C. Brownlee | Secretary | Department of Native Affairs | — | — |
| 1879 | Hon. C. Brownlee | Resident Commissioner | Resident Commissioner for Native Affairs Department | — | — |

### Deterministic checks: `brownlee_charles_e1846-2` vs `Brownlee, C___Cape of Good Hope___1877`

- [PASS] surname_gate: bio 'BROWNLEE' vs stint 'Brownlee, C' (exact)
- [PASS] initials: bio ['C'] ~ stint ['C']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Cape of Good Hope'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1879
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

