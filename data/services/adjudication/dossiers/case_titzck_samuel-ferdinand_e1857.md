<!-- {"case_id": "case_titzck_samuel-ferdinand_e1857", "bio_ids": ["titzck_samuel-ferdinand_e1857"], "stint_ids": ["Titzck, S. F___Windward Islands___1880"]} -->
# Dossier case_titzck_samuel-ferdinand_e1857

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `titzck_samuel-ferdinand_e1857`

- Printed name: **TITZCK, SAMUEL FERDINAND**
- Birth year: not printed
- Appears in editions: [1883, 1886]

### Verbatim printed entry text (OCR)

**Version `col1883-L29765.v` — printed in editions [1883, 1886]:**

> TITZCK, SAMUEL FERDINAND.—Marshal and postmaster, Tobago, appointed July, 1880; is also escheator-general and casual receiver, visiting justice to the gaol, and a notary public; was acting provost marshal-general from Aug., 1857, to Sept., 1858; placed on the commission of the peace in 1859; clerk of legislative assembly 1860; and clerk of legislative council 1861; was stipendiary magistrate from April, 1862, to July, 1880; pro-chief justice and local commissioner of incumbered estates court, 1884.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1857–1858 | acting provost marshal-general | — | [1883, 1886] |
| 1 | 1859–1859 | commission of the peace | — | [1883, 1886] |
| 2 | 1860–1860 | clerk of legislative assembly | — | [1883, 1886] |
| 3 | 1861–1861 | clerk of legislative council | — | [1883, 1886] |
| 4 | 1862–1880 | stipendiary magistrate | — | [1883, 1886] |
| 5 | 1880 | Marshal and postmaster | Tobago | [1883, 1886] |
| 6 | 1884–1884 | pro-chief justice and local commissioner of incumbered estates court | — | [1883, 1886] |

## Candidate stint `Titzck, S. F___Windward Islands___1880`

- Staff-list name: **Titzck, S. F** | colony: **Windward Islands** | listed 1880–1883 | editions [1880, 1883]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1880 | S. F. Titzck | Stipendiary Magistrates and Coroners | Civil Establishment | — | — |
| 1883 | S. F. Titzck | Provost Marshal | Judicial Establishment | — | — |

### Deterministic checks: `titzck_samuel-ferdinand_e1857` vs `Titzck, S. F___Windward Islands___1880`

- [PASS] surname_gate: bio 'TITZCK' vs stint 'Titzck, S. F' (exact)
- [PASS] initials: bio ['S', 'F'] ~ stint ['S', 'F']
- [PASS] age_gate: stint starts 1880; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Windward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1880-1883
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

