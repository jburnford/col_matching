<!-- {"case_id": "case_donne_arthur-courtenay_b1892", "bio_ids": ["donne_arthur-courtenay_b1892"], "stint_ids": ["Donne, A. C___Tanganyika___1920"]} -->
# Dossier case_donne_arthur-courtenay_b1892

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `donne_arthur-courtenay_b1892`

- Printed name: **DONNE, ARTHUR COURTENAY**
- Birth year: 1892 (attested in editions [1940])
- Appears in editions: [1940]

### Verbatim printed entry text (OCR)

**Version `col1940-L63820.v` — printed in editions [1940]:**

> DONNE, ARTHUR COURTENAY, B.A. (Oxon.).—B. 1892; ed. at Bradford Coll. and Univ. Coll., Oxford; junr. astt. sec., Tanganyika, 1919-23; admin. offr., 1923; supt. of educn., 1928.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1919–1923 | junr. astt. sec. | Tanganyika | [1940] |
| 1 | 1923 | admin. offr | Tanganyika *(inherited from previous clause)* | [1940] |
| 2 | 1928 | supt. of educn | Tanganyika *(inherited from previous clause)* | [1940] |

## Candidate stint `Donne, A. C___Tanganyika___1920`

- Staff-list name: **Donne, A. C** | colony: **Tanganyika** | listed 1920–1923 | editions [1920, 1921, 1922, 1923]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1920 | Captain A. C. Donne | Assistant Secretaries | Secretariat | — | Captain |
| 1921 | A. C. Donne | Assistant Secretaries | Secretariat | — | — |
| 1922 | A. C. Donne | Assistant Secretaries | Secretariat | — | — |
| 1923 | A. C. Donne | Assistant Secretary | Secretariat | — | — |

### Deterministic checks: `donne_arthur-courtenay_b1892` vs `Donne, A. C___Tanganyika___1920`

- [PASS] surname_gate: bio 'DONNE' vs stint 'Donne, A. C' (exact)
- [PASS] initials: bio ['A', 'C'] ~ stint ['A', 'C']
- [PASS] age_gate: stint starts 1920, birth 1892 (age 28)
- [PASS] colony: 3 placed event(s) resolve to 'Tanganyika'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1920-1923
- [FAIL] position_sim: best 50 vs bar 60: 'junr. astt. sec.' ~ 'Assistant Secretary'
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

