<!-- {"case_id": "case_keating_john-henry_b1872", "bio_ids": ["keating_john-henry_b1872"], "stint_ids": ["Keating, John Henry___Commonwealth Of Australia___1905"]} -->
# Dossier case_keating_john-henry_b1872

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `keating_john-henry_b1872`

- Printed name: **KEATING, JOHN HENRY**
- Birth year: 1872 (attested in editions [1907, 1908, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1920, 1921, 1922])
- Appears in editions: [1907, 1908, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1920, 1921, 1922]

### Verbatim printed entry text (OCR)

**Version `col1907-L45213.v` — printed in editions [1907, 1908, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1920, 1921, 1922]:**

> KEATING, HON. JOHN HENRY.—B., 1872; called to the bar, Tasmania, 1894; senator for Tasmania, C. of Aust., 1901; min. without portfolio, 5th July, 1905; vice-pres. of exec. coun., 13th Oct., 1906; min. for home affairs, Jan., 1907.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1894 | called to the bar | Tasmania | [1907, 1908, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1920, 1921, 1922] |
| 1 | 1901 | senator for Tasmania, C. of Aust | Tasmania *(inherited from previous clause)* | [1907, 1908, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1920, 1921, 1922] |
| 2 | 1905 | min. without portfolio | Tasmania *(inherited from previous clause)* | [1907, 1908, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1920, 1921, 1922] |
| 3 | 1906 | vice-pres. of exec. coun | Tasmania *(inherited from previous clause)* | [1907, 1908, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1920, 1921, 1922] |
| 4 | 1907 | min. for home affairs | Tasmania *(inherited from previous clause)* | [1907, 1908, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1920, 1921, 1922] |

## Candidate stint `Keating, John Henry___Commonwealth Of Australia___1905`

- Staff-list name: **Keating, John Henry** | colony: **Commonwealth Of Australia** | listed 1905–1907 | editions [1905, 1907]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | J. H. Keating | Senator | Senate | — | — |
| 1907 | J. H. Keating | Vice-President of Executive Council | Senate | — | — |
| 1907 | The Hon. John Henry Keating | Vice-President of the Executive Council | Executive Council | — | — |

### Deterministic checks: `keating_john-henry_b1872` vs `Keating, John Henry___Commonwealth Of Australia___1905`

- [PASS] surname_gate: bio 'KEATING' vs stint 'Keating, John Henry' (exact)
- [PASS] initials: bio ['J', 'H'] ~ stint ['J', 'H']
- [PASS] age_gate: stint starts 1905, birth 1872 (age 33)
- [FAIL] colony: no placed event resolves to 'Commonwealth Of Australia'
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

