<!-- {"case_id": "case_nicolay_e-f_b1911", "bio_ids": ["nicolay_e-f_b1911"], "stint_ids": ["Nicolay, E. F___Uganda___1949"]} -->
# Dossier case_nicolay_e-f_b1911

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `nicolay_e-f_b1911`

- Printed name: **NICOLAY, E. F**
- Birth year: 1911 (attested in editions [1957])
- Honours: M.C (1945)
- Appears in editions: [1957]

### Verbatim printed entry text (OCR)

**Version `col1957-L26004.v` — printed in editions [1957]:**

> NICOLAY, E. F., M.C. (1945).—b. 1911; ed. Itchen Sch. and Univ. Coll., Southampton; mil. serv., 1940–46; mil. eng. services, India, 1936–39; Nig., 1939–42; engnr., Uga., 1946; resdt. engnr., Mombasa major project, P.W.D., Ken., 1953.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1936–1939 | mil. eng. services, India | — | [1957] |
| 1 | 1939–1942 | mil. eng. services, India | Nigeria | [1957] |
| 2 | 1946 | engnr. | Uganda | [1957] |
| 3 | 1953 | resdt. engnr., Mombasa major project, P.W.D. | Kenya | [1957] |

## Candidate stint `Nicolay, E. F___Uganda___1949`

- Staff-list name: **Nicolay, E. F** | colony: **Uganda** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | E. F. Nicolay | Executive Engineers and Assistant Engineers | Public Works | — | — |
| 1951 | E. F. Nicolay | Executive Engineers and Assistant Engineers | Public Works | — | — |

### Deterministic checks: `nicolay_e-f_b1911` vs `Nicolay, E. F___Uganda___1949`

- [PASS] surname_gate: bio 'NICOLAY' vs stint 'Nicolay, E. F' (exact)
- [PASS] initials: bio ['E', 'F'] ~ stint ['E', 'F']
- [PASS] age_gate: stint starts 1949, birth 1911 (age 38)
- [PASS] colony: 1 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 26 vs bar 60: 'engnr.' ~ 'Executive Engineers and Assistant Engineers'
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

