<!-- {"case_id": "case_ballantine_richard-waverley-head_b1896", "bio_ids": ["ballantine_richard-waverley-head_b1896"], "stint_ids": ["Ballantine, R. W. H___Nigeria___1929"]} -->
# Dossier case_ballantine_richard-waverley-head_b1896

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `ballantine_richard-waverley-head_b1896`

- Printed name: **BALLANTINE, Richard Waverley Head**
- Birth year: 1896 (attested in editions [1948])
- Honours: C.B.E
- Appears in editions: [1948]

### Verbatim printed entry text (OCR)

**Version `col1948-L30953.v` — printed in editions [1948]:**

> BALLANTINE, Richard Waverley Head, C.B.E.—b. 1896; ed. Ormond Coll., Dublin; on mil. serv. 1914-20; dist. inspr., R.I.C., 1920; apptd. Nig. police, 1922; asst. comsnr., 1938; dep. inspr. gen. police, Pal., 1941; comsnr. of police, G.C., 1944.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1920 | dist. inspr., R.I.C | — | [1948] |
| 1 | 1922 | apptd. Nig. police | — | [1948] |
| 2 | 1938 | asst. comsnr | — | [1948] |
| 3 | 1941 | dep. inspr. gen. police | Palestine | [1948] |
| 4 | 1944 | comsnr. of police | Gold Coast | [1948] |

## Candidate stint `Ballantine, R. W. H___Nigeria___1929`

- Staff-list name: **Ballantine, R. W. H** | colony: **Nigeria** | listed 1929–1939 | editions [1929, 1930, 1933, 1934, 1936, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1929 | R. W. H. Ballantine | Commissioners and Assistant Commissioners | Marine | M.C. | Captain |
| 1930 | Capt. R. W. H. Ballantine | Commissioners and Assistant Commissioners | Police | — | Captain |
| 1933 | R. W. H. Ballantine | Commissioner/Assistant Commissioner | Police | — | Captain |
| 1934 | R. W. H. Ballantine | Commissioner/Assistant Commissioner | Police | — | Captain |
| 1936 | R. W. H. Ballantine | Commissioners and Assistant Commissioners | Police | — | Captain |
| 1939 | Capt. R. W. H. Ballantine | Superintendent | Police | — | Captain |

### Deterministic checks: `ballantine_richard-waverley-head_b1896` vs `Ballantine, R. W. H___Nigeria___1929`

- [PASS] surname_gate: bio 'BALLANTINE' vs stint 'Ballantine, R. W. H' (exact)
- [PASS] initials: bio ['R', 'W', 'H'] ~ stint ['R', 'W', 'H']
- [PASS] age_gate: stint starts 1929, birth 1896 (age 33)
- [FAIL] colony: no placed event resolves to 'Nigeria'
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

