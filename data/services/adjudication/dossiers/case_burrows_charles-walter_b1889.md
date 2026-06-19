<!-- {"case_id": "case_burrows_charles-walter_b1889", "bio_ids": ["burrows_charles-walter_b1889"], "stint_ids": ["Burrows, W___Fiji___1925"]} -->
# Dossier case_burrows_charles-walter_b1889

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 21 official(s) with this surname in the graph's staff lists; 12 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Burrows, W___Fiji___1925` is also gate-compatible with biography(ies) outside this case: ['burrows_f-w_e1845', 'burrows_william_b1883'] (already linked elsewhere or filtered).

## Biography `burrows_charles-walter_b1889`

- Printed name: **BURROWS, Charles Walter**
- Birth year: 1889 (attested in editions [1950])
- Appears in editions: [1950]

### Verbatim printed entry text (OCR)

**Version `col1950-L34089.v` — printed in editions [1950]:**

> BURROWS, Charles Walter.—b. 1889; ed. St. Dunstan's Coll.; apptd. F.O., 1907; admry., 1908; N.H.I. comsnr., 1912; admry., 1914-20; min. health, 1920; min. labour, 1921; seconded as industrial advr., Trin., 1944; lab. advr., col. dev. and welf., 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1907 | apptd. F.O | — | [1950] |
| 1 | 1908 | admry | — | [1950] |
| 2 | 1912 | N.H.I. comsnr | — | [1950] |
| 3 | 1914–1920 | admry | — | [1950] |
| 4 | 1920 | min. health | — | [1950] |
| 5 | 1921 | min. labour | — | [1950] |
| 6 | 1944 | seconded as industrial advr. | Trinidad | [1950] |
| 7 | 1946 | lab. advr., col. dev. and welf | Trinidad *(inherited from previous clause)* | [1950] |

## Candidate stint `Burrows, W___Fiji___1925`

- Staff-list name: **Burrows, W** | colony: **Fiji** | listed 1925–1940 | editions [1925, 1927, 1928, 1929, 1930, 1932, 1933, 1934, 1936, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1925 | W. Burrows | District Commissioner | District Administration | — | — |
| 1927 | W. Burrows | District Commissioner | District Administration | — | — |
| 1928 | W. Burrows | District Commissioner | District Administration | — | — |
| 1929 | W. Burrows | District Commissioner | District Administration | — | — |
| 1930 | W. Burrows | District Commissioner | District Administration | — | — |
| 1932 | W. Burrows | District Commissioner | District Administration | — | — |
| 1933 | W. Burrows | District Commissioner | District Administration | — | — |
| 1934 | W. Burrows | District Commissioner | District Administration | — | — |
| 1936 | W. Burrows | District Commissioners | District Administration | — | — |
| 1937 | W. Burrows | District Commissioners | District Administration | — | — |
| 1939 | W. Burrows | Administrative Officer, Grade II | District Administration | — | — |
| 1940 | W. Burrows | Administrative Officer, Grade II | District Administration | — | Commander |

### Deterministic checks: `burrows_charles-walter_b1889` vs `Burrows, W___Fiji___1925`

- [PASS] surname_gate: bio 'BURROWS' vs stint 'Burrows, W' (exact)
- [PASS] initials: bio ['C', 'W'] ~ stint ['W']
- [PASS] age_gate: stint starts 1925, birth 1889 (age 36)
- [FAIL] colony: no placed event resolves to 'Fiji'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1925-1940
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

