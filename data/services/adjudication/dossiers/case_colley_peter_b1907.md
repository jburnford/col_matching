<!-- {"case_id": "case_colley_peter_b1907", "bio_ids": ["colley_peter_b1907"], "stint_ids": ["Colley, P___Western Pacific___1936"]} -->
# Dossier case_colley_peter_b1907

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['colley_peter_b1907'] carry a single initial only — the namesake trap applies.

## Biography `colley_peter_b1907`

- Printed name: **COLLEY, Peter**
- Birth year: 1907 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L31861.v` — printed in editions [1948, 1949, 1950, 1951]:**

> COLLEY, Peter.—b. 1907; ed. Downside Sch., Somerset; clk., Fiji, 1929; clk., res. comsnt., off., Br. Sol. Is. Prot., 1933; cadet, 1941; cadet, N. Heb., 1942; admin. offr., 1945.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1929 | clk. | Fiji | [1948, 1949, 1950, 1951] |
| 1 | 1933 | clk., res. comsnt., off., Br. Sol. Is. Prot | Fiji *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 2 | 1941 | cadet | Fiji *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 3 | 1942 | cadet, N. Heb | Fiji *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 4 | 1945 | admin. offr | Fiji *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Colley, P___Western Pacific___1936`

- Staff-list name: **Colley, P** | colony: **Western Pacific** | listed 1936–1939 | editions [1936, 1937, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | P. Colley | Clerk, Resident Commissioner's office | Secretariat | — | — |
| 1937 | P. Colley | Clerk, Resident Commissioner's office | Secretariat | — | — |
| 1939 | P. Colley | Clerk | Secretariat | — | — |

### Deterministic checks: `colley_peter_b1907` vs `Colley, P___Western Pacific___1936`

- [PASS] surname_gate: bio 'COLLEY' vs stint 'Colley, P' (exact)
- [PASS] initials: bio ['P'] ~ stint ['P']
- [PASS] age_gate: stint starts 1936, birth 1907 (age 29)
- [FAIL] colony: no placed event resolves to 'Western Pacific'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1936-1939
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

