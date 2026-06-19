<!-- {"case_id": "case_hickman_a-e_e1918", "bio_ids": ["hickman_a-e_e1918"], "stint_ids": ["Hickman, Albert___Newfoundland___1913"]} -->
# Dossier case_hickman_a-e_e1918

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Hickman, Albert___Newfoundland___1913` is also gate-compatible with biography(ies) outside this case: ['hickman_albert-e_e1913'] (already linked elsewhere or filtered).

## Biography `hickman_a-e_e1918`

- Printed name: **HICKMAN, A. E**
- Birth year: not printed
- Appears in editions: [1918]

### Verbatim printed entry text (OCR)

**Version `col1918-L51311.v` — printed in editions [1918]:**

> HICKMAN, HON. A. E.—Minister without portfolio, Newfoundland, Jan., 1918.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1918 | Minister without portfolio | Newfoundland | [1918] |

## Candidate stint `Hickman, Albert___Newfoundland___1913`

- Staff-list name: **Hickman, Albert** | colony: **Newfoundland** | listed 1913–1921 | editions [1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1913 | A. E. Hickman | Consul | Foreign Consuls | — | — |
| 1914 | A. E. Hickman | Consul | Foreign Consuls | — | — |
| 1915 | A. E. Hickman | Consul | Foreign Consuls | — | — |
| 1917 | Albert Hickman | Member for Bay de Verde | House of Assembly | — | — |
| 1917 | A. E. Hickman | Consul | Foreign Consuls | — | — |
| 1918 | A. E. Hickman | Consul | Foreign Consuls | — | — |
| 1918 | A. E. Hickman | Consul | Judicial Establishment | — | — |
| 1919 | A. E. Hickman | Consul | Foreign Consuls | — | — |
| 1920 | A. E. Hickman | Consul | Foreign Consuls | — | — |
| 1921 | A. E. Hickman | Consul | Foreign Consuls | — | — |

### Deterministic checks: `hickman_a-e_e1918` vs `Hickman, Albert___Newfoundland___1913`

- [PASS] surname_gate: bio 'HICKMAN' vs stint 'Hickman, Albert' (exact)
- [PASS] initials: bio ['A', 'E'] ~ stint ['A']
- [PASS] age_gate: stint starts 1913; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Newfoundland'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1913-1921
- [FAIL] position_sim: best 20 vs bar 60: 'Minister without portfolio' ~ 'Member for Bay de Verde'
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

