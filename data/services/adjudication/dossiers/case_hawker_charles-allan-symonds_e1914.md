<!-- {"case_id": "case_hawker_charles-allan-symonds_e1914", "bio_ids": ["hawker_charles-allan-symonds_e1914"], "stint_ids": ["Hawker, A___Australia___1912", "Hawker, A___South Australia___1907", "Hawker, C. A___Cape of Good Hope___1905"]} -->
# Dossier case_hawker_charles-allan-symonds_e1914

## Case context

- 1 biography(ies) and 3 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hawker_charles-allan-symonds_e1914`

- Printed name: **HAWKER, Charles Allan Symonds**
- Birth year: not printed
- Terminal: resigned 1932 — “resigned, Oct., 1932.”
- Appears in editions: [1932, 1933, 1934, 1935, 1936, 1937]

### Verbatim printed entry text (OCR)

**Version `col1932-L60972.v` — printed in editions [1932, 1933, 1934, 1935, 1936, 1937]:**

> HAWKER, Charles Allan Symonds—Served European War 1914-17 (wounded); M.H.R., Commonwealth of Australia, 1929; min. for markets and repatriation, Lyons' ministry, 1931; resigned, Oct., 1932.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914–1917 | Served European War | — | [1932, 1933, 1934, 1935, 1936, 1937] |
| 1 | 1929 | M.H.R. | Commonwealth of Australia | [1932, 1933, 1934, 1935, 1936, 1937] |
| 2 | 1931 | min. for markets and repatriation, Lyons' ministry | Commonwealth of Australia *(inherited from previous clause)* | [1932, 1933, 1934, 1935, 1936, 1937] |

## Candidate stint `Hawker, A___Australia___1912`

- Staff-list name: **Hawker, A** | colony: **Australia** | listed 1912–1918 | editions [1912, 1913, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | A. Hawker | Sub-Oversers | Printing Department | — | — |
| 1913 | A. Hawker | Sub-Overseers | Printing Department | — | — |
| 1918 | A. Hawker | Sub-Overseers | Printing Department | — | — |

### Deterministic checks: `hawker_charles-allan-symonds_e1914` vs `Hawker, A___Australia___1912`

- [PASS] surname_gate: bio 'HAWKER' vs stint 'Hawker, A' (exact)
- [PASS] initials: bio ['C', 'A', 'S'] ~ stint ['A']
- [PASS] age_gate: stint starts 1912; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1918
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Hawker, A___South Australia___1907`

- Staff-list name: **Hawker, A** | colony: **South Australia** | listed 1907–1917 | editions [1907, 1908, 1909, 1917]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1907 | A. Hawker | Sub-Overseers | Printing Department | — | — |
| 1908 | A. Hawker | Sub-Overseers | Printing Department | — | — |
| 1909 | A. Hawker | Sub-Overseers | Printing Department | — | — |
| 1917 | A. Hawker | Sub-Overseers | Printing Department | — | — |

### Deterministic checks: `hawker_charles-allan-symonds_e1914` vs `Hawker, A___South Australia___1907`

- [PASS] surname_gate: bio 'HAWKER' vs stint 'Hawker, A' (exact)
- [PASS] initials: bio ['C', 'A', 'S'] ~ stint ['A']
- [PASS] age_gate: stint starts 1907; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'South Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1907-1917
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Hawker, C. A___Cape of Good Hope___1905`

- Staff-list name: **Hawker, C. A** | colony: **Cape of Good Hope** | listed 1905–1907 | editions [1905, 1906, 1907]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | C. Hawker | General Assistant | Field Establishment | — | — |
| 1906 | C. A. Hawker | General and Field Assistants | Field Establishment | — | — |
| 1907 | C. A. Hawker | Field Assistant | Field Establishment | — | — |

### Deterministic checks: `hawker_charles-allan-symonds_e1914` vs `Hawker, C. A___Cape of Good Hope___1905`

- [PASS] surname_gate: bio 'HAWKER' vs stint 'Hawker, C. A' (exact)
- [PASS] initials: bio ['C', 'A', 'S'] ~ stint ['C', 'A']
- [PASS] age_gate: stint starts 1905; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Cape of Good Hope'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1907
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

