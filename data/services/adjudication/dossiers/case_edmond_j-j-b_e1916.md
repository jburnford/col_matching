<!-- {"case_id": "case_edmond_j-j-b_e1916", "bio_ids": ["edmond_j-j-b_e1916"], "stint_ids": ["Edmond, Jacques___Mauritius___1877", "Edmond___Trinidad___1877"]} -->
# Dossier case_edmond_j-j-b_e1916

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `edmond_j-j-b_e1916`

- Printed name: **EDMOND, J. J. B**
- Birth year: not printed
- Honours: M.B, M.C
- Appears in editions: [1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933]

### Verbatim printed entry text (OCR)

**Version `col1924-L53996.v` — printed in editions [1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933]:**

> EDMOND, J. J. B., M.C., M.B., C.H.R. (Edin.).—R.A.M.C., July, 1916 to Aug., 1919; med. offr., Trans-Zambesia Rly. constrn., Portuguese E. Africa, July, 1920 to Dec., 1921; med. offr., Tanganyika Territory, 30th June, 1922.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1916–1919 | R.A.M.C | — | [1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933] |
| 1 | 1920–1921 | med. offr., Trans-Zambesia Rly. constrn., Portuguese E. Africa | — | [1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933] |
| 2 | 1922 | med. offr., Tanganyika Territory | Tanganyika | [1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933] |

## Candidate stint `Edmond, Jacques___Mauritius___1877`

- Staff-list name: **Edmond, Jacques** | colony: **Mauritius** | listed 1877–1879 | editions [1877, 1879]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | Jacques Edmond | Dispenser, Public Hospital | Medical Department | — | — |
| 1879 | Jacques Edmond | Tide Waiter | Revenue Department | — | — |

### Deterministic checks: `edmond_j-j-b_e1916` vs `Edmond, Jacques___Mauritius___1877`

- [PASS] surname_gate: bio 'EDMOND' vs stint 'Edmond, Jacques' (exact)
- [PASS] initials: bio ['J', 'J', 'B'] ~ stint ['J']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Mauritius'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1879
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Edmond___Trinidad___1877`

- Staff-list name: **Edmond** | colony: **Trinidad** | listed 1877–1878 | editions [1877, 1878]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | Edmond | Professor | College of the Immaculate Conception | — | — |
| 1878 | Edmond | — | College of the Immaculate Conception | — | — |

### Deterministic checks: `edmond_j-j-b_e1916` vs `Edmond___Trinidad___1877`

- [PASS] surname_gate: bio 'EDMOND' vs stint 'Edmond' (exact)
- [PASS] initials: bio ['J', 'J', 'B'] ~ stint ['?']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Trinidad'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1878
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

