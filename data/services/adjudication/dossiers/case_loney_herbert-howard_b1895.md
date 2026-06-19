<!-- {"case_id": "case_loney_herbert-howard_b1895", "bio_ids": ["loney_herbert-howard_b1895"], "stint_ids": ["Loney, H. H___Kenya___1939"]} -->
# Dossier case_loney_herbert-howard_b1895

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `loney_herbert-howard_b1895`

- Printed name: **LONEY, Herbert Howard**
- Birth year: 1895 (attested in editions [1948])
- Honours: A.M.I.C.E
- Appears in editions: [1948]

### Verbatim printed entry text (OCR)

**Version `col1948-L34125.v` — printed in editions [1948]:**

> LONEY, Herbert Howard, A.M.I.C.E.—b. 1895; ed. Merchant Venturers Technical Coll., mem. inst. Br. engrns.; on mil. serv., 1915-19, lieut.; Bt., P.O. Eng., 1911; posts and tels., Nig., 1919; asst. engrn. posts and tels., Ken., Uga., and T.T., 1937.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1911 | Bt., P.O. Eng | — | [1948] |
| 1 | 1919 | posts and tels. | Nigeria | [1948] |
| 2 | 1937 | asst. engrn. posts and tels., Ken., Uga., and T.T | Nigeria *(inherited from previous clause)* | [1948] |

## Candidate stint `Loney, H. H___Kenya___1939`

- Staff-list name: **Loney, H. H** | colony: **Kenya** | listed 1939–1940 | editions [1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | H. H. Loney | Assistant Engineer | Posts and Telegraphs Department | — | — |
| 1940 | H. H. Loney | Assistant Engineer | Posts and Telegraphs Department | — | — |

### Deterministic checks: `loney_herbert-howard_b1895` vs `Loney, H. H___Kenya___1939`

- [PASS] surname_gate: bio 'LONEY' vs stint 'Loney, H. H' (exact)
- [PASS] initials: bio ['H', 'H'] ~ stint ['H', 'H']
- [PASS] age_gate: stint starts 1939, birth 1895 (age 44)
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1939-1940
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

