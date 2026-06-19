<!-- {"case_id": "case_meeek_a-i_e1918", "bio_ids": ["meeek_a-i_e1918"], "stint_ids": ["Meek, A. I___Tanganyika___1923"]} -->
# Dossier case_meeek_a-i_e1918

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Meek, A. I___Tanganyika___1923` is also gate-compatible with biography(ies) outside this case: ['meek_a-i_b1889'] (already linked elsewhere or filtered).

## Biography `meeek_a-i_e1918`

- Printed name: **MEEEK, A. I**
- Birth year: not printed
- Honours: L.R.C.P, L.R.C.S
- Appears in editions: [1930]

### Verbatim printed entry text (OCR)

**Version `col1930-L66780.v` — printed in editions [1930]:**

> MEEEK, A. I., L.R.C.P., L.R.C.S., D.P.H. (Edin.), L.R.F.P. & S. (Glas.)—R.A.M.C., Aug., 1918 to May, 1920; med. offr., Tanganyika Territory, May, 1922.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1918–1920 | R.A.M.C | — | [1930] |
| 1 | 1922 | med. offr., Tanganyika Territory | Tanganyika | [1930] |

## Candidate stint `Meek, A. I___Tanganyika___1923`

- Staff-list name: **Meek, A. I** | colony: **Tanganyika** | listed 1923–1924 | editions [1923, 1924]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1923 | A. I. Meek | Medical Officer | Medical Division | — | — |
| 1924 | A. I. Meek | Medical Officer | Medical Division | — | — |

### Deterministic checks: `meeek_a-i_e1918` vs `Meek, A. I___Tanganyika___1923`

- [PASS] surname_gate: bio 'MEEEK' vs stint 'Meek, A. I' (fuzzy:1)
- [PASS] initials: bio ['A', 'I'] ~ stint ['A', 'I']
- [PASS] age_gate: stint starts 1923; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Tanganyika'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1923-1924
- [FAIL] position_sim: best 45 vs bar 60: 'med. offr., Tanganyika Territory' ~ 'Medical Officer'
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

