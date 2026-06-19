<!-- {"case_id": "case_paulin_h-b_e1836", "bio_ids": ["paulin_h-b_e1836"], "stint_ids": ["Paulin, H. B___Canada___1877"]} -->
# Dossier case_paulin_h-b_e1836

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `paulin_h-b_e1836`

- Printed name: **PAULIN, H. B.**
- Birth year: not printed
- Terminal: retired 1882 — “retired, 1882”
- Appears in editions: [1883, 1886, 1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1883-L29040.v` — printed in editions [1883, 1886, 1888, 1889, 1890]:**

> PAULIN, H. B.—Appointed assistant privy secretary to the late Major-General Sir John Harvey, in 1836; entered the imperial customs service, Nova Scotia, in 1845, and resigned in order to accept colonial employment as controller of customs and registrar of shipping, Halifax, N.S.; retired, 1882.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1836 | assistant privy secretary | — | [1883, 1886, 1888, 1889, 1890] |
| 1 | 1845 | imperial customs service | Nova Scotia | [1883, 1886, 1888, 1889, 1890] |
| 2 | ? | controller of customs and registrar of shipping | Nova Scotia | [1883, 1886, 1888, 1889, 1890] |

## Candidate stint `Paulin, H. B___Canada___1877`

- Staff-list name: **Paulin, H. B** | colony: **Canada** | listed 1877–1883 | editions [1877, 1878, 1879, 1880, 1883]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | H. B. Paulin | Controller of Shipping | Customs Department | — | — |
| 1878 | H. B. Paulin | Controller of Shipping | Customs Department | — | — |
| 1879 | H. B. Paulin | Controller of Shipping | Customs Department | — | — |
| 1880 | H. B. Paulin | Controller of Shipping | Customs Department | — | — |
| 1883 | H. B. Paulin | Controller of Shipping | Customs Department | — | — |

### Deterministic checks: `paulin_h-b_e1836` vs `Paulin, H. B___Canada___1877`

- [PASS] surname_gate: bio 'PAULIN' vs stint 'Paulin, H. B' (exact)
- [PASS] initials: bio ['H', 'B'] ~ stint ['H', 'B']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Canada'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1883
- [FAIL] position_sim: best 35 vs bar 60: 'imperial customs service' ~ 'Controller of Shipping'
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

