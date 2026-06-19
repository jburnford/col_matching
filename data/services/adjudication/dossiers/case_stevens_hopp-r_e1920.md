<!-- {"case_id": "case_stevens_hopp-r_e1920", "bio_ids": ["stevens_hopp-r_e1920"], "stint_ids": ["Stevens, H___Southern Nigeria___1905", "Stevens, Hope___Leeward Islands___1922", "Stevens, R___Bermuda___1894"]} -->
# Dossier case_stevens_hopp-r_e1920

## Case context

- 1 biography(ies) and 3 candidate stint(s) are entangled in this case.
- Corpus context: 66 official(s) with this surname in the graph's staff lists; 28 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Stevens, H___Southern Nigeria___1905` is also gate-compatible with biography(ies) outside this case: ['stevens_thomas-hamilton_e1873'] (already linked elsewhere or filtered).
- NOTE: stint `Stevens, Hope___Leeward Islands___1922` is also gate-compatible with biography(ies) outside this case: ['stevens_thomas-hamilton_e1873'] (already linked elsewhere or filtered).

## Biography `stevens_hopp-r_e1920`

- Printed name: **STEVENS, HOPP R**
- Birth year: not printed
- Appears in editions: [1924, 1925]

### Verbatim printed entry text (OCR)

**Version `col1924-L58123.v` — printed in editions [1924, 1925]:**

> STEVENS, HOPP R.—Senr. copyist, Treasy, St. Kitts, 1920; ag. sup. rev. offr., 1921; ag. clk. and storekeeper, P.W.D., 1921; clk. and storekeeper, P.W.D., 1922.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1920 | Senr. copyist, Treasy | St. Kitts | [1924, 1925] |
| 1 | 1921 | ag. sup. rev. offr | St. Kitts *(inherited from previous clause)* | [1924, 1925] |
| 2 | 1922 | clk. and storekeeper, P.W.D | St. Kitts *(inherited from previous clause)* | [1924, 1925] |

## Candidate stint `Stevens, H___Southern Nigeria___1905`

- Staff-list name: **Stevens, H** | colony: **Southern Nigeria** | listed 1905–1907 | editions [1905, 1907]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | H. Stevens | Moulder | Marine Department | — | — |
| 1907 | H. Stevens | Moulder | Marine Department | — | — |

### Deterministic checks: `stevens_hopp-r_e1920` vs `Stevens, H___Southern Nigeria___1905`

- [PASS] surname_gate: bio 'STEVENS' vs stint 'Stevens, H' (exact)
- [PASS] initials: bio ['H', 'R'] ~ stint ['H']
- [PASS] age_gate: stint starts 1905; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Southern Nigeria'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1907
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Stevens, Hope___Leeward Islands___1922`

- Staff-list name: **Stevens, Hope** | colony: **Leeward Islands** | listed 1922–1925 | editions [1922, 1923, 1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | H. Stevens | Clerk and Inspector of Works | Public Works | — | — |
| 1923 | H. Stevens | Clerk and Inspector of Works | Public Works | — | — |
| 1924 | Hope Stevens | Clerk and Inspector of Works | Public Works | — | — |
| 1925 | Hope Stevens | Clerk and Inspector of Works | Public Works | — | — |

### Deterministic checks: `stevens_hopp-r_e1920` vs `Stevens, Hope___Leeward Islands___1922`

- [PASS] surname_gate: bio 'STEVENS' vs stint 'Stevens, Hope' (exact)
- [PASS] initials: bio ['H', 'R'] ~ stint ['H']
- [PASS] age_gate: stint starts 1922; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1922-1925
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Stevens, R___Bermuda___1894`

- Staff-list name: **Stevens, R** | colony: **Bermuda** | listed 1894–1896 | editions [1894, 1896]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1894 | R. Stevens | Wesleyan Ministers | Ecclesiastical Establishment | — | — |
| 1896 | R. Stevens | Wesleyan Ministers | Ecclesiastical Establishment | — | — |

### Deterministic checks: `stevens_hopp-r_e1920` vs `Stevens, R___Bermuda___1894`

- [PASS] surname_gate: bio 'STEVENS' vs stint 'Stevens, R' (exact)
- [PASS] initials: bio ['H', 'R'] ~ stint ['R']
- [PASS] age_gate: stint starts 1894; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Bermuda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1894-1896
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

