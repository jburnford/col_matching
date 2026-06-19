<!-- {"case_id": "case_seamark_f-w-h_b1910", "bio_ids": ["seamark_f-w-h_b1910"], "stint_ids": ["Seamark, F. W. H___Sierra Leone___1949"]} -->
# Dossier case_seamark_f-w-h_b1910

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `seamark_f-w-h_b1910`

- Printed name: **SEAMARK, F. W. H**
- Birth year: 1910 (attested in editions [1958, 1959, 1960, 1961])
- Appears in editions: [1958, 1959, 1960, 1961, 1962, 1963]

### Verbatim printed entry text (OCR)

**Version `col1958-L26771.v` — printed in editions [1958, 1959, 1960, 1961]:**

> SEAMARK, F. W. H.—b. 1910; ed. Bedford Tech. Inst.; mil. serv., 1939-45; flt. lt. (desps. twice); storekpr., S.L., 1946; chief storekpr., 1947; supt., stores, Uga., 1952; redesign, chief storekpr., 1954; chmn., comtee. to invest price structure and availability of motor spares, S.L.

**Version `col1962-L26295.v` — printed in editions [1962, 1963]:**

> SEAMARK, F. W. H.—b. 1910; ed. Bedford Tech. Inst.; mil. serv., 1939-45, flt. lt. (desps. twice); storekpr., S.L., 1946; chief storekpr., 1947; supt., stores, Uga., 1952; redesig. chief storekpr., 1954-62. (Uga. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | storekpr. | Sierra Leone | [1958, 1959, 1960, 1961, 1962, 1963] |
| 1 | 1947 | chief storekpr | Sierra Leone *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963] |
| 2 | 1952 | supt., stores | Uganda | [1958, 1959, 1960, 1961, 1962, 1963] |
| 3 | 1954 | redesign, chief storekpr | Uganda *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963] |

## Candidate stint `Seamark, F. W. H___Sierra Leone___1949`

- Staff-list name: **Seamark, F. W. H** | colony: **Sierra Leone** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | F. W. H. Seamark | Chief Storekeeper | Public Works | — | — |
| 1950 | F. W. H. Seamark | Chief Storekeeper | Public Works | — | — |
| 1951 | F. W. H. Seamark | Chief Storekeeper | Public Works | — | — |

### Deterministic checks: `seamark_f-w-h_b1910` vs `Seamark, F. W. H___Sierra Leone___1949`

- [PASS] surname_gate: bio 'SEAMARK' vs stint 'Seamark, F. W. H' (exact)
- [PASS] initials: bio ['F', 'W', 'H'] ~ stint ['F', 'W', 'H']
- [PASS] age_gate: stint starts 1949, birth 1910 (age 39)
- [PASS] colony: 2 placed event(s) resolve to 'Sierra Leone'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [PASS] position_sim: best 90 vs bar 60: 'chief storekpr' ~ 'Chief Storekeeper'
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

