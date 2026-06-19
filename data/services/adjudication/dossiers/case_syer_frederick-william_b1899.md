<!-- {"case_id": "case_syer_frederick-william_b1899", "bio_ids": ["syer_frederick-william_b1899"], "stint_ids": ["Syer, F. W___Nigeria___1930"]} -->
# Dossier case_syer_frederick-william_b1899

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `syer_frederick-william_b1899`

- Printed name: **SYER, Frederick William**
- Birth year: 1899 (attested in editions [1948])
- Appears in editions: [1948]

### Verbatim printed entry text (OCR)

**Version `col1948-L36265.v` — printed in editions [1948]:**

> SYER, Frederick William.—b. 1899; ed. Kent Coll., Canterbury; on mil. serv., lt.-col.; apptd. police, Gib., 1920; senr. asst. supt., police, Nig., 1928; police, Pal., 1940; asst. inspr.-gen., 1943.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1920 | apptd. police | Gibraltar | [1948] |
| 1 | 1928 | senr. asst. supt., police | Nigeria | [1948] |
| 2 | 1940 | police | Palestine | [1948] |
| 3 | 1943 | asst. inspr.-gen | Palestine *(inherited from previous clause)* | [1948] |

## Candidate stint `Syer, F. W___Nigeria___1930`

- Staff-list name: **Syer, F. W** | colony: **Nigeria** | listed 1930–1939 | editions [1930, 1933, 1934, 1936, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1930 | F. W. Syer | Commissioners and Assistant Commissioners | Police | — | — |
| 1933 | F. W. Syer | Commissioner/Assistant Commissioner | Police | — | — |
| 1934 | F. W. Syer | Commissioner/Assistant Commissioner | Police | — | — |
| 1936 | F. W. Syer | Commissioners and Assistant Commissioners | Police | — | — |
| 1939 | F. W. Syer | Senior Assistant Superintendent | Police | — | — |

### Deterministic checks: `syer_frederick-william_b1899` vs `Syer, F. W___Nigeria___1930`

- [PASS] surname_gate: bio 'SYER' vs stint 'Syer, F. W' (exact)
- [PASS] initials: bio ['F', 'W'] ~ stint ['F', 'W']
- [PASS] age_gate: stint starts 1930, birth 1899 (age 31)
- [PASS] colony: 1 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1930-1939
- [FAIL] position_sim: best 54 vs bar 60: 'senr. asst. supt., police' ~ 'Senior Assistant Superintendent'
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

