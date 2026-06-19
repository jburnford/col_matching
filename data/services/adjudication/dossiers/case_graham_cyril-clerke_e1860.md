<!-- {"case_id": "case_graham_cyril-clerke_e1860", "bio_ids": ["graham_cyril-clerke_e1860"], "stint_ids": ["Graham, C. C___New Zealand___1900", "Graham, C. C___Windward Islands___1877"]} -->
# Dossier case_graham_cyril-clerke_e1860

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 89 official(s) with this surname in the graph's staff lists; 31 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `graham_cyril-clerke_e1860`

- Printed name: **GRAHAM, CYRIL CLERKE**
- Birth year: not printed
- Honours: C.M.G. (1877)
- Appears in editions: [1883, 1886, 1888, 1889, 1890, 1894]

### Verbatim printed entry text (OCR)

**Version `col1883-L27720.v` — printed in editions [1883, 1886, 1888, 1889, 1890, 1894]:**

> GRAHAM, CYRIL CLERKE, C.M.G. (1877).—Was honorarily attached to Lord Dufferin, British commissioner in Syria, from September 10, 1860, till June, 1861; private secretary to the Earl of Carnarvon, secretary of state for the colonies, 6th July, 1866, to 9th March, 1867; lieutenant-governor, Grenada, 1875, to September, 1877.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1860–1861 | honorarily attached to Lord Dufferin, British commissioner | Syria | [1883, 1886, 1888, 1889, 1890, 1894] |
| 1 | 1866–1867 | private secretary to the Earl of Carnarvon, secretary of state for the colonies | — | [1883, 1886, 1888, 1889, 1890, 1894] |
| 2 | 1875–1877 | lieutenant-governor | Grenada | [1883, 1886, 1888, 1889, 1890, 1894] |

## Candidate stint `Graham, C. C___New Zealand___1900`

- Staff-list name: **Graham, C. C** | colony: **New Zealand** | listed 1900–1909 | editions [1900, 1905, 1906, 1907, 1908, 1909]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1900 | C. C. Graham | Stipendiary Magistrate | Judicial | — | — |
| 1905 | C. C. Graham | Stipendiary Magistrate | Judicial | — | — |
| 1906 | C. C. Graham | Stipendiary Magistrate | Judicial | — | — |
| 1907 | C. C. Graham | Stipendiary Magistrate | Judicial | — | — |
| 1908 | C. C. Graham | Stipendiary Magistrate | Judicial | — | — |
| 1909 | C. C. Graham | Stipendiary Magistrate | Judicial | — | — |

### Deterministic checks: `graham_cyril-clerke_e1860` vs `Graham, C. C___New Zealand___1900`

- [PASS] surname_gate: bio 'GRAHAM' vs stint 'Graham, C. C' (exact)
- [PASS] initials: bio ['C', 'C'] ~ stint ['C', 'C']
- [PASS] age_gate: stint starts 1900; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'New Zealand'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1900-1909
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Graham, C. C___Windward Islands___1877`

- Staff-list name: **Graham, C. C** | colony: **Windward Islands** | listed 1877–1889 | editions [1877, 1878, 1880, 1883, 1889]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | C. C. Graham | — | Governors | — | — |
| 1878 | C. C. Graham | — | Governors | — | — |
| 1880 | C. C. Graham | — | Governors | — | — |
| 1883 | C. C. Graham | — | Governors | — | — |

### Deterministic checks: `graham_cyril-clerke_e1860` vs `Graham, C. C___Windward Islands___1877`

- [PASS] surname_gate: bio 'GRAHAM' vs stint 'Graham, C. C' (exact)
- [PASS] initials: bio ['C', 'C'] ~ stint ['C', 'C']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Windward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1889
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

