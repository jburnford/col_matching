<!-- {"case_id": "case_kennan_myles_b1894", "bio_ids": ["kennan_myles_b1894"], "stint_ids": ["Kennan, Myles___Basutoland___1920"]} -->
# Dossier case_kennan_myles_b1894

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['kennan_myles_b1894'] carry a single initial only — the namesake trap applies.

## Biography `kennan_myles_b1894`

- Printed name: **KENNAN, MYLES**
- Birth year: 1894 (attested in editions [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1935, 1936])
- Appears in editions: [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1935, 1936]

### Verbatim printed entry text (OCR)

**Version `col1927-L60277.v` — printed in editions [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1935, 1936]:**

> KENNAN, MYLES.—B. 1894; clk., Basutoland, 1913; war serv., 1915-18; sub-inspr., Basutoland mounted pol., 1926.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1913 | clk. | Basutoland | [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1935, 1936] |
| 1 | 1926 | sub-inspr., Basutoland mounted pol | Basutoland | [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1935, 1936] |

## Candidate stint `Kennan, Myles___Basutoland___1920`

- Staff-list name: **Kennan, Myles** | colony: **Basutoland** | listed 1920–1925 | editions [1920, 1921, 1922, 1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1920 | Myles Kennan | Clerk to Assistant Commissioner | Civil Establishment | — | — |
| 1921 | Myles Kennan | Clerk to Assistant Commissioner | Establishment | — | — |
| 1922 | Myles Kennan | Clerk to Assistant Commissioner, Leribe | Establishment | — | — |
| 1924 | Myles Kennan | Clerk to Assistant Commissioner | District Administration | — | — |
| 1925 | Myles Kennan | Clerk to Assistant Commissioners | District Administration | — | — |

### Deterministic checks: `kennan_myles_b1894` vs `Kennan, Myles___Basutoland___1920`

- [PASS] surname_gate: bio 'KENNAN' vs stint 'Kennan, Myles' (exact)
- [PASS] initials: bio ['M'] ~ stint ['M']
- [PASS] age_gate: stint starts 1920, birth 1894 (age 26)
- [PASS] colony: 2 placed event(s) resolve to 'Basutoland'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1920-1925
- [FAIL] position_sim: best 42 vs bar 60: 'sub-inspr., Basutoland mounted pol' ~ 'Clerk to Assistant Commissioner'
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

