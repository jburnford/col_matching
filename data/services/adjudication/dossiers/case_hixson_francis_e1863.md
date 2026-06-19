<!-- {"case_id": "case_hixson_francis_e1863", "bio_ids": ["hixson_francis_e1863"], "stint_ids": ["Hixson, F___New South Wales___1877", "Hixson, F___New South Wales___1896"]} -->
# Dossier case_hixson_francis_e1863

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['hixson_francis_e1863'] carry a single initial only — the namesake trap applies.

## Biography `hixson_francis_e1863`

- Printed name: **HIXSON, FRANCIS**
- Birth year: not printed
- Appears in editions: [1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908]

### Verbatim printed entry text (OCR)

**Version `col1888-L34033.v` — printed in editions [1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908]:**

> HIXSON, FRANCIS, late Master, R.N.—Served fifteen years on Australian station, principally in surveying and exploring service; superintendent of pilots, lighthouses, and harbours, N.S. Wales, Jan., 1863; organised N. S. W. Naval Bde., 1863, and still commands it; President, marine board, April, 1872.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1863 | superintendent of pilots, lighthouses, and harbours | New South Wales | [1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908] |
| 1 | 1872 | President, marine board | — | [1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908] |

## Candidate stint `Hixson, F___New South Wales___1877`

- Staff-list name: **Hixson, F** | colony: **New South Wales** | listed 1877–1886 | editions [1877, 1878, 1879, 1880, 1886]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | F. Hixson | President | Marine Board | — | — |
| 1878 | F. Hixson | President | Marine Board | — | — |
| 1879 | F. Hixson | President | Marine Board | — | — |
| 1880 | F. Hixson | President | Marine Board | — | — |
| 1886 | F. Hixson | President | Marine Board | — | — |

### Deterministic checks: `hixson_francis_e1863` vs `Hixson, F___New South Wales___1877`

- [PASS] surname_gate: bio 'HIXSON' vs stint 'Hixson, F' (exact)
- [PASS] initials: bio ['F'] ~ stint ['F']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'New South Wales'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1886
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Hixson, F___New South Wales___1896`

- Staff-list name: **Hixson, F** | colony: **New South Wales** | listed 1896–1900 | editions [1896, 1898, 1899, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1896 | F. Hixson | President | Marine Board | — | — |
| 1896 | F. Hixson | Captain Commanding Naval Forces | Naval Defence | — | — |
| 1898 | F. Hixson | Captain Commanding Naval Forces | Naval Defence | — | Captain |
| 1898 | F. Hixson | President | Marine Board | — | — |
| 1899 | F. Hixson | President | Marine Board | — | — |
| 1899 | F. Hixson | Captain Commanding Naval Forces | Naval Defence | — | Captain |
| 1900 | F. Hixson | Captain Commanding Naval Forces | Naval Defence | — | Captain |
| 1900 | F. Hixson | President | Marine Board | — | — |

### Deterministic checks: `hixson_francis_e1863` vs `Hixson, F___New South Wales___1896`

- [PASS] surname_gate: bio 'HIXSON' vs stint 'Hixson, F' (exact)
- [PASS] initials: bio ['F'] ~ stint ['F']
- [PASS] age_gate: stint starts 1896; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'New South Wales'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1896-1900
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

