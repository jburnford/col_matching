<!-- {"case_id": "case_dempsey_p-s_b1909", "bio_ids": ["dempsey_p-s_b1909"], "stint_ids": ["Dempsey, P. S___Singapore___1949"]} -->
# Dossier case_dempsey_p-s_b1909

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `dempsey_p-s_b1909`

- Printed name: **DEMPSEY, P. S.**
- Birth year: 1909 (attested in editions [1956, 1958, 1959])
- Appears in editions: [1956, 1957, 1958, 1959]

### Verbatim printed entry text (OCR)

**Version `col1956-L20794.v` — printed in editions [1956, 1958, 1959]:**

> DEMPSEY, P. S.—b. 1909; ed. Caldicott Prep Sch., Hitchin, Kingswood Sch., Bath, and Westminster Coll., Univ. of London; naval serv., 1942-45, lt.-comdr., M.R.N.V.R.; teacher, Anglo-Chinese Schs., S.S. and F.M.S., 1936; prin., Anderson Sch., Ipoh, 1946; supvr., private schs., S'pore, 1947; inspr., schs., 1950; exams. sec., Fed. of Mal., 1951; prin., teachers' training coll., S'pore, 1952-58.

**Version `col1957-L22508.v` — printed in editions [1957]:**

> DEMPESEY, P. S.—b. 1909; ed. Caldicott Prep Sch., Hitchin, Kingswood Sch., Bath, and Westminster Coll., Univ. of London; naval serv., 1942-45; lt.-comdr., M.R.N.V.R.; teacher, Anglo-Chinese Schs., S.S. and F.M.S., 1936; supvr., private schs., S'pore, 1947; inspr., schs., 1950; exams. sec., Fed. of Mal., 1951; prin., teachers' training Coll., S'pore, 1952.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1936–1936 | teacher | Straits Settlements and Federated Malay States | [1956, 1957, 1958, 1959] |
| 1 | 1942–1945 | naval serv., lt.-comdr., M.R.N.V.R. | — | [1956, 1957, 1958, 1959] |
| 2 | 1946–1946 | prin., Anderson Sch. | — | [1956, 1958, 1959] |
| 3 | 1947–1947 | supvr., private schs. | Singapore | [1956, 1957, 1958, 1959] |
| 4 | 1950–1950 | inspr., schs. | Straits Settlements *(inherited from previous clause)* | [1956, 1957, 1958, 1959] |
| 5 | 1951–1951 | exams. sec. | Federation of Malaya | [1956, 1957, 1958, 1959] |
| 6 | 1952–1958 | prin., teachers' training coll. | Singapore | [1956, 1957, 1958, 1959] |

## Candidate stint `Dempsey, P. S___Singapore___1949`

- Staff-list name: **Dempsey, P. S** | colony: **Singapore** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | P. S. Dempsey | Supervisor of Private English Schools | Education | — | — |
| 1951 | P. S. Dempsey | Inspectors of Schools | Education | — | — |

### Deterministic checks: `dempsey_p-s_b1909` vs `Dempsey, P. S___Singapore___1949`

- [PASS] surname_gate: bio 'DEMPSEY' vs stint 'Dempsey, P. S' (exact)
- [PASS] initials: bio ['P', 'S'] ~ stint ['P', 'S']
- [PASS] age_gate: stint starts 1949, birth 1909 (age 40)
- [PASS] colony: 2 placed event(s) resolve to 'Singapore'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 41 vs bar 60: 'prin., teachers' training coll.' ~ 'Supervisor of Private English Schools'
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

