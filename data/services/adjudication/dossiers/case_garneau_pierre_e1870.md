<!-- {"case_id": "case_garneau_pierre_e1870", "bio_ids": ["garneau_pierre_e1870"], "stint_ids": ["Garneau, P___Canada___1877", "Garneau, P___Canada___1898"]} -->
# Dossier case_garneau_pierre_e1870

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['garneau_pierre_e1870'] carry a single initial only — the namesake trap applies.

## Biography `garneau_pierre_e1870`

- Printed name: **GARNEAU, PIERRE**
- Birth year: not printed
- Appears in editions: [1890, 1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909]

### Verbatim printed entry text (OCR)

**Version `col1890-L34138.v` — printed in editions [1890, 1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909]:**

> GARNEAU, PIERRE.—Merchant and member of board of trade, Quebec; late gvt. director of North Shore Railway; Mayor, 1870-73; M.L.A., Quebec, 1873-78 and 1881-86; member of provincial ex. council and ministry as commr. of agric., pub. wks. and crown lands, 1874-78; M.L.C., Quebec, 1887, and again commr. of agric., pub. wks. and crown lands to 1891.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1870–1873 | Mayor | — | [1890, 1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909] |
| 1 | 1873–1878 | M.L.A. | Quebec | [1890, 1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909] |
| 2 | 1874–1878 | member of provincial ex. council and ministry as commr. of agric., pub. wks. and crown lands | — | [1890, 1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909] |
| 3 | 1881–1886 | M.L.A. | Quebec | [1890, 1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909] |
| 4 | 1887–1887 | M.L.C. | Quebec | [1890, 1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909] |
| 5 | ?–1891 | commr. of agric., pub. wks. and crown lands | — | [1890, 1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909] |

## Candidate stint `Garneau, P___Canada___1877`

- Staff-list name: **Garneau, P** | colony: **Canada** | listed 1877–1878 | editions [1877, 1878]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | P. Garneau | Commissioner of Crown Lands | Executive Council | — | — |
| 1878 | P. Garneau | Commissioner of Crown Lands | EXECUTIVE COUNCIL | — | — |

### Deterministic checks: `garneau_pierre_e1870` vs `Garneau, P___Canada___1877`

- [PASS] surname_gate: bio 'GARNEAU' vs stint 'Garneau, P' (exact)
- [PASS] initials: bio ['P'] ~ stint ['P']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1878
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Garneau, P___Canada___1898`

- Staff-list name: **Garneau, P** | colony: **Canada** | listed 1898–1899 | editions [1898, 1899]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1898 | P. Garneau | Member | Legislative Council | — | — |
| 1899 | P Garneau | — | Members | — | — |
| 1899 | Garneau | — | Members | — | — |

### Deterministic checks: `garneau_pierre_e1870` vs `Garneau, P___Canada___1898`

- [PASS] surname_gate: bio 'GARNEAU' vs stint 'Garneau, P' (exact)
- [PASS] initials: bio ['P'] ~ stint ['P']
- [PASS] age_gate: stint starts 1898; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1898-1899
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

