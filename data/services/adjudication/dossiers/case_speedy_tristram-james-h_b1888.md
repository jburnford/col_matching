<!-- {"case_id": "case_speedy_tristram-james-h_b1888", "bio_ids": ["speedy_tristram-james-h_b1888"], "stint_ids": ["Speedy, T. J. H___North Borneo___1933"]} -->
# Dossier case_speedy_tristram-james-h_b1888

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `speedy_tristram-james-h_b1888`

- Printed name: **SPEEDY, Tristram James H**
- Birth year: 1888 (attested in editions [1949, 1950])
- Honours: F.R.G.S, F.R.S.A
- Appears in editions: [1949, 1950]

### Verbatim printed entry text (OCR)

**Version `col1949-L35813.v` — printed in editions [1949, 1950]:**

> SPEEDY, Tristram James H., F.S.I. (Lond.), F.R.G.S., F.R.S.A., M.T.P.I. (N.Z.), M.S.I. (N.Z.).—b. 1888; survr. (Chartered Co.'s survr.), N. Borneo, 1919; ch. survr., 1923; survr.-gen., 1929; col. surv. surv. as survr.-gen., N. Borneo, 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1919 | survr. (Chartered Co.'s survr.) | North Borneo | [1949, 1950] |
| 1 | 1923 | ch. survr | North Borneo *(inherited from previous clause)* | [1949, 1950] |
| 2 | 1929 | survr.-gen | North Borneo *(inherited from previous clause)* | [1949, 1950] |
| 3 | 1946 | col. surv. surv. as survr.-gen. | North Borneo | [1949, 1950] |

## Candidate stint `Speedy, T. J. H___North Borneo___1933`

- Staff-list name: **Speedy, T. J. H** | colony: **North Borneo** | listed 1933–1949 | editions [1933, 1936, 1940, 1949]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | T. J. H. Speedy | Surveyor General | Staff | — | — |
| 1936 | T. J. H. Speedy | Surveyor General | Civil Service | — | — |
| 1940 | T. J. H. Speedy | Surveyor-General | Civil Service | — | — |
| 1949 | T. J. H. Speedy | Surveyor-General | Survey | — | — |

### Deterministic checks: `speedy_tristram-james-h_b1888` vs `Speedy, T. J. H___North Borneo___1933`

- [PASS] surname_gate: bio 'SPEEDY' vs stint 'Speedy, T. J. H' (exact)
- [PASS] initials: bio ['T', 'J', 'H'] ~ stint ['T', 'J', 'H']
- [PASS] age_gate: stint starts 1933, birth 1888 (age 45)
- [PASS] colony: 4 placed event(s) resolve to 'North Borneo'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1933-1949
- [PASS] position_sim: best 70 vs bar 60: 'survr.-gen' ~ 'Surveyor-General'
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

