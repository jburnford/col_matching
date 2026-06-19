<!-- {"case_id": "case_burt_j-c_b1915", "bio_ids": ["burt_j-c_b1915"], "stint_ids": ["Burt, J. C___Gold Coast___1949"]} -->
# Dossier case_burt_j-c_b1915

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 18 official(s) with this surname in the graph's staff lists; 10 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `burt_j-c_b1915`

- Printed name: **BURT, J. C**
- Birth year: 1915 (attested in editions [1953, 1954, 1955, 1956, 1957, 1958, 1959])
- Appears in editions: [1953, 1954, 1955, 1956, 1957, 1958, 1959]

### Verbatim printed entry text (OCR)

**Version `col1953-L16758.v` — printed in editions [1953, 1954, 1955, 1956, 1957, 1958, 1959]:**

> BURT, J. C.—b. 1915; ed. Harris Academy, Dundee, and St. Andrews Univ.; solr. (Scotland); barrister-at-law, Middle Temple; mil. serv., 1940-46; dist. mag., G.C., 1946; registr.-gen., 1951 (Ghana civil service).

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | dist. mag. | Gold Coast | [1953, 1954, 1955, 1956, 1957, 1958, 1959] |
| 1 | 1951 | registr.-gen | Gold Coast *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957, 1958, 1959] |

## Candidate stint `Burt, J. C___Gold Coast___1949`

- Staff-list name: **Burt, J. C** | colony: **Gold Coast** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | J. C. Burt | District Magistrate | Judicial | — | — |
| 1950 | J. C. Burt | District Magistrates | Judicial | — | — |
| 1951 | J. C. Burt | District Magistrate | Judicial | — | — |

### Deterministic checks: `burt_j-c_b1915` vs `Burt, J. C___Gold Coast___1949`

- [PASS] surname_gate: bio 'BURT' vs stint 'Burt, J. C' (exact)
- [PASS] initials: bio ['J', 'C'] ~ stint ['J', 'C']
- [PASS] age_gate: stint starts 1949, birth 1915 (age 34)
- [PASS] colony: 2 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 59 vs bar 60: 'dist. mag.' ~ 'District Magistrate'
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

