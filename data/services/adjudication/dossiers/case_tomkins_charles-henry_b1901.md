<!-- {"case_id": "case_tomkins_charles-henry_b1901", "bio_ids": ["tomkins_charles-henry_b1901"], "stint_ids": ["Tomkins, C. H___Gold Coast___1929"]} -->
# Dossier case_tomkins_charles-henry_b1901

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `tomkins_charles-henry_b1901`

- Printed name: **TOMKINS, Charles Henry**
- Birth year: 1901 (attested in editions [1949, 1950])
- Appears in editions: [1949, 1950]

### Verbatim printed entry text (OCR)

**Version `col1949-L36244.v` — printed in editions [1949, 1950]:**

> TOMKINS, Charles Henry.—b. 1901; on mil. serv., 1919-23 and 1940-43; Br. p.o., 1923; spl. serv. tel. foreman, G.C., 1928; tel. inspr., 1932; senr., 1944; asst. supt. stores, 1945.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1923 | Br. p.o | — | [1949, 1950] |
| 1 | 1928 | spl. serv. tel. foreman | Gold Coast | [1949, 1950] |
| 2 | 1932 | tel. inspr | Gold Coast *(inherited from previous clause)* | [1949, 1950] |
| 3 | 1944 | senr | Gold Coast *(inherited from previous clause)* | [1949, 1950] |
| 4 | 1945 | asst. supt. stores | Gold Coast *(inherited from previous clause)* | [1949, 1950] |

## Candidate stint `Tomkins, C. H___Gold Coast___1929`

- Staff-list name: **Tomkins, C. H** | colony: **Gold Coast** | listed 1929–1930 | editions [1929, 1930]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1929 | C. H. Tomkins | Telegraph Foremen | Engineering Branch | — | — |
| 1930 | C. H. Tomkins | Telegraph Foreman | Engineering Branch | — | — |

### Deterministic checks: `tomkins_charles-henry_b1901` vs `Tomkins, C. H___Gold Coast___1929`

- [PASS] surname_gate: bio 'TOMKINS' vs stint 'Tomkins, C. H' (exact)
- [PASS] initials: bio ['C', 'H'] ~ stint ['C', 'H']
- [PASS] age_gate: stint starts 1929, birth 1901 (age 28)
- [PASS] colony: 4 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1929-1930
- [FAIL] position_sim: best 59 vs bar 60: 'spl. serv. tel. foreman' ~ 'Telegraph Foreman'
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

