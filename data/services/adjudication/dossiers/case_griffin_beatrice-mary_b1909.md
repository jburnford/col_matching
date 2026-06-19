<!-- {"case_id": "case_griffin_beatrice-mary_b1909", "bio_ids": ["griffin_beatrice-mary_b1909"], "stint_ids": ["Griffin, B. M___Kenya___1950"]} -->
# Dossier case_griffin_beatrice-mary_b1909

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 40 official(s) with this surname in the graph's staff lists; 22 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `griffin_beatrice-mary_b1909`

- Printed name: **GRIFFIN, Beatrice Mary**
- Birth year: 1909 (attested in editions [1950, 1951])
- Appears in editions: [1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1950-L35944.v` — printed in editions [1950, 1951]:**

> GRIFFIN, Beatrice Mary.—b. 1909; ed. Royal Sch. for Naval Officers’ Daughters, Twickenham; (asst. dispenser’s cert.) nursing sister, Gib., 1936; senr. matron, Cyprus, 1945; matron in ch., Ken., 1949.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1936 | (asst. dispenser’s cert.) nursing sister | Gibraltar | [1950, 1951] |
| 1 | 1945 | senr. matron | Cyprus | [1950, 1951] |
| 2 | 1949 | matron in ch. | Kenya | [1950, 1951] |

## Candidate stint `Griffin, B. M___Kenya___1950`

- Staff-list name: **Griffin, B. M** | colony: **Kenya** | listed 1950–1951 | editions [1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | B. M. Griffin | Matron-in-Chief | Medical | — | — |
| 1951 | B. M. Griffin | Matron-in-Chief | Medical | — | — |

### Deterministic checks: `griffin_beatrice-mary_b1909` vs `Griffin, B. M___Kenya___1950`

- [PASS] surname_gate: bio 'GRIFFIN' vs stint 'Griffin, B. M' (exact)
- [PASS] initials: bio ['B', 'M'] ~ stint ['B', 'M']
- [PASS] age_gate: stint starts 1950, birth 1909 (age 41)
- [PASS] colony: 1 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1950-1951
- [FAIL] position_sim: best 48 vs bar 60: 'matron in ch.' ~ 'Matron-in-Chief'
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

