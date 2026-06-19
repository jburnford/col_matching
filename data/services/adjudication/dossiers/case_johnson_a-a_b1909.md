<!-- {"case_id": "case_johnson_a-a_b1909", "bio_ids": ["johnson_a-a_b1909"], "stint_ids": ["Johnson, A. C. A___Sierra Leone___1933"]} -->
# Dossier case_johnson_a-a_b1909

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 224 official(s) with this surname in the graph's staff lists; 86 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Johnson, A. C. A___Sierra Leone___1933` is also gate-compatible with biography(ies) outside this case: ['johnson_charles_b1912'] (already linked elsewhere or filtered).

## Biography `johnson_a-a_b1909`

- Printed name: **JOHNSON, A. A**
- Birth year: 1909 (attested in editions [1957, 1959, 1964])
- Appears in editions: [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1957-L24530.v` — printed in editions [1957, 1959, 1964]:**

> JOHNSON, A. A.—b. 1909; ed. Taunton's Sch., S'ton; printer, N. Rhod., 1945; senr. printer, 1952; asst. govt. printer, 1954-63.

**Version `col1958-L24084.v` — printed in editions [1958, 1960, 1961, 1962, 1963]:**

> JOHNSTON, A. A.—b. 1909; ed. Taunton's Sch., S'ton; printer, N. Rhod., 1945; senr. printer, 1952; asst. govt. printer, 1954.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1945 | printer | Northern Rhodesia | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 1 | 1952 | senr. printer | Northern Rhodesia *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 2 | 1954–1963 | asst. govt. printer | Northern Rhodesia *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |

## Candidate stint `Johnson, A. C. A___Sierra Leone___1933`

- Staff-list name: **Johnson, A. C. A** | colony: **Sierra Leone** | listed 1933–1940 | editions [1933, 1934, 1936, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | A. Johnson | Medical Officer | Medical | — | — |
| 1934 | A. Johnson | Medical Officers | Medical | — | — |
| 1936 | A. Johnson | Medical Officers | Medical | — | — |
| 1937 | A. Johnson | Medical Officers (Col. Med. Service) | Medical Department | — | — |
| 1939 | A. Johnson | Medical Officer | Medical Department | — | — |
| 1940 | A. Johnson | Medical Officers (Col. Med. Service) | Medical Department | — | — |

### Deterministic checks: `johnson_a-a_b1909` vs `Johnson, A. C. A___Sierra Leone___1933`

- [PASS] surname_gate: bio 'JOHNSON' vs stint 'Johnson, A. C. A' (exact)
- [PASS] initials: bio ['A', 'A'] ~ stint ['A', 'C', 'A']
- [PASS] age_gate: stint starts 1933, birth 1909 (age 24)
- [FAIL] colony: no placed event resolves to 'Sierra Leone'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1933-1940
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

