<!-- {"case_id": "case_coe_victor-rembrandt_b1894", "bio_ids": ["coe_victor-rembrandt_b1894"], "stint_ids": ["Coe, V. R___Gold Coast___1923"]} -->
# Dossier case_coe_victor-rembrandt_b1894

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `coe_victor-rembrandt_b1894`

- Printed name: **COE, Victor Rembrandt**
- Birth year: 1894 (attested in editions [1948, 1949])
- Honours: A.M.I.S.E, M.R.S.I
- Appears in editions: [1948, 1949]

### Verbatim printed entry text (OCR)

**Version `col1948-L31830.v` — printed in editions [1948, 1949]:**

> COE, Victor Rembrandt, M.R.S.I., A.M.I.S.E.—b. 1894; on mil. serv. 1915-19; sany. supt., G.C., 1923.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1923 | sany. supt. | Gold Coast | [1948, 1949] |

## Candidate stint `Coe, V. R___Gold Coast___1923`

- Staff-list name: **Coe, V. R** | colony: **Gold Coast** | listed 1923–1929 | editions [1923, 1924, 1927, 1928, 1929]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1923 | V. R. Coe | Superintending Sanitary Inspector | Sanitation Branch | — | — |
| 1924 | V. R. Coe | Supervising Sanitary Inspector | Sanitation Branch | — | — |
| 1927 | V. R. Coe | Supervising Sanitary Inspector | Sanitation Branch | — | — |
| 1928 | V. R. Coe | Superintending Sanitary Inspector | Sanitation Branch | — | — |
| 1929 | V. R. Coe | Superintending Sanitary Inspector | Sanitation Branch | — | — |

### Deterministic checks: `coe_victor-rembrandt_b1894` vs `Coe, V. R___Gold Coast___1923`

- [PASS] surname_gate: bio 'COE' vs stint 'Coe, V. R' (exact)
- [PASS] initials: bio ['V', 'R'] ~ stint ['V', 'R']
- [PASS] age_gate: stint starts 1923, birth 1894 (age 29)
- [PASS] colony: 1 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1923-1929
- [FAIL] position_sim: best 43 vs bar 60: 'sany. supt.' ~ 'Superintending Sanitary Inspector'
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

