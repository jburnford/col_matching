<!-- {"case_id": "case_feasey_gilbert-george_b1891", "bio_ids": ["feasey_gilbert-george_b1891"], "stint_ids": ["Feasey, G. G___Nigeria___1918"]} -->
# Dossier case_feasey_gilbert-george_b1891

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `feasey_gilbert-george_b1891`

- Printed name: **FEASEY, GILBERT GEORGE**
- Birth year: 1891 (attested in editions [1935, 1936])
- Appears in editions: [1935, 1936, 1937]

### Verbatim printed entry text (OCR)

**Version `dol1935-L58487.v` — printed in editions [1935, 1936]:**

> FEASEY, GILBERT GEORGE.—B. 1891; ed. Westminster; served with H.A.C. and Nigeria Regt., W.A.F.F.; active commn. Cameroons; ast. dist. offr., Nigeria, Apr., 1914; dep. res., Apr., 1933; adm. offr., cls. I, 1935.

**Version `col1937-L60849.v` — printed in editions [1937]:**

> FRASEY, GILBERT GEORGE.—B. 1891; ed. Westminster; served with H.A.C. and Nigeria Regt., W.A.F.F.; active serv., Cameroons; astm. dist. offr., Nigeria, Apr., 1914; dep. res., Apr., 1933; res., July, 1934.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914 | ast. dist. offr. | Nigeria | [1935, 1936, 1937] |
| 1 | 1933 | dep. res | Nigeria *(inherited from previous clause)* | [1935, 1936, 1937] |
| 2 | 1934 | res | Nigeria *(inherited from previous clause)* | [1937] |
| 3 | 1935 | adm. offr., cls. I | Nigeria *(inherited from previous clause)* | [1935, 1936] |

## Candidate stint `Feasey, G. G___Nigeria___1918`

- Staff-list name: **Feasey, G. G** | colony: **Nigeria** | listed 1918–1919 | editions [1918, 1919]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1918 | G. G. Feasey | Sixty‑four Assistant District Officer | Northern Provinces | — | — |
| 1919 | G. G. Feasey | Sixty-four Assistant District Officers | NORTHERN PROVINCES | — | — |

### Deterministic checks: `feasey_gilbert-george_b1891` vs `Feasey, G. G___Nigeria___1918`

- [PASS] surname_gate: bio 'FEASEY' vs stint 'Feasey, G. G' (exact)
- [PASS] initials: bio ['G', 'G'] ~ stint ['G', 'G']
- [PASS] age_gate: stint starts 1918, birth 1891 (age 27)
- [PASS] colony: 4 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1918-1919
- [FAIL] position_sim: best 53 vs bar 60: 'ast. dist. offr.' ~ 'Sixty‑four Assistant District Officer'
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

