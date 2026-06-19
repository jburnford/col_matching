<!-- {"case_id": "case_richardson_w-a_b1919", "bio_ids": ["richardson_w-a_b1919"], "stint_ids": ["Richardson, W. A___West Indies Federation___1961"]} -->
# Dossier case_richardson_w-a_b1919

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 76 official(s) with this surname in the graph's staff lists; 30 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `richardson_w-a_b1919`

- Printed name: **RICHARDSON, W. A**
- Birth year: 1919 (attested in editions [1960, 1961, 1962, 1963])
- Honours: O.B.E (1962)
- Appears in editions: [1960, 1961, 1962, 1963]

### Verbatim printed entry text (OCR)

**Version `col1960-L27374.v` — printed in editions [1960, 1961, 1962, 1963]:**

> RICHARDSON, W. A., O.B.E. (1962)—b. 1919; ed. Queen's Royal Coll., Trin., and King's Coll., London; B.B.C., 1951; fed. inf. offr., pre-fed. orgn., W.I., 1957; T.W.I., 1958-62.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1951 | B.B.C | — | [1960, 1961, 1962, 1963] |
| 1 | 1957 | fed. inf. offr., pre-fed. orgn. | West Indies | [1960, 1961, 1962, 1963] |
| 2 | 1958–1962 | T.W.I | West Indies *(inherited from previous clause)* | [1960, 1961, 1962, 1963] |

## Candidate stint `Richardson, W. A___West Indies Federation___1961`

- Staff-list name: **Richardson, W. A** | colony: **West Indies Federation** | listed 1961–1962 | editions [1961, 1962]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1961 | W. A. Richardson | Federal Information Officer | Civil Establishment | — | — |
| 1962 | W. A. Richardson | Federal Information Officer | Civil Establishment | — | — |

### Deterministic checks: `richardson_w-a_b1919` vs `Richardson, W. A___West Indies Federation___1961`

- [PASS] surname_gate: bio 'RICHARDSON' vs stint 'Richardson, W. A' (exact)
- [PASS] initials: bio ['W', 'A'] ~ stint ['W', 'A']
- [PASS] age_gate: stint starts 1961, birth 1919 (age 42)
- [PASS] colony: 2 placed event(s) resolve to 'West Indies Federation'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1961-1962
- [FAIL] position_sim: best 13 vs bar 60: 'T.W.I' ~ 'Federal Information Officer'
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

