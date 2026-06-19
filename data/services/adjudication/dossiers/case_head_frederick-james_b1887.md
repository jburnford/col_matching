<!-- {"case_id": "case_head_frederick-james_b1887", "bio_ids": ["head_frederick-james_b1887"], "stint_ids": ["Head, F. J___Southern Nigeria___1912"]} -->
# Dossier case_head_frederick-james_b1887

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `head_frederick-james_b1887`

- Printed name: **HEAD, FREDERICK JAMES**
- Birth year: 1887 (attested in editions [1931])
- Appears in editions: [1931]

### Verbatim printed entry text (OCR)

**Version `col1931-L65215.v` — printed in editions [1931]:**

> HEAD, FREDERICK JAMES.—B. 1887; ed. Merchant Venturer Tech. Coll., Bristol; asst. supt., tels., Nigeria, 1911; engr., 1914; lieut., R.W.A.F.F., 1914-15; suptg. engr., 1922; divnl. engr., 1927.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1911 | asst. supt., tels. | Nigeria | [1931] |
| 1 | 1914 | engr | Nigeria *(inherited from previous clause)* | [1931] |
| 2 | 1922 | suptg. engr | Nigeria *(inherited from previous clause)* | [1931] |
| 3 | 1927 | divnl. engr | Nigeria *(inherited from previous clause)* | [1931] |

## Candidate stint `Head, F. J___Southern Nigeria___1912`

- Staff-list name: **Head, F. J** | colony: **Southern Nigeria** | listed 1912–1913 | editions [1912, 1913]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | F. J. Head | Assistant Superintendent | Telegraphs | — | — |
| 1913 | F. J. Head | Assistant Superintendent | Telegraphs | — | — |

### Deterministic checks: `head_frederick-james_b1887` vs `Head, F. J___Southern Nigeria___1912`

- [PASS] surname_gate: bio 'HEAD' vs stint 'Head, F. J' (exact)
- [PASS] initials: bio ['F', 'J'] ~ stint ['F', 'J']
- [PASS] age_gate: stint starts 1912, birth 1887 (age 25)
- [FAIL] colony: no placed event resolves to 'Southern Nigeria'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1913
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

