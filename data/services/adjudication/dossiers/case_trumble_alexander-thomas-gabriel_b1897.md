<!-- {"case_id": "case_trumble_alexander-thomas-gabriel_b1897", "bio_ids": ["trumble_alexander-thomas-gabriel_b1897"], "stint_ids": ["Trumble, A. T. G___Nigeria___1929"]} -->
# Dossier case_trumble_alexander-thomas-gabriel_b1897

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `trumble_alexander-thomas-gabriel_b1897`

- Printed name: **TRUMBLE, Alexander Thomas Gabriel**
- Birth year: 1897 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L36497.v` — printed in editions [1948, 1949, 1950, 1951]:**

> TRUMBLE, Alexander Thomas Gabriel.—b. 1897; ed. St. Dunstan's Coll., Catford, Lond.; on mil. serv. 1914–19, 2nd lieut.; asst. acctnt., marine dept., 1923; police, Nig., 1927; supt., 1942; senr., 1949.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1923 | asst. acctnt., marine dept | — | [1948, 1949, 1950, 1951] |
| 1 | 1927 | police | Nigeria | [1948, 1949, 1950, 1951] |
| 2 | 1942 | supt | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 3 | 1949 | senr | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Trumble, A. T. G___Nigeria___1929`

- Staff-list name: **Trumble, A. T. G** | colony: **Nigeria** | listed 1929–1939 | editions [1929, 1930, 1933, 1934, 1936, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1929 | A. T. G. Trumble | Commissioners and Assistant Commissioners | Marine | — | — |
| 1930 | A. T. G. Trumble | Commissioners and Assistant Commissioners | Police | — | — |
| 1933 | A. T. G. Trumble | Commissioner/Assistant Commissioner | Police | — | — |
| 1934 | A. T. G. Trumble | Commissioner/Assistant Commissioner | Police | — | — |
| 1936 | A. T. G. Trumble | Commissioners and Assistant Commissioners | Police | — | — |
| 1939 | A. T. G. Trumble | Senior Assistant Superintendent | Police | — | — |

### Deterministic checks: `trumble_alexander-thomas-gabriel_b1897` vs `Trumble, A. T. G___Nigeria___1929`

- [PASS] surname_gate: bio 'TRUMBLE' vs stint 'Trumble, A. T. G' (exact)
- [PASS] initials: bio ['A', 'T', 'G'] ~ stint ['A', 'T', 'G']
- [PASS] age_gate: stint starts 1929, birth 1897 (age 32)
- [PASS] colony: 3 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1929-1939
- [FAIL] position_sim: best 20 vs bar 60: 'police' ~ 'Commissioner/Assistant Commissioner'
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

