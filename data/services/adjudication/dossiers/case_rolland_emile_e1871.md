<!-- {"case_id": "case_rolland_emile_e1871", "bio_ids": ["rolland_emile_e1871"], "stint_ids": ["Rolland, E. S___Cape of Good Hope___1877"]} -->
# Dossier case_rolland_emile_e1871

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['rolland_emile_e1871'] carry a single initial only — the namesake trap applies.

## Biography `rolland_emile_e1871`

- Printed name: **ROLLAND, EMILE**
- Birth year: not printed
- Appears in editions: [1886, 1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1886-L35521.v` — printed in editions [1886]:**

> ROLLAND, EMILE.—Assistant resident magistrate of district of Thaba Bosigo, Basutoland, Sept., 1871, acting magistrate, Berea, July, 1882; provisionally appointed resident magistrate, Matatiele, 11th July, 1883.

**Version `col1888-L35800.v` — printed in editions [1888, 1889, 1890]:**

> ROLLAND, EMILE.—Assistant R.M., Thaba Bosigo, Basutoland, Sept., 1871, acting magistrate, Berea, July, 1882; provisional R.M., Matatiele, 11th July, 1883.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1871 | Assistant resident magistrate of district of Thaba Bosigo | Basutoland | [1886, 1888, 1889, 1890] |
| 1 | 1882 | acting magistrate | Berea | [1886, 1888, 1889, 1890] |
| 2 | 1883 | provisionally appointed resident magistrate | Matatiele | [1886] |
| 3 | 1883 | provisional R.M. | — | [1888, 1889, 1890] |

## Candidate stint `Rolland, E. S___Cape of Good Hope___1877`

- Staff-list name: **Rolland, E. S** | colony: **Cape of Good Hope** | listed 1877–1883 | editions [1877, 1879, 1883]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | E. Rolland | Assistant Magistrate, Thaba Bosigo | Basutoland | — | — |
| 1879 | E. S. Rolland | Director Model School, Educational Department | Basutoland | — | — |
| 1883 | E. S. Rolland | Deputy-Inspector of Schools | Educational Department | — | — |

### Deterministic checks: `rolland_emile_e1871` vs `Rolland, E. S___Cape of Good Hope___1877`

- [PASS] surname_gate: bio 'ROLLAND' vs stint 'Rolland, E. S' (exact)
- [PASS] initials: bio ['E'] ~ stint ['E', 'S']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Cape of Good Hope'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1883
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

