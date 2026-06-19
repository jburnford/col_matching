<!-- {"case_id": "case_stevens_frank-lewis_b1887", "bio_ids": ["stevens_frank-lewis_b1887"], "stint_ids": ["Stevens, F. L___Kenya___1922", "Stevens, F. L___Kenya___1937"]} -->
# Dossier case_stevens_frank-lewis_b1887

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 66 official(s) with this surname in the graph's staff lists; 28 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `stevens_frank-lewis_b1887`

- Printed name: **STEVENS, Frank Lewis**
- Birth year: 1887 (attested in editions [1949])
- Honours: M.B.E
- Appears in editions: [1949]

### Verbatim printed entry text (OCR)

**Version `col1949-L35897.v` — printed in editions [1949]:**

> STEVENS, Frank Lewis, M.B.E.—b. 1887; tel. inspr., B. E.A., 1913; sub-engnr., 1918; asst. engrnr., Ken., Uga. and T.T., 1934; div. engr., E.A., 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1913 | tel. inspr., B. E.A | — | [1949] |
| 1 | 1918 | sub-engnr | — | [1949] |
| 2 | 1934 | asst. engrnr., Ken., Uga. and T.T | Uganda | [1949] |
| 3 | 1946 | div. engr., E.A | Uganda *(inherited from previous clause)* | [1949] |

## Candidate stint `Stevens, F. L___Kenya___1922`

- Staff-list name: **Stevens, F. L** | colony: **Kenya** | listed 1922–1932 | editions [1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1932]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | F. L. Stevens | Sub-Engineer | Post and Telegraphs Department | — | — |
| 1923 | F. L. Stevens | Sub-Engineer | Post and Telegraph Department | — | — |
| 1924 | F. L. Stevens | Sub-Engineers | Post and Telegraph Department | — | — |
| 1925 | F. L. Stevens | Sub-Engineers | Post and Telegraph Department | — | — |
| 1927 | F. L. Stevens | Sub-Engineers | Engineering Staff | — | — |
| 1928 | F. L. Stevens | Sub-Engineers | Engineering Staff | — | — |
| 1929 | F. L. Stevens | Sub-Engineers | Engineering Staff | — | — |
| 1930 | F. L. Stevens | Sub-Engineers | Posts and Telegraphs Department | — | — |
| 1932 | F. L. Stevens | Sub-Engineers | Posts and Telegraphs Department | — | — |

### Deterministic checks: `stevens_frank-lewis_b1887` vs `Stevens, F. L___Kenya___1922`

- [PASS] surname_gate: bio 'STEVENS' vs stint 'Stevens, F. L' (exact)
- [PASS] initials: bio ['F', 'L'] ~ stint ['F', 'L']
- [PASS] age_gate: stint starts 1922, birth 1887 (age 35)
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1922-1932
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Stevens, F. L___Kenya___1937`

- Staff-list name: **Stevens, F. L** | colony: **Kenya** | listed 1937–1940 | editions [1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1937 | F. L. Stevens | Assistant Engineers | Posts and Telegraphs Department | — | — |
| 1939 | F. L. Stevens | Assistant Engineer | Posts and Telegraphs Department | — | — |
| 1940 | F. L. Stevens | Assistant Engineer | Posts and Telegraphs Department | — | — |

### Deterministic checks: `stevens_frank-lewis_b1887` vs `Stevens, F. L___Kenya___1937`

- [PASS] surname_gate: bio 'STEVENS' vs stint 'Stevens, F. L' (exact)
- [PASS] initials: bio ['F', 'L'] ~ stint ['F', 'L']
- [PASS] age_gate: stint starts 1937, birth 1887 (age 50)
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1937-1940
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

