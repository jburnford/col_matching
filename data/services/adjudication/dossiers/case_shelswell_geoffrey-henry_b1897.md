<!-- {"case_id": "case_shelswell_geoffrey-henry_b1897", "bio_ids": ["shelswell_geoffrey-henry_b1897"], "stint_ids": ["Shelswell, G. H___Zanzibar___1923"]} -->
# Dossier case_shelswell_geoffrey-henry_b1897

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `shelswell_geoffrey-henry_b1897`

- Printed name: **SHELSWELL, GEOFFREY HENRY**
- Birth year: 1897 (attested in editions [1927])
- Appears in editions: [1925, 1927]

### Verbatim printed entry text (OCR)

**Version `col1927-L62715.v` — printed in editions [1927]:**

> SHELSWELL, GEOFFREY HENRY.—B. 1897; ed. Whitgift Schol.; served with R.F.A. in India, Mesopotamia and Persia; ast. pol. offr., Mesopotamia, 1918-20; personal ast. to Sir Arnold Wilson, ag. civ. comanr., 1918; Iraq rebellion, 1920; A.D.C., Zanzibar, 1921; priv. sec. to res. and 2nd ast. sec., secretariat, in 1921 to 1924; clk. of coun., 1924; ag. 1st ast. sec., 10th Sept. to 29th Dec., 1924.

**Version `col1925-L59301.v` — printed in editions [1925]:**

> SHELLOWELL, GEOFFREY HENRY.—B. 1897; 1. Whitgift Schl.; served with R.F.A. in India, Mesopotamia and Persia; asst. pol. offr., Mesopotamia, 1918-20; personal asst. to Sir Arnold Wilson, ag. civ. consmr., 1918; A.D.C., Zanzibar, 1921; ag. priv. sec. to res., and 2nd asst. sec. secretariat, in 1921 to 24; clk. of coun., 1924; 1st asst. sec., 10th Sept., 1924.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1918–1920 | ast. pol. offr. | Mesopotamia | [1925, 1927] |
| 1 | 1920 | Iraq rebellion | Iraq | [1927] |
| 2 | 1921 | A.D.C. | Zanzibar | [1925, 1927] |
| 3 | 1924 | clk. of coun | Zanzibar *(inherited from previous clause)* | [1925, 1927] |

## Candidate stint `Shelswell, G. H___Zanzibar___1923`

- Staff-list name: **Shelswell, G. H** | colony: **Zanzibar** | listed 1923–1927 | editions [1923, 1924, 1925, 1927]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1923 | G. H. Shelswell | Assistant District Commissioner | District Administration | — | Captain |
| 1924 | G. H. Shelswell | 2nd Grade Administrative Officer | District Administration | — | Captain |
| 1925 | G. H. Shelswell | 2nd Grade Administrative Officer | District Administration | — | Captain |
| 1927 | G. H. Shelswell | 2nd Grade Administrative Officer | District Administration | — | Captain |

### Deterministic checks: `shelswell_geoffrey-henry_b1897` vs `Shelswell, G. H___Zanzibar___1923`

- [PASS] surname_gate: bio 'SHELSWELL' vs stint 'Shelswell, G. H' (exact)
- [PASS] initials: bio ['G', 'H'] ~ stint ['G', 'H']
- [PASS] age_gate: stint starts 1923, birth 1897 (age 26)
- [PASS] colony: 2 placed event(s) resolve to 'Zanzibar'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1923-1927
- [FAIL] position_sim: best 24 vs bar 60: 'clk. of coun' ~ 'Assistant District Commissioner'
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

