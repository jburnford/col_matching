<!-- {"case_id": "case_ingham_phillip-stanley_b1888", "bio_ids": ["ingham_phillip-stanley_b1888"], "stint_ids": ["Ingham, P. S___Bermuda___1920"]} -->
# Dossier case_ingham_phillip-stanley_b1888

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 14 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `ingham_phillip-stanley_b1888`

- Printed name: **INGHAM, Phillip Stanley**
- Birth year: 1888 (attested in editions [1948, 1949])
- Appears in editions: [1948, 1949]

### Verbatim printed entry text (OCR)

**Version `col1948-L33559.v` — printed in editions [1948, 1949]:**

> INGHAM, Phillip Stanley, M.M.—b. 1888; ed. Saltus Gram. Sch., Bermuda; on mil. serv. 1915-17 and 1931-35, maj.; post office clk., Berm., 1919; asst. col. postmstr., 1922; col. postmstr., 1929; vice-pres., Berm. V.F.Assn.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1919 | post office clk. | Bermuda | [1948, 1949] |
| 1 | 1922 | asst. col. postmstr | Bermuda *(inherited from previous clause)* | [1948, 1949] |
| 2 | 1929 | col. postmstr | Bermuda *(inherited from previous clause)* | [1948, 1949] |

## Candidate stint `Ingham, P. S___Bermuda___1920`

- Staff-list name: **Ingham, P. S** | colony: **Bermuda** | listed 1920–1939 | editions [1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1936, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1920 | P. S. Ingham | 3rd Clerk | Post Office Department | — | — |
| 1921 | P. S. Ingham | 1st Clerk | Post Office Department | — | — |
| 1922 | P. S. Ingham | Assist. Colonial Postmaster | Post Office Department | — | — |
| 1923 | P. S. Ingham | Assist. Colonial Postmaster | Post Office Department | — | — |
| 1924 | P. S. Ingham | Assist. Colonial Postmaster | Post Office Department | — | — |
| 1925 | P. S. Ingham | Assist. Colonial Postmaster | Post Office Department | — | — |
| 1927 | P. S. Ingham | Assist. Colonial Postmaster | Post Office Department | — | — |
| 1928 | P. S. Ingham | Assist. Colonial Postmaster | Post Office Department | — | — |
| 1929 | P. S. Ingham | Assist. Colonial Postmaster | Post Office Department | — | — |
| 1930 | P. S. Ingham | Colonial Postmaster | Post Office Department | — | — |
| 1931 | P. S. Ingham | Colonial Postmaster | Post Office Department | — | — |
| 1932 | P. S. Ingham | Colonial Postmaster | Post Office Department | — | — |
| 1933 | P. S. Ingham | Colonial Postmaster | Post Office Department | — | — |
| 1934 | P. S. Ingham | Colonial Postmaster | Post Office Department | — | — |
| 1936 | P. S. Ingham | Colonial Postmaster | Post Office Department | — | — |
| 1939 | P. S. Ingham | Colonial Postmaster | Post Office Department | — | — |

### Deterministic checks: `ingham_phillip-stanley_b1888` vs `Ingham, P. S___Bermuda___1920`

- [PASS] surname_gate: bio 'INGHAM' vs stint 'Ingham, P. S' (exact)
- [PASS] initials: bio ['P', 'S'] ~ stint ['P', 'S']
- [PASS] age_gate: stint starts 1920, birth 1888 (age 32)
- [PASS] colony: 3 placed event(s) resolve to 'Bermuda'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1920-1939
- [PASS] position_sim: best 79 vs bar 60: 'asst. col. postmstr' ~ 'Assist. Colonial Postmaster'
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

