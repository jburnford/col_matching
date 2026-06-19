<!-- {"case_id": "case_lightroot-boston_c-m_b1913", "bio_ids": ["lightroot-boston_c-m_b1913"], "stint_ids": ["Lightfoot-Boston, C___Sierra Leone___1949"]} -->
# Dossier case_lightroot-boston_c-m_b1913

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `lightroot-boston_c-m_b1913`

- Printed name: **LIGHTROOT-BOSTON, C. M**
- Birth year: 1913 (attested in editions [1956])
- Honours: M.B.E (1956)
- Appears in editions: [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963]

### Verbatim printed entry text (OCR)

**Version `col1956-L22544.v` — printed in editions [1956]:**

> LIGHTROOT-BOSTON, Mrs. C.—b. 1913; ed. Freetown Secondary Sch. for Girls; senr. nurse, S.L., 1939; nursing sister, 1943; senr., 1952.

**Version `col1957-L25039.v` — printed in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963]:**

> LIGHTFOOT-BOSTON, Mrs. C. M., M.B.E. (1956).—b. 1913; ed. Freetown Secondary Sch. for Girls; senr. nurse, S.L., 1939; nursing sister, 1943; senr., 1952. (S.L. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1939 | senr. nurse | Sierra Leone | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 1 | 1943 | nursing sister | Sierra Leone *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 2 | 1952 | senr | Sierra Leone *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963] |

## Candidate stint `Lightfoot-Boston, C___Sierra Leone___1949`

- Staff-list name: **Lightfoot-Boston, C** | colony: **Sierra Leone** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | C. Lightfoot-Boston | Nursing Sister | Medical | — | — |
| 1950 | C. Lightfoot-Boston | Nursing Sister | Medical | — | — |
| 1951 | Mrs. C. Lightfoot-Boston | Nursing Sister | Medical | — | — |

### Deterministic checks: `lightroot-boston_c-m_b1913` vs `Lightfoot-Boston, C___Sierra Leone___1949`

- [PASS] surname_gate: bio 'LIGHTROOT-BOSTON' vs stint 'Lightfoot-Boston, C' (fuzzy:1)
- [PASS] initials: bio ['C', 'M'] ~ stint ['C']
- [PASS] age_gate: stint starts 1949, birth 1913 (age 36)
- [PASS] colony: 3 placed event(s) resolve to 'Sierra Leone'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1949-1951
- [PASS] position_sim: best 100 vs bar 60: 'nursing sister' ~ 'Nursing Sister'
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

