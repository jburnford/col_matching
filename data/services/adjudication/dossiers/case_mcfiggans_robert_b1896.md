<!-- {"case_id": "case_mcfiggans_robert_b1896", "bio_ids": ["mcfiggans_robert_b1896"], "stint_ids": ["McFiggans, R___Kenya___1949"]} -->
# Dossier case_mcfiggans_robert_b1896

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['mcfiggans_robert_b1896'] carry a single initial only — the namesake trap applies.

## Biography `mcfiggans_robert_b1896`

- Printed name: **McFIGGANS, Robert**
- Birth year: 1896 (attested in editions [1948, 1949, 1950, 1951])
- Honours: M.B
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L34295.v` — printed in editions [1948, 1949, 1950, 1951]:**

> McFIGGANS, Robert, M.B., Ch.B.—b. 1896; ed. Falkirk High Sch., Edinburgh Univ.; on war serv. 1916-18; med. offr., Ken., 1926; S.M.O., 1947.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1926 | med. offr. | Kenya | [1948, 1949, 1950, 1951] |
| 1 | 1947 | S.M.O | Kenya *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `McFiggans, R___Kenya___1949`

- Staff-list name: **McFiggans, R** | colony: **Kenya** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | R. McFiggans | Senior Medical Officers | Medical | — | — |
| 1950 | R. McFiggans | Senior Medical Officers | Medical | — | — |
| 1951 | R. McFiggans | Senior Medical Officer | Medical | — | — |

### Deterministic checks: `mcfiggans_robert_b1896` vs `McFiggans, R___Kenya___1949`

- [PASS] surname_gate: bio 'McFIGGANS' vs stint 'McFiggans, R' (exact)
- [PASS] initials: bio ['R'] ~ stint ['R']
- [PASS] age_gate: stint starts 1949, birth 1896 (age 53)
- [PASS] colony: 2 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 16 vs bar 60: 'S.M.O' ~ 'Senior Medical Officer'
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

