<!-- {"case_id": "case_polak_k-w_b1904", "bio_ids": ["polak_k-w_b1904"], "stint_ids": ["Polack, K. W___Jamaica___1937"]} -->
# Dossier case_polak_k-w_b1904

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `polak_k-w_b1904`

- Printed name: **POLAK, K. W**
- Birth year: 1904 (attested in editions [1957, 1958, 1959])
- Appears in editions: [1957, 1958, 1959]

### Verbatim printed entry text (OCR)

**Version `col1957-L26427.v` — printed in editions [1957, 1958, 1959]:**

> POLAK, K. W.—b. 1904; ed. Manning's Sch., J'ca; barrister-at-law, Lincoln's Inn; asst. clk., resdt. mag's courts dept., J'ca, 1924; dep. clk., courts, 1934; clk. to atty.-gen., 1938; clk., courts, 1944; resdt. mag. 1953–58.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1924 | asst. clk., resdt. mag's courts dept. | Jamaica | [1957, 1958, 1959] |
| 1 | 1934 | dep. clk., courts | Jamaica *(inherited from previous clause)* | [1957, 1958, 1959] |
| 2 | 1938 | clk. to atty.-gen | Jamaica *(inherited from previous clause)* | [1957, 1958, 1959] |
| 3 | 1944 | clk., courts | Jamaica *(inherited from previous clause)* | [1957, 1958, 1959] |
| 4 | 1953–1958 | resdt. mag | Jamaica *(inherited from previous clause)* | [1957, 1958, 1959] |

## Candidate stint `Polack, K. W___Jamaica___1937`

- Staff-list name: **Polack, K. W** | colony: **Jamaica** | listed 1937–1940 | editions [1937, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1937 | K. W. Polack | Senior Assistant Clerk of Court | Senior Assistant Clerks of Courts | — | — |
| 1940 | K. W. Polack | Clerk to Chief Justice | Judicial and Legal | — | — |

### Deterministic checks: `polak_k-w_b1904` vs `Polack, K. W___Jamaica___1937`

- [PASS] surname_gate: bio 'POLAK' vs stint 'Polack, K. W' (fuzzy:1)
- [PASS] initials: bio ['K', 'W'] ~ stint ['K', 'W']
- [PASS] age_gate: stint starts 1937, birth 1904 (age 33)
- [PASS] colony: 5 placed event(s) resolve to 'Jamaica'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1937-1940
- [FAIL] position_sim: best 49 vs bar 60: 'dep. clk., courts' ~ 'Senior Assistant Clerk of Court'
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

