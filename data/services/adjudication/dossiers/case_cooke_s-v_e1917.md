<!-- {"case_id": "case_cooke_s-v_e1917", "bio_ids": ["cooke_s-v_e1917", "cooke_s-v_e1917-2"], "stint_ids": ["Cooke, S. V___Kenya___1940"]} -->
# Dossier case_cooke_s-v_e1917

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 46 official(s) with this surname in the graph's staff lists; 25 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Cooke, S. V___Kenya___1940'] have more than one claimant biography in this case.

## Biography `cooke_s-v_e1917`

- Printed name: **COOKE, S. V**
- Birth year: not printed
- Appears in editions: [1918, 1919, 1921, 1922, 1924, 1925, 1927, 1930, 1931]

### Verbatim printed entry text (OCR)

**Version `col1918-L49542.v` — printed in editions [1918, 1919, 1921, 1922, 1924, 1925, 1927, 1930, 1931]:**

> COOKE, S. V.—Asst. dist. comsnr., E.A.P., Jan., 1917.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1917 | Asst. dist. comsnr. | East Africa Protectorate | [1918, 1919, 1921, 1922, 1924, 1925, 1927, 1930, 1931] |

## Biography `cooke_s-v_e1917-2`

- Printed name: **COOKE, S. V**
- Birth year: not printed
- Appears in editions: [1932, 1933, 1935, 1936]

### Verbatim printed entry text (OCR)

**Version `dol1935-L57740.v` — printed in editions [1935, 1936]:**

> COOKE, S. V.—Asst. dist. commnr., E.A.P., Jan., 1917; accompanied S. Aulitian (Somali) patrol, 1917-18; polit. offr., Turkana, 1921; A.G.S. med. and clasp.; dist. commnr., Kenya, 1928; dist. offr., Tanganyika Territory, July, 1931.

**Version `col1932-L59286.v` — printed in editions [1932, 1933]:**

> COOKE, S. V.—Asts. dist. commr., E.A.P., Jan., 1917; dist., offr. Tanganyika Territory, July, 1931.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1917 | Asst. dist. commnr. | East Africa Protectorate | [1932, 1933, 1935, 1936] |
| 1 | 1921 | polit. offr., Turkana | East Africa Protectorate *(inherited from previous clause)* | [1935, 1936] |
| 2 | 1928 | dist. commnr. | Kenya | [1935, 1936] |
| 3 | 1931 | dist. offr., Tanganyika Territory | Tanganyika | [1932, 1933, 1935, 1936] |

## Candidate stint `Cooke, S. V___Kenya___1940`

- Staff-list name: **Cooke, S. V** | colony: **Kenya** | listed 1940–1948 | editions [1940, 1946, 1948]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1940 | S. V. Cooke | European Elected Member | — | — | — |
| 1946 | S. V. Cooke | Member | European Elected Members | — | — |
| 1948 | S. V. Cooke | — | Legislative Council | — | — |

### Deterministic checks: `cooke_s-v_e1917` vs `Cooke, S. V___Kenya___1940`

- [PASS] surname_gate: bio 'COOKE' vs stint 'Cooke, S. V' (exact)
- [PASS] initials: bio ['S', 'V'] ~ stint ['S', 'V']
- [PASS] age_gate: stint starts 1940; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1940-1948
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `cooke_s-v_e1917-2` vs `Cooke, S. V___Kenya___1940`

- [PASS] surname_gate: bio 'COOKE' vs stint 'Cooke, S. V' (exact)
- [PASS] initials: bio ['S', 'V'] ~ stint ['S', 'V']
- [PASS] age_gate: stint starts 1940; no printed birth year — UNCHECKED
- [PASS] colony: 3 placed event(s) resolve to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1940-1948
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

