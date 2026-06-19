<!-- {"case_id": "case_flinn_william-henry_b1896", "bio_ids": ["flinn_william-henry_b1896"], "stint_ids": ["Flinn, W. H___Cyprus___1922"]} -->
# Dossier case_flinn_william-henry_b1896

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Flinn, W. H___Cyprus___1922` is also gate-compatible with biography(ies) outside this case: ['flinn_william-henry_b1895'] (already linked elsewhere or filtered).

## Biography `flinn_william-henry_b1896`

- Printed name: **FLINN, William Henry**
- Birth year: 1896 (attested in editions [1923])
- Honours: O.B.E (1918)
- Appears in editions: [1923]

### Verbatim printed entry text (OCR)

**Version `col1923-L54396.v` — printed in editions [1923]:**

> FLINN, Major William Henry, O.B.E. (1918).—B. 1896; ed. St. Andrew's Coll. and Trinity Coll., Dublin; Royal Irish Regt. and staff, 1914-19; admtn. offr., Nigeria, Sept., 1919; asst. sec., ch. sec.'s office, Cyprus, Mar., 1921; A.D.C. and priv. sec. to H. Commr., 14th Apr., 1921; ag. clk., exec. coun., Feb.-Mar., 1922; passed exam. in mod. Greek, Apr., 1922; ag. ch. asst. sec., July, 1922; ag. commr., Sept., 1922; ag. local commr., police, Sept., 1922.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914–1919 | Royal Irish Regt. and staff | — | [1923] |
| 1 | 1919 | admtn. offr. | Nigeria | [1923] |
| 2 | 1921 | asst. sec., ch. sec.'s office | Cyprus | [1923] |
| 3 | 1922 | ag. clk., exec. coun., Feb.- | Cyprus *(inherited from previous clause)* | [1923] |

## Candidate stint `Flinn, W. H___Cyprus___1922`

- Staff-list name: **Flinn, W. H** | colony: **Cyprus** | listed 1922–1925 | editions [1922, 1923, 1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | W. H. Flinn | Assistant Secretary | Office of the Chief Secretary to Government | — | Major |
| 1922 | W. H. Flinn | Private Secretary | Civil Establishment | — | Major |
| 1923 | W. H. Flinn | Assistant Secretary | Office of the Chief Secretary to Government | — | Major |
| 1923 | W. H. Flinn | Private Secretary | Civil Establishment | — | Major |
| 1924 | W. H. Flinn | Assistant Secretary | Office of the Chief Secretary to Government | — | Major |
| 1924 | W. H. Flinn | Private Secretary | Civil Establishment | — | Major |
| 1925 | W. H. Flinn | Assistant Secretary | Office of the Chief Secretary to Government | — | Major |
| 1925 | W. H. Flinn | Private Secretary | Civil Establishment | — | Major |

### Deterministic checks: `flinn_william-henry_b1896` vs `Flinn, W. H___Cyprus___1922`

- [PASS] surname_gate: bio 'FLINN' vs stint 'Flinn, W. H' (exact)
- [PASS] initials: bio ['W', 'H'] ~ stint ['W', 'H']
- [PASS] age_gate: stint starts 1922, birth 1896 (age 26)
- [PASS] colony: 2 placed event(s) resolve to 'Cyprus'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1922-1925
- [FAIL] position_sim: best 43 vs bar 60: 'asst. sec., ch. sec.'s office' ~ 'Assistant Secretary'
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

