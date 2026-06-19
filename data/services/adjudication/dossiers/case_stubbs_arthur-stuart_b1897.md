<!-- {"case_id": "case_stubbs_arthur-stuart_b1897", "bio_ids": ["stubbs_arthur-stuart_b1897"], "stint_ids": ["Stubbs, A___New Zealand___1912"]} -->
# Dossier case_stubbs_arthur-stuart_b1897

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 16 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `stubbs_arthur-stuart_b1897`

- Printed name: **STUBBS, Arthur Stuart**
- Birth year: 1897 (attested in editions [1949, 1950])
- Appears in editions: [1949, 1950]

### Verbatim printed entry text (OCR)

**Version `col1949-L35986.v` — printed in editions [1949, 1950]:**

> STUBBS, Arthur Stuart.—b. 1897; ed. Severn Rd. Sch., Cardiff and St. Owens Sch., Hereford; on mil. serv., 1915-19 and 1939-42; apptd. Br. post serv., 1913; Ken., 1921-23; survr., posts and tels., Nig., 1943.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1913 | apptd. Br. post serv | — | [1949, 1950] |
| 1 | 1921–1923 | apptd. Br. post serv | Kenya | [1949, 1950] |
| 2 | 1943 | survr., posts and tels. | Nigeria | [1949, 1950] |

## Candidate stint `Stubbs, A___New Zealand___1912`

- Staff-list name: **Stubbs, A** | colony: **New Zealand** | listed 1912–1922 | editions [1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1922]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | A. Stubbs | Registrar of Court of Appeal | Judicial | — | — |
| 1913 | A. Stubbs | Registrar of the Supreme Court, Wellington, and Registrar of Court of Appeal | Judicial | — | — |
| 1914 | A. Stubbs | Registrar of the Supreme Court | Judicial | — | — |
| 1915 | A. Stubbs | Registrar of the Supreme Court | Judicial | — | — |
| 1917 | A. Stubbs | Registrar of the Supreme Court | Judicial | — | — |
| 1918 | A. Stubbs | Registrar of the Supreme Court | Judicial | — | — |
| 1919 | A. Stubbs | Registrar of the Supreme Court | Supreme Court | — | — |
| 1920 | A. Stubbs | Registrar of the Supreme Court | Judicial | — | — |
| 1922 | A. Stubbs | Registrar of the Supreme Court | Judicial | — | — |

### Deterministic checks: `stubbs_arthur-stuart_b1897` vs `Stubbs, A___New Zealand___1912`

- [PASS] surname_gate: bio 'STUBBS' vs stint 'Stubbs, A' (exact)
- [PASS] initials: bio ['A', 'S'] ~ stint ['A']
- [PASS] age_gate: stint starts 1912, birth 1897 (age 15)
- [FAIL] colony: no placed event resolves to 'New Zealand'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1922
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

