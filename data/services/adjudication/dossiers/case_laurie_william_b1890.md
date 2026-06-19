<!-- {"case_id": "case_laurie_william_b1890", "bio_ids": ["laurie_william_b1890"], "stint_ids": ["Laurie, C. W. F___Barbados___1928"]} -->
# Dossier case_laurie_william_b1890

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 17 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['laurie_william_b1890'] carry a single initial only — the namesake trap applies.

## Biography `laurie_william_b1890`

- Printed name: **LAURIE, WILLIAM**
- Birth year: 1890 (attested in editions [1936])
- Appears in editions: [1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1936-L62361.v` — printed in editions [1936]:**

> LAURIE, WILLIAM, M.Inst.M., M.Cy.E.—B. 1890; astt. engrnr., Kedah, Apr., 1920; ag. exec. engrnr., Johore, Jan., 1925; exec. engrnr., F.M.S., Apr., 1929; do., Kedah, June, 1933.

**Version `col1939-L68518.v` — printed in editions [1939, 1940]:**

> LAURIE, WILLIAM, M.Inst.M., M.Cy.E.—B. 1890; ass't engnr., Kedah, Apr., 1920; exec. engnr., F.M.S., Apr., 1929; ag. senr. exec. engnr., Nov., 1936; senr. exec. engnr., Jan., 1938.

**Version `col1937-L62524.v` — printed in editions [1937]:**

> LAURIE, William, M.Inst. M., M.Cy.E.—B. 1890; asts. engnr., Kedah, Apr., 1920; exec. engnr., F.M.S., Apr., 1929; do., Kedah, June, 1933.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1920 | astt. engrnr. | Kedah | [1936, 1937, 1939, 1940] |
| 1 | 1925 | ag. exec. engrnr. | Johore | [1936] |
| 2 | 1929 | exec. engrnr. | Federated Malay States | [1936, 1937, 1939, 1940] |
| 3 | 1933 | exec. engrnr. | Kedah | [1936, 1937] |
| 4 | 1936 | ag. senr. exec. engnr | Federated Malay States *(inherited from previous clause)* | [1939, 1940] |
| 5 | 1938 | senr. exec. engnr | Federated Malay States *(inherited from previous clause)* | [1939, 1940] |

## Candidate stint `Laurie, C. W. F___Barbados___1928`

- Staff-list name: **Laurie, C. W. F** | colony: **Barbados** | listed 1928–1930 | editions [1928, 1929, 1930]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1928 | C. W. F. Laurie | Assistant Master | Educational | — | — |
| 1929 | C. W. F. Laurie | Assistant Masters | Educational | — | — |
| 1930 | C. W. F. Laurie | Assistant Master | Educational | — | — |

### Deterministic checks: `laurie_william_b1890` vs `Laurie, C. W. F___Barbados___1928`

- [PASS] surname_gate: bio 'LAURIE' vs stint 'Laurie, C. W. F' (exact)
- [PASS] initials: bio ['W'] ~ stint ['C', 'W', 'F']
- [PASS] age_gate: stint starts 1928, birth 1890 (age 38)
- [FAIL] colony: no placed event resolves to 'Barbados'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1928-1930
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

