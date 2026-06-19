<!-- {"case_id": "case_hillary_denis_b1886", "bio_ids": ["hillary_denis_b1886"], "stint_ids": ["Hillary, D___Straits Settlements___1931"]} -->
# Dossier case_hillary_denis_b1886

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['hillary_denis_b1886'] carry a single initial only — the namesake trap applies.

## Biography `hillary_denis_b1886`

- Printed name: **HILLARY, DENIS**
- Birth year: 1886 (attested in editions [1935, 1936, 1937])
- Appears in editions: [1935, 1936, 1937]

### Verbatim printed entry text (OCR)

**Version `dol1935-L59424.v` — printed in editions [1935, 1936, 1937]:**

> HILLARY, DENIS.—B. 1886; pol. probr., S.S., Dec., 1908; inspr., pol., Malacca, Mar., 1912; ch. inspr., pol., K. Star, Kedah, July, 1915; ag. asst. comsnr., pol., N. Kedah, Sept., 1919; do., S. Patani, Apr., 1926; do., S. Kedah, Dec., 1927; asst. supt., pol., S'pore, July, 1928; J.P., S'pore, Oct., 1928; ag. comsnr., pol., Kelantan, Sept., 1934.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1908 | pol. probr. | Straits Settlements | [1935, 1936, 1937] |
| 1 | 1912 | inspr., pol., Malacca | Straits Settlements *(inherited from previous clause)* | [1935, 1936, 1937] |
| 2 | 1915 | ch. inspr., pol., K. Star | Kedah | [1935, 1936, 1937] |
| 3 | 1919 | ag. asst. comsnr., pol., N. Kedah | Kedah *(inherited from previous clause)* | [1935, 1936, 1937] |
| 4 | 1926 | do., S. Patani | Kedah *(inherited from previous clause)* | [1935, 1936, 1937] |
| 5 | 1927 | do., S. Kedah | Kedah *(inherited from previous clause)* | [1935, 1936, 1937] |
| 6 | 1928 | asst. supt., pol., S'pore | Kedah *(inherited from previous clause)* | [1935, 1936, 1937] |
| 7 | 1934 | ag. comsnr., pol. | Kelantan | [1935, 1936, 1937] |

## Candidate stint `Hillary, D___Straits Settlements___1931`

- Staff-list name: **Hillary, D** | colony: **Straits Settlements** | listed 1931–1939 | editions [1931, 1933, 1934, 1936, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | D. Hillary | Assistant Superintendent | Police | — | — |
| 1933 | D. Hillary | Superintendent (Commandant Depot) | Police | — | — |
| 1934 | D. Hillary | Superintendent (Commandant Depot) | Police | — | — |
| 1936 | D. Hillary | Assistant Superintendent | Police | — | — |
| 1939 | D. Hillary | Assistant Superintendent | Police | — | — |

### Deterministic checks: `hillary_denis_b1886` vs `Hillary, D___Straits Settlements___1931`

- [PASS] surname_gate: bio 'HILLARY' vs stint 'Hillary, D' (exact)
- [PASS] initials: bio ['D'] ~ stint ['D']
- [PASS] age_gate: stint starts 1931, birth 1886 (age 45)
- [PASS] colony: 2 placed event(s) resolve to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1931-1939
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

