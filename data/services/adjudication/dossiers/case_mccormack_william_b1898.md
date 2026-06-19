<!-- {"case_id": "case_mccormack_william_b1898", "bio_ids": ["mccormack_william_b1898"], "stint_ids": ["McCormack, W___Mauritius___1936", "McCormack, W___Mauritius___1949"]} -->
# Dossier case_mccormack_william_b1898

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['mccormack_william_b1898'] carry a single initial only — the namesake trap applies.

## Biography `mccormack_william_b1898`

- Printed name: **McCORMACK, William**
- Birth year: 1898 (attested in editions [1948, 1949])
- Appears in editions: [1948, 1949]

### Verbatim printed entry text (OCR)

**Version `col1948-L34230.v` — printed in editions [1948, 1949]:**

> McCORMACK, William.—b. 1898; police, Maur., 1931; asst. ch. offr., prisons, 1935; senr. ch. offr., 1945.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1931 | police | Mauritius | [1948, 1949] |
| 1 | 1935 | asst. ch. offr., prisons | Mauritius *(inherited from previous clause)* | [1948, 1949] |
| 2 | 1945 | senr. ch. offr | Mauritius *(inherited from previous clause)* | [1948, 1949] |

## Candidate stint `McCormack, W___Mauritius___1936`

- Staff-list name: **McCormack, W** | colony: **Mauritius** | listed 1936–1939 | editions [1936, 1937, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | W. McCormack | Assistant Chief Officer | Prisons Department | — | — |
| 1937 | W. McCormack | Assistant Chief Officer | Prisons Department | — | — |
| 1939 | W. McCormack | Assistant Chief Officer | Prisons Department | — | — |

### Deterministic checks: `mccormack_william_b1898` vs `McCormack, W___Mauritius___1936`

- [PASS] surname_gate: bio 'McCORMACK' vs stint 'McCormack, W' (exact)
- [PASS] initials: bio ['W'] ~ stint ['W']
- [PASS] age_gate: stint starts 1936, birth 1898 (age 38)
- [PASS] colony: 3 placed event(s) resolve to 'Mauritius'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1936-1939
- [FAIL] position_sim: best 56 vs bar 60: 'asst. ch. offr., prisons' ~ 'Assistant Chief Officer'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `McCormack, W___Mauritius___1949`

- Staff-list name: **McCormack, W** | colony: **Mauritius** | listed 1949–1950 | editions [1949, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | W. McCormack | Assistant Superintendent | PRISONS AND INDUSTRIAL SCHOOL | — | — |
| 1950 | W. McCormack | Assistant Superintendent | PRISONS AND INDUSTRIAL SCHOOL | — | — |

### Deterministic checks: `mccormack_william_b1898` vs `McCormack, W___Mauritius___1949`

- [PASS] surname_gate: bio 'McCORMACK' vs stint 'McCormack, W' (exact)
- [PASS] initials: bio ['W'] ~ stint ['W']
- [PASS] age_gate: stint starts 1949, birth 1898 (age 51)
- [PASS] colony: 3 placed event(s) resolve to 'Mauritius'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1950
- [FAIL] position_sim: best 22 vs bar 60: 'senr. ch. offr' ~ 'Assistant Superintendent'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

