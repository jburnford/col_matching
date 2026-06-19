<!-- {"case_id": "case_dimes_douglas-henry_b1886", "bio_ids": ["dimes_douglas-henry_b1886"], "stint_ids": ["Dines, D. H___Tanganyika___1924"]} -->
# Dossier case_dimes_douglas-henry_b1886

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `dimes_douglas-henry_b1886`

- Printed name: **DIMES, DOUGLAS HENRY**
- Birth year: 1886 (attested in editions [1927, 1928, 1929, 1930, 1931, 1933, 1934, 1935, 1936, 1937, 1939, 1940])
- Honours: M.R.C.V.S
- Appears in editions: [1927, 1928, 1929, 1930, 1931, 1933, 1934, 1935, 1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1927-L58440.v` — printed in editions [1927, 1928, 1929, 1930, 1931, 1933, 1934, 1935, 1936, 1937, 1939, 1940]:**

> DIMES, CAPT. DOUGLAS HENRY, M.R.C.V.S.—B., 1886; ed. Kingbridge Gram. Schol. and Schol. of Agr., S. Devon; R. Vety. Coll., London; lieut., R.A.V.C. (S.R.), 1913; war serv. in France and Belgium, 1914-19; vety. offr., Tanganyika Territory, Jan., 1923.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1913 | lieut., R.A.V.C. (S.R.) | — | [1927, 1928, 1929, 1930, 1931, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 1 | 1923 | vety. offr., Tanganyika Territory | Tanganyika | [1927, 1928, 1929, 1930, 1931, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |

## Candidate stint `Dines, D. H___Tanganyika___1924`

- Staff-list name: **Dines, D. H** | colony: **Tanganyika** | listed 1924–1925 | editions [1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1924 | D. H. Dines | Veterinary Officers | Veterinary Department | — | — |
| 1925 | D. H. Dines | Veterinary Officer | Veterinary Department | — | — |

### Deterministic checks: `dimes_douglas-henry_b1886` vs `Dines, D. H___Tanganyika___1924`

- [PASS] surname_gate: bio 'DIMES' vs stint 'Dines, D. H' (fuzzy:1)
- [PASS] initials: bio ['D', 'H'] ~ stint ['D', 'H']
- [PASS] age_gate: stint starts 1924, birth 1886 (age 38)
- [PASS] colony: 1 placed event(s) resolve to 'Tanganyika'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1924-1925
- [FAIL] position_sim: best 46 vs bar 60: 'vety. offr., Tanganyika Territory' ~ 'Veterinary Officer'
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

