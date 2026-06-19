<!-- {"case_id": "case_randle_samuel_b1897", "bio_ids": ["randle_samuel_b1897"], "stint_ids": ["Randle, S___Hong Kong___1933"]} -->
# Dossier case_randle_samuel_b1897

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['randle_samuel_b1897'] carry a single initial only — the namesake trap applies.

## Biography `randle_samuel_b1897`

- Printed name: **RANDLE, Samuel**
- Birth year: 1897 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L35416.v` — printed in editions [1948, 1949, 1950, 1951]:**

> RANDLE, Samuel.—b. 1897; ed. Hill Street Sch., Brierley Hill; on mil. serv. 1917–18; clk., H.K., 1925; senr. clerical and acctng. clk., 1928; asst. supt., of mails, 1933; supt. of mails, 1936; contrlr. of posts, 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1925 | clk. | Hong Kong | [1948, 1949, 1950, 1951] |
| 1 | 1928 | senr. clerical and acctng. clk | Hong Kong *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 2 | 1933 | asst. supt., of mails | Hong Kong *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 3 | 1936 | supt. of mails | Hong Kong *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 4 | 1938 | contrlr. of posts | Hong Kong *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Randle, S___Hong Kong___1933`

- Staff-list name: **Randle, S** | colony: **Hong Kong** | listed 1933–1940 | editions [1933, 1934, 1936, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | S. Randle | Assistant Superintendent | Post Office | — | — |
| 1934 | S. Randle | Assistant Superintendent | Post Office | — | — |
| 1936 | S. Randle | Assistant Superintendent | Post Office | — | — |
| 1937 | S. Randle | Superintendent of Mails | Post Office | — | — |
| 1939 | S. Randle | Controller of Posts | Post Office | — | — |
| 1940 | S. Randle | Controller of Posts | Post Office | — | — |

### Deterministic checks: `randle_samuel_b1897` vs `Randle, S___Hong Kong___1933`

- [PASS] surname_gate: bio 'RANDLE' vs stint 'Randle, S' (exact)
- [PASS] initials: bio ['S'] ~ stint ['S']
- [PASS] age_gate: stint starts 1933, birth 1897 (age 36)
- [PASS] colony: 5 placed event(s) resolve to 'Hong Kong'
- [PASS] tenure_overlap: 4 event tenure(s) overlap stint years 1933-1940
- [PASS] position_sim: best 91 vs bar 60: 'contrlr. of posts' ~ 'Controller of Posts'
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

