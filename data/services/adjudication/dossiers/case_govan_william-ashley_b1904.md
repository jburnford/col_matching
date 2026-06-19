<!-- {"case_id": "case_govan_william-ashley_b1904", "bio_ids": ["govan_william-ashley_b1904"], "stint_ids": ["Govan, W. A___Gold Coast___1929"]} -->
# Dossier case_govan_william-ashley_b1904

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `govan_william-ashley_b1904`

- Printed name: **GOVAN, William Ashley**
- Birth year: 1904 (attested in editions [1948, 1949, 1950, 1951])
- Honours: C.P.M (1945)
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L32920.v` — printed in editions [1948, 1949, 1950, 1951]:**

> GOVAN, William Ashley, C.P.M. (1945).—b. 1904; ed. Glasg. Acad. and the Ley's Sch., Cambridge; asst. supt., police, G.C., 1928; supt., 1942.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | asst. supt., police | Gold Coast | [1948, 1949, 1950, 1951] |
| 1 | 1942 | supt | Gold Coast *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Govan, W. A___Gold Coast___1929`

- Staff-list name: **Govan, W. A** | colony: **Gold Coast** | listed 1929–1936 | editions [1929, 1930, 1932, 1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1929 | W. A. Govan | Commissioners and Assistant Commissioners of Police | Police Department | — | — |
| 1930 | W. A. Govan | Commissioners and Assistant Commissioners of Police | Police Department | — | — |
| 1932 | W. A. Govan | Commissioners and Assistant Commissioners of Police | Police Department | — | — |
| 1934 | W. A. Govan | Commissioners and Assistant Commissioners of Police | Police Department | — | — |
| 1936 | W. A. Govan | Commissioners and Assistant Commissioners of Police | Police Department | — | — |

### Deterministic checks: `govan_william-ashley_b1904` vs `Govan, W. A___Gold Coast___1929`

- [PASS] surname_gate: bio 'GOVAN' vs stint 'Govan, W. A' (exact)
- [PASS] initials: bio ['W', 'A'] ~ stint ['W', 'A']
- [PASS] age_gate: stint starts 1929, birth 1904 (age 25)
- [PASS] colony: 2 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1929-1936
- [FAIL] position_sim: best 55 vs bar 60: 'asst. supt., police' ~ 'Commissioners and Assistant Commissioners of Police'
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

