<!-- {"case_id": "case_van-de-linde_p-a-m_b1918", "bio_ids": ["van-de-linde_p-a-m_b1918"], "stint_ids": ["Van de Linde, P. A. M___Hong Kong___1949"]} -->
# Dossier case_van-de-linde_p-a-m_b1918

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `van-de-linde_p-a-m_b1918`

- Printed name: **VAN DE LINDE, P. A. M**
- Birth year: 1918 (attested in editions [1966])
- Appears in editions: [1966]

### Verbatim printed entry text (OCR)

**Version `col1966-L18628.v` — printed in editions [1966]:**

> VAN DE LINDE, P. A. M.—b. 1918; ed. Monkton Combe Sch., Bath, and St. Bart's Hosp.; mil. serv., 1942–46, maj.; M.O., H.K., 1946; prin. health offr., 1959; redesig. prin. M. and H. offr., 1959; A.D.M.H.S., 1963.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | M.O. | Hong Kong | [1966] |
| 1 | 1959 | prin. health offr | Hong Kong *(inherited from previous clause)* | [1966] |
| 2 | 1963 | A.D.M.H.S | Hong Kong *(inherited from previous clause)* | [1966] |

## Candidate stint `Van de Linde, P. A. M___Hong Kong___1949`

- Staff-list name: **Van de Linde, P. A. M** | colony: **Hong Kong** | listed 1949–1950 | editions [1949, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | P. A. M. Van de Linde | Medical Officer | Medical | — | — |
| 1950 | P. A. M. Van de Linde | Medical and Health Officer | MEDICAL | — | — |

### Deterministic checks: `van-de-linde_p-a-m_b1918` vs `Van de Linde, P. A. M___Hong Kong___1949`

- [PASS] surname_gate: bio 'VAN DE LINDE' vs stint 'Van de Linde, P. A. M' (exact)
- [PASS] initials: bio ['P', 'A', 'M'] ~ stint ['P', 'A', 'M']
- [PASS] age_gate: stint starts 1949, birth 1918 (age 31)
- [PASS] colony: 3 placed event(s) resolve to 'Hong Kong'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1950
- [FAIL] position_sim: best 24 vs bar 60: 'M.O.' ~ 'Medical Officer'
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

