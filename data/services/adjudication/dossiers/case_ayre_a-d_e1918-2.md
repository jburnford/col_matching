<!-- {"case_id": "case_ayre_a-d_e1918-2", "bio_ids": ["ayre_a-d_e1918-2"], "stint_ids": ["Ayre, A. D___Kenya___1909", "Ayre, A. D___Tanganyika___1920"]} -->
# Dossier case_ayre_a-d_e1918-2

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `ayre_a-d_e1918-2`

- Printed name: **AYRE, A. D**
- Birth year: not printed
- Appears in editions: [1921, 1922]

### Verbatim printed entry text (OCR)

**Version `col1921-L54230.v` — printed in editions [1921, 1922]:**

> AYRE, A. D.—Chief acctnt., G.P.O., E. Africa Prot., Mar., 1918; dep. P.M.G., Tanganyika Territory, 1st Oct., 1919.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1918 | Chief acctnt., G.P.O., E. Africa Prot | — | [1921, 1922] |
| 1 | 1919 | dep. P.M.G., Tanganyika Territory | Tanganyika | [1921, 1922] |

## Candidate stint `Ayre, A. D___Kenya___1909`

- Staff-list name: **Ayre, A. D** | colony: **Kenya** | listed 1909–1920 | editions [1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1920]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1909 | A. D. Ayre | First Class Postmaster | Post and Telegraphs | — | — |
| 1910 | A. D. Ayre | First Class Postmaster | Post and Telegraphs | — | — |
| 1911 | A. D. Ayre | First Class Postmaster | Post and Telegraphs | — | — |
| 1912 | A. D. Ayre | First Class Postmaster | Post and Telegraphs | — | — |
| 1913 | A. D. Ayre | First Class Postmaster | Post and Telegraphs | — | — |
| 1914 | A. D. Ayre | First Class Postmaster | Post and Telegraphs | — | — |
| 1915 | A. D. Ayre | Assistant Postmaster-General | Post and Telegraphs | — | — |
| 1917 | A. D. Ayre | Assistant Postmasters-General | Post and Telegraphs | — | — |
| 1918 | A. D. Ayre | Assistant Postmasters-General | Post and Telegraphs | — | — |
| 1920 | A. D. Ayre | Chief Accountant | Post and Telegraphs | — | — |

### Deterministic checks: `ayre_a-d_e1918-2` vs `Ayre, A. D___Kenya___1909`

- [PASS] surname_gate: bio 'AYRE' vs stint 'Ayre, A. D' (exact)
- [PASS] initials: bio ['A', 'D'] ~ stint ['A', 'D']
- [PASS] age_gate: stint starts 1909; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1909-1920
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Ayre, A. D___Tanganyika___1920`

- Staff-list name: **Ayre, A. D** | colony: **Tanganyika** | listed 1920–1922 | editions [1920, 1921, 1922]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1920 | A. D. Ayre | Deputy Postmaster-General | Post and Telegraphs Department | — | — |
| 1921 | A. D. Ayre | Deputy Postmaster-General | Post and Telegraphs Department | — | — |
| 1922 | A. D. Ayre | Deputy Postmaster-General | Post and Telegraphs Department | — | — |

### Deterministic checks: `ayre_a-d_e1918-2` vs `Ayre, A. D___Tanganyika___1920`

- [PASS] surname_gate: bio 'AYRE' vs stint 'Ayre, A. D' (exact)
- [PASS] initials: bio ['A', 'D'] ~ stint ['A', 'D']
- [PASS] age_gate: stint starts 1920; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Tanganyika'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1920-1922
- [FAIL] position_sim: best 42 vs bar 60: 'dep. P.M.G., Tanganyika Territory' ~ 'Deputy Postmaster-General'
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

