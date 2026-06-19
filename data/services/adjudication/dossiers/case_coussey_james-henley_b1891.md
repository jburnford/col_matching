<!-- {"case_id": "case_coussey_james-henley_b1891", "bio_ids": ["coussey_james-henley_b1891"], "stint_ids": ["Coussey, J. Henley___Gold Coast___1949"]} -->
# Dossier case_coussey_james-henley_b1891

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `coussey_james-henley_b1891`

- Printed name: **COUSSEY, James Henley**
- Birth year: 1891 (attested in editions [1950, 1951, 1955, 1956])
- Honours: K.B.E, Kt. Bach (1950)
- Appears in editions: [1948, 1950, 1951, 1953, 1955, 1956]

### Verbatim printed entry text (OCR)

**Version `col1950-L34631.v` — printed in editions [1950, 1951, 1955, 1956]:**

> COUSSEY, Sir James, Kt. Bach. (1950).—b. 1891; ed. Hampton Gram. Sch.; barrister, Middle Temple; in practice, G.C., 1913-44; prov. M.E.C., 1943; puisne judge, 1944; chmn., comtee. for constitutional reform, 1949; justice of appeal, W.A. ct. of appeal, G.C., 1952; pres., 1955.

**Version `col1953-L16985.v` — printed in editions [1953]:**

> COUSSEY, Sir James, K.B.E., Kt. Bach. (1950).—b. 1891; ed. Hampton Gram. Sch.; barrister Middle Temple, 1913; in practice, G.C., 1913–44; prov. M.E.C., 1943; puisne judge, 1944; chmn., comtce. for constitutional reform, 1949; justice of appeal, W.A. ct. of appeal, G.C., 1952.

**Version `col1948-L31949.v` — printed in editions [1948]:**

> COUSSEY, James Henley.—b. 1891; ed. Hampton Gram. Sch.; barrister, Middle Temple; in practice, G.C., 1913-44; provincial M.E.C., 1943; puisne judge, 1944.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1913–1944 | in practice | Gold Coast | [1948, 1950, 1951, 1953, 1955, 1956] |
| 1 | 1913 | barrister Middle Temple | — | [1953] |
| 2 | 1943 | prov. M.E.C | Gold Coast *(inherited from previous clause)* | [1948, 1950, 1951, 1953, 1955, 1956] |
| 3 | 1944 | puisne judge | Gold Coast *(inherited from previous clause)* | [1948, 1950, 1951, 1953, 1955, 1956] |
| 4 | 1949 | chmn., comtee. for constitutional reform | Gold Coast *(inherited from previous clause)* | [1950, 1951, 1953, 1955, 1956] |
| 5 | 1952 | justice of appeal, W.A. ct. of appeal | Gold Coast | [1950, 1951, 1953, 1955, 1956] |
| 6 | 1955 | pres | Gold Coast *(inherited from previous clause)* | [1950, 1951, 1955, 1956] |

## Candidate stint `Coussey, J. Henley___Gold Coast___1949`

- Staff-list name: **Coussey, J. Henley** | colony: **Gold Coast** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | J. H. Coussey | Puisne Judge | Judicial | — | — |
| 1950 | J. H. Coussey | Puisne Judges | Judicial | — | — |
| 1951 | Sir J. Henley Coussey | Puisne Judge | Judicial | — | — |

### Deterministic checks: `coussey_james-henley_b1891` vs `Coussey, J. Henley___Gold Coast___1949`

- [PASS] surname_gate: bio 'COUSSEY' vs stint 'Coussey, J. Henley' (exact)
- [PASS] initials: bio ['J', 'H'] ~ stint ['J', 'H']
- [PASS] age_gate: stint starts 1949, birth 1891 (age 58)
- [PASS] colony: 6 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1949-1951
- [PASS] position_sim: best 100 vs bar 60: 'puisne judge' ~ 'Puisne Judge'
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

