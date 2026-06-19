<!-- {"case_id": "case_kauntz_w-h_e1914", "bio_ids": ["kauntz_w-h_e1914"], "stint_ids": ["Kauntze, W. H___Kenya___1922", "Kauntze, W. H___Uganda___1939"]} -->
# Dossier case_kauntz_w-h_e1914

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- Phase 1 found `kauntz_w-h_e1914` ↔ `Kauntze, W. H___Kenya___1922` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Kauntze, W. H___Kenya___1922` is also gate-compatible with biography(ies) outside this case: ['kauntze_william-henry_e1914'] (already linked elsewhere or filtered).
- Phase 1 found `kauntz_w-h_e1914` ↔ `Kauntze, W. H___Uganda___1939` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Kauntze, W. H___Uganda___1939` is also gate-compatible with biography(ies) outside this case: ['kauntze_william-henry_e1914'] (already linked elsewhere or filtered).

## Biography `kauntz_w-h_e1914`

- Printed name: **KAUNTZ, W. H**
- Birth year: not printed
- Honours: B.A, M.B
- Appears in editions: [1935]

### Verbatim printed entry text (OCR)

**Version `dol1935-L59934.v` — printed in editions [1935]:**

> KAUNTZ, W. H., B.A., M.D.; Ch.B. (Vic. Univ.), M.B., B.S. (Lond.), M.R.C.S. (Eng.), L.R.C.P. (Lond.), Cert. London S.H. and T.M.; (1st place and med.), D.P.H. (Vic. Univ.)—W. African med. staff, Jan., 1914 to Jan., 1919; served with W. African Forces, Aug., 1914 to Mar., 1916; seconded for serv., E. Africa Prot., Mar., 1916 to Jan., 1919; ment in desps.; pathologist and astt. bacteriologist, Kenya, Jan., 1919; dir., laboratory services, Kenya, Apr., 1919; dir., med. and san'y. services, Uganda, Nov., 1932.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914–1919 | W. African med. staff | — | [1935] |
| 1 | 1914–1916 | served with W. African Forces | — | [1935] |
| 2 | 1916–1919 | seconded for serv., E. Africa Prot | — | [1935] |
| 3 | 1919 | pathologist and astt. bacteriologist | Kenya | [1935] |
| 4 | 1932 | dir., med. and san'y. services | Uganda | [1935] |

## Candidate stint `Kauntze, W. H___Kenya___1922`

- Staff-list name: **Kauntze, W. H** | colony: **Kenya** | listed 1922–1925 | editions [1922, 1923, 1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | W. H. Kauntze | Bacteriologist | Medical | — | — |
| 1923 | W. H. Kauntze | Bacteriologist | Medical | — | — |
| 1924 | W. H. Kauntze | Bacteriologist | Medical | — | — |
| 1925 | W. H. Kauntze | Bacteriologist | Medical Department | — | — |

### Deterministic checks: `kauntz_w-h_e1914` vs `Kauntze, W. H___Kenya___1922`

- [PASS] surname_gate: bio 'KAUNTZ' vs stint 'Kauntze, W. H' (fuzzy:1)
- [PASS] initials: bio ['W', 'H'] ~ stint ['W', 'H']
- [PASS] age_gate: stint starts 1922; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1922-1925
- [PASS] position_sim: best 100 vs bar 60: 'pathologist and astt. bacteriologist' ~ 'Bacteriologist'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Kauntze, W. H___Uganda___1939`

- Staff-list name: **Kauntze, W. H** | colony: **Uganda** | listed 1939–1940 | editions [1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | W. H. Kauntze | Director of Medical Services | Medical | C.M.G. | — |
| 1940 | W. H. Kauntze | Director of Medical Services | Medical | C.M.G. | — |

### Deterministic checks: `kauntz_w-h_e1914` vs `Kauntze, W. H___Uganda___1939`

- [PASS] surname_gate: bio 'KAUNTZ' vs stint 'Kauntze, W. H' (fuzzy:1)
- [PASS] initials: bio ['W', 'H'] ~ stint ['W', 'H']
- [PASS] age_gate: stint starts 1939; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1939-1940
- [PASS] position_sim: best 64 vs bar 60: 'dir., med. and san'y. services' ~ 'Director of Medical Services'
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

