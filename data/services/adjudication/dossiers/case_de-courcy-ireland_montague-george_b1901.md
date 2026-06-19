<!-- {"case_id": "case_de-courcy-ireland_montague-george_b1901", "bio_ids": ["de-courcy-ireland_montague-george_b1901"], "stint_ids": ["de Courcy-Ireland, M. G___Uganda___1933"]} -->
# Dossier case_de-courcy-ireland_montague-george_b1901

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `de-courcy-ireland_montague-george_b1901`

- Printed name: **DE COURCY-IRELAND, Montague George**
- Birth year: 1901 (attested in editions [1951])
- Appears in editions: [1951]

### Verbatim printed entry text (OCR)

**Version `col1951-L37507.v` — printed in editions [1951]:**

> DE COURCY-IRELAND, Montague George.—b. 1901; ed. Lancing Coll. and Camb. Univ., B.A. (Cantab.); apptd. agric. dept., Uga., 1928; senr. agric. offr., 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | apptd. agric. dept. | Uganda | [1951] |
| 1 | 1946 | senr. agric. offr | Uganda *(inherited from previous clause)* | [1951] |

## Candidate stint `de Courcy-Ireland, M. G___Uganda___1933`

- Staff-list name: **de Courcy-Ireland, M. G** | colony: **Uganda** | listed 1933–1949 | editions [1933, 1936, 1937, 1939, 1940, 1949]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | M. G. de Courcy-Ireland | Agricultural Officer | Agricultural Department—Educational Division | — | — |
| 1936 | M. G. de Courcy-Ireland | Agricultural Officers | Agricultural Department—Educational Division | — | — |
| 1937 | M. G. de Courcy-Ireland | Agricultural Officer | Agricultural Department—Educational Division | — | — |
| 1939 | M. G. de Courcy-Ireland | Agricultural Officer | Agricultural Department | — | — |
| 1940 | M. G. de Courcy-Ireland | Agricultural Officer | Agricultural Department | — | — |
| 1949 | M. G. de Courcy-Ireland | Senior Agricultural Officer | Agricultural | — | — |

### Deterministic checks: `de-courcy-ireland_montague-george_b1901` vs `de Courcy-Ireland, M. G___Uganda___1933`

- [PASS] surname_gate: bio 'DE COURCY-IRELAND' vs stint 'de Courcy-Ireland, M. G' (exact)
- [PASS] initials: bio ['M', 'G'] ~ stint ['M', 'G']
- [PASS] age_gate: stint starts 1933, birth 1901 (age 32)
- [PASS] colony: 2 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1933-1949
- [PASS] position_sim: best 71 vs bar 60: 'senr. agric. offr' ~ 'Senior Agricultural Officer'
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

