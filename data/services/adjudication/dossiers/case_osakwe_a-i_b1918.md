<!-- {"case_id": "case_osakwe_a-i_b1918", "bio_ids": ["osakwe_a-i_b1918"], "stint_ids": ["Osakwe, A. I___Nigeria___1958"]} -->
# Dossier case_osakwe_a-i_b1918

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `osakwe_a-i_b1918`

- Printed name: **OSAKWE, A. I.**
- Birth year: 1918 (attested in editions [1958, 1959, 1960, 1961])
- Appears in editions: [1958, 1959, 1960, 1961]

### Verbatim printed entry text (OCR)

**Version `col1958-L25744.v` — printed in editions [1958, 1959, 1960, 1961]:**

> OSAKWE, A. I.—b. 1918; ed. Dennis Memorial Gram. Sch., Onitsha, King's Coll., Lagos, and St. Peter's Hall, Oxford; admin. offr., Nig., 1946; secon. as industrial relations offr., Nig. coal corp'n., 1952, sec. of corp'n., 1953; dir., recruitment and training, E. Nig., 1954; perm. sec., min. of agric., 1957; sec. to ex. co., 1958.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | admin. offr. | Nigeria | [1958, 1959, 1960, 1961] |
| 1 | 1952 | industrial relations offr. | Nigeria | [1958, 1959, 1960, 1961] |
| 2 | 1953 | sec. of corp'n. | — | [1958, 1959, 1960, 1961] |
| 3 | 1954 | dir., recruitment and training | Eastern Nigeria | [1958, 1959, 1960, 1961] |
| 4 | 1957 | perm. sec., min. of agric. | — | [1958, 1959, 1960, 1961] |
| 5 | 1958 | sec. to ex. co. | — | [1958, 1959, 1960, 1961] |

## Candidate stint `Osakwe, A. I___Nigeria___1958`

- Staff-list name: **Osakwe, A. I** | colony: **Nigeria** | listed 1958–1960 | editions [1958, 1960]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1958 | A. I. Osakwe | Permanent Secretaries and Senior District Officers | Civil Establishment | — | — |
| 1960 | A. I. Osakwe | Secretary to Executive Council | Civil Establishment | — | — |

### Deterministic checks: `osakwe_a-i_b1918` vs `Osakwe, A. I___Nigeria___1958`

- [PASS] surname_gate: bio 'OSAKWE' vs stint 'Osakwe, A. I' (exact)
- [PASS] initials: bio ['A', 'I'] ~ stint ['A', 'I']
- [PASS] age_gate: stint starts 1958, birth 1918 (age 40)
- [PASS] colony: 3 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1958-1960
- [FAIL] position_sim: best 54 vs bar 60: 'dir., recruitment and training' ~ 'Permanent Secretaries and Senior District Officers'
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

