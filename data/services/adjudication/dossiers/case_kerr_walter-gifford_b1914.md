<!-- {"case_id": "case_kerr_walter-gifford_b1914", "bio_ids": ["kerr_walter-gifford_b1914"], "stint_ids": ["Kerr, W. G___Kenya___1949"]} -->
# Dossier case_kerr_walter-gifford_b1914

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 68 official(s) with this surname in the graph's staff lists; 23 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `kerr_walter-gifford_b1914`

- Printed name: **KERR, Walter Gifford**
- Birth year: 1914 (attested in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962])
- Honours: M.B
- Appears in editions: [1951, 1956, 1957, 1958, 1959, 1960, 1961, 1962]

### Verbatim printed entry text (OCR)

**Version `col1956-L22296.v` — printed in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962]:**

> KERR, W. G.—b. 1914; ed. Merchiston Castle Prep. Sch. and Edin. Univ.; mil. serv., 1933-38; M.O., Ken., 1939; specialist (surgical), Tang., 1950; senr., 1960-61.

**Version `col1951-L39734.v` — printed in editions [1951]:**

> KERR, Walter Gifford, M.B., Ch.B. (Edin.), F.R.C.S. (Edin.).—b. 1914; ed. Merchiston Castle Prep. Sch. and Edin. Acad.; on mil. serv., 1933-48; med. offr., Ken., 1939; surg. spec., Tang., 1950.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1939 | M.O. | Kenya | [1951, 1956, 1957, 1958, 1959, 1960, 1961, 1962] |
| 1 | 1950 | specialist (surgical) | Tanganyika | [1951, 1956, 1957, 1958, 1959, 1960, 1961, 1962] |
| 2 | 1960–1961 | senr | Tanganyika *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962] |

## Candidate stint `Kerr, W. G___Kenya___1949`

- Staff-list name: **Kerr, W. G** | colony: **Kenya** | listed 1949–1950 | editions [1949, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | W. G. Kerr | Medical Officer | Medical | — | — |
| 1950 | W. G. Kerr | Medical Officer | Medical | — | — |

### Deterministic checks: `kerr_walter-gifford_b1914` vs `Kerr, W. G___Kenya___1949`

- [PASS] surname_gate: bio 'KERR' vs stint 'Kerr, W. G' (exact)
- [PASS] initials: bio ['W', 'G'] ~ stint ['W', 'G']
- [PASS] age_gate: stint starts 1949, birth 1914 (age 35)
- [PASS] colony: 1 placed event(s) resolve to 'Kenya'
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

