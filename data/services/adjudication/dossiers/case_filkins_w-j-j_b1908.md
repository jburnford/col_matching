<!-- {"case_id": "case_filkins_w-j-j_b1908", "bio_ids": ["filkins_w-j-j_b1908"], "stint_ids": ["Filkins, W. J___Uganda___1949"]} -->
# Dossier case_filkins_w-j-j_b1908

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `filkins_w-j-j_b1908`

- Printed name: **FILKINS, W. J. J**
- Birth year: 1908 (attested in editions [1957, 1958, 1960, 1961, 1962])
- Appears in editions: [1957, 1958, 1960, 1961, 1962]

### Verbatim printed entry text (OCR)

**Version `col1957-L22998.v` — printed in editions [1957, 1958, 1960, 1961, 1962]:**

> FILKINS, W. J. J.—b. 1908; ed. Ethelburga St. Sch. and St. Thos. Hosp. Med. Sch.; supt., physiol. lab., Uga., 1944–61.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1944–1961 | supt., physiol. lab. | Uganda | [1957, 1958, 1960, 1961, 1962] |

## Candidate stint `Filkins, W. J___Uganda___1949`

- Staff-list name: **Filkins, W. J** | colony: **Uganda** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | W. J. Filkins | Physiological Laboratory Superintendent | Medical | — | — |
| 1951 | W. Filkins | Physiological Laboratory Superintendent | MEDICAL | — | — |

### Deterministic checks: `filkins_w-j-j_b1908` vs `Filkins, W. J___Uganda___1949`

- [PASS] surname_gate: bio 'FILKINS' vs stint 'Filkins, W. J' (exact)
- [PASS] initials: bio ['W', 'J', 'J'] ~ stint ['W', 'J']
- [PASS] age_gate: stint starts 1949, birth 1908 (age 41)
- [PASS] colony: 1 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 58 vs bar 60: 'supt., physiol. lab.' ~ 'Physiological Laboratory Superintendent'
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

