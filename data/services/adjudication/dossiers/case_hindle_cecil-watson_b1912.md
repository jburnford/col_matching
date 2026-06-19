<!-- {"case_id": "case_hindle_cecil-watson_b1912", "bio_ids": ["hindle_cecil-watson_b1912"], "stint_ids": ["Hindle, C. W___Kenya___1939"]} -->
# Dossier case_hindle_cecil-watson_b1912

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hindle_cecil-watson_b1912`

- Printed name: **HINDLE, Cecil Watson**
- Birth year: 1912 (attested in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962])
- Appears in editions: [1948, 1949, 1950, 1951, 1956, 1957, 1958, 1959, 1960, 1961, 1962]

### Verbatim printed entry text (OCR)

**Version `col1956-L21888.v` — printed in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962]:**

> HINDLE, C. W.—b. 1912; ed. Prince of Wales Sch., Nairobi; survey cadet, Ken., 1929; staff survr., 1936; comsnr., lands, B.S.I.P., 1946; survr., Tang., 1952; supt. of surveys, 1955; chief survr., 1960.

**Version `col1948-L33347.v` — printed in editions [1948, 1949, 1950, 1951]:**

> HINDLE, Cecil Watson.—b. 1912; ed. Prince of Wales Sch., Nairobi; licensed survr.; survey cadet, Ken., 1929; staff survr., 1936; comsnr. of lands, Br. Sol. Is. Prot., 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1929 | survey cadet | Kenya | [1948, 1949, 1950, 1951, 1956, 1957, 1958, 1959, 1960, 1961, 1962] |
| 1 | 1936 | staff survr | Kenya *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1956, 1957, 1958, 1959, 1960, 1961, 1962] |
| 2 | 1946 | comsnr., lands, B.S.I.P | Kenya *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1956, 1957, 1958, 1959, 1960, 1961, 1962] |
| 3 | 1952 | survr. | Tanganyika | [1956, 1957, 1958, 1959, 1960, 1961, 1962] |
| 4 | 1955 | supt. of surveys | Tanganyika *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962] |
| 5 | 1960 | chief survr | Tanganyika *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962] |

## Candidate stint `Hindle, C. W___Kenya___1939`

- Staff-list name: **Hindle, C. W** | colony: **Kenya** | listed 1939–1940 | editions [1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | C. W. Hindle | Staff Surveyors | Lands and Settlement | — | — |
| 1940 | C. W. Hindle | Staff Surveyors | Lands and Settlement | — | — |

### Deterministic checks: `hindle_cecil-watson_b1912` vs `Hindle, C. W___Kenya___1939`

- [PASS] surname_gate: bio 'HINDLE' vs stint 'Hindle, C. W' (exact)
- [PASS] initials: bio ['C', 'W'] ~ stint ['C', 'W']
- [PASS] age_gate: stint starts 1939, birth 1912 (age 27)
- [PASS] colony: 3 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1939-1940
- [PASS] position_sim: best 85 vs bar 60: 'staff survr' ~ 'Staff Surveyors'
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

