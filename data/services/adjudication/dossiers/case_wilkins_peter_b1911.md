<!-- {"case_id": "case_wilkins_peter_b1911", "bio_ids": ["wilkins_peter_b1911"], "stint_ids": ["Wilkins, P___Sierra Leone___1936"]} -->
# Dossier case_wilkins_peter_b1911

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 12 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['wilkins_peter_b1911'] carry a single initial only — the namesake trap applies.

## Biography `wilkins_peter_b1911`

- Printed name: **WILKINS, Peter**
- Birth year: 1911 (attested in editions [1953, 1954, 1955])
- Appears in editions: [1950, 1951, 1953, 1954, 1955]

### Verbatim printed entry text (OCR)

**Version `col1953-L19551.v` — printed in editions [1953, 1954, 1955]:**

> WILKINS, P.—b. 1911; ed. Rossall Sch. and St. John's Coll., Oxford; cadet, S.L., 1934; asst. dist. comsnr., 1937; dist. comsnr., 1941; secon. to C.O., 1945-47; senr. asst. col. sec., G.C., 1948; senr. asst. sec., min. of educ. and soc. welf., 1950; prin. asst. sec., 1952; perm. sec., 1954.

**Version `col1950-L40736.v` — printed in editions [1950, 1951]:**

> WILKINS, Peter.—b. 1911; ed. Rossall Sch. and St. John's Coll., Oxford, M.A. (Oxon); cadet, S.L., 1934; asst. dist. comsnr., 1937; dist. comsnr., 1941; seconded to C.O., 1945-47; trans. to G.C., 1948; senr. asst. col. sec., 1948.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1934 | cadet | Sierra Leone | [1950, 1951, 1953, 1954, 1955] |
| 1 | 1937 | asst. dist. comsnr | Sierra Leone *(inherited from previous clause)* | [1950, 1951, 1953, 1954, 1955] |
| 2 | 1941 | dist. comsnr | Sierra Leone *(inherited from previous clause)* | [1950, 1951, 1953, 1954, 1955] |
| 3 | 1945–1947 | secon. to C.O | Sierra Leone *(inherited from previous clause)* | [1950, 1951, 1953, 1954, 1955] |
| 4 | 1948 | senr. asst. col. sec. | Gold Coast | [1950, 1951, 1953, 1954, 1955] |
| 5 | 1948 | trans. to G.C | Sierra Leone *(inherited from previous clause)* | [1950, 1951] |
| 6 | 1950 | senr. asst. sec., min. of educ. and soc. welf | Gold Coast *(inherited from previous clause)* | [1953, 1954, 1955] |
| 7 | 1952 | prin. asst. sec | Gold Coast *(inherited from previous clause)* | [1953, 1954, 1955] |
| 8 | 1954 | perm. sec | Gold Coast *(inherited from previous clause)* | [1953, 1954, 1955] |

## Candidate stint `Wilkins, P___Sierra Leone___1936`

- Staff-list name: **Wilkins, P** | colony: **Sierra Leone** | listed 1936–1940 | editions [1936, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | P. Wilkins | Assistant District Commissioner | Civil Establishment | — | — |
| 1937 | P. Wilkins | Assistant District Commissioner | Civil Establishment | — | — |
| 1939 | P. Wilkins | Assistant District Commissioner | Provincial Administration | — | — |
| 1940 | P. Wilkins | District Commissioner | Provincial Administration | — | — |

### Deterministic checks: `wilkins_peter_b1911` vs `Wilkins, P___Sierra Leone___1936`

- [PASS] surname_gate: bio 'WILKINS' vs stint 'Wilkins, P' (exact)
- [PASS] initials: bio ['P'] ~ stint ['P']
- [PASS] age_gate: stint starts 1936, birth 1911 (age 25)
- [PASS] colony: 5 placed event(s) resolve to 'Sierra Leone'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1936-1940
- [PASS] position_sim: best 69 vs bar 60: 'dist. comsnr' ~ 'District Commissioner'
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

