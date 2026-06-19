<!-- {"case_id": "case_monckton_hugh_b1881", "bio_ids": ["monckton_hugh_b1881"], "stint_ids": ["Monckton, H. L___Leeward Islands___1905"]} -->
# Dossier case_monckton_hugh_b1881

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['monckton_hugh_b1881'] carry a single initial only — the namesake trap applies.

## Biography `monckton_hugh_b1881`

- Printed name: **MONCKTON, HUGH**
- Birth year: 1881 (attested in editions [1937, 1939, 1940])
- Appears in editions: [1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1937-L63234.v` — printed in editions [1937, 1939, 1940]:**

> MONCKTON, HUGH, CLAUD.—B. 1881; ed. Bradfield Coll., Berks; clk., native dept., Fiji, 1901; cadet, 1504; ch. clk., native dept., 1907; stip. mag., 1912; acct. and asst. stip. mag., 1913; dist. commnr., Ra., 1914; do., Nandronga, and Tholo West, nom. M.L.C., 1930; ag. sec. for native affrs., 1935; M.E.C., 1935; oll., M.L.C., 1937; advr. on native affrs., 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1901 | clk., native dept. | Fiji | [1937, 1939, 1940] |
| 1 | 1907 | ch. clk., native dept | Fiji *(inherited from previous clause)* | [1937, 1939, 1940] |
| 2 | 1912 | stip. mag | Fiji *(inherited from previous clause)* | [1937, 1939, 1940] |
| 3 | 1913 | acct. and asst. stip. mag | Fiji *(inherited from previous clause)* | [1937, 1939, 1940] |
| 4 | 1914 | dist. commnr., Ra | Fiji *(inherited from previous clause)* | [1937, 1939, 1940] |
| 5 | 1930 | do., Nandronga, and Tholo West, nom. M.L.C | Fiji *(inherited from previous clause)* | [1937, 1939, 1940] |
| 6 | 1935 | ag. sec. for native affrs | Fiji *(inherited from previous clause)* | [1937, 1939, 1940] |
| 7 | 1937 | oll., M.L.C | Fiji *(inherited from previous clause)* | [1937, 1939, 1940] |
| 8 | 1938 | advr. on native affrs | Fiji *(inherited from previous clause)* | [1937, 1939, 1940] |

## Candidate stint `Monckton, H. L___Leeward Islands___1905`

- Staff-list name: **Monckton, H. L** | colony: **Leeward Islands** | listed 1905–1907 | editions [1905, 1906, 1907]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | H. L. Monckton | Chief Minister of Religion | Chief Ministers of Religion | — | — |
| 1906 | Rev. H. L. Monckton | Chief Minister of Religion | Chief Ministers of Religion | — | — |
| 1907 | Rev. H. L. Monckton | Chief Minister of Religion | Chief Ministers of Religion | — | — |

### Deterministic checks: `monckton_hugh_b1881` vs `Monckton, H. L___Leeward Islands___1905`

- [PASS] surname_gate: bio 'MONCKTON' vs stint 'Monckton, H. L' (exact)
- [PASS] initials: bio ['H'] ~ stint ['H', 'L']
- [PASS] age_gate: stint starts 1905, birth 1881 (age 24)
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1907
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

