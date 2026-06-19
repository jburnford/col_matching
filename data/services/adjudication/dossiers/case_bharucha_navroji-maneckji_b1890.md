<!-- {"case_id": "case_bharucha_navroji-maneckji_b1890", "bio_ids": ["bharucha_navroji-maneckji_b1890"], "stint_ids": ["Bharucha, N. M___Ceylon___1920"]} -->
# Dossier case_bharucha_navroji-maneckji_b1890

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Bharucha, N. M___Ceylon___1920` is also gate-compatible with biography(ies) outside this case: ['bharucha_navroji-manekji_b1890'] (already linked elsewhere or filtered).

## Biography `bharucha_navroji-maneckji_b1890`

- Printed name: **BHARUCHA, Navroji Maneckji**
- Birth year: 1890 (attested in editions [1915])
- Appears in editions: [1915]

### Verbatim printed entry text (OCR)

**Version `col1915-L45235.v` — printed in editions [1915]:**

> BHARUCHA, Navroji Maneckji.—B. 1890; B.A., Cantab, cadet, Ceylon civ. ser., Jan., 1914; office asst. to gov’t. agt., N.W. Prov., Jan., 1914; attached to Kurunegala Kach., June, 1914.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914 | B.A., Cantab, cadet, Ceylon civ. ser | Ceylon | [1915] |

## Candidate stint `Bharucha, N. M___Ceylon___1920`

- Staff-list name: **Bharucha, N. M** | colony: **Ceylon** | listed 1920–1937 | editions [1920, 1921, 1922, 1923, 1925, 1927, 1929, 1934, 1936, 1937]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1920 | N. M. Bharucha | Commissioner of Requests and Police Magistrate | Judicial Establishment | — | — |
| 1921 | N. M. Bharucha | Commissioner of Requests | Southern Circuit | — | — |
| 1922 | N. M. Bharucha | Assistant Collector and Landing Surveyor | Northern Province | — | — |
| 1923 | N. M. Bharucha | District Judge, Commissioner of Requests, Police Magistrate | Northern Circuit | — | — |
| 1925 | N. M. Bharucha | District Judge, Commissioner of Requests, Police Magistrate | Judicial Establishment | — | — |
| 1927 | N. M. Bharucha | Assistant Settlement Officer | Land Settlement Department | — | — |
| 1929 | N. M. Bharucha | District Judge | District of Colombo and Midland Circuit | — | — |
| 1934 | N. M. Bharucha | District Judge | District Judges, Commissioners of Requests, Police Magistrates and Municipal Magistrates | — | — |
| 1936 | N. M. Bharucha | District Judge, Commissioner of Requests and Police Magistrate | District Judges, Commissioners of Requests, Police Magistrates and Municipal Magistrates | — | — |
| 1937 | N. M. Bharucha | Assistant Collector of Customs | Western Province | — | — |
| 1937 | N. M. Bharucha | District Judge | District Judges, Commissioners of Requests, Police Magistrates and Municipal Magistrates | — | — |

### Deterministic checks: `bharucha_navroji-maneckji_b1890` vs `Bharucha, N. M___Ceylon___1920`

- [PASS] surname_gate: bio 'BHARUCHA' vs stint 'Bharucha, N. M' (exact)
- [PASS] initials: bio ['N', 'M'] ~ stint ['N', 'M']
- [PASS] age_gate: stint starts 1920, birth 1890 (age 30)
- [PASS] colony: 1 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1920-1937
- [FAIL] position_sim: best 49 vs bar 60: 'B.A., Cantab, cadet, Ceylon civ. ser' ~ 'Assistant Collector and Landing Surveyor'
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

