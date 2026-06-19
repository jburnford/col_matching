<!-- {"case_id": "case_jacobs_b-l_b1918", "bio_ids": ["jacobs_b-l_b1918"], "stint_ids": ["Jacobs, B. L___Uganda___1949"]} -->
# Dossier case_jacobs_b-l_b1918

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 21 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Jacobs, B. L___Uganda___1949` is also gate-compatible with biography(ies) outside this case: ['jacobs_x_b1909'] (already linked elsewhere or filtered).

## Biography `jacobs_b-l_b1918`

- Printed name: **JACOBS, B. L**
- Birth year: 1918 (attested in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Terminal: retired 1965 — “retd., apptd. admin. trng. expert, Basuto., 1965.”
- Appears in editions: [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1958-L23996.v` — printed in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> JACOBS, B. L.—b. 1918; ed. Mercers' Sch.; mil. serv., 1939–46, major; admin. cadet, Uga., 1947; asst. D.O., 1949; D.O., 1954; dist. comsnr., 1955; senr. D.O., 1961; secon. dir. studies, Makerere Univ. Coll., 1961–65; retd., apptd. admin. trng. expert, Basuto., 1965.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1947 | admin. cadet | Uganda | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1949 | asst. D.O | Uganda *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1954 | asst. D.O | Dominions Office | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 3 | 1955 | dist. comsnr | Dominions Office *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 4 | 1961 | senr. D.O | Dominions Office *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Jacobs, B. L___Uganda___1949`

- Staff-list name: **Jacobs, B. L** | colony: **Uganda** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | B. L. Jacobs | District Officers and Assistant District Officers | Provincial Administration | — | — |
| 1949 | B. L. Jacobs | Secretaries (Seconded from the Provincial Administration) | Secretariat | — | — |
| 1951 | B. L. Jacobs | District Officers and Assistant District Officers | Provincial Administration | — | — |

### Deterministic checks: `jacobs_b-l_b1918` vs `Jacobs, B. L___Uganda___1949`

- [PASS] surname_gate: bio 'JACOBS' vs stint 'Jacobs, B. L' (exact)
- [PASS] initials: bio ['B', 'L'] ~ stint ['B', 'L']
- [PASS] age_gate: stint starts 1949, birth 1918 (age 31)
- [PASS] colony: 2 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 37 vs bar 60: 'asst. D.O' ~ 'District Officers and Assistant District Officers'
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

