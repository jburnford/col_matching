<!-- {"case_id": "case_whitley_thomas-sydney-douglas_b1909", "bio_ids": ["whitley_thomas-sydney-douglas_b1909"], "stint_ids": ["Whitley, T. S. D___Hong Kong___1950"]} -->
# Dossier case_whitley_thomas-sydney-douglas_b1909

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `whitley_thomas-sydney-douglas_b1909`

- Printed name: **WHITLEY, Thomas Sydney Douglas**
- Birth year: 1909 (attested in editions [1950, 1951])
- Appears in editions: [1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1950-L40689.v` — printed in editions [1950, 1951]:**

> WHITLEY, Thomas Sydney Douglas.—b. 1909; H.K.V.D.C., 1941-45; prob'r.; senr. cler. and acctg. staff, H.K., 1928; senr. exec. offr., cl. II, 1947.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | senr. cler. and acctg. staff | Hong Kong | [1950, 1951] |
| 1 | 1941–1945 | H.K.V.D.C | — | [1950, 1951] |
| 2 | 1947 | senr. exec. offr., cl. II | Hong Kong *(inherited from previous clause)* | [1950, 1951] |

## Candidate stint `Whitley, T. S. D___Hong Kong___1950`

- Staff-list name: **Whitley, T. S. D** | colony: **Hong Kong** | listed 1950–1952 | editions [1950, 1952]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | T. S. D. Whitley | Organisation and Methods Officer | Secretariat | — | — |
| 1952 | T. S. D. Whitley | Quartering Authority | Civil Establishment | — | — |

### Deterministic checks: `whitley_thomas-sydney-douglas_b1909` vs `Whitley, T. S. D___Hong Kong___1950`

- [PASS] surname_gate: bio 'WHITLEY' vs stint 'Whitley, T. S. D' (exact)
- [PASS] initials: bio ['T', 'S', 'D'] ~ stint ['T', 'S', 'D']
- [PASS] age_gate: stint starts 1950, birth 1909 (age 41)
- [PASS] colony: 2 placed event(s) resolve to 'Hong Kong'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1950-1952
- [FAIL] position_sim: best 38 vs bar 60: 'senr. exec. offr., cl. II' ~ 'Organisation and Methods Officer'
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

