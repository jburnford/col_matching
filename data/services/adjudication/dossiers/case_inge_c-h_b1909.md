<!-- {"case_id": "case_inge_c-h_b1909", "bio_ids": ["inge_c-h_b1909"], "stint_ids": ["Inge, C. H___Aden___1949"]} -->
# Dossier case_inge_c-h_b1909

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `inge_c-h_b1909`

- Printed name: **INGE, C. H**
- Birth year: 1909 (attested in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963])
- Appears in editions: [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963]

### Verbatim printed entry text (OCR)

**Version `col1956-L22113.v` — printed in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963]:**

> INGE, C. H.—b. 1909; ed. Rugby Sch. and Oxford Univ.; polit. offr., Aden prot., 1941; dir., antiquities, 1947-53; ret. 1962.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1941 | polit. offr. | Aden | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 1 | 1947–1953 | dir., antiquities | Aden *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 2 | 1962 | ret | Aden *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963] |

## Candidate stint `Inge, C. H___Aden___1949`

- Staff-list name: **Inge, C. H** | colony: **Aden** | listed 1949–1950 | editions [1949, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | C. H. Inge | Assistant Secretary (Pol.) | Secretariat | — | — |
| 1950 | C. H. Inge | Assistant Secretaries | Secretariat | — | — |
| 1950 | C. H. Inge | Political Officers | ADEN PROTECTORATE | — | — |

### Deterministic checks: `inge_c-h_b1909` vs `Inge, C. H___Aden___1949`

- [PASS] surname_gate: bio 'INGE' vs stint 'Inge, C. H' (exact)
- [PASS] initials: bio ['C', 'H'] ~ stint ['C', 'H']
- [PASS] age_gate: stint starts 1949, birth 1909 (age 40)
- [PASS] colony: 3 placed event(s) resolve to 'Aden'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1950
- [FAIL] position_sim: best 39 vs bar 60: 'dir., antiquities' ~ 'Assistant Secretaries'
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

