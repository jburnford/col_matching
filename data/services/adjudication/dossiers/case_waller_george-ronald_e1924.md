<!-- {"case_id": "case_waller_george-ronald_e1924", "bio_ids": ["waller_george-ronald_e1924"], "stint_ids": ["Waller, G. R___Nigeria___1933"]} -->
# Dossier case_waller_george-ronald_e1924

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 11 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `waller_george-ronald_e1924`

- Printed name: **WALLER, GEORGE RONALD**
- Birth year: not printed
- Honours: M.B
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L71537.v` — printed in editions [1939, 1940]:**

> WALLER, GEORGE RONALD, M.B., Ch.B. (Ed.) D.P.H. (Eng.), Cert. of L.S.T. Med.—Med. offr., Nigeria, 1924; senr. health offr., 1928; A.D.M.S. (health), Sierra Leone, 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1924 | Med. offr. | Nigeria | [1939, 1940] |
| 1 | 1928 | senr. health offr | Nigeria *(inherited from previous clause)* | [1939, 1940] |
| 2 | 1938 | A.D.M.S. (health) | Sierra Leone | [1939, 1940] |

## Candidate stint `Waller, G. R___Nigeria___1933`

- Staff-list name: **Waller, G. R** | colony: **Nigeria** | listed 1933–1939 | editions [1933, 1934, 1936, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | G. R. Waller | Senior Health Officer | Medical Health Service | — | — |
| 1934 | G. R. Waller | Senior Health Officer | Medical Health Service | — | — |
| 1936 | G. R. Waller | Senior Health Officers | Medical Health Service | — | — |
| 1939 | G. R. Waller | Senior Health Officers | Medical Health Service | — | — |

### Deterministic checks: `waller_george-ronald_e1924` vs `Waller, G. R___Nigeria___1933`

- [PASS] surname_gate: bio 'WALLER' vs stint 'Waller, G. R' (exact)
- [PASS] initials: bio ['G', 'R'] ~ stint ['G', 'R']
- [PASS] age_gate: stint starts 1933; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1933-1939
- [PASS] position_sim: best 86 vs bar 60: 'senr. health offr' ~ 'Senior Health Officer'
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

