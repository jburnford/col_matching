<!-- {"case_id": "case_moore_r_b1915", "bio_ids": ["moore_r_b1915"], "stint_ids": ["Moore, R. C. P___Windward Islands___1950"]} -->
# Dossier case_moore_r_b1915

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 128 official(s) with this surname in the graph's staff lists; 38 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['moore_r_b1915'] carry a single initial only — the namesake trap applies.

## Biography `moore_r_b1915`

- Printed name: **MOORE, R**
- Birth year: 1915 (attested in editions [1962])
- Appears in editions: [1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1962-L24588.v` — printed in editions [1962]:**

> MOORE, R.—b. 1915; ed. Kings Sch., Glos.; civ. engr. pupil, 1933; engr. asst. local govt., U.K., 1936; mil. serv., 1939–46, Royal Eng. capt.; senr. civ. engr., loc. govt., U.K., 1946; staff. engr. (roads), Fiji, 1951.

**Version `col1963-L22989.v` — printed in editions [1963, 1964, 1965, 1966]:**

> MOORE, R.—b. 1915; ed. King's Sch., Glos.; mil. serv., 1939–46, Royal Eng., capt.; civ. engr. pupil., 1933; engr. asst. local govt., U.K., 1936; senr. civ. engr., loc. govt., U.K., 1946; staff. engr. (roads), Fiji, 1951–65.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1933 | civ. engr. pupil | — | [1962, 1963, 1964, 1965, 1966] |
| 1 | 1936 | engr. asst. local govt., U.K | — | [1962, 1963, 1964, 1965, 1966] |
| 2 | 1946 | senr. civ. engr., loc. govt., U.K | — | [1962, 1963, 1964, 1965, 1966] |
| 3 | 1951 | staff. engr. (roads) | Fiji | [1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Moore, R. C. P___Windward Islands___1950`

- Staff-list name: **Moore, R. C. P** | colony: **Windward Islands** | listed 1950–1952 | editions [1950, 1952]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | R. C. P. Moore | Elected | Legislative Council | — | — |
| 1952 | R. C. P. Moore | Elected | Legislative Council | — | — |

### Deterministic checks: `moore_r_b1915` vs `Moore, R. C. P___Windward Islands___1950`

- [PASS] surname_gate: bio 'MOORE' vs stint 'Moore, R. C. P' (exact)
- [PASS] initials: bio ['R'] ~ stint ['R', 'C', 'P']
- [PASS] age_gate: stint starts 1950, birth 1915 (age 35)
- [FAIL] colony: no placed event resolves to 'Windward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1950-1952
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

