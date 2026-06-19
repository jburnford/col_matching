<!-- {"case_id": "case_atherton_e-n_e1852", "bio_ids": ["atherton_e-n_e1852"], "stint_ids": ["Atherton, E. N___Ceylon___1877"]} -->
# Dossier case_atherton_e-n_e1852

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `atherton_e-n_e1852`

- Printed name: **ATHERTON, E. N.**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L26254.v` — printed in editions [1883]:**

> ATHERTON, E. N.—Appointed a writer in Ceylon, 1852; assistant government agent and police magistrate of Mullaitivu, 1853; acting assistant government agent, commissioner of requests and police magistrate of Regalla, from 1854 to 1858; assistant agent at Kurunegala, 1861; district judge commissioner of requests and police magistrate, Tangalla, 1862; ditto at Galle, June, 1864; assistant government agent at Puttalam, October, 1865; assistant government agent and district judge, &c., at Mannar, 1868; landing surveyor, Colombo, 1870; acting assistant government agent, Ratnapura, March, 1872, confirmed, Oct., 1873; acting district judge, Batticaloa, 1876.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1852 | writer | Ceylon | [1883] |
| 1 | 1853 | assistant government agent and police magistrate | Mullaitivu | [1883] |
| 2 | 1854–1858 | acting assistant government agent, commissioner of requests and police magistrate | Regalla | [1883] |
| 3 | 1861 | assistant agent | Kurunegala | [1883] |
| 4 | 1862 | district judge commissioner of requests and police magistrate | Tangalla | [1883] |
| 5 | 1864 | district judge commissioner of requests and police magistrate | Galle | [1883] |
| 6 | 1865 | assistant government agent | Puttalam | [1883] |
| 7 | 1868 | assistant government agent and district judge, &c. | Mannar | [1883] |
| 8 | 1870 | landing surveyor | Colombo | [1883] |
| 9 | 1872–1873 | acting assistant government agent | Ratnapura | [1883] |
| 10 | 1876 | acting district judge | Batticaloa | [1883] |

## Candidate stint `Atherton, E. N___Ceylon___1877`

- Staff-list name: **Atherton, E. N** | colony: **Ceylon** | listed 1877–1880 | editions [1877, 1878, 1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | E. N. Atherton | Assistant Government Agent | Government Agencies | — | — |
| 1878 | E. N. Atherton | Assistant Government Agent | Government Agencies | — | — |
| 1879 | E. N. Atherton | Assistant Government Agent | Government Agencies | — | — |
| 1880 | E. N. Atherton | Assistant Government Agent | Government Agencies | — | — |

### Deterministic checks: `atherton_e-n_e1852` vs `Atherton, E. N___Ceylon___1877`

- [PASS] surname_gate: bio 'ATHERTON' vs stint 'Atherton, E. N' (exact)
- [PASS] initials: bio ['E', 'N'] ~ stint ['E', 'N']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Ceylon'
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

