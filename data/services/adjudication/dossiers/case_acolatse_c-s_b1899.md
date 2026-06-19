<!-- {"case_id": "case_acolatse_c-s_b1899", "bio_ids": ["acolatse_c-s_b1899"], "stint_ids": ["Acolatse, C. S___Gold Coast___1949"]} -->
# Dossier case_acolatse_c-s_b1899

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `acolatse_c-s_b1899`

- Printed name: **ACOLATSE, C. S**
- Birth year: 1899 (attested in editions [1953])
- Appears in editions: [1953, 1954, 1955, 1956]

### Verbatim printed entry text (OCR)

**Version `col1953-L16293.v` — printed in editions [1953]:**

> ACOLATSE, C. S.—b. 1899; ed. Livingstone Coll., Salisbury, N.C., U.S.A., and Cambridge Univ.; barrister-at-law (Lincoln's Inn), 1930; in practice, Gold Coast, 1931-43; dist. mag., 1943; puisne judge, Gold Coast, 1952.

**Version `col1956-L19315.v` — printed in editions [1956]:**

> ACOLATSE, C. S.—b. 1899; ed. Livingstone Coll., Salisbury, U.S.A., and Cambridge Univ.; barrister-at-law, Lincoln's Inn; dist. mag., G.C., 1943; puisne judge, 1952; mem., comsnr. enq., strike and riots, Freetown, S.L., 1955.

**Version `col1954-L19264.v` — printed in editions [1954, 1955]:**

> ACOLATSE, C. S.—b. 1899 ; ed. Livingston College, Salisbury, U.S.A., and Cambridge Univ.; barrister-at-law, Lincoln’s Inn ; dist. mag., G.C., 1943 ; puisne judge, 1952.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1930 | barrister-at-law (Lincoln's Inn) | — | [1953] |
| 1 | 1931–1943 | in practice | Gold Coast | [1953] |
| 2 | 1943 | dist. mag | Gold Coast | [1953, 1954, 1955, 1956] |
| 3 | 1952 | puisne judge | Gold Coast | [1953, 1954, 1955, 1956] |
| 4 | 1955 | mem., comsnr. enq., strike and riots, Freetown | Sierra Leone | [1956] |

## Candidate stint `Acolatse, C. S___Gold Coast___1949`

- Staff-list name: **Acolatse, C. S** | colony: **Gold Coast** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | C. S. Acolatse | District Magistrate | Judicial | — | — |
| 1950 | C. S. Acolatse | District Magistrates | Judicial | — | — |
| 1951 | C. S. Acolatse | District Magistrate | Judicial | — | — |

### Deterministic checks: `acolatse_c-s_b1899` vs `Acolatse, C. S___Gold Coast___1949`

- [PASS] surname_gate: bio 'ACOLATSE' vs stint 'Acolatse, C. S' (exact)
- [PASS] initials: bio ['C', 'S'] ~ stint ['C', 'S']
- [PASS] age_gate: stint starts 1949, birth 1899 (age 50)
- [PASS] colony: 3 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 59 vs bar 60: 'dist. mag' ~ 'District Magistrate'
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

