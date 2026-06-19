<!-- {"case_id": "case_hay_walter-gurnby_e1884", "bio_ids": ["hay_walter-gurnby_e1884"], "stint_ids": ["Hay, William___Cape of Good Hope___1896"]} -->
# Dossier case_hay_walter-gurnby_e1884

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 34 official(s) with this surname in the graph's staff lists; 21 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hay_walter-gurnby_e1884`

- Printed name: **HAY, WALTER GURNBY**
- Birth year: not printed
- Appears in editions: [1890]

### Verbatim printed entry text (OCR)

**Version `col1890-L34676.v` — printed in editions [1890]:**

> HAY, WALTER GURNBY.—Ed. at Haileybury Coll. Served in Bechuanaland expdn., 1884-5; priv. secy. to Sir James Hay, governor, S. Leone, Oct., 1888; was capt. second in command, Largo expedition, 1888, and mentioned in despatches.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1884–1885 | — | Bechuanaland | [1890] |
| 1 | 1888 | priv. secy. to Sir James Hay, governor | Sierra Leone | [1890] |
| 2 | 1888–1888 | capt. second in command, Largo expedition | — | [1890] |

## Candidate stint `Hay, William___Cape of Good Hope___1896`

- Staff-list name: **Hay, William** | colony: **Cape of Good Hope** | listed 1896–1897 | editions [1896, 1897]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1896 | William Hay | — | House of Assembly | — | — |
| 1897 | William Hay | — | Members | — | — |

### Deterministic checks: `hay_walter-gurnby_e1884` vs `Hay, William___Cape of Good Hope___1896`

- [PASS] surname_gate: bio 'HAY' vs stint 'Hay, William' (exact)
- [PASS] initials: bio ['W', 'G'] ~ stint ['W']
- [PASS] age_gate: stint starts 1896; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Cape of Good Hope'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1896-1897
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

