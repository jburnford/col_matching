<!-- {"case_id": "case_philips_c-h_e1915", "bio_ids": ["philips_c-h_e1915"], "stint_ids": ["Philips, C. H___Tanganyika___1922"]} -->
# Dossier case_philips_c-h_e1915

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `philips_c-h_e1915`

- Printed name: **PHILIPS, C. H**
- Birth year: not printed
- Appears in editions: [1940]

### Verbatim printed entry text (OCR)

**Version `col1940-L67576.v` — printed in editions [1940]:**

> PHILIPS, C. H., L.M.S.S.A. (Lond.)—Tempy. lieut., R.A.M.C., Jan., 1915 (General List); med. offr., Tanganyika Territory, Dec., 1920.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1915 | Tempy. lieut., R.A.M.C | — | [1940] |
| 1 | 1920 | med. offr., Tanganyika Territory | Tanganyika | [1940] |

## Candidate stint `Philips, C. H___Tanganyika___1922`

- Staff-list name: **Philips, C. H** | colony: **Tanganyika** | listed 1922–1924 | editions [1922, 1923, 1924]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | C. H. Philips | Medical Officer | Medical Division | — | — |
| 1923 | C. H. Philips | Medical Officer | Medical Division | — | — |
| 1924 | C. H. Philips | Medical Officer | Medical Division | — | — |

### Deterministic checks: `philips_c-h_e1915` vs `Philips, C. H___Tanganyika___1922`

- [PASS] surname_gate: bio 'PHILIPS' vs stint 'Philips, C. H' (exact)
- [PASS] initials: bio ['C', 'H'] ~ stint ['C', 'H']
- [PASS] age_gate: stint starts 1922; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Tanganyika'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1922-1924
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

