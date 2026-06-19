<!-- {"case_id": "case_larter_l-n-h_b1908", "bio_ids": ["larter_l-n-h_b1908", "larter_leslie-n-h_e1930"], "stint_ids": ["Larter, L. N. H___Jamaica___1933"]} -->
# Dossier case_larter_l-n-h_b1908

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Larter, L. N. H___Jamaica___1933'] have more than one claimant biography in this case.
- Phase 1 found `larter_l-n-h_b1908` ↔ `Larter, L. N. H___Jamaica___1933` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- Phase 1 found `larter_leslie-n-h_e1930` ↔ `Larter, L. N. H___Jamaica___1933` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).

## Biography `larter_l-n-h_b1908`

- Printed name: **LARTER, L. N. H**
- Birth year: 1908 (attested in editions [1956, 1957])
- Appears in editions: [1956, 1957]

### Verbatim printed entry text (OCR)

**Version `col1956-L22415.v` — printed in editions [1956, 1957]:**

> LARTER, L. N. H.—b. 1908 ; ed. Latymer Upper Sch., London, London and Camb. Univs. and I.C.T.A.; geneticist, J'ca, 1932; botanist, 1936; senr., 1943; botanist, Mal., 1947; senr., 1952; ag. ch. research offr., 1955.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1932 | geneticist | Jamaica | [1956, 1957] |
| 1 | 1936 | botanist | Jamaica *(inherited from previous clause)* | [1956, 1957] |
| 2 | 1943 | senr | Jamaica *(inherited from previous clause)* | [1956, 1957] |
| 3 | 1947 | botanist | Malaya | [1956, 1957] |
| 4 | 1952 | senr | Malaya *(inherited from previous clause)* | [1956, 1957] |
| 5 | 1955 | ag. ch. research offr | Malaya *(inherited from previous clause)* | [1956, 1957] |

## Biography `larter_leslie-n-h_e1930`

- Printed name: **LARTER, Leslie N. H**
- Birth year: not printed
- Honours: A.I.C.T.A, A.R.C.S
- Appears in editions: [1935, 1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `dol1935-L60156.v` — printed in editions [1935, 1936, 1937, 1939, 1940]:**

> LARTER, Leslie N. H., B.Sc., A.R.C.S., A.I.C.T.A.—Ed. Imp. Coll. (Lond.), schol. and medallist, graduated (1st cls. honors), 1929; col. agrl. schol., Fitzwilliam House, Camb., and Imp. Coll. of Trop. Agr., Trinidad, 1930-32; geneticist, Jamaica, Nov., 1932.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1930–1932 | col. agrl. schol., Fitzwilliam House, Camb., and Imp. Coll. of Trop. Agr. | Trinidad | [1935, 1936, 1937, 1939, 1940] |
| 1 | 1932 | geneticist | Jamaica | [1935, 1936, 1937, 1939, 1940] |

## Candidate stint `Larter, L. N. H___Jamaica___1933`

- Staff-list name: **Larter, L. N. H** | colony: **Jamaica** | listed 1933–1940 | editions [1933, 1934, 1937, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | L. N. H. Larter | Geneticist | Department of Science and Agriculture | — | — |
| 1934 | L. N. H. Larter | Geneticist | Department of Science and Agriculture | — | — |
| 1937 | L. N. H. Larter | Botanist | Department of Science and Agriculture | — | — |
| 1940 | L. N. H. Larter | Botanist | Department of Science and Agriculture | — | — |

### Deterministic checks: `larter_l-n-h_b1908` vs `Larter, L. N. H___Jamaica___1933`

- [PASS] surname_gate: bio 'LARTER' vs stint 'Larter, L. N. H' (exact)
- [PASS] initials: bio ['L', 'N', 'H'] ~ stint ['L', 'N', 'H']
- [PASS] age_gate: stint starts 1933, birth 1908 (age 25)
- [PASS] colony: 3 placed event(s) resolve to 'Jamaica'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1933-1940
- [PASS] position_sim: best 100 vs bar 60: 'geneticist' ~ 'Geneticist'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

### Deterministic checks: `larter_leslie-n-h_e1930` vs `Larter, L. N. H___Jamaica___1933`

- [PASS] surname_gate: bio 'LARTER' vs stint 'Larter, L. N. H' (exact)
- [PASS] initials: bio ['L', 'N', 'H'] ~ stint ['L', 'N', 'H']
- [PASS] age_gate: stint starts 1933; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Jamaica'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1933-1940
- [PASS] position_sim: best 100 vs bar 60: 'geneticist' ~ 'Geneticist'
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

