<!-- {"case_id": "case_dye_w-h_b1889", "bio_ids": ["dye_w-h_b1889"], "stint_ids": ["Dye, W. H___Nyasaland___1922"]} -->
# Dossier case_dye_w-h_b1889

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `dye_w-h_b1889`

- Printed name: **DYE, W. H.**
- Birth year: 1889 (attested in editions [1933, 1934, 1935, 1937, 1939, 1940])
- Appears in editions: [1933, 1934, 1935, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1933-L59405.v` — printed in editions [1933, 1934, 1935, 1937, 1939, 1940]:**

> DYE, W. H., M.R.C.S., L.R.C.P., L.D.S. (Eng.), D.T.M. and H. (Lond.), cert., Lond. S.H. and T.M. (Distinc.).—B. 1889; R.A.M.C., 1914-25; surg. specialist, 1918-20; N. Persian forces memorial med., for research, 1924 and 1927; seconded, Nyasaland Aug., 1921-Apr., 1925; med. offr., Tanganyika Territory, 1925; senr. med. offr., Uganda, 1934.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914–1925 | R.A.M.C. | — | [1933, 1934, 1935, 1937, 1939, 1940] |
| 1 | 1918–1920 | surg. specialist | — | [1933, 1934, 1935, 1937, 1939, 1940] |
| 2 | 1921–1925 | seconded | Nyasaland | [1933, 1934, 1935, 1937, 1939, 1940] |
| 3 | 1924–1927 | N. Persian forces memorial med., for research | — | [1933, 1934, 1935, 1937, 1939, 1940] |
| 4 | 1925 | med. offr. | Tanganyika Territory | [1933, 1934, 1935, 1937, 1939, 1940] |
| 5 | 1934 | senr. med. offr. | Uganda | [1933, 1934, 1935, 1937, 1939, 1940] |

## Candidate stint `Dye, W. H___Nyasaland___1922`

- Staff-list name: **Dye, W. H** | colony: **Nyasaland** | listed 1922–1923 | editions [1922, 1923]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | W. H. Dye | Medical Officer | Medical Department | — | — |
| 1923 | W. H. Dye | Medical Officer | Medical Department | — | — |

### Deterministic checks: `dye_w-h_b1889` vs `Dye, W. H___Nyasaland___1922`

- [PASS] surname_gate: bio 'DYE' vs stint 'Dye, W. H' (exact)
- [PASS] initials: bio ['W', 'H'] ~ stint ['W', 'H']
- [PASS] age_gate: stint starts 1922, birth 1889 (age 33)
- [PASS] colony: 1 placed event(s) resolve to 'Nyasaland'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1922-1923
- [FAIL] position_sim: best 35 vs bar 60: 'seconded' ~ 'Medical Officer'
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

