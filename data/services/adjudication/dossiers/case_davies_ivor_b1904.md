<!-- {"case_id": "case_davies_ivor_b1904", "bio_ids": ["davies_ivor_b1904"], "stint_ids": ["Davies, E. M. R. I___Nyasaland___1936"]} -->
# Dossier case_davies_ivor_b1904

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 137 official(s) with this surname in the graph's staff lists; 84 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['davies_ivor_b1904'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Davies, E. M. R. I___Nyasaland___1936` is also gate-compatible with biography(ies) outside this case: ['davies_r_b1921'] (already linked elsewhere or filtered).

## Biography `davies_ivor_b1904`

- Printed name: **DAVIES, Ivor**
- Birth year: 1904 (attested in editions [1951])
- Appears in editions: [1951]

### Verbatim printed entry text (OCR)

**Version `col1951-L37441.v` — printed in editions [1951]:**

> DAVIES, Ivor.—b. 1904; ed. Drayton Sch., Ealing; acctnt., rlwy., Nig., 1936; asst. treas., Gib., 1941; collr. rev., 1943; senr. acctnt.; acctnt. gen., Nyasa., 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1936 | acctnt., rlwy. | Nigeria | [1951] |
| 1 | 1941 | asst. treas. | Gibraltar | [1951] |
| 2 | 1943 | collr. rev | Gibraltar *(inherited from previous clause)* | [1951] |
| 3 | 1946 | acctnt. gen. | Nyasaland | [1951] |

## Candidate stint `Davies, E. M. R. I___Nyasaland___1936`

- Staff-list name: **Davies, E. M. R. I** | colony: **Nyasaland** | listed 1936–1937 | editions [1936, 1937]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | E. M. R. I. Davies | Nurses | Medical | — | — |
| 1937 | E. M. R. I. Davies | Nurse | Nurses | — | — |

### Deterministic checks: `davies_ivor_b1904` vs `Davies, E. M. R. I___Nyasaland___1936`

- [PASS] surname_gate: bio 'DAVIES' vs stint 'Davies, E. M. R. I' (exact)
- [PASS] initials: bio ['I'] ~ stint ['E', 'M', 'R', 'I']
- [PASS] age_gate: stint starts 1936, birth 1904 (age 32)
- [PASS] colony: 1 placed event(s) resolve to 'Nyasaland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1936-1937
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

