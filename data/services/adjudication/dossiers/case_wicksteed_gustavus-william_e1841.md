<!-- {"case_id": "case_wicksteed_gustavus-william_e1841", "bio_ids": ["wicksteed_gustavus-william_e1841", "wicksteed_gustavus-william_e1841-2"], "stint_ids": ["Wicksteed, Gustavus___Canada___1879"]} -->
# Dossier case_wicksteed_gustavus-william_e1841

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Wicksteed, Gustavus___Canada___1879'] have more than one claimant biography in this case.

## Biography `wicksteed_gustavus-william_e1841`

- Printed name: **WICKSTEED, GUSTAVUS WILLIAM**
- Birth year: not printed
- Appears in editions: [1883, 1886]

### Verbatim printed entry text (OCR)

**Version `col1883-L29981.v` — printed in editions [1883, 1886]:**

> WICKSTEED, GUSTAVUS WILLIAM, Q.C.—Law clerk of the house of commons of Canada; at the re-union of the two Canadas in 1841, was appointed law clerk of the legislative assembly of the re-united provinces; also the head of the translation department; he has also acted on several commissions.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1841 | law clerk of the legislative assembly | Canada | [1883, 1886] |
| 1 | ? | Law clerk of the house of commons | Canada | [1883, 1886] |
| 2 | ? | head of the translation department | — | [1883, 1886] |

## Biography `wicksteed_gustavus-william_e1841-2`

- Printed name: **WICKSTEED, GUSTAVUS WILLIAM**
- Birth year: not printed
- Terminal: retired 1887 — “retired 1887.”
- Appears in editions: [1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1889-L36297.v` — printed in editions [1889, 1890]:**

> WICKSTEED, GUSTAVUS WILLIAM, Q.C.—Law clerk of the house of commons of Canada; assistant law clerk in the legislative assembly of Lower Canada; at the re-union of the two Canadas in 1841, was appointed law clerk of the legislative assembly of the re-united provinces; also head of the translation department; appointed to the same offices of the confederation of the two provinces as the Dominion of Canada in 1867; retired 1887.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1841 | law clerk of the legislative assembly | Canada | [1889, 1890] |
| 1 | 1867 | same offices | Canada | [1889, 1890] |
| 2 | ? | Law clerk of the house of commons | Canada | [1889, 1890] |
| 3 | ? | assistant law clerk | Lower Canada | [1889, 1890] |
| 4 | ? | head of the translation department | — | [1889, 1890] |

## Candidate stint `Wicksteed, Gustavus___Canada___1879`

- Staff-list name: **Wicksteed, Gustavus** | colony: **Canada** | listed 1879–1880 | editions [1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1879 | G. W. Wicksteed | Law Clerk | House of Commons | — | — |
| 1880 | G. W. Wicksteed | Law Clerk | House of Commons | — | — |

### Deterministic checks: `wicksteed_gustavus-william_e1841` vs `Wicksteed, Gustavus___Canada___1879`

- [PASS] surname_gate: bio 'WICKSTEED' vs stint 'Wicksteed, Gustavus' (exact)
- [PASS] initials: bio ['G', 'W'] ~ stint ['G']
- [PASS] age_gate: stint starts 1879; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1879-1880
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `wicksteed_gustavus-william_e1841-2` vs `Wicksteed, Gustavus___Canada___1879`

- [PASS] surname_gate: bio 'WICKSTEED' vs stint 'Wicksteed, Gustavus' (exact)
- [PASS] initials: bio ['G', 'W'] ~ stint ['G']
- [PASS] age_gate: stint starts 1879; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Canada'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1879-1880
- [FAIL] position_sim: best 38 vs bar 60: 'same offices' ~ 'Law Clerk'
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

