<!-- {"case_id": "case_mulligan_hugh-waddell_b1901", "bio_ids": ["mulligan_hugh-waddell_b1901"], "stint_ids": ["Mulligan, H. W___Nigeria___1949"]} -->
# Dossier case_mulligan_hugh-waddell_b1901

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mulligan_hugh-waddell_b1901`

- Printed name: **MULLIGAN, Hugh Waddell**
- Birth year: 1901 (attested in editions [1949, 1950, 1951])
- Honours: C.M.G (1954), D.T.M, M.D
- Appears in editions: [1949, 1950, 1951, 1953, 1954]

### Verbatim printed entry text (OCR)

**Version `col1949-L34500.v` — printed in editions [1949, 1950, 1951]:**

> MULLIGAN, Hugh Waddell, M.D., Ch.B., D.Sc., D.T.M.—b. 1901; ed. Robert Gordon’s Coll., Aberdeen and Aberdeen Univ., M.D. (hons. and gold medal); on mil. serv. 1940–43, col. (a/brig.); apptd. 1923; med. offr., India, 1923–47; Nig., 1947; lecturer, L/N., 1936–37; health surv. & devel. comttee, India, 1943–45; numerous papers on protozoology, immunology, pathology, etc.

**Version `col1953-L18528.v` — printed in editions [1953, 1954]:**

> MULLIGAN, H. W., C.M.G. (1954).—b. 1901; ed. Robert Gordon's Coll., Aberdeen, and Aberdeen and Chicago Unv.; mil. serv., 1940-43, col.; I.M.S., 1923; dir., W.A. inst. for trypan. research, 1947; lecturer, L/N., 1936-37; health surv. and dev. comttee., India, 1943-45; numerous papers on protozoology, immunology, pathology, etc.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1923 | apptd | — | [1949, 1950, 1951] |
| 1 | 1923–1947 | med. offr., India | — | [1949, 1950, 1951] |
| 2 | 1923 | I.M.S | — | [1953, 1954] |
| 3 | 1936–1937 | lecturer, L/N | Nigeria *(inherited from previous clause)* | [1949, 1950, 1951, 1953, 1954] |
| 4 | 1943–1945 | health surv. & devel. comttee, India | Nigeria *(inherited from previous clause)* | [1949, 1950, 1951, 1953, 1954] |
| 5 | 1947 | med. offr., India | Nigeria | [1949, 1950, 1951] |
| 6 | 1947 | dir., W.A. inst. for trypan. research | — | [1953, 1954] |

## Candidate stint `Mulligan, H. W___Nigeria___1949`

- Staff-list name: **Mulligan, H. W** | colony: **Nigeria** | listed 1949–1952 | editions [1949, 1952]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | H. W. Mulligan | Director, West African Institute for Trypanosomiasis Research | Sleeping Sickness Service | — | Colonel |
| 1952 | H. W. Mulligan | Director (Nigerian Organisation) of West African Institute for Trypanosomiasis Research | Civil Establishment | — | Colonel |

### Deterministic checks: `mulligan_hugh-waddell_b1901` vs `Mulligan, H. W___Nigeria___1949`

- [PASS] surname_gate: bio 'MULLIGAN' vs stint 'Mulligan, H. W' (exact)
- [PASS] initials: bio ['H', 'W'] ~ stint ['H', 'W']
- [PASS] age_gate: stint starts 1949, birth 1901 (age 48)
- [PASS] colony: 3 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1952
- [FAIL] position_sim: best 22 vs bar 60: 'med. offr., India' ~ 'Director, West African Institute for Trypanosomiasis Research'
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

