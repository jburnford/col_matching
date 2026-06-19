<!-- {"case_id": "case_arthur_edward_b1904", "bio_ids": ["arthur_edward_b1904"], "stint_ids": ["Arthur, E. C___Grenada___1963"]} -->
# Dossier case_arthur_edward_b1904

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 22 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['arthur_edward_b1904'] carry a single initial only — the namesake trap applies.

## Biography `arthur_edward_b1904`

- Printed name: **ARTHUR, Edward**
- Birth year: 1904 (attested in editions [1949, 1950])
- Appears in editions: [1949, 1950]

### Verbatim printed entry text (OCR)

**Version `col1949-L30113.v` — printed in editions [1949, 1950]:**

> ARTHUR, Edward, B.Sc. (Glas.).—b. 1904; ed. Queens Pk. Sch. and Royal Tech. Coll., Glasgow; asst. supt., dispensers’ training sch., Lagos, Nig., 1929; supt., pharmacy sch., 1933; educ. dept., 1939.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1929 | asst. supt., dispensers’ training sch., Lagos | Nigeria | [1949, 1950] |
| 1 | 1933 | supt., pharmacy sch | Nigeria *(inherited from previous clause)* | [1949, 1950] |

## Candidate stint `Arthur, E. C___Grenada___1963`

- Staff-list name: **Arthur, E. C** | colony: **Grenada** | listed 1963–1966 | editions [1963, 1964, 1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1963 | E. C. Arthur | Veterinary Officer | Civil Establishment | — | — |
| 1964 | E. C. Arthur | Veterinary Officer | Civil Establishment | — | — |
| 1965 | E. C. Arthur | Veterinary Officer | Civil Establishment | — | — |
| 1966 | E. C. Arthur | Veterinary Officer | Civil Establishment | — | — |

### Deterministic checks: `arthur_edward_b1904` vs `Arthur, E. C___Grenada___1963`

- [PASS] surname_gate: bio 'ARTHUR' vs stint 'Arthur, E. C' (exact)
- [PASS] initials: bio ['E'] ~ stint ['E', 'C']
- [PASS] age_gate: stint starts 1963, birth 1904 (age 59)
- [FAIL] colony: no placed event resolves to 'Grenada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1963-1966
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

