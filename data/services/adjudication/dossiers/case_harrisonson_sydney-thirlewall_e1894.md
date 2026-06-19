<!-- {"case_id": "case_harrisonson_sydney-thirlewall_e1894", "bio_ids": ["harrisonson_sydney-thirlewall_e1894"], "stint_ids": ["Harrisson, S. T___Barbados___1912", "Harrisson, S. T___Gold Coast___1896"]} -->
# Dossier case_harrisonson_sydney-thirlewall_e1894

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- Phase 1 found `harrisonson_sydney-thirlewall_e1894` ↔ `Harrisson, S. T___Barbados___1912` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Harrisson, S. T___Barbados___1912` is also gate-compatible with biography(ies) outside this case: ['harrisson_sydney-thirlwall_e1894'] (already linked elsewhere or filtered).
- NOTE: stint `Harrisson, S. T___Gold Coast___1896` is also gate-compatible with biography(ies) outside this case: ['harrisson_sydney-thirlwall_e1894'] (already linked elsewhere or filtered).

## Biography `harrisonson_sydney-thirlewall_e1894`

- Printed name: **HARRISONSON, SYDNEY THIRLEWALL**
- Birth year: not printed
- Honours: C.M.G (1908), O.B.E (1919)
- Appears in editions: [1906, 1919, 1922, 1925]

### Verbatim printed entry text (OCR)

**Version `col1906-L45967.v` — printed in editions [1906, 1919, 1922, 1925]:**

> HARRISONSON, SYDNEY THIRLEWALL, C.M.G. (1908), O.B.E. (1919).—Ed. Blackheath; apptd. ast. acct., P.W.D., G. C. Col., 9th Nov., 1894; ch. acct., 2nd June, 1897; ast. acct., W.A.F.F., 26th Feb., 1898; ch. acct., 8th Nov., 1899; treas., N. Nig., 1st Jan., 1900; comptroller of customs, Barbados, 1908.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1894 | apptd. ast. acct., P.W.D. | Gold Coast | [1906, 1919, 1922, 1925] |
| 1 | 1897 | ch. acct | Gold Coast *(inherited from previous clause)* | [1906, 1919, 1922, 1925] |
| 2 | 1898 | ast. acct., W.A.F.F | Gold Coast *(inherited from previous clause)* | [1906, 1919, 1922, 1925] |
| 3 | 1899 | ch. acct | Gold Coast *(inherited from previous clause)* | [1906, 1919, 1922, 1925] |
| 4 | 1900 | treas. | Northern Nigeria | [1906, 1919, 1922, 1925] |
| 5 | 1908 | comptroller of customs | Barbados | [1906, 1919, 1922, 1925] |

## Candidate stint `Harrisson, S. T___Barbados___1912`

- Staff-list name: **Harrisson, S. T** | colony: **Barbados** | listed 1912–1913 | editions [1912, 1913]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | S. T. Harrisson | Controller | Customs | C.M.G. | — |
| 1913 | S. T. Harrisson | Controller | Customs | C.M.G. | — |

### Deterministic checks: `harrisonson_sydney-thirlewall_e1894` vs `Harrisson, S. T___Barbados___1912`

- [PASS] surname_gate: bio 'HARRISONSON' vs stint 'Harrisson, S. T' (fuzzy:2)
- [PASS] initials: bio ['S', 'T'] ~ stint ['S', 'T']
- [PASS] age_gate: stint starts 1912; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Barbados'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1912-1913
- [FAIL] position_sim: best 56 vs bar 60: 'comptroller of customs' ~ 'Controller'
- [PASS] honour: shared: C.M.G
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Harrisson, S. T___Gold Coast___1896`

- Staff-list name: **Harrisson, S. T** | colony: **Gold Coast** | listed 1896–1897 | editions [1896, 1897]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1896 | S. T. Harrisson | Clerical Assistant to Chief Clerk and Accountant | Public Works Department | — | — |
| 1897 | S. T. Harrisson | Clerical Assistant to Chief Clerk and Accountant | Public Works Department | — | — |

### Deterministic checks: `harrisonson_sydney-thirlewall_e1894` vs `Harrisson, S. T___Gold Coast___1896`

- [PASS] surname_gate: bio 'HARRISONSON' vs stint 'Harrisson, S. T' (fuzzy:2)
- [PASS] initials: bio ['S', 'T'] ~ stint ['S', 'T']
- [PASS] age_gate: stint starts 1896; no printed birth year — UNCHECKED
- [PASS] colony: 4 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1896-1897
- [FAIL] position_sim: best 36 vs bar 60: 'apptd. ast. acct., P.W.D.' ~ 'Clerical Assistant to Chief Clerk and Accountant'
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

