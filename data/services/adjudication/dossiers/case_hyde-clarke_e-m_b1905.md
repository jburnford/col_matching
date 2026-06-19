<!-- {"case_id": "case_hyde-clarke_e-m_b1905", "bio_ids": ["hyde-clarke_e-m_b1905"], "stint_ids": ["Hyde-Clarke, E. M___Kenya___1949"]} -->
# Dossier case_hyde-clarke_e-m_b1905

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hyde-clarke_e-m_b1905`

- Printed name: **HYDE-CLARKE, E. M**
- Birth year: 1905 (attested in editions [1948, 1949, 1950, 1951, 1953])
- Honours: M.B.E
- Appears in editions: [1948, 1949, 1950, 1951, 1953]

### Verbatim printed entry text (OCR)

**Version `col1948-L33542.v` — printed in editions [1948, 1949, 1950, 1951, 1953]:**

> HYDE-CLARKE, E. M., M.B.E.—b. 1905; ed. St. George's Sch., Harpenden, Lond. Sch. of Econ. and Wadham Coll., Oxford; cadet, Ken., 1927; asst. sec., secretariat, 1939; personal asst., chmn., agric. prod. and settlement bd., 1944; civil reabsorption offr. and dir., man/woman power, 1945; labour comsnr., 1945; official M.L.C., 1946; perm. sec. to min. of local govt., G.C., 1950; ret. and re-apptd. estab. sec. (temp.), 1952; sec. to various comtees.; chmn., sub-comte. of the labour advisory bd. on native registration.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1927 | cadet | Kenya | [1948, 1949, 1950, 1951, 1953] |
| 1 | 1939 | asst. sec., secretariat | Kenya *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1953] |
| 2 | 1944 | personal asst., chmn., agric. prod. and settlement bd | Kenya *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1953] |
| 3 | 1945 | civil reabsorption offr. and dir., man/woman power | Kenya *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1953] |
| 4 | 1946 | official M.L.C | Kenya *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1953] |
| 5 | 1950 | perm. sec. to min. of local govt. | Gold Coast | [1948, 1949, 1950, 1951, 1953] |
| 6 | 1952 | ret. and re-apptd. estab. sec. (temp.) | Gold Coast *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1953] |

## Candidate stint `Hyde-Clarke, E. M___Kenya___1949`

- Staff-list name: **Hyde-Clarke, E. M** | colony: **Kenya** | listed 1949–1950 | editions [1949, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | E. M. Hyde-Clarke | Labour Commissioner | Labour | — | — |
| 1950 | E. M. Hyde-Clarke | Labour Commissioner | Labour | — | — |

### Deterministic checks: `hyde-clarke_e-m_b1905` vs `Hyde-Clarke, E. M___Kenya___1949`

- [PASS] surname_gate: bio 'HYDE-CLARKE' vs stint 'Hyde-Clarke, E. M' (exact)
- [PASS] initials: bio ['E', 'M'] ~ stint ['E', 'M']
- [PASS] age_gate: stint starts 1949, birth 1905 (age 44)
- [PASS] colony: 5 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1950
- [FAIL] position_sim: best 32 vs bar 60: 'official M.L.C' ~ 'Labour Commissioner'
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

