<!-- {"case_id": "case_leyns_peter_b1851", "bio_ids": ["leyns_peter_b1851"], "stint_ids": ["Leys, P___Labuan___1878"]} -->
# Dossier case_leyns_peter_b1851

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['leyns_peter_b1851'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Leys, P___Labuan___1878` is also gate-compatible with biography(ies) outside this case: ['leys_peter_e1876'] (already linked elsewhere or filtered).

## Biography `leyns_peter_b1851`

- Printed name: **LEYNS, PETER**
- Birth year: 1851 (attested in editions [1917])
- Honours: C.M.G (1890)
- Appears in editions: [1917]

### Verbatim printed entry text (OCR)

**Version `col1917-L51260.v` — printed in editions [1917]:**

> LEYNS, PETER, C.M.G. (1890).—B. 1851; ed. at Univs. of Glasgow and Edinburgh, of which latter he is a graduate in medicine; entered col. service, Labuan, Feb., 1876; administd. the govt., 1881-7; held a coman. as H.B.M.'s consul-gen. for Borneo; ret., 1889.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1876 | entered col. service | Labuan | [1917] |
| 1 | 1881–1887 | administd. the govt | Labuan *(inherited from previous clause)* | [1917] |
| 2 | 1889 | ret | Labuan *(inherited from previous clause)* | [1917] |

## Candidate stint `Leys, P___Labuan___1878`

- Staff-list name: **Leys, P** | colony: **Labuan** | listed 1878–1906 | editions [1878, 1879, 1880, 1883, 1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1878 | P. Leys | Colonial Surgeon | Civil Establishment | — | — |
| 1879 | Dr. P. Leys | Colonial Surgeon | Civil Establishment | — | — |
| 1880 | Dr. P. Leys | Colonial Surgeon | Civil Establishment | — | — |
| 1883 | P. Leys | Acting Governor | Civil Establishment | — | — |
| 1894 | P. Leys (acting) | — | Governors | — | — |

### Deterministic checks: `leyns_peter_b1851` vs `Leys, P___Labuan___1878`

- [PASS] surname_gate: bio 'LEYNS' vs stint 'Leys, P' (fuzzy:1)
- [PASS] initials: bio ['P'] ~ stint ['P']
- [PASS] age_gate: stint starts 1878, birth 1851 (age 27)
- [PASS] colony: 3 placed event(s) resolve to 'Labuan'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1878-1906
- [FAIL] position_sim: best 48 vs bar 60: 'administd. the govt' ~ 'Acting Governor'
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

