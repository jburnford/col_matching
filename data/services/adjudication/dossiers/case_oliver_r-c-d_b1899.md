<!-- {"case_id": "case_oliver_r-c-d_b1899", "bio_ids": ["oliver_r-c-d_b1899"], "stint_ids": ["Oliver, R. C. D___Bahamas___1957"]} -->
# Dossier case_oliver_r-c-d_b1899

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 32 official(s) with this surname in the graph's staff lists; 14 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Oliver, R. C. D___Bahamas___1957` is also gate-compatible with biography(ies) outside this case: ['oliver_charles_e1880'] (already linked elsewhere or filtered).

## Biography `oliver_r-c-d_b1899`

- Printed name: **OLIVER, R. C. D**
- Birth year: 1899 (attested in editions [1959, 1960, 1961])
- Appears in editions: [1959, 1960, 1961]

### Verbatim printed entry text (OCR)

**Version `col1959-L26518.v` — printed in editions [1959, 1960, 1961]:**

> OLIVER, R. C. D.—b. 1899; ed. Epsom Coll., R.M.A. Sandhurst; comsmd. Royal Berks. Regt.; mil. serv. world wars I and II; sec., exchange control, Bah., 1947; dep. contrlr., 1952; contrlr., 1956-60.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1947 | sec., exchange control | Bahamas | [1959, 1960, 1961] |
| 1 | 1952 | dep. contrlr | Bahamas *(inherited from previous clause)* | [1959, 1960, 1961] |
| 2 | 1956–1960 | contrlr | Bahamas *(inherited from previous clause)* | [1959, 1960, 1961] |

## Candidate stint `Oliver, R. C. D___Bahamas___1957`

- Staff-list name: **Oliver, R. C. D** | colony: **Bahamas** | listed 1957–1960 | editions [1957, 1958, 1959, 1960]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1957 | Major R. C. D. Oliver | Exchange Controller | Civil Establishment | — | Major |
| 1958 | Major R. C. D. Oliver | Exchange Controller | Civil Establishment | — | Major |
| 1959 | Major R. C. D. Oliver | Exchange Controller | Civil Establishment | — | Major |
| 1960 | R. C. D. Oliver | Exchange Controller | Civil Establishment | — | Major |

### Deterministic checks: `oliver_r-c-d_b1899` vs `Oliver, R. C. D___Bahamas___1957`

- [PASS] surname_gate: bio 'OLIVER' vs stint 'Oliver, R. C. D' (exact)
- [PASS] initials: bio ['R', 'C', 'D'] ~ stint ['R', 'C', 'D']
- [PASS] age_gate: stint starts 1957, birth 1899 (age 58)
- [PASS] colony: 3 placed event(s) resolve to 'Bahamas'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1957-1960
- [PASS] position_sim: best 60 vs bar 60: 'dep. contrlr' ~ 'Exchange Controller'
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

