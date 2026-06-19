<!-- {"case_id": "case_piggott_charles-francis-lovell_b1890", "bio_ids": ["piggott_charles-francis-lovell_b1890"], "stint_ids": ["Piggott, C. F. L___Tanganyika___1920"]} -->
# Dossier case_piggott_charles-francis-lovell_b1890

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `piggott_charles-francis-lovell_b1890`

- Printed name: **PIGGOTT, CHARLES FRANCIS LOVELL**
- Birth year: 1890 (attested in editions [1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931])
- Appears in editions: [1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931]

### Verbatim printed entry text (OCR)

**Version `col1923-L57373.v` — printed in editions [1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931]:**

> PIGGOTT, CHARLES FRANCIS LOVELL, M.A.—B. 1890; ed. Dean Close Schol. and Univ. Coll., Oxford; asst. sec., Tanganyika Territory, 1919-22; supt. educn., dept., N. Prov., Nigeria, 17th May, 1922.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1919–1922 | asst. sec., Tanganyika Territory | Tanganyika | [1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931] |
| 1 | 1922 | supt. educn., dept., N. Prov. | Nigeria | [1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931] |

## Candidate stint `Piggott, C. F. L___Tanganyika___1920`

- Staff-list name: **Piggott, C. F. L** | colony: **Tanganyika** | listed 1920–1922 | editions [1920, 1921, 1922]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1920 | Captain C. F. L. Piggott | Assistant Secretaries | Secretariat | — | Captain |
| 1921 | C. F. L. Piggott | Assistant Secretaries | Secretariat | — | — |
| 1922 | C. F. L. Piggott | Assistant Secretaries | Secretariat | — | — |

### Deterministic checks: `piggott_charles-francis-lovell_b1890` vs `Piggott, C. F. L___Tanganyika___1920`

- [PASS] surname_gate: bio 'PIGGOTT' vs stint 'Piggott, C. F. L' (exact)
- [PASS] initials: bio ['C', 'F', 'L'] ~ stint ['C', 'F', 'L']
- [PASS] age_gate: stint starts 1920, birth 1890 (age 30)
- [PASS] colony: 1 placed event(s) resolve to 'Tanganyika'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1920-1922
- [FAIL] position_sim: best 48 vs bar 60: 'asst. sec., Tanganyika Territory' ~ 'Assistant Secretaries'
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

