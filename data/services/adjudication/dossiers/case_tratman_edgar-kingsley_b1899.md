<!-- {"case_id": "case_tratman_edgar-kingsley_b1899", "bio_ids": ["tratman_edgar-kingsley_b1899"], "stint_ids": ["Tratman, E. K___Straits Settlements___1931"]} -->
# Dossier case_tratman_edgar-kingsley_b1899

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `tratman_edgar-kingsley_b1899`

- Printed name: **TRATMAN, EDGAR KINGSLEY**
- Birth year: 1899 (attested in editions [1935, 1936, 1937, 1939, 1940])
- Honours: L.D.S, M.D.S
- Appears in editions: [1935, 1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `dol1935-L62786.v` — printed in editions [1935, 1936, 1937, 1939, 1940]:**

> TRATMAN, EDGAR KINGSLEY, L.D.S., M.D.S.—B., 1899; ed. Clifton Coll. and Bristol Univ.; prof., dental surgery, coll. of med., S'pore, Oct., 1929; mem., dental bd., F.M.S., Apr., 1931; do., S.S., July, 1931.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1929 | prof., dental surgery, coll. of med., S'pore | — | [1935, 1936, 1937, 1939, 1940] |
| 1 | 1931 | mem., dental bd. | Federated Malay States | [1935, 1936, 1937, 1939, 1940] |

## Candidate stint `Tratman, E. K___Straits Settlements___1931`

- Staff-list name: **Tratman, E. K** | colony: **Straits Settlements** | listed 1931–1936 | editions [1931, 1933, 1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | E. K. Tratman | Professor of Dental Surgery | King Edward VII College of Medicine | — | — |
| 1933 | E. K. Tratman | Professor of Dental Surgery | King Edward VII College of Medicine | — | — |
| 1934 | E. K. Tratman | Professor of Dental Surgery | King Edward VII College of Medicine, Singapore | — | — |
| 1936 | E. K. Tratman | Professor of Dental Surgery | Medical | — | — |

### Deterministic checks: `tratman_edgar-kingsley_b1899` vs `Tratman, E. K___Straits Settlements___1931`

- [PASS] surname_gate: bio 'TRATMAN' vs stint 'Tratman, E. K' (exact)
- [PASS] initials: bio ['E', 'K'] ~ stint ['E', 'K']
- [PASS] age_gate: stint starts 1931, birth 1899 (age 32)
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1931-1936
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

