<!-- {"case_id": "case_duff_steuart-murray_b1906", "bio_ids": ["duff_steuart-murray_b1906"], "stint_ids": ["Duff, S. M___Ceylon___1931"]} -->
# Dossier case_duff_steuart-murray_b1906

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 32 official(s) with this surname in the graph's staff lists; 18 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Duff, S. M___Ceylon___1931` is also gate-compatible with biography(ies) outside this case: ['duff_stuart-murray_b1906'] (already linked elsewhere or filtered).

## Biography `duff_steuart-murray_b1906`

- Printed name: **DUFF, STEUART MURRAY**
- Birth year: 1906 (attested in editions [1931, 1932, 1933, 1934, 1935])
- Appears in editions: [1930, 1931, 1932, 1933, 1934, 1935]

### Verbatim printed entry text (OCR)

**Version `col1931-L63894.v` — printed in editions [1931, 1932, 1933, 1934, 1935]:**

> DUFF, STEUART MURRAY, B.A.—B. 1906; cadet, Ceylon civ. serv., 1928; attd., Kandy kach., Jan., 1929; attd. Anuradhapura kach., Jan., 1930; office asst., Nuwara Eliya kach., May, 1930; pol. mag., Gampola, Oct., 1931; office asst., Jaffna kach., Feb., 1934.

**Version `col1930-L64081.v` — printed in editions [1930]:**

> DUFF, STEUART MURRAY.—B. 1906; cadet, Ceylon civ., serv., 1928; attd., Kandy kach., Jan., 1929.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | cadet, Ceylon civ. serv | Ceylon | [1930, 1931, 1932, 1933, 1934, 1935] |
| 1 | 1929 | attd., Kandy kach | Ceylon *(inherited from previous clause)* | [1930, 1931, 1932, 1933, 1934, 1935] |
| 2 | 1930 | attd. Anuradhapura kach | Ceylon *(inherited from previous clause)* | [1931, 1932, 1933, 1934, 1935] |
| 3 | 1931 | pol. mag., Gampola | Ceylon *(inherited from previous clause)* | [1931, 1932, 1933, 1934, 1935] |
| 4 | 1934 | office asst., Jaffna kach | Ceylon *(inherited from previous clause)* | [1931, 1932, 1933, 1934, 1935] |

## Candidate stint `Duff, S. M___Ceylon___1931`

- Staff-list name: **Duff, S. M** | colony: **Ceylon** | listed 1931–1940 | editions [1931, 1936, 1937, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | S. M. Duff | Office Assistant | Government Agencies | — | — |
| 1931 | S. M. Duff | Clerk | Civil Establishment | — | — |
| 1936 | S. M. Duff | Commissioner of Requests and Police Magistrate | District Judges, Commissioners of Requests, Police Magistrates and Municipal Magistrates | — | — |
| 1936 | S. M. Duff | Office Assistant | North Western Province | — | — |
| 1937 | S. M. Duff | Additional Assistant Government Agent (Land) | SOUTHERN PROVINCE | — | — |
| 1937 | S. M. Duff | Police Magistrate and Municipal Magistrate | District Judges, Commissioners of Requests, Police Magistrates and Municipal Magistrates | — | — |
| 1940 | S. M. Duff | Secretary | Colombo Port Commission | — | — |

### Deterministic checks: `duff_steuart-murray_b1906` vs `Duff, S. M___Ceylon___1931`

- [PASS] surname_gate: bio 'DUFF' vs stint 'Duff, S. M' (exact)
- [PASS] initials: bio ['S', 'M'] ~ stint ['S', 'M']
- [PASS] age_gate: stint starts 1931, birth 1906 (age 25)
- [PASS] colony: 5 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 4 event tenure(s) overlap stint years 1931-1940
- [PASS] position_sim: best 67 vs bar 60: 'office asst., Jaffna kach' ~ 'Office Assistant'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

