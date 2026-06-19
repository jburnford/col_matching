<!-- {"case_id": "case_bacon_percy_b1899", "bio_ids": ["bacon_percy_b1899"], "stint_ids": ["Bacon, P___Mauritius___1925"]} -->
# Dossier case_bacon_percy_b1899

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['bacon_percy_b1899'] carry a single initial only — the namesake trap applies.

## Biography `bacon_percy_b1899`

- Printed name: **BACON, Percy**
- Birth year: 1899 (attested in editions [1950])
- Appears in editions: [1948, 1949, 1950]

### Verbatim printed entry text (OCR)

**Version `col1950-L33358.v` — printed in editions [1950]:**

> BACON, Percy.—b. 1899; ed. Camb. Univ., M.A.; apptd. Maur., 1923; headmr. Royal Coll. Sch., Maur., 1942; prin., boys’ sec. sch., Bo., S.L., 1948.

**Version `col1948-L30911.v` — printed in editions [1948, 1949]:**

> BACON, Percy.—b. 1899; ed. Cambridge Univ., M.A.; apptd. Maur., 1923; head-mastr., Royal Coll. Sch., Maur., 1942.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1923 | apptd. Maur | — | [1948, 1949, 1950] |
| 1 | 1942 | headmr. Royal Coll. Sch. | Mauritius | [1948, 1949, 1950] |
| 2 | 1948 | prin., boys’ sec. sch., Bo. | Sierra Leone | [1950] |

## Candidate stint `Bacon, P___Mauritius___1925`

- Staff-list name: **Bacon, P** | colony: **Mauritius** | listed 1925–1939 | editions [1925, 1927, 1928, 1929, 1931, 1932, 1936, 1937, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1925 | P. Bacon | Masters | Education | — | — |
| 1927 | P. Bacon | Masters | Education | — | — |
| 1928 | P. Bacon | Masters | Education | — | — |
| 1929 | P. Bacon | Masters | Education | — | — |
| 1931 | P. Bacon | Masters | Education | — | — |
| 1932 | P. Bacon | Masters | Education | — | — |
| 1936 | P. Bacon | Teacher | Education | — | — |
| 1937 | P. Bacon | Masters | Education | — | — |
| 1939 | P. Bacon | Masters | Education | — | — |

### Deterministic checks: `bacon_percy_b1899` vs `Bacon, P___Mauritius___1925`

- [PASS] surname_gate: bio 'BACON' vs stint 'Bacon, P' (exact)
- [PASS] initials: bio ['P'] ~ stint ['P']
- [PASS] age_gate: stint starts 1925, birth 1899 (age 26)
- [PASS] colony: 1 placed event(s) resolve to 'Mauritius'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1925-1939
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

