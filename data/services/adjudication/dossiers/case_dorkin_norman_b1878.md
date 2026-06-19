<!-- {"case_id": "case_dorkin_norman_b1878", "bio_ids": ["dorkin_norman_b1878"], "stint_ids": ["Dorkin, N___Tanganyika___1920"]} -->
# Dossier case_dorkin_norman_b1878

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['dorkin_norman_b1878'] carry a single initial only — the namesake trap applies.

## Biography `dorkin_norman_b1878`

- Printed name: **DORKIN, NORMAN**
- Birth year: 1878 (attested in editions [1925, 1927, 1928, 1929, 1930, 1931, 1932])
- Appears in editions: [1925, 1927, 1928, 1929, 1930, 1931, 1932]

### Verbatim printed entry text (OCR)

**Version `col1925-L55392.v` — printed in editions [1925, 1927, 1928, 1929, 1930, 1931, 1932]:**

> DORKIN, NORMAN.—B. 1878; O.F.S. govt. rly.s., 1897-99; Imp. Mily. Rly.s., 1900-02; Cent. S. African rly.s., 1903-06; S. African rly.s., 1909-14; E. African mily. rly.s., 1915-18; Tanganyika rly.s., 1919; served in Boer War, 1899-1902; rebellion, S. Africa, 1914-15; E. African forces, 1915-18; ment. twice in despatches; oh. storekeeper, Tanganyika rly.s., 1919.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1897–1899 | O.F.S. govt. rly.s | Orange Free State | [1925, 1927, 1928, 1929, 1930, 1931, 1932] |
| 1 | 1899–1902 | served in Boer War | Tanganyika *(inherited from previous clause)* | [1925, 1927, 1928, 1929, 1930, 1931, 1932] |
| 2 | 1900–1902 | Imp. Mily. Rly.s | Orange Free State *(inherited from previous clause)* | [1925, 1927, 1928, 1929, 1930, 1931, 1932] |
| 3 | 1903–1906 | Cent. S. African rly.s | Orange Free State *(inherited from previous clause)* | [1925, 1927, 1928, 1929, 1930, 1931, 1932] |
| 4 | 1909–1914 | S. African rly.s | Orange Free State *(inherited from previous clause)* | [1925, 1927, 1928, 1929, 1930, 1931, 1932] |
| 5 | 1914–1915 | rebellion, S. Africa | Tanganyika *(inherited from previous clause)* | [1925, 1927, 1928, 1929, 1930, 1931, 1932] |
| 6 | 1915–1918 | E. African mily. rly.s | Orange Free State *(inherited from previous clause)* | [1925, 1927, 1928, 1929, 1930, 1931, 1932] |
| 7 | 1915–1918 | E. African forces | Tanganyika *(inherited from previous clause)* | [1925, 1927, 1928, 1929, 1930, 1931, 1932] |
| 8 | 1919 | Tanganyika rly.s | Tanganyika | [1925, 1927, 1928, 1929, 1930, 1931, 1932] |

## Candidate stint `Dorkin, N___Tanganyika___1920`

- Staff-list name: **Dorkin, N** | colony: **Tanganyika** | listed 1920–1925 | editions [1920, 1921, 1922, 1923, 1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1920 | N. Dorkin | Chief Storekeeper | Railway Department | — | Captain |
| 1921 | N. Dorkin | Chief Storekeeper | Railways | — | — |
| 1922 | N. Dorkin | Chief Storekeeper | Railways | — | — |
| 1923 | N. Dorkin | Chief Storekeeper | Railways | — | — |
| 1924 | N. Dorkin | Chief Storekeeper | Railways | — | — |
| 1925 | N. Dorkin | Chief Storekeeper | Railways | — | — |

### Deterministic checks: `dorkin_norman_b1878` vs `Dorkin, N___Tanganyika___1920`

- [PASS] surname_gate: bio 'DORKIN' vs stint 'Dorkin, N' (exact)
- [PASS] initials: bio ['N'] ~ stint ['N']
- [PASS] age_gate: stint starts 1920, birth 1878 (age 42)
- [PASS] colony: 4 placed event(s) resolve to 'Tanganyika'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1920-1925
- [FAIL] position_sim: best 19 vs bar 60: 'Tanganyika rly.s' ~ 'Chief Storekeeper'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

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

