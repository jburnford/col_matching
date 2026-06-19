<!-- {"case_id": "case_doole_edgar-capt-r-of-o_b1886", "bio_ids": ["doole_edgar-capt-r-of-o_b1886"], "stint_ids": ["Doole, E___Gold Coast___1927"]} -->
# Dossier case_doole_edgar-capt-r-of-o_b1886

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Doole, E___Gold Coast___1927` is also gate-compatible with biography(ies) outside this case: ['doole_edward_b1886'] (already linked elsewhere or filtered).

## Biography `doole_edgar-capt-r-of-o_b1886`

- Printed name: **DOOLE, EDGAR (CAPT. R. OF O.)**
- Birth year: 1886 (attested in editions [1935])
- Honours: F.R.G.S, M.I.A.E
- Appears in editions: [1935, 1936, 1937]

### Verbatim printed entry text (OCR)

**Version `dol1935-L58161.v` — printed in editions [1935]:**

> DOOLE, EDGAR (CAPT. R. OF O.), M.I.A.Mech.E., M.I.A.E., F.R.G.S.—B. 1886; A.S.C. (mech. transp.), 1914; engnr. offr., Tank Corpsa, 1917; R. of O., 1921; asst. mech. engrnr., P.W.D., Gold Coast, Nov., 1921; transf'd., motor transp. dept., Aug., 1922; engnr. transp. offr., Nov., 1922.

**Version `col1936-L60313.v` — printed in editions [1936, 1937]:**

> DOOLEY, Edgar (Capt. R. of O.), A.M.I.Mech.E., M.I.A.E., F.R.G.S.—B. 1886; A.S.C. (mech. transp't.), 1914; engrnr. offr., Tank Corps, 1917; R. of O., 1921; asst. mech. engrnr., P.W.D., Gold Coast, Nov., 1921; transf'd., motor transp't. dept., Aug., 1922; engrnr. transp't. offr., Nov., 1922.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914 | A.S.C. (mech. transp.) | — | [1935, 1936, 1937] |
| 1 | 1917 | engnr. offr., Tank Corpsa | — | [1935, 1936, 1937] |
| 2 | 1921 | R. of O | — | [1935, 1936, 1937] |
| 3 | 1921 | asst. mech. engrnr., P.W.D. | Gold Coast | [1935, 1936, 1937] |
| 4 | 1922 | transf'd., motor transp. dept | Gold Coast *(inherited from previous clause)* | [1935, 1936, 1937] |

## Candidate stint `Doole, E___Gold Coast___1927`

- Staff-list name: **Doole, E** | colony: **Gold Coast** | listed 1927–1936 | editions [1927, 1928, 1929, 1930, 1932, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | E. Doole | Engineer Transport Officer | Transport Department | — | Captain |
| 1928 | E. Doole | Engineer Transport Officer | Transport Department | — | Captain |
| 1929 | E. Doole | Engineer Transport Officers | Transport Department | — | Captain |
| 1930 | E. Doole | Engineer Transport Officers | Transport Department | — | Captain |
| 1932 | E. Doole | Engineer Transport Officer | Transport Department | — | Captain |
| 1936 | E. Doole | Engineer Transport Officer | Transport Department | — | Captain |

### Deterministic checks: `doole_edgar-capt-r-of-o_b1886` vs `Doole, E___Gold Coast___1927`

- [PASS] surname_gate: bio 'DOOLE' vs stint 'Doole, E' (exact)
- [PASS] initials: bio ['E', 'R', 'O', 'O'] ~ stint ['E']
- [PASS] age_gate: stint starts 1927, birth 1886 (age 41)
- [PASS] colony: 2 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1927-1936
- [FAIL] position_sim: best 46 vs bar 60: 'transf'd., motor transp. dept' ~ 'Engineer Transport Officers'
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

