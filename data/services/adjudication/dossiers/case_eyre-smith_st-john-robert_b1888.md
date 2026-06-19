<!-- {"case_id": "case_eyre-smith_st-john-robert_b1888", "bio_ids": ["eyre-smith_st-john-robert_b1888"], "stint_ids": ["Eyre-Smith, St. J. R___Gold Coast___1929"]} -->
# Dossier case_eyre-smith_st-john-robert_b1888

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `eyre-smith_st-john-robert_b1888`

- Printed name: **EYRE-SMITH, ST. JOHN ROBERT**
- Birth year: 1888 (attested in editions [1936])
- Honours: M.C.
- Appears in editions: [1933, 1935, 1936, 1937, 1940]

### Verbatim printed entry text (OCR)

**Version `col1936-L60563.v` — printed in editions [1936]:**

> EYRE-SMITH, CAIT. ST. JOHN ROBERT, M.C.—B. 1888; ed. St. Edmunds Coll., Ware; served with R.A.S.C., France and Germany, 1915-19; Turkey, 1919-20, ment. in desps.; asst. dist. comsnr., Gold Coast, 1921; dist. comsnr., 1925; asst. sec., native affrs., 1931.

**Version `col1933-L59556.v` — printed in editions [1933, 1935, 1937, 1940]:**

> EYRE-SMITH, CAPT. ST. JOHN ROBERT, M.C.—B. 1888; ed. St. Edmunds Coll., Ware; wrangler with R.A.S.C., France and Germany, 1915-16; Turkey, 1919-20; mem. in despe.; asst. dist. comsnr., Gold Coast, 1921; dist. comsnr., 1922; asst. sec., native affrs., 1931.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1915–1919 | served with R.A.S.C. | France and Germany | [1936] |
| 1 | 1915–1916 | wrangler with R.A.S.C., France and Germany | — | [1933, 1935, 1937, 1940] |
| 2 | 1919–1920 | — | Turkey | [1936] |
| 3 | 1919–1920 | Turkey | — | [1933, 1935, 1937, 1940] |
| 4 | 1921 | asst. dist. comsnr. | Gold Coast | [1933, 1935, 1936, 1937, 1940] |
| 5 | 1922 | dist. comsnr | Gold Coast *(inherited from previous clause)* | [1933, 1935, 1937, 1940] |
| 6 | 1925 | dist. comsnr. | — | [1936] |
| 7 | 1931 | asst. sec., native affrs. | Gold Coast *(inherited from previous clause)* | [1933, 1935, 1936, 1937, 1940] |

## Candidate stint `Eyre-Smith, St. J. R___Gold Coast___1929`

- Staff-list name: **Eyre-Smith, St. J. R** | colony: **Gold Coast** | listed 1929–1932 | editions [1929, 1932]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1929 | St. J. R. Eyre-Smith | District Commissioner / Assistant District Commissioner | Administrative and Political Service | — | Captain |
| 1932 | Capt. St. J. R. Eyre-Smith | Assistant Secretary for Native Affairs | Secretary for Native Affairs Office | — | Captain |

### Deterministic checks: `eyre-smith_st-john-robert_b1888` vs `Eyre-Smith, St. J. R___Gold Coast___1929`

- [PASS] surname_gate: bio 'EYRE-SMITH' vs stint 'Eyre-Smith, St. J. R' (exact)
- [PASS] initials: bio ['S', 'J', 'R'] ~ stint ['S', 'J', 'R']
- [PASS] age_gate: stint starts 1929, birth 1888 (age 41)
- [PASS] colony: 3 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1929-1932
- [PASS] position_sim: best 71 vs bar 60: 'asst. sec., native affrs.' ~ 'Assistant Secretary for Native Affairs'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

