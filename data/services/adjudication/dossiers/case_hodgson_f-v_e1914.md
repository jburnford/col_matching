<!-- {"case_id": "case_hodgson_f-v_e1914", "bio_ids": ["hodgson_f-v_e1914"], "stint_ids": ["Hodgson, F___Northern Rhodesia___1930", "Hodgson, F___Northern Rhodesia___1936"]} -->
# Dossier case_hodgson_f-v_e1914

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 37 official(s) with this surname in the graph's staff lists; 21 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Hodgson, F___Northern Rhodesia___1930` is also gate-compatible with biography(ies) outside this case: ['hodgson_f_e1873', 'hodgson_frederic-mitchell_b1851'] (already linked elsewhere or filtered).
- NOTE: stint `Hodgson, F___Northern Rhodesia___1936` is also gate-compatible with biography(ies) outside this case: ['hodgson_f_e1873', 'hodgson_frederic-mitchell_b1851'] (already linked elsewhere or filtered).

## Biography `hodgson_f-v_e1914`

- Printed name: **HODGSON, F. V**
- Birth year: not printed
- Appears in editions: [1917, 1918, 1919, 1920, 1921, 1922, 1923]

### Verbatim printed entry text (OCR)

**Version `col1917-L50417.v` — printed in editions [1917, 1918, 1919, 1920, 1921, 1922, 1923]:**

> HODGSON, F. V.—Treasy. asst., E.A.P., May, 1914.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914 | Treasy. asst. | East Africa Protectorate | [1917, 1918, 1919, 1920, 1921, 1922, 1923] |

## Candidate stint `Hodgson, F___Northern Rhodesia___1930`

- Staff-list name: **Hodgson, F** | colony: **Northern Rhodesia** | listed 1930–1931 | editions [1930, 1931]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1930 | F. Hodgson | Industrial Inspector | Native Education | — | — |
| 1931 | F. Hodgson | Industrial Inspector | Native Education | — | — |

### Deterministic checks: `hodgson_f-v_e1914` vs `Hodgson, F___Northern Rhodesia___1930`

- [PASS] surname_gate: bio 'HODGSON' vs stint 'Hodgson, F' (exact)
- [PASS] initials: bio ['F', 'V'] ~ stint ['F']
- [PASS] age_gate: stint starts 1930; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Northern Rhodesia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1930-1931
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Hodgson, F___Northern Rhodesia___1936`

- Staff-list name: **Hodgson, F** | colony: **Northern Rhodesia** | listed 1936–1940 | editions [1936, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | F. Hodgson | Principal, Lusaka Trades School | Native Education | — | — |
| 1937 | F. Hodgson | Principal, Lusaka Trades School | Native Education | — | — |
| 1939 | F. Hodgson | Principal | Native Education | — | — |
| 1940 | F. Hodgson | Principal, Munali Training Centre | Native Education | — | — |

### Deterministic checks: `hodgson_f-v_e1914` vs `Hodgson, F___Northern Rhodesia___1936`

- [PASS] surname_gate: bio 'HODGSON' vs stint 'Hodgson, F' (exact)
- [PASS] initials: bio ['F', 'V'] ~ stint ['F']
- [PASS] age_gate: stint starts 1936; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Northern Rhodesia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1936-1940
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

