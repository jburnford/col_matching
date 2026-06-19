<!-- {"case_id": "case_bassadone_g_e1873", "bio_ids": ["bassadone_g_e1873", "bassadone_g_e1873-2"], "stint_ids": ["Bassadone, George___Gibraltar___1877"]} -->
# Dossier case_bassadone_g_e1873

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['bassadone_g_e1873', 'bassadone_g_e1873-2'] carry a single initial only — the namesake trap applies.
- CONTESTED: stint(s) ['Bassadone, George___Gibraltar___1877'] have more than one claimant biography in this case.
- Phase 1 found `bassadone_g_e1873` ↔ `Bassadone, George___Gibraltar___1877` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- Phase 1 found `bassadone_g_e1873-2` ↔ `Bassadone, George___Gibraltar___1877` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).

## Biography `bassadone_g_e1873`

- Printed name: **BASSADONE, G**
- Birth year: not printed
- Appears in editions: [1886, 1888, 1889]

### Verbatim printed entry text (OCR)

**Version `col1886-L32072.v` — printed in editions [1886, 1888, 1889]:**

> BASSADONE, G.—Chief clerk, colonial treasury, Gibraltar, 27 Feb., 1873.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1873 | Chief clerk, colonial treasury | Gibraltar | [1886, 1888, 1889] |

## Biography `bassadone_g_e1873-2`

- Printed name: **BASSADONE, G**
- Birth year: not printed
- Appears in editions: [1890, 1894]

### Verbatim printed entry text (OCR)

**Version `col1890-L32513.v` — printed in editions [1890, 1894]:**

> BASSADONE, G.—Chief clerk, colonial treasury, Gibraltar, 1873; ditto, port office and collr. of lighthouse tolls, 1883.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1873 | Chief clerk, colonial treasury | Gibraltar | [1890, 1894] |
| 1 | 1883 | ditto, port office and collr. of lighthouse tolls | Gibraltar *(inherited from previous clause)* | [1890, 1894] |

## Candidate stint `Bassadone, George___Gibraltar___1877`

- Staff-list name: **Bassadone, George** | colony: **Gibraltar** | listed 1877–1890 | editions [1877, 1878, 1879, 1880, 1883, 1886, 1888, 1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | George Bassadone | 1st Clerk | Treasury | — | — |
| 1878 | George Bassadone | 1st Clerk | Treasury | — | — |
| 1879 | George Bassadone | 1st Clerk | Treasury | — | — |
| 1880 | George Bassadone | 1st Clerk | Treasury | — | — |
| 1883 | George Bassadone | 1st Clerk | Treasury | — | — |
| 1886 | George Bassadone | Chief Clerk | Port Office | — | — |
| 1888 | George Bassadone | Chief Clerk | Port Office | — | — |
| 1889 | George Bassadone | Chief Clerk | Port Office | — | — |
| 1890 | George Bassadone | Chief Clerk | Port Office | — | — |

### Deterministic checks: `bassadone_g_e1873` vs `Bassadone, George___Gibraltar___1877`

- [PASS] surname_gate: bio 'BASSADONE' vs stint 'Bassadone, George' (exact)
- [PASS] initials: bio ['G'] ~ stint ['G']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Gibraltar'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1890
- [PASS] position_sim: best 100 vs bar 60: 'Chief clerk, colonial treasury' ~ 'Chief Clerk'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): 1 agreeing edition-year(s) [1886] pos~100 (bar: >=2)
- [PASS] place_inherited: at least one supporting event names its place in print

### Deterministic checks: `bassadone_g_e1873-2` vs `Bassadone, George___Gibraltar___1877`

- [PASS] surname_gate: bio 'BASSADONE' vs stint 'Bassadone, George' (exact)
- [PASS] initials: bio ['G'] ~ stint ['G']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Gibraltar'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1877-1890
- [PASS] position_sim: best 100 vs bar 60: 'Chief clerk, colonial treasury' ~ 'Chief Clerk'
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

