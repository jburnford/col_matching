<!-- {"case_id": "case_finlay_thomas-victor-william_b1899", "bio_ids": ["finlay_thomas-victor-william_b1899"], "stint_ids": ["Finlay, T. V. W___Nigeria___1929"]} -->
# Dossier case_finlay_thomas-victor-william_b1899

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 21 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `finlay_thomas-victor-william_b1899`

- Printed name: **FINLAY, Thomas Victor William**
- Birth year: 1899 (attested in editions [1948, 1949, 1950])
- Honours: C.M.G (1948)
- Appears in editions: [1948, 1949, 1950]

### Verbatim printed entry text (OCR)

**Version `col1948-L32585.v` — printed in editions [1948, 1949, 1950]:**

> FINLAY, Thomas Victor William, C.M.G. (1948).—b. 1899; ed. King's Hosp., Dublin; on mil. serv. 1918-19; apptd. col. police, 1925; supt., 1937; asst. comsnr., Nig., 1943; dep. comsnr., 1945; comsnr., 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1925 | apptd. col. police | — | [1948, 1949, 1950] |
| 1 | 1937 | supt | — | [1948, 1949, 1950] |
| 2 | 1943 | asst. comsnr. | Nigeria | [1948, 1949, 1950] |
| 3 | 1945 | dep. comsnr | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950] |
| 4 | 1946 | comsnr | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950] |

## Candidate stint `Finlay, T. V. W___Nigeria___1929`

- Staff-list name: **Finlay, T. V. W** | colony: **Nigeria** | listed 1929–1939 | editions [1929, 1930, 1933, 1934, 1936, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1929 | T. V. W. Finlay | Commissioners and Assistant Commissioners | Marine | — | — |
| 1930 | T. V. W. Finlay | Commissioners and Assistant Commissioners | Police | — | — |
| 1933 | T. V. W. Finlay | Commissioner/Assistant Commissioner | Police | — | — |
| 1934 | T. V. W. Finlay | Commissioner/Assistant Commissioner | Police | — | — |
| 1936 | T. V. W. Finlay | Commissioners and Assistant Commissioners | Police | — | — |
| 1939 | T. V. W. Finlay | Superintendent | Police | — | — |

### Deterministic checks: `finlay_thomas-victor-william_b1899` vs `Finlay, T. V. W___Nigeria___1929`

- [PASS] surname_gate: bio 'FINLAY' vs stint 'Finlay, T. V. W' (exact)
- [PASS] initials: bio ['T', 'V', 'W'] ~ stint ['T', 'V', 'W']
- [PASS] age_gate: stint starts 1929, birth 1899 (age 30)
- [PASS] colony: 3 placed event(s) resolve to 'Nigeria'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1929-1939
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

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

