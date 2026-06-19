<!-- {"case_id": "case_hopkins_lister-george_b1910", "bio_ids": ["hopkins_lister-george_b1910"], "stint_ids": ["Hopkins, L. G___Jamaica___1949"]} -->
# Dossier case_hopkins_lister-george_b1910

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 29 official(s) with this surname in the graph's staff lists; 14 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hopkins_lister-george_b1910`

- Printed name: **HOPKINS, Lister George**
- Birth year: 1910 (attested in editions [1948, 1949, 1950, 1951])
- Honours: O.B.E (1950)
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L33446.v` — printed in editions [1948, 1949, 1950, 1951]:**

> HOPKINS, Lister George, O.B.E. (1950), B.E. (Queensland), M.A. (Oxon).—b. 1910; ed. Toowoomba Gram. Sch., Univ. of Queensland, and Univ. of Oxford (Queensland Rhodes schol.); senr. asst. statistician, Pal., 1935; asst. govt. statistician, 1944; seconded as vital statistics advsr., J'ca., 1944; sec., Pal. wages comte., 1942; superintended W.I. census, 1946; produced W.I. census reports, 1948-50.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1935 | senr. asst. statistician | Palestine | [1948, 1949, 1950, 1951] |
| 1 | 1942 | sec., Pal. wages comte | Palestine | [1948, 1949, 1950, 1951] |
| 2 | 1944 | asst. govt. statistician | Palestine *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 3 | 1944 | seconded as vital statistics advsr. | Jamaica | [1948, 1949, 1950, 1951] |
| 4 | 1946 | superintended W.I. census | Palestine *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 5 | 1948–1950 | produced W.I. census reports | Palestine *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Hopkins, L. G___Jamaica___1949`

- Staff-list name: **Hopkins, L. G** | colony: **Jamaica** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | L. G. Hopkins | Vital Statistics Adviser (Colonial Development and Welfare Scheme D 153) | Registrar General and Island Record Office | — | — |
| 1950 | L. G. Hopkins | Vital Statistics Adviser (Colonial Development and Welfare Scheme D 153) | Registrar General and Island Record Office | — | — |
| 1951 | L. G. Hopkins | Vital Statistics Adviser (Colonial Development and Welfare Scheme D 153) | Registrar-General and Island Record | — | — |

### Deterministic checks: `hopkins_lister-george_b1910` vs `Hopkins, L. G___Jamaica___1949`

- [PASS] surname_gate: bio 'HOPKINS' vs stint 'Hopkins, L. G' (exact)
- [PASS] initials: bio ['L', 'G'] ~ stint ['L', 'G']
- [PASS] age_gate: stint starts 1949, birth 1910 (age 39)
- [PASS] colony: 1 placed event(s) resolve to 'Jamaica'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

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

