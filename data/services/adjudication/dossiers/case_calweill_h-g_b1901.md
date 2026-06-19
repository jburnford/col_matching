<!-- {"case_id": "case_calweill_h-g_b1901", "bio_ids": ["calweill_h-g_b1901"], "stint_ids": ["Calwell, H. G___Tanganyika___1940"]} -->
# Dossier case_calweill_h-g_b1901

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Calwell, H. G___Tanganyika___1940` is also gate-compatible with biography(ies) outside this case: ['calwell_h-g_b1901'] (already linked elsewhere or filtered).

## Biography `calweill_h-g_b1901`

- Printed name: **CALWEILL, H. G**
- Birth year: 1901 (attested in editions [1939])
- Honours: B.A, M.B
- Appears in editions: [1939]

### Verbatim printed entry text (OCR)

**Version `col1939-L65315.v` — printed in editions [1939]:**

> CALWEILL, H. G., B.A., M.B., R.Ch., B.A.O. Hons.) (Bel.), D.T.M. & H. (Lond.) (Gold Med., Diseases of Children, Belfast).—B. 1901; med. offr., Tanganyika Territory, Apr., 1931.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1931 | med. offr., Tanganyika Territory | Tanganyika | [1939] |

## Candidate stint `Calwell, H. G___Tanganyika___1940`

- Staff-list name: **Calwell, H. G** | colony: **Tanganyika** | listed 1940–1949 | editions [1940, 1949]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1940 | H. G. Calwell | Medical Officer | Medical Department | — | — |
| 1949 | H. G. Calwell | Sleeping Sickness Officer | Medical and Sanitation | — | — |

### Deterministic checks: `calweill_h-g_b1901` vs `Calwell, H. G___Tanganyika___1940`

- [PASS] surname_gate: bio 'CALWEILL' vs stint 'Calwell, H. G' (fuzzy:1)
- [PASS] initials: bio ['H', 'G'] ~ stint ['H', 'G']
- [PASS] age_gate: stint starts 1940, birth 1901 (age 39)
- [PASS] colony: 1 placed event(s) resolve to 'Tanganyika'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1940-1949
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

