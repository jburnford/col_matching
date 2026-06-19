<!-- {"case_id": "case_woolfall_richard_b1901", "bio_ids": ["woolfall_richard_b1901"], "stint_ids": ["Woolfall, R___Kenya___1929"]} -->
# Dossier case_woolfall_richard_b1901

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['woolfall_richard_b1901'] carry a single initial only — the namesake trap applies.

## Biography `woolfall_richard_b1901`

- Printed name: **WOOLFALL, Richard**
- Birth year: 1901 (attested in editions [1957])
- Honours: A.M.I.E.E, I.S.O (1956)
- Appears in editions: [1948, 1949, 1950, 1951, 1957]

### Verbatim printed entry text (OCR)

**Version `col1957-L28590.v` — printed in editions [1957]:**

> WOOLFALL, R., I.S.O. (1956)—b. 1901; ed. Tiber Sch., L'pool; Br. P.O., 1919-25; tel. inspr., E.A. posts and tels. dept., 1925; sub-engnr., 1933; asst. engrn., 1945; exec engrn., 1951; dep. regl. dir., 1952.

**Version `col1948-L37032.v` — printed in editions [1948, 1949, 1950, 1951]:**

> WOOLFALL, Richard, A.M.I.E.E., A.M.Brit.I.R.E.—b. 1901; ed. Tiber Sch., Liverpool; tel. inspr., Ken., Uga. and T.T. posts and tels. dept., 1925; asst. engrnr., Ken., Uga. and T.T. (later, E.A.), 1945.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1919–1925 | Br. P.O | — | [1957] |
| 1 | 1925 | tel. inspr., E.A. posts and tels. dept | Uganda | [1948, 1949, 1950, 1951, 1957] |
| 2 | 1933 | sub-engnr | — | [1957] |
| 3 | 1945 | asst. engrn | — | [1957] |
| 4 | 1945 | asst. engrnr., Ken., Uga. and T.T. (later, E.A.) | Uganda *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 5 | 1951 | exec engrn | — | [1957] |
| 6 | 1952 | dep. regl. dir | — | [1957] |

## Candidate stint `Woolfall, R___Kenya___1929`

- Staff-list name: **Woolfall, R** | colony: **Kenya** | listed 1929–1932 | editions [1929, 1930, 1932]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1929 | R. Woolfall | Telegraph Inspectors | Engineering Staff | — | — |
| 1930 | R. Woolfall | Telegraph Inspectors | Posts and Telegraphs Department | — | — |
| 1932 | R. Woolfall | Telegraph Inspectors | Posts and Telegraphs Department | — | — |

### Deterministic checks: `woolfall_richard_b1901` vs `Woolfall, R___Kenya___1929`

- [PASS] surname_gate: bio 'WOOLFALL' vs stint 'Woolfall, R' (exact)
- [PASS] initials: bio ['R'] ~ stint ['R']
- [PASS] age_gate: stint starts 1929, birth 1901 (age 28)
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1929-1932
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

