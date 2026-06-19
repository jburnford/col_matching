<!-- {"case_id": "case_saltwell_edward-joseph_b1890", "bio_ids": ["saltwell_edward-joseph_b1890"], "stint_ids": ["Saltwell, E. J___Nigeria___1934"]} -->
# Dossier case_saltwell_edward-joseph_b1890

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `saltwell_edward-joseph_b1890`

- Printed name: **SALTWELL, EDWARD JOSEPH**
- Birth year: 1890 (attested in editions [1940])
- Appears in editions: [1940]

### Verbatim printed entry text (OCR)

**Version `col1940-L68189.v` — printed in editions [1940]:**

> SALTWELL, CAPTAIN EDWARD JOSEPH, M.C.—B. 1890; army serv., 1914-21; admstv. offr., cls. IV, Nigeria, 1921; cls. III, 1924; ag. senr. asst. sec., N. Provs., Oct., 1937-Feb., 1938; ag. senr. asst. sec., Nigerian secret., Feb., 1938-Mar., 1938; ag. princ. asst. sec., do., Apr., 1938-Jan., 1939; offr., cls. II, Aug., 1939.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914–1921 | army serv | — | [1940] |
| 1 | 1921 | admstv. offr., cls. IV | Nigeria | [1940] |
| 2 | 1924 | cls. III | Nigeria *(inherited from previous clause)* | [1940] |
| 3 | 1937–1938 | ag. senr. asst. sec., N. Provs | Nigeria *(inherited from previous clause)* | [1940] |
| 4 | 1938–1938 | ag. senr. asst. sec., Nigerian secret | Dominions Office | [1940] |
| 5 | 1939 | offr., cls. II | Dominions Office *(inherited from previous clause)* | [1940] |

## Candidate stint `Saltwell, E. J___Nigeria___1934`

- Staff-list name: **Saltwell, E. J** | colony: **Nigeria** | listed 1934–1939 | editions [1934, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | E. J. Saltwell | — | Administrative Service | M.C | Captain |
| 1939 | Capt. E. J. Saltwell | Assistant Secretary | Nigerian Secretariat | M.C. | Captain |

### Deterministic checks: `saltwell_edward-joseph_b1890` vs `Saltwell, E. J___Nigeria___1934`

- [PASS] surname_gate: bio 'SALTWELL' vs stint 'Saltwell, E. J' (exact)
- [PASS] initials: bio ['E', 'J'] ~ stint ['E', 'J']
- [PASS] age_gate: stint starts 1934, birth 1890 (age 44)
- [PASS] colony: 3 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1934-1939
- [FAIL] position_sim: best 51 vs bar 60: 'ag. senr. asst. sec., N. Provs' ~ 'Assistant Secretary'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

