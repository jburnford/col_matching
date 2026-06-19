<!-- {"case_id": "case_strawbridge_william_e1862", "bio_ids": ["strawbridge_william_e1862"], "stint_ids": ["Strawbridge, W___South Australia___1877", "Strawbridge, W___South Australia___1888"]} -->
# Dossier case_strawbridge_william_e1862

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['strawbridge_william_e1862'] carry a single initial only — the namesake trap applies.

## Biography `strawbridge_william_e1862`

- Printed name: **STRAWBRIDGE, WILLIAM**
- Birth year: not printed
- Appears in editions: [1894, 1896, 1897]

### Verbatim printed entry text (OCR)

**Version `col1894-L34139.v` — printed in editions [1894, 1896, 1897]:**

> STRAWBRIDGE, WILLIAM.—Entd. survey and crown lds. dept., S. Australia, as cadet, June, 1862, after several promotions was apptd. examiner of licensed surveyor's work and ditsman., June, 1872; and chief ditsman., Ap. 1877; dept. surveyor-general, July, 1885.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1862 | cadet | South Australia | [1894, 1896, 1897] |
| 1 | 1872 | examiner of licensed surveyor's work and ditsman. | — | [1894, 1896, 1897] |
| 2 | 1877 | chief ditsman. | — | [1894, 1896, 1897] |
| 3 | 1885 | dept. surveyor-general | — | [1894, 1896, 1897] |

## Candidate stint `Strawbridge, W___South Australia___1877`

- Staff-list name: **Strawbridge, W** | colony: **South Australia** | listed 1877–1880 | editions [1877, 1878, 1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | W. Strawbridge | Draftsmen | Survey Department | — | — |
| 1878 | W. Strawbridge | Chief Draughtsman | Survey Department | — | — |
| 1879 | W. Strawbridge | Chief Draughtsman | Survey Department | — | — |
| 1880 | W. Strawbridge | Chief Draughtsman | Survey Department | — | — |

### Deterministic checks: `strawbridge_william_e1862` vs `Strawbridge, W___South Australia___1877`

- [PASS] surname_gate: bio 'STRAWBRIDGE' vs stint 'Strawbridge, W' (exact)
- [PASS] initials: bio ['W'] ~ stint ['W']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'South Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1880
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Strawbridge, W___South Australia___1888`

- Staff-list name: **Strawbridge, W** | colony: **South Australia** | listed 1888–1909 | editions [1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | W. Strawbridge | Deputy Surveyor-General | Survey Department | — | — |
| 1889 | W. Strawbridge | Deputy Surveyor-General | Survey Department | — | — |
| 1890 | W. Strawbridge | Deputy Surveyor-General | Survey Department | — | — |
| 1894 | W. Strawbridge | Deputy Surveyor-General | Survey Department | — | — |
| 1896 | W. Strawbridge | Surveyor-General | Survey Department | — | — |
| 1897 | W. Strawbridge | Surveyor-General | Survey Department | — | — |
| 1898 | W. Strawbridge | Surveyor-General | Survey Department | — | — |
| 1899 | W. Strawbridge | Surveyor-General | Survey Department | — | — |
| 1900 | W. Strawbridge | Surveyor-General | Survey Department | — | — |
| 1905 | W. Strawbridge | Surveyor-General | Survey Department | — | — |
| 1906 | W. Strawbridge | Surveyor-General | Survey Department | — | — |
| 1907 | W. Strawbridge | Surveyor-General | Survey Department | — | — |
| 1908 | W. Strawbridge | Surveyor-General | Survey Department | — | — |
| 1909 | W. Strawbridge | Surveyor-General | Survey Department | — | — |

### Deterministic checks: `strawbridge_william_e1862` vs `Strawbridge, W___South Australia___1888`

- [PASS] surname_gate: bio 'STRAWBRIDGE' vs stint 'Strawbridge, W' (exact)
- [PASS] initials: bio ['W'] ~ stint ['W']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'South Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1888-1909
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

