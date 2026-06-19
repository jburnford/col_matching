<!-- {"case_id": "case_whitehouse_george-cecil_b1900", "bio_ids": ["whitehouse_george-cecil_b1900"], "stint_ids": ["Whitehouse, G. C___Uganda___1924"]} -->
# Dossier case_whitehouse_george-cecil_b1900

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `whitehouse_george-cecil_b1900`

- Printed name: **WHITEHOUSE, George Cecil**
- Birth year: 1900 (attested in editions [1948, 1949])
- Appears in editions: [1948, 1949]

### Verbatim printed entry text (OCR)

**Version `col1948-L36806.v` — printed in editions [1948, 1949]:**

> WHITEHOUSE, George Cecil.—b. 1900; ed. Gresham's Sch.; cadet, Uga., 1923; dist. comsnr.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1923 | cadet | Uganda | [1948, 1949] |

## Candidate stint `Whitehouse, G. C___Uganda___1924`

- Staff-list name: **Whitehouse, G. C** | colony: **Uganda** | listed 1924–1949 | editions [1924, 1925, 1927, 1928, 1929, 1930, 1933, 1936, 1937, 1939, 1940, 1949]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1924 | G. C. Whitehouse | 2nd Grade Administrative Officer | Administration | — | — |
| 1925 | G. C. Whitehouse | 2nd Grade Administrative Officer | Civil Establishment | — | — |
| 1927 | G. C. Whitehouse | Administrative Officer | Provincial Administration | — | — |
| 1928 | G. C. Whitehouse | Administrative Officer | Provincial Administration | — | — |
| 1929 | G. C. Whitehouse | Administrative Officer | Provincial Administration | — | — |
| 1930 | G. C. Whitehouse | District Officer | District Officers and Assistant District Officers | — | — |
| 1933 | G. C. Whitehouse | District Officers and Assistant District Officers | Provincial Administration | — | — |
| 1936 | G. C. Whitehouse | District Officer | Provincial Administration | — | — |
| 1937 | G. C. Whitehouse | District Officers and Assistant District Officers | Provincial Administration | — | — |
| 1939 | G. C. Whitehouse | District Officer | Provincial Administration | — | — |
| 1940 | G. C. Whitehouse | District Officers and Assistant District Officers | Provincial Administration | — | — |
| 1949 | G. C. Whitehouse | District Officers and Assistant District Officers | Provincial Administration | — | — |

### Deterministic checks: `whitehouse_george-cecil_b1900` vs `Whitehouse, G. C___Uganda___1924`

- [PASS] surname_gate: bio 'WHITEHOUSE' vs stint 'Whitehouse, G. C' (exact)
- [PASS] initials: bio ['G', 'C'] ~ stint ['G', 'C']
- [PASS] age_gate: stint starts 1924, birth 1900 (age 24)
- [PASS] colony: 1 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1924-1949
- [FAIL] position_sim: best 22 vs bar 60: 'cadet' ~ 'Administrative Officer'
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

