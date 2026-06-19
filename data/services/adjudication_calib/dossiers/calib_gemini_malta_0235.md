<!-- {"case_id": "calib_gemini_malta_0235", "bio_ids": ["schranz_e-g_b1905"], "stint_ids": ["Schranz, E. G___Malta___1933", "Schranz, E. G___Malta___1956"]} -->
# Dossier calib_gemini_malta_0235

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `schranz_e-g_b1905`

- Printed name: **SCHRANZ, E. G**
- Birth year: 1905 (attested in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964])
- Appears in editions: [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1956-L23999.v` — printed in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]:**

> SCHRANZ, E. G.—b. 1905; ed. Lyceum and Royal Univ. of Malta; civ. serv. (admin.), Malta, 1926; acctnt., 1944; admin. sec., P.W.D., 1947.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1926 | civ. serv. (admin.) | Malta | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 1 | 1944 | acctnt | Malta *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 2 | 1947 | admin. sec., P.W.D | Malta *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |

## Candidate stint `Schranz, E. G___Malta___1933`

- Staff-list name: **Schranz, E. G** | colony: **Malta** | listed 1933–1940 | editions [1933, 1934, 1936, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | E. G. Schranz | Clerks, 2nd Class | Public Works Department | — | — |
| 1934 | E. G. Schranz | Clerks, 2nd Class | Public Works Department | — | — |
| 1936 | E. G. Schranz | Clerks, 2nd Class | Public Works Department | — | — |
| 1937 | E. G. Schranz | Clerks, 2nd Class | Public Works Department | — | — |
| 1939 | E. G. Schranz | Clerks, 2nd Class | Public Works Department | — | — |
| 1940 | E. G. Schranz | Clerks, 2nd Class | Public Works Department | — | — |

### Deterministic checks: `schranz_e-g_b1905` vs `Schranz, E. G___Malta___1933`

- [PASS] surname_gate: bio 'SCHRANZ' vs stint 'Schranz, E. G' (exact)
- [PASS] initials: bio ['E', 'G'] ~ stint ['E', 'G']
- [PASS] age_gate: stint starts 1933, birth 1905 (age 28)
- [PASS] colony: 3 placed event(s) resolve to 'Malta'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1933-1940
- [FAIL] position_sim: best 40 vs bar 60: 'civ. serv. (admin.)' ~ 'Clerks, 2nd Class'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Schranz, E. G___Malta___1956`

- Staff-list name: **Schranz, E. G** | colony: **Malta** | listed 1956–1961 | editions [1956, 1957, 1958, 1959, 1960, 1961]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1956 | E. G. Schranz | Administrative Secretary, Public Works Department | The Maltese Government | — | — |
| 1957 | E. G. Schranz | Administrative Secretary, Public Works Department | The Maltese Government | — | — |
| 1958 | E. G. Schranz | Administrative Secretary, Public Works Department | The Maltese Government | — | — |
| 1959 | E. G. Schranz | Administrative Secretary, Public Works Department | The Maltese Government | — | — |
| 1960 | E. G. Schranz | Administrative Secretary, Public Works Department | Judiciary | — | — |
| 1961 | E. G. Schranz | Administrative Secretary, Public Works Department | Civil Establishment | — | — |

### Deterministic checks: `schranz_e-g_b1905` vs `Schranz, E. G___Malta___1956`

- [PASS] surname_gate: bio 'SCHRANZ' vs stint 'Schranz, E. G' (exact)
- [PASS] initials: bio ['E', 'G'] ~ stint ['E', 'G']
- [PASS] age_gate: stint starts 1956, birth 1905 (age 51)
- [PASS] colony: 3 placed event(s) resolve to 'Malta'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1956-1961
- [PASS] position_sim: best 64 vs bar 60: 'admin. sec., P.W.D' ~ 'Administrative Secretary, Public Works Department'
- [FAIL] honour: no shared honour
- [PASS] edition_cooccurrence: 6 agreeing edition-year(s) [1956, 1957, 1958, 1959, 1960, 1961] pos~64 (bar: >=2)
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

