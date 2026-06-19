<!-- {"case_id": "case_neff_ebroll-aubrey_b1887", "bio_ids": ["neff_ebroll-aubrey_b1887"], "stint_ids": ["Neff, E. A___Fiji___1922"]} -->
# Dossier case_neff_ebroll-aubrey_b1887

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `neff_ebroll-aubrey_b1887`

- Printed name: **NEFF, EBROLL AUBREY**
- Birth year: 1887 (attested in editions [1936, 1937, 1939, 1940])
- Honours: C.M.G. (1939)
- Appears in editions: [1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1936-L63306.v` — printed in editions [1936, 1937, 1939, 1940]:**

> NEFF, EBROLL AUBREY, C.M.G., 1939, M.D., L.C.P. & S. (Alberta), D.P.H., B. 1887; ed. High Schl., Ingersoll, Ont., Toronto Univ. and Western Univ.; on war serv. with rank of major, 1914-19; dist. med. offr., Fiji, and med. supt., Cent. Leper Hosp., Makogai, Fiji, 1921; two Rockefeller foundation fellowships, 1926 and 1931; rep. S. Pacific cols. at Internat. Leprosy Confce., Manila, 1931; senr. med. offr., (new dir. med. services), Cyprus, Nov., 1934.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914–1919 | war serv. with rank of major | — | [1936, 1937, 1939, 1940] |
| 1 | 1921 | dist. med. offr. and med. supt., Cent. Leper Hosp. | Fiji | [1936, 1937, 1939, 1940] |
| 2 | 1926–1931 | Rockefeller foundation fellowships | — | [1936, 1937, 1939, 1940] |
| 3 | 1931 | rep. S. Pacific cols. at Internat. Leprosy Confce. | — | [1936, 1937, 1939, 1940] |
| 4 | 1934 | senr. med. offr., (new dir. med. services) | Cyprus | [1936, 1937, 1939, 1940] |

## Candidate stint `Neff, E. A___Fiji___1922`

- Staff-list name: **Neff, E. A** | colony: **Fiji** | listed 1922–1934 | editions [1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1932, 1934]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | E. A. Neff | District Medical Officer | Medical Department | — | — |
| 1923 | E. A. Neff | District Medical Officer | Medical Department | — | — |
| 1924 | E. A. Neff | District Medical Officer | Medical Department | — | — |
| 1925 | E. A. Neff | District Medical Officers | Medical Department | — | — |
| 1927 | E. A. Neff | Medical Superintendent | Medical Department | — | — |
| 1928 | E. A. Neff | Medical Superintendent | Medical Department | — | — |
| 1929 | Dr. E. A. Neff | Medical Superintendent | Medical Department | — | — |
| 1930 | Dr. E. A. Neff | Medical Superintendent | Medical Department | — | — |
| 1932 | E. A. Neff | District Medical Officer | Medical Department | — | — |
| 1934 | E. A. Neff | District Medical Officer | Medical Department | — | — |

### Deterministic checks: `neff_ebroll-aubrey_b1887` vs `Neff, E. A___Fiji___1922`

- [PASS] surname_gate: bio 'NEFF' vs stint 'Neff, E. A' (exact)
- [PASS] initials: bio ['E', 'A'] ~ stint ['E', 'A']
- [PASS] age_gate: stint starts 1922, birth 1887 (age 35)
- [PASS] colony: 1 placed event(s) resolve to 'Fiji'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1922-1934
- [FAIL] position_sim: best 48 vs bar 60: 'dist. med. offr. and med. supt., Cent. Leper Hosp.' ~ 'District Medical Officers'
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

