<!-- {"case_id": "case_babbi_burland-arthur_b1907-2", "bio_ids": ["babbi_burland-arthur_b1907-2"], "stint_ids": ["Babb, B. A___Zanzibar___1952"]} -->
# Dossier case_babbi_burland-arthur_b1907-2

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `babbi_burland-arthur_b1907-2`

- Printed name: **BABBI, Burland Arthur**
- Birth year: 1907 (attested in editions [1953])
- Appears in editions: [1950, 1953]

### Verbatim printed entry text (OCR)

**Version `col1953-L16408.v` — printed in editions [1953]:**

> BABBI, B. A.—b. 1907; ed. Bedford Modern Sch. and St. John's Coll., Camb.; mil. serv., 1941-45, lt.-cmdt.; supt., educ., Nig., 1929; educ. offr., Tang., 1945; dir., educ., Zanz., 1951.

**Version `col1950-L33352.v` — printed in editions [1950]:**

> BABBI, Burland Arthur.—b. 1907; ed. Bedford Modern Sch. and St. John’s Coll., Camb., B.A. (Cantab.), dip. ed. (Cantab.); on mil. serv., 1941–45, lt.-col.; supt., educ., Nig., 1929; educ. offr., T.T., 1945.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1929 | supt., educ. | Nigeria | [1950, 1953] |
| 1 | 1951 | dir., educ. | Zanzibar | [1953] |

## Candidate stint `Babb, B. A___Zanzibar___1952`

- Staff-list name: **Babb, B. A** | colony: **Zanzibar** | listed 1952–1953 | editions [1952, 1953]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1952 | B. A. Babb | Director of Education | Civil Establishment | — | — |
| 1953 | B. A. Babb | Director of Education | Civil Establishment | — | — |

### Deterministic checks: `babbi_burland-arthur_b1907-2` vs `Babb, B. A___Zanzibar___1952`

- [PASS] surname_gate: bio 'BABBI' vs stint 'Babb, B. A' (fuzzy:1)
- [PASS] initials: bio ['B', 'A'] ~ stint ['B', 'A']
- [PASS] age_gate: stint starts 1952, birth 1907 (age 45)
- [PASS] colony: 1 placed event(s) resolve to 'Zanzibar'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1952-1953
- [FAIL] position_sim: best 55 vs bar 60: 'dir., educ.' ~ 'Director of Education'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): 1 agreeing edition-year(s) [1953] pos~55 (bar: >=2)
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

