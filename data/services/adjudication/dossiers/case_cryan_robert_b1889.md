<!-- {"case_id": "case_cryan_robert_b1889", "bio_ids": ["cryan_robert_b1889"], "stint_ids": ["Cryan, R___Hong Kong___1927"]} -->
# Dossier case_cryan_robert_b1889

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['cryan_robert_b1889'] carry a single initial only — the namesake trap applies.

## Biography `cryan_robert_b1889`

- Printed name: **CRYAN, ROBERT**
- Birth year: 1889 (attested in editions [1937, 1940])
- Appears in editions: [1937, 1940]

### Verbatim printed entry text (OCR)

**Version `col1937-L60087.v` — printed in editions [1937, 1940]:**

> CRYAN, ROBERT.—B. 1889; asst. elec. engnr., P.W.D., Hong Kong, 1924; elec. engnr., 1934; ag. ch. do., 1928, 1931, 1935.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1924–1924 | asst. elec. engnr., P.W.D. | Hong Kong | [1937, 1940] |
| 1 | 1928–1935 | ag. ch. do. | — | [1937, 1940] |
| 2 | 1934–1934 | elec. engnr. | — | [1937, 1940] |

## Candidate stint `Cryan, R___Hong Kong___1927`

- Staff-list name: **Cryan, R** | colony: **Hong Kong** | listed 1927–1940 | editions [1927, 1928, 1929, 1930, 1931, 1933, 1934, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | R. Cryan | Engineer | Electrical | — | — |
| 1928 | R. Cryan | Engineer | Electrical | — | — |
| 1929 | R. Cryan | Engineers | Electrical | — | — |
| 1930 | R. Cryan | Engineer | Electrical | — | — |
| 1931 | R. Cryan | Engineer | Electrical | — | — |
| 1933 | R. Cryan | Assistant Electrical Engineer | Public Works Department | — | — |
| 1934 | R. Cryan | Assistant Electrical Engineer | Public Works Department | — | — |
| 1937 | R. Cryan | Electrical Engineer | Public Works Department | — | — |
| 1939 | R. Cryan | Chief Electrical Engineer | Public Works Department | — | — |
| 1940 | R. Cryan | Chief Electrical Engineer | Public Works Department | — | — |

### Deterministic checks: `cryan_robert_b1889` vs `Cryan, R___Hong Kong___1927`

- [PASS] surname_gate: bio 'CRYAN' vs stint 'Cryan, R' (exact)
- [PASS] initials: bio ['R'] ~ stint ['R']
- [PASS] age_gate: stint starts 1927, birth 1889 (age 38)
- [PASS] colony: 1 placed event(s) resolve to 'Hong Kong'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1927-1940
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

