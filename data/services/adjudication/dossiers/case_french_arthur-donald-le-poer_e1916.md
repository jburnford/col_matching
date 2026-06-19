<!-- {"case_id": "case_french_arthur-donald-le-poer_e1916", "bio_ids": ["french_arthur-donald-le-poer_e1916"], "stint_ids": ["French, A. Parker___Southern Nigeria___1911"]} -->
# Dossier case_french_arthur-donald-le-poer_e1916

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 29 official(s) with this surname in the graph's staff lists; 14 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `french_arthur-donald-le-poer_e1916`

- Printed name: **FRENCH, ARTHUR DONALD LE POER**
- Birth year: not printed
- Appears in editions: [1925]

### Verbatim printed entry text (OCR)

**Version `col1925-L59950.v` — printed in editions [1925]:**

> FRENCH, ARTHUR DONALD LE POER, O.A.C. (c).—Senr. coffee offr., agrl. dept., Kenya, 1916.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1916 | Senr. coffee offr., agrl. dept. | Kenya | [1925] |

## Candidate stint `French, A. Parker___Southern Nigeria___1911`

- Staff-list name: **French, A. Parker** | colony: **Southern Nigeria** | listed 1911–1912 | editions [1911, 1912]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1911 | A. Parker French | Assistant Chief Clerk | Infantry | — | — |
| 1912 | A. Parker French | Assistant Chief Clerk | Customs | — | — |

### Deterministic checks: `french_arthur-donald-le-poer_e1916` vs `French, A. Parker___Southern Nigeria___1911`

- [PASS] surname_gate: bio 'FRENCH' vs stint 'French, A. Parker' (exact)
- [PASS] initials: bio ['A', 'D', 'L', 'P'] ~ stint ['A', 'P']
- [PASS] age_gate: stint starts 1911; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Southern Nigeria'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1911-1912
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

