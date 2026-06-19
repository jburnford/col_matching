<!-- {"case_id": "case_nankivell_k_b1903", "bio_ids": ["nankivell_k_b1903"], "stint_ids": ["Nankivell, K___Straits Settlements___1931"]} -->
# Dossier case_nankivell_k_b1903

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['nankivell_k_b1903'] carry a single initial only — the namesake trap applies.

## Biography `nankivell_k_b1903`

- Printed name: **NANKIVELL, K**
- Birth year: 1903 (attested in editions [1954, 1955, 1956, 1957])
- Appears in editions: [1954, 1955, 1956, 1957]

### Verbatim printed entry text (OCR)

**Version `col1954-L21688.v` — printed in editions [1954, 1955, 1956, 1957]:**

> NANKIVELL, K.—b. 1903; ed. High Sch., Braintree, and King's Coll., Lond.; mil. serv., 1942-45; asst. engrnr., Mal. P.W.S., 1926; exec. engrnr., 1935; senr., 1940; state engrnr., gr. II, 1947; gr. I, 1948; D.P.W., 1953.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1926 | asst. engrnr., Mal. P.W.S | Malaya | [1954, 1955, 1956, 1957] |
| 1 | 1935 | exec. engrnr | Malaya *(inherited from previous clause)* | [1954, 1955, 1956, 1957] |
| 2 | 1940 | senr | Malaya *(inherited from previous clause)* | [1954, 1955, 1956, 1957] |
| 3 | 1947 | state engrnr., gr. II | Malaya *(inherited from previous clause)* | [1954, 1955, 1956, 1957] |
| 4 | 1948 | gr. I | Malaya *(inherited from previous clause)* | [1954, 1955, 1956, 1957] |
| 5 | 1953 | D.P.W | Malaya *(inherited from previous clause)* | [1954, 1955, 1956, 1957] |

## Candidate stint `Nankivell, K___Straits Settlements___1931`

- Staff-list name: **Nankivell, K** | colony: **Straits Settlements** | listed 1931–1939 | editions [1931, 1933, 1934, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | K. Nankivell | Assistant Engineer | Public Works | — | — |
| 1933 | K. Nankivell | Assistant Engineers | Public Works | — | — |
| 1934 | K. Nankivell | Assistant Engineer | Public Works | — | — |
| 1939 | K. Nankivell | Executive Engineers | Public Works | — | — |

### Deterministic checks: `nankivell_k_b1903` vs `Nankivell, K___Straits Settlements___1931`

- [PASS] surname_gate: bio 'NANKIVELL' vs stint 'Nankivell, K' (exact)
- [PASS] initials: bio ['K'] ~ stint ['K']
- [PASS] age_gate: stint starts 1931, birth 1903 (age 28)
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1931-1939
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

