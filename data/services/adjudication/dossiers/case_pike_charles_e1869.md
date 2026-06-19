<!-- {"case_id": "case_pike_charles_e1869", "bio_ids": ["pike_charles_e1869"], "stint_ids": ["Pike, C___Gold Coast___1889", "Pike, C___Windward Islands___1905"]} -->
# Dossier case_pike_charles_e1869

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 15 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['pike_charles_e1869'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Pike, C___Gold Coast___1889` is also gate-compatible with biography(ies) outside this case: ['pike_x_e1869'] (already linked elsewhere or filtered).
- NOTE: stint `Pike, C___Windward Islands___1905` is also gate-compatible with biography(ies) outside this case: ['pike_x_e1869'] (already linked elsewhere or filtered).

## Biography `pike_charles_e1869`

- Printed name: **PIKE, Charles**
- Birth year: not printed
- Appears in editions: [1883, 1886]

### Verbatim printed entry text (OCR)

**Version `col1883-L29119.v` — printed in editions [1883, 1886]:**

> PIKE, Charles.—Acting second clerk in the treasury, Sierra Leone, August, 1869; chief clerk of customs, Lagos, 1870; acting second clerk and cashier, treasury, 1871; acting deputy collector part of 1872 to 1875; acting assistant collector and treasurer, 1875; confirmed, 5th July, 1876; collector and treasurer of the Gold Coast, 1885.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1869 | Acting second clerk in the treasury | Sierra Leone | [1883, 1886] |
| 1 | 1870 | chief clerk of customs | Lagos | [1883, 1886] |
| 2 | 1871 | acting second clerk and cashier, treasury | Lagos *(inherited from previous clause)* | [1883, 1886] |
| 3 | 1872–1875 | acting deputy collector part of | Lagos *(inherited from previous clause)* | [1883, 1886] |
| 4 | 1875 | acting assistant collector and treasurer | Lagos *(inherited from previous clause)* | [1883, 1886] |
| 5 | 1876 | confirmed | Lagos *(inherited from previous clause)* | [1883, 1886] |
| 6 | 1885 | collector and treasurer of the Gold Coast | Lagos *(inherited from previous clause)* | [1883, 1886] |

## Candidate stint `Pike, C___Gold Coast___1889`

- Staff-list name: **Pike, C** | colony: **Gold Coast** | listed 1889–1894 | editions [1889, 1890, 1894]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1889 | C. Pike | Treasurer | Treasury | C.M.G. | — |
| 1890 | C. Pike | Treasurer | Treasury | C.M.G. | — |
| 1894 | C. Pike | Sub-Inspectors | Interior Trade Roads | — | — |

### Deterministic checks: `pike_charles_e1869` vs `Pike, C___Gold Coast___1889`

- [PASS] surname_gate: bio 'PIKE' vs stint 'Pike, C' (exact)
- [PASS] initials: bio ['C'] ~ stint ['C']
- [PASS] age_gate: stint starts 1889; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Gold Coast'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1889-1894
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Pike, C___Windward Islands___1905`

- Staff-list name: **Pike, C** | colony: **Windward Islands** | listed 1905–1908 | editions [1905, 1906, 1907, 1908]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | C. Pike | District Medical Officers | Medical | — | — |
| 1906 | C. Pike | District Medical Officer | Medical | — | — |
| 1907 | C. Pike | District Medical Officer | Medical | — | — |
| 1908 | C. Pike | District Medical Officer | Medical | — | — |

### Deterministic checks: `pike_charles_e1869` vs `Pike, C___Windward Islands___1905`

- [PASS] surname_gate: bio 'PIKE' vs stint 'Pike, C' (exact)
- [PASS] initials: bio ['C'] ~ stint ['C']
- [PASS] age_gate: stint starts 1905; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Windward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1908
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

