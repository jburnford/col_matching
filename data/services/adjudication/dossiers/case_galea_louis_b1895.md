<!-- {"case_id": "case_galea_louis_b1895", "bio_ids": ["galea_louis_b1895"], "stint_ids": ["Galea, L___Malta___1949"]} -->
# Dossier case_galea_louis_b1895

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 25 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['galea_louis_b1895'] carry a single initial only — the namesake trap applies.

## Biography `galea_louis_b1895`

- Printed name: **GALEA, Louis**
- Birth year: 1895 (attested in editions [1951, 1955, 1957])
- Honours: C.B.E (1955), O.B.E (1950)
- Appears in editions: [1951, 1955, 1956, 1957]

### Verbatim printed entry text (OCR)

**Version `col1951-L38250.v` — printed in editions [1951, 1955, 1957]:**

> GALEA, Louis, LL.D.—b. 1895; ed. St. Ignatius and St. Aloysius Colls. and Royal Univ. of Malta; advoc. for the poor and curator ex-officio, Malta, 1930-36; nom. mem. coun. of gov., 1939-40; reg. protection offr., 1940-41; atty.-gen., 1941; ex-off., M.E.C., 1941-47; supplementary judge various occasions; acted as legal sec., 1947; chmn., public serv. comsn., 1947.

**Version `col1956-L21274.v` — printed in editions [1956]:**

> GALIEA, L., C.B.E. (1955), O.B.E. (1950).—b. 1895; ed. St. Ignatius and St. Aloysius Coll. and Royal Univ. of Malta; advoc. for the poor and curator ex officio, Malta, 1930–36; nom. mem., coun. of govt., 1939–40; secon. reg. protection offr., 1940–41; atty.-gen., 1941; M.E.C., 1941–47; supplementary judge, 1929–32; chmn., public serv. comsn., 1947.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1929–1932 | supplementary judge | Malta *(inherited from previous clause)* | [1956] |
| 1 | 1930–1936 | advoc. for the poor and curator ex-officio | Malta | [1951, 1955, 1956, 1957] |
| 2 | 1939–1940 | nom. mem. coun. of gov | Malta *(inherited from previous clause)* | [1951, 1955, 1956, 1957] |
| 3 | 1940–1941 | reg. protection offr | Malta *(inherited from previous clause)* | [1951, 1955, 1956, 1957] |
| 4 | 1941 | atty.-gen | Malta *(inherited from previous clause)* | [1951, 1955, 1956, 1957] |
| 5 | 1947 | acted as legal sec | Malta *(inherited from previous clause)* | [1951, 1955, 1956, 1957] |

## Candidate stint `Galea, L___Malta___1949`

- Staff-list name: **Galea, L** | colony: **Malta** | listed 1949–1955 | editions [1949, 1950, 1951, 1952, 1953, 1954, 1955]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | L. Galea | Attorney-General | Legal | — | — |
| 1950 | L. Galea | Attorney-General | LEGAL | — | — |
| 1951 | L. Galea | Attorney-General | Legal | — | — |
| 1952 | L. Galea | Attorney-General | Maltese Government | — | — |
| 1953 | L. Galea | Attorney-General | The Maltese Government | — | — |
| 1954 | L. Galea | Attorney-General | The Maltese Government | — | — |
| 1955 | L. Galea | Attorney-General | THE MALTESE GOVERNMENT | — | — |

### Deterministic checks: `galea_louis_b1895` vs `Galea, L___Malta___1949`

- [PASS] surname_gate: bio 'GALEA' vs stint 'Galea, L' (exact)
- [PASS] initials: bio ['L'] ~ stint ['L']
- [PASS] age_gate: stint starts 1949, birth 1895 (age 54)
- [PASS] colony: 6 placed event(s) resolve to 'Malta'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1955
- [FAIL] position_sim: best 36 vs bar 60: 'acted as legal sec' ~ 'Attorney-General'
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

