<!-- {"case_id": "case_priestman_harold-edney_b1888", "bio_ids": ["priestman_harold-edney_b1888"], "stint_ids": ["Priestman, H. E___Nigeria___1925"]} -->
# Dossier case_priestman_harold-edney_b1888

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `priestman_harold-edney_b1888`

- Printed name: **PRIESTMAN, HAROLD EDNEY**
- Birth year: 1888 (attested in editions [1936, 1937, 1939, 1940])
- Honours: C.M.G (1937)
- Appears in editions: [1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1936-L63849.v` — printed in editions [1936, 1937, 1939, 1940]:**

> PRIESTMAN, HAROLD EDNEY, C.M.G. (1937), B.A. (Dublin).—B. 1888; mil. serv., 1914-19; temp. admin. offr., min. of lab., 1919; astt. dist. offr., Nigeria, 1921; attached, to C.O., 1930; seconded as ag. col. sec. and senr. astt. col. sec., Gambia, 1931; resumed duties, C.O., 1932; resumed substantive appt., Nigeria, 1933; admin. sec. to high commr., for Basutoland, Bech. Prot. and Swaziland, 1935.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1919 | temp. admin. offr., min. of lab | — | [1936, 1937, 1939, 1940] |
| 1 | 1921 | astt. dist. offr. | Nigeria | [1936, 1937, 1939, 1940] |
| 2 | 1930 | attached, to C.O | Nigeria *(inherited from previous clause)* | [1936, 1937, 1939, 1940] |
| 3 | 1931 | seconded as ag. col. sec. and senr. astt. col. sec. | Gambia | [1936, 1937, 1939, 1940] |
| 4 | 1932 | resumed duties | Colonial Office | [1936, 1937, 1939, 1940] |
| 5 | 1933 | resumed substantive appt. | Nigeria | [1936, 1937, 1939, 1940] |
| 6 | 1935 | admin. sec. to high commr., for Basutoland, Bech. Prot. and Swaziland | Bechuanaland | [1936, 1937, 1939, 1940] |

## Candidate stint `Priestman, H. E___Nigeria___1925`

- Staff-list name: **Priestman, H. E** | colony: **Nigeria** | listed 1925–1927 | editions [1925, 1927]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1925 | H. E. Priestman | 294 District Officers | Political | — | — |
| 1927 | H. E. Priestman | Assistant Secretary | Nigerian Secretariat | — | — |

### Deterministic checks: `priestman_harold-edney_b1888` vs `Priestman, H. E___Nigeria___1925`

- [PASS] surname_gate: bio 'PRIESTMAN' vs stint 'Priestman, H. E' (exact)
- [PASS] initials: bio ['H', 'E'] ~ stint ['H', 'E']
- [PASS] age_gate: stint starts 1925, birth 1888 (age 37)
- [PASS] colony: 3 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1925-1927
- [FAIL] position_sim: best 57 vs bar 60: 'astt. dist. offr.' ~ '294 District Officers'
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

