<!-- {"case_id": "case_whineray_sidney-buckingham_b1879", "bio_ids": ["whineray_sidney-buckingham_b1879"], "stint_ids": ["Whineray, S. B___Tanganyika___1923"]} -->
# Dossier case_whineray_sidney-buckingham_b1879

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `whineray_sidney-buckingham_b1879`

- Printed name: **WHINERAY, SIDNEY BUCKINGHAM**
- Birth year: 1879 (attested in editions [1929, 1930, 1931, 1932])
- Appears in editions: [1929, 1930, 1931, 1932]

### Verbatim printed entry text (OCR)

**Version `col1929-L64973.v` — printed in editions [1929, 1930, 1931, 1932]:**

> WHINERAY, SIDNEY BUCKINGHAM.—B. 1879; ass't. acct., Baro Kano rly., N. Nigeria, 1911; Nigerian rly., 1913; sp. investgn., accts., miny. of munitions, 1918; ass't. acct., Tanganyika rly., 1922; ag. dep. ch. acct., 1923 and 1928-29.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1911 | ass't. acct., Baro Kano rly. | Nigeria | [1929, 1930, 1931, 1932] |
| 1 | 1913 | Nigerian rly. | Nigeria | [1929, 1930, 1931, 1932] |
| 2 | 1918 | sp. investgn., accts., miny. of munitions | — | [1929, 1930, 1931, 1932] |
| 3 | 1922 | ass't. acct. | Tanganyika | [1929, 1930, 1931, 1932] |
| 4 | 1923–1929 | ag. dep. ch. acct. | — | [1929, 1930, 1931, 1932] |

## Candidate stint `Whineray, S. B___Tanganyika___1923`

- Staff-list name: **Whineray, S. B** | colony: **Tanganyika** | listed 1923–1925 | editions [1923, 1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1923 | S. B. Whineray | Assistant Chief Accountants | Railways | — | — |
| 1924 | S. B. Whineray | Assistant Chief Accountants | Railways | — | — |
| 1925 | S. B. Whineray | Assistant Chief Accountants | Railways | — | — |

### Deterministic checks: `whineray_sidney-buckingham_b1879` vs `Whineray, S. B___Tanganyika___1923`

- [PASS] surname_gate: bio 'WHINERAY' vs stint 'Whineray, S. B' (exact)
- [PASS] initials: bio ['S', 'B'] ~ stint ['S', 'B']
- [PASS] age_gate: stint starts 1923, birth 1879 (age 44)
- [PASS] colony: 1 placed event(s) resolve to 'Tanganyika'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1923-1925
- [FAIL] position_sim: best 50 vs bar 60: 'ass't. acct.' ~ 'Assistant Chief Accountants'
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

