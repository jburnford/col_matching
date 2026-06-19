<!-- {"case_id": "case_plant_wilson_b1903", "bio_ids": ["plant_wilson_b1903"], "stint_ids": ["Plant, Wilson___Gambia___1936"]} -->
# Dossier case_plant_wilson_b1903

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['plant_wilson_b1903'] carry a single initial only — the namesake trap applies.

## Biography `plant_wilson_b1903`

- Printed name: **PLANT, Wilson**
- Birth year: 1903 (attested in editions [1948, 1949, 1950])
- Appears in editions: [1948, 1949, 1950]

### Verbatim printed entry text (OCR)

**Version `col1948-L35261.v` — printed in editions [1948, 1949, 1950]:**

> PLANT, Wilson.—b. 1903; ed. Gonville and Caius Coll., Cambridge, B.A. (hons.) (Cantab.); supt. of educ., Nig., 1927; admin. offr., Gambia, 1934; Nig., 1944.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1927 | supt. of educ. | Nigeria | [1948, 1949, 1950] |
| 1 | 1934 | admin. offr. | Gambia | [1948, 1949, 1950] |
| 2 | 1944 | admin. offr. | Nigeria | [1948, 1949, 1950] |

## Candidate stint `Plant, Wilson___Gambia___1936`

- Staff-list name: **Plant, Wilson** | colony: **Gambia** | listed 1936–1940 | editions [1936, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | Wilson Plant | Commissioners and Assistant Commissioners | Provincial Administration | — | — |
| 1937 | Wilson Plant | Assistant Commissioner | Provincial Administration | — | — |
| 1939 | Wilson Plant | Commissioners and Assistant Commissioners | Provincial Administration | — | — |
| 1940 | Wilson Plant | Commissioner/Assistant Commissioner | Provincial Administration | — | — |

### Deterministic checks: `plant_wilson_b1903` vs `Plant, Wilson___Gambia___1936`

- [PASS] surname_gate: bio 'PLANT' vs stint 'Plant, Wilson' (exact)
- [PASS] initials: bio ['W'] ~ stint ['W']
- [PASS] age_gate: stint starts 1936, birth 1903 (age 33)
- [PASS] colony: 1 placed event(s) resolve to 'Gambia'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1936-1940
- [FAIL] position_sim: best 38 vs bar 60: 'admin. offr.' ~ 'Commissioners and Assistant Commissioners'
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

