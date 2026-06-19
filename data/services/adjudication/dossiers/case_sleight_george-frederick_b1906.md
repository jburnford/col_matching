<!-- {"case_id": "case_sleight_george-frederick_b1906", "bio_ids": ["sleight_george-frederick_b1906"], "stint_ids": ["Sleight, G. F___Cyprus___1939"]} -->
# Dossier case_sleight_george-frederick_b1906

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Sleight, G. F___Cyprus___1939` is also gate-compatible with biography(ies) outside this case: ['sleight_g-f_b1905'] (already linked elsewhere or filtered).

## Biography `sleight_george-frederick_b1906`

- Printed name: **SLEIGHT, GEORGE FREDERICK**
- Birth year: 1906 (attested in editions [1939, 1940])
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L70665.v` — printed in editions [1939, 1940]:**

> SLEIGHT, GEORGE FREDERICK, M.A. (New Zealand), Ph.D. (London).—B. 1906; ed. Waipuani and Univ. Coll., Wellington, New Zealand and London Univ.; headmr., Normal Schi., Cyprus, Aug., 1937 (title changed to principal 1938).

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1937 | headmr., Normal Schi. | Cyprus | [1939, 1940] |

## Candidate stint `Sleight, G. F___Cyprus___1939`

- Staff-list name: **Sleight, G. F** | colony: **Cyprus** | listed 1939–1956 | editions [1939, 1949, 1951, 1953, 1954, 1955, 1956]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | Dr. G. F. Sleight | Principal | Normal School | — | — |
| 1949 | G. F. Sleight | Director of Education | Education | — | — |
| 1951 | Dr. G. F. Sleight | Director of Education | Education | — | — |
| 1953 | G. F. Sleight | Director of Education | Civil Establishment | — | — |
| 1954 | G. F. Sleight | Director of Education | Civil Establishment | — | — |
| 1955 | G. F. Sleight | Director of Education | Civil Establishment | — | — |
| 1956 | G. F. Sleight | Director of Education | Civil Establishment | — | — |

### Deterministic checks: `sleight_george-frederick_b1906` vs `Sleight, G. F___Cyprus___1939`

- [PASS] surname_gate: bio 'SLEIGHT' vs stint 'Sleight, G. F' (exact)
- [PASS] initials: bio ['G', 'F'] ~ stint ['G', 'F']
- [PASS] age_gate: stint starts 1939, birth 1906 (age 33)
- [PASS] colony: 1 placed event(s) resolve to 'Cyprus'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1939-1956
- [FAIL] position_sim: best 36 vs bar 60: 'headmr., Normal Schi.' ~ 'Director of Education'
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

