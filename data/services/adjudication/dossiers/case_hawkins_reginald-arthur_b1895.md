<!-- {"case_id": "case_hawkins_reginald-arthur_b1895", "bio_ids": ["hawkins_reginald-arthur_b1895"], "stint_ids": ["Hawkins, R. A___Kenya___1922"]} -->
# Dossier case_hawkins_reginald-arthur_b1895

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 16 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hawkins_reginald-arthur_b1895`

- Printed name: **HAWKINS, Reginald Arthur**
- Birth year: 1895 (attested in editions [1948, 1949])
- Appears in editions: [1948, 1949]

### Verbatim printed entry text (OCR)

**Version `col1948-L33234.v` — printed in editions [1948, 1949]:**

> HAWKINS, Reginald Arthur.—b. 1895; ed. Eveswell Sch., Newport, Mon.; on mil. serv. 1914-18; clk., vet. dept., E.A.P., 1920; asst. supt., land dept., Ken., 1929; registr. of titles, 1930.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1920 | clk., vet. dept. | East Africa Protectorate | [1948, 1949] |
| 1 | 1929 | asst. supt., land dept. | Kenya | [1948, 1949] |
| 2 | 1930 | registr. of titles | Kenya *(inherited from previous clause)* | [1948, 1949] |

## Candidate stint `Hawkins, R. A___Kenya___1922`

- Staff-list name: **Hawkins, R. A** | colony: **Kenya** | listed 1922–1940 | editions [1922, 1923, 1924, 1927, 1928, 1929, 1930, 1931, 1932, 1934, 1936, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | R. A. Hawkins | Clerk | Veterinary | — | — |
| 1923 | R. A. Hawkins | Clerk | Veterinary | — | — |
| 1924 | R. A. Hawkins | Clerks | Agricultural | — | — |
| 1927 | R. A. Hawkins | Clerks | Department of Lands | — | — |
| 1928 | R. A. Hawkins | Clerks | Land Registry Division | — | — |
| 1929 | R. A. Hawkins | Clerks | Registration Division | — | — |
| 1930 | R. A. Hawkins | Clerk | Registration Division | — | — |
| 1931 | R. A. Hawkins | Office Superintendent | Survey and Registration Department | — | — |
| 1932 | R. A. Hawkins | Registrar of Titles | Survey and Registration Department | — | — |
| 1934 | R. A. Hawkins | Registrar of Titles | Survey and Registration Department | — | — |
| 1936 | R. A. Hawkins | Registrars of Titles | Local Government, Lands and Settlement | — | — |
| 1937 | R. A. Hawkins | Registrar of Titles | Local Government, Lands and Settlement | — | — |
| 1939 | R. A. Hawkins | Registrars of Titles | Lands and Settlement | — | — |
| 1940 | R. A. Hawkins | Registrar of Titles | Lands and Settlement | — | — |

### Deterministic checks: `hawkins_reginald-arthur_b1895` vs `Hawkins, R. A___Kenya___1922`

- [PASS] surname_gate: bio 'HAWKINS' vs stint 'Hawkins, R. A' (exact)
- [PASS] initials: bio ['R', 'A'] ~ stint ['R', 'A']
- [PASS] age_gate: stint starts 1922, birth 1895 (age 27)
- [PASS] colony: 3 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1922-1940
- [PASS] position_sim: best 94 vs bar 60: 'registr. of titles' ~ 'Registrar of Titles'
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

