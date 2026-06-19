<!-- {"case_id": "case_chorley_thomas-wallace_b1909", "bio_ids": ["chorley_thomas-wallace_b1909"], "stint_ids": ["Chorley, T. W___Uganda___1936"]} -->
# Dossier case_chorley_thomas-wallace_b1909

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `chorley_thomas-wallace_b1909`

- Printed name: **CHORLEY, Thomas Wallace**
- Birth year: 1909 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L31760.v` — printed in editions [1948, 1949, 1950, 1951]:**

> CHORLEY, Thomas Wallace.—b. 1909; ed. Heversham Sch. (Gram.), and Nairobi Govt. Sch.; laboratory apprentice to entomologist, 1929; laboratory asst., 1935; senr. field offr., tsetse control dept., 1946, Uga.; author of numerous papers and articles for agricultural and entomological journals.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1929 | laboratory apprentice to entomologist | — | [1948, 1949, 1950, 1951] |
| 1 | 1935 | laboratory asst. | — | [1948, 1949, 1950, 1951] |
| 2 | 1946 | senr. field offr., tsetse control dept. | Uganda | [1948, 1949, 1950, 1951] |

## Candidate stint `Chorley, T. W___Uganda___1936`

- Staff-list name: **Chorley, T. W** | colony: **Uganda** | listed 1936–1940 | editions [1936, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | T. W. Chorley | Laboratory Assistant | Agricultural Department | — | — |
| 1937 | T. W. Chorley | Laboratory Assistant | Agricultural Department | — | — |
| 1939 | T. W. Chorley | Laboratory Assistant | Agricultural Department | — | — |
| 1940 | T. W. Chorley | Laboratory Assistant | Medical | — | — |

### Deterministic checks: `chorley_thomas-wallace_b1909` vs `Chorley, T. W___Uganda___1936`

- [PASS] surname_gate: bio 'CHORLEY' vs stint 'Chorley, T. W' (exact)
- [PASS] initials: bio ['T', 'W'] ~ stint ['T', 'W']
- [PASS] age_gate: stint starts 1936, birth 1909 (age 27)
- [PASS] colony: 1 placed event(s) resolve to 'Uganda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1936-1940
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

