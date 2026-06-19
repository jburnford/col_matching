<!-- {"case_id": "case_laird_john_b1878", "bio_ids": ["laird_john_b1878"], "stint_ids": ["Laird, J___Straits Settlements___1931", "Laird, W. J___Sierra Leone___1936"]} -->
# Dossier case_laird_john_b1878

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['laird_john_b1878'] carry a single initial only — the namesake trap applies.

## Biography `laird_john_b1878`

- Printed name: **LAIRD, JOHN**
- Birth year: 1878 (attested in editions [1932])
- Honours: A.R.S.M
- Appears in editions: [1932]

### Verbatim printed entry text (OCR)

**Version `col1932-L61829.v` — printed in editions [1932]:**

> LAIRD, JOHN, A.R.S.M.—B. 1878; inspr., mines, Selangor, Aug., 1902; sec. for mil. ser., Nov., 1915; lieut., R.G.A., July, 1917; asst. warden, mines, Perak, Nov., 1919; warden, mines, Perak, June, 1928; ag. senr. warden, mines, F.M.S., 1931.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1902 | inspr., mines, Selangor | — | [1932] |
| 1 | 1915 | sec. for mil. ser | — | [1932] |
| 2 | 1917 | lieut., R.G.A | — | [1932] |
| 3 | 1919 | asst. warden, mines, Perak | — | [1932] |
| 4 | 1928 | warden, mines, Perak | — | [1932] |
| 5 | 1931 | ag. senr. warden, mines | Federated Malay States | [1932] |

## Candidate stint `Laird, J___Straits Settlements___1931`

- Staff-list name: **Laird, J** | colony: **Straits Settlements** | listed 1931–1933 | editions [1931, 1933]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | J. Laird | Warden of Mines, Perak | Mines | — | — |
| 1933 | J. Laird | Warden of Mines | Mines | — | — |

### Deterministic checks: `laird_john_b1878` vs `Laird, J___Straits Settlements___1931`

- [PASS] surname_gate: bio 'LAIRD' vs stint 'Laird, J' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1931, birth 1878 (age 53)
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1931-1933
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Laird, W. J___Sierra Leone___1936`

- Staff-list name: **Laird, W. J** | colony: **Sierra Leone** | listed 1936–1940 | editions [1936, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | W. J. Laird | Medical Officers | Medical | — | — |
| 1937 | W. J. Laird | Medical Officers (Col. Med. Service) | Medical Department | — | — |
| 1939 | W. J. Laird | Medical Officer | Medical Department | — | — |
| 1940 | W. J. Laird | Medical Officers (Col. Med. Service) | Medical Department | — | — |

### Deterministic checks: `laird_john_b1878` vs `Laird, W. J___Sierra Leone___1936`

- [PASS] surname_gate: bio 'LAIRD' vs stint 'Laird, W. J' (exact)
- [PASS] initials: bio ['J'] ~ stint ['W', 'J']
- [PASS] age_gate: stint starts 1936, birth 1878 (age 58)
- [FAIL] colony: no placed event resolves to 'Sierra Leone'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1936-1940
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

