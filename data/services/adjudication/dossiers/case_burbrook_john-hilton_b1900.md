<!-- {"case_id": "case_burbrook_john-hilton_b1900", "bio_ids": ["burbrook_john-hilton_b1900"], "stint_ids": ["Burbrook, J. H___Uganda___1939"]} -->
# Dossier case_burbrook_john-hilton_b1900

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `burbrook_john-hilton_b1900`

- Printed name: **BURBROOK, John Hilton**
- Birth year: 1900 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951, 1957, 1958, 1959]

### Verbatim printed entry text (OCR)

**Version `col1948-L31501.v` — printed in editions [1948, 1949, 1950, 1951]:**

> BURBROOK, John Hilton.—b. 1900; ed. Acton County Sch., Middlesex; on mil. serv. 1915–19; Egyptian police, 1921; asst. supt. of police, Uga., 1937; senr. asst. supt. of police, 1942; supt., 1946.

**Version `col1957-L21561.v` — printed in editions [1957, 1958, 1959]:**

> BURBROOK, J. H., Chevalier of the Order of the Nile and of the Royal Order of the Sword of Sweden.—b. 1900; ed. Acton County Sch., Mddx.; mil. serv., 1915-19, cpl.; Egyptian police, 1921; asst. supt., police, Uga., 1937; supt., 1946; dep. prin. immig. offr., 1951-58.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1921 | Egyptian police | — | [1948, 1949, 1950, 1951, 1957, 1958, 1959] |
| 1 | 1937 | asst. supt. of police | Uganda | [1948, 1949, 1950, 1951, 1957, 1958, 1959] |
| 2 | 1942 | senr. asst. supt. of police | Uganda *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 3 | 1946 | supt | Uganda *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1957, 1958, 1959] |
| 4 | 1951–1958 | dep. prin. immig. offr | Uganda *(inherited from previous clause)* | [1957, 1958, 1959] |

## Candidate stint `Burbrook, J. H___Uganda___1939`

- Staff-list name: **Burbrook, J. H** | colony: **Uganda** | listed 1939–1951 | editions [1939, 1940, 1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | J. H. Burbrook | Superintendents, Assistant Superintendents and Cadets | Police | — | — |
| 1940 | J. H. Burbrook | Superintendent, Assistant Superintendent and Cadet | Police | — | — |
| 1949 | J. H. Burbrook | Superintendents, Assistants and Cadets | Police | — | — |
| 1951 | J. H. Burbrook | Superintendents, Assistants and Cadets | Police | — | — |

### Deterministic checks: `burbrook_john-hilton_b1900` vs `Burbrook, J. H___Uganda___1939`

- [PASS] surname_gate: bio 'BURBROOK' vs stint 'Burbrook, J. H' (exact)
- [PASS] initials: bio ['J', 'H'] ~ stint ['J', 'H']
- [PASS] age_gate: stint starts 1939, birth 1900 (age 39)
- [PASS] colony: 4 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 4 event tenure(s) overlap stint years 1939-1951
- [FAIL] position_sim: best 45 vs bar 60: 'asst. supt. of police' ~ 'Superintendent, Assistant Superintendent and Cadet'
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

