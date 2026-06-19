<!-- {"case_id": "case_baker_victor_b1897", "bio_ids": ["baker_victor_b1897"], "stint_ids": ["Baker, W. V. C___Fiji___1950"]} -->
# Dossier case_baker_victor_b1897

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 91 official(s) with this surname in the graph's staff lists; 52 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['baker_victor_b1897'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Baker, W. V. C___Fiji___1950` is also gate-compatible with biography(ies) outside this case: ['baker_william-vernon-carew_b1915', 'baker_william_e1878'] (already linked elsewhere or filtered).

## Biography `baker_victor_b1897`

- Printed name: **BAKER, Victor**
- Birth year: 1897 (attested in editions [1949])
- Appears in editions: [1948, 1949]

### Verbatim printed entry text (OCR)

**Version `col1949-L30207.v` — printed in editions [1949]:**

> BAKER, Victor.—b. 1897; ed. Higher Elem. Sch., Swindon; fitter, rlwys., Nig., 1928; loco foreman, gr. II, 1930; gr. I, 1937; asst. dist. supt., gr. II, 1942; senr. asst. loco supt., 1946.

**Version `col1948-L30945.v` — printed in editions [1948]:**

> BAKER, Victor.—b. 1897; ed. Higher Elem. Sch., Swindon; shed artisan, Nig., 1928; loco. foreman, 1929; asst. dist. running supt., 1942; senr. asst. loco. supt., 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | fitter, rlwys. | Nigeria | [1948, 1949] |
| 1 | 1929 | loco. foreman | Nigeria *(inherited from previous clause)* | [1948] |
| 2 | 1930 | loco foreman, gr. II | Nigeria *(inherited from previous clause)* | [1949] |
| 3 | 1937 | gr. I | Nigeria *(inherited from previous clause)* | [1949] |
| 4 | 1942 | asst. dist. supt., gr. II | Nigeria *(inherited from previous clause)* | [1948, 1949] |
| 5 | 1946 | senr. asst. loco supt | Nigeria *(inherited from previous clause)* | [1948, 1949] |

## Candidate stint `Baker, W. V. C___Fiji___1950`

- Staff-list name: **Baker, W. V. C** | colony: **Fiji** | listed 1950–1951 | editions [1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | W. V. C. Baker | Assistant Secretary (seconded from District Administration) | Secretariat | — | — |
| 1951 | W. V. C. Baker | Administrative Officer (Grade II) | District Administration | — | — |

### Deterministic checks: `baker_victor_b1897` vs `Baker, W. V. C___Fiji___1950`

- [PASS] surname_gate: bio 'BAKER' vs stint 'Baker, W. V. C' (exact)
- [PASS] initials: bio ['V'] ~ stint ['W', 'V', 'C']
- [PASS] age_gate: stint starts 1950, birth 1897 (age 53)
- [FAIL] colony: no placed event resolves to 'Fiji'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1950-1951
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

