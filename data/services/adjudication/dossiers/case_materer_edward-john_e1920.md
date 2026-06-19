<!-- {"case_id": "case_materer_edward-john_e1920", "bio_ids": ["materer_edward-john_e1920"], "stint_ids": ["Mateer, E. J___Uganda___1921"]} -->
# Dossier case_materer_edward-john_e1920

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- Phase 1 found `materer_edward-john_e1920` ↔ `Mateer, E. J___Uganda___1921` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Mateer, E. J___Uganda___1921` is also gate-compatible with biography(ies) outside this case: ['mateer_edward-john_e1920'] (already linked elsewhere or filtered).

## Biography `materer_edward-john_e1920`

- Printed name: **MATERER, EDWARD JOHN**
- Birth year: not printed
- Appears in editions: [1931]

### Verbatim printed entry text (OCR)

**Version `col1931-L66592.v` — printed in editions [1931]:**

> MATERER, EDWARD JOHN.—Ed. Foyle Coll. and Taunton Schol.; asst. treas., Uganda, 10th July, 1920.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1920 | asst. treas. | Uganda | [1931] |

## Candidate stint `Mateer, E. J___Uganda___1921`

- Staff-list name: **Mateer, E. J** | colony: **Uganda** | listed 1921–1940 | editions [1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1933, 1936, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1921 | E. J. Mateer | Assistant | Treasury and Savings Bank | — | Captain |
| 1922 | Capt. E. J. Mateer | Assistant | Treasury and Savings Bank | — | Captain |
| 1923 | E. J. Mateer | Assistant Treasurer, 2nd Grade | Treasury and Savings Bank | — | Captain |
| 1924 | E. J. Mateer | Assistant Treasurer, 2nd Grade | Treasury and Savings Bank | — | Captain |
| 1925 | E. J. Mateer | Assistant Treasurer, 2nd Grade | Treasury and Savings Bank | — | Captain |
| 1927 | Capt. E. J. Mateer | Senior Assistant and Assistant Treasurers | Treasury and Savings Bank | — | Captain |
| 1928 | Captain E. J. Mateer | Senior Assistant Treasurer | Treasury and Savings Bank | — | Captain |
| 1929 | E. J. Mateer | Assistant Treasurer | Treasury and Savings Bank | — | Captain |
| 1930 | E. J. Mateer | Assistant Treasurer | Treasury and Savings Bank | — | Captain |
| 1933 | E. J. Mateer | Senior Assistant Treasurer | Treasury and Savings Bank | — | Captain |
| 1936 | E. J. Mateer | Principal Assistant Treasurer | Treasury and Savings Bank | — | Captain |
| 1937 | E. J. Mateer | Principal Assistant Treasurer | Treasury and Savings Bank | — | Captain |
| 1939 | Capt. E. J. Mateer | Principal Assistant Accountant-General | Accountant-General's Department | — | Captain |
| 1940 | E. J. Mateer | Principal Assistant Treasurer | Accountant-General's Department | — | Captain |

### Deterministic checks: `materer_edward-john_e1920` vs `Mateer, E. J___Uganda___1921`

- [PASS] surname_gate: bio 'MATERER' vs stint 'Mateer, E. J' (fuzzy:1)
- [PASS] initials: bio ['E', 'J'] ~ stint ['E', 'J']
- [PASS] age_gate: stint starts 1921; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1921-1940
- [PASS] position_sim: best 69 vs bar 60: 'asst. treas.' ~ 'Assistant Treasurer'
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

