<!-- {"case_id": "case_eagle_piercy_e1903", "bio_ids": ["eagle_piercy_e1903"], "stint_ids": ["Eagle, P___South Africa___1912"]} -->
# Dossier case_eagle_piercy_e1903

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['eagle_piercy_e1903'] carry a single initial only — the namesake trap applies.

## Biography `eagle_piercy_e1903`

- Printed name: **EAGLE, PIERCY**
- Birth year: not printed
- Appears in editions: [1920]

### Verbatim printed entry text (OCR)

**Version `col1920-L53216.v` — printed in editions [1920]:**

> EAGLE, PIERCY.—Draughtsman, P.W.D., Transvaal, Nov., 1903; asst. architect, July, 1904; architect, Mar., 1907; architect, P.W.D., Union of S. Africa, Apl., 1912; seconded as dir. of wks. in S.W. Africa Prot., Feb. to Dec., 1915.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1903 | Draughtsman, P.W.D. | Transvaal | [1920] |
| 1 | 1904 | asst. architect | Transvaal *(inherited from previous clause)* | [1920] |
| 2 | 1907 | architect | Transvaal *(inherited from previous clause)* | [1920] |
| 3 | 1912 | architect, P.W.D., Union of S. Africa | Transvaal *(inherited from previous clause)* | [1920] |
| 4 | 1915 | seconded as dir. of wks. in S.W. Africa Prot | Transvaal *(inherited from previous clause)* | [1920] |

## Candidate stint `Eagle, P___South Africa___1912`

- Staff-list name: **Eagle, P** | colony: **South Africa** | listed 1912–1918 | editions [1912, 1914, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | P. Eagle | Architect | Province of Transvaal | — | — |
| 1914 | P. Eagle | Architect | Public Works Department | — | — |
| 1918 | P. Eagle | Architect | Public Works Department | — | — |

### Deterministic checks: `eagle_piercy_e1903` vs `Eagle, P___South Africa___1912`

- [PASS] surname_gate: bio 'EAGLE' vs stint 'Eagle, P' (exact)
- [PASS] initials: bio ['P'] ~ stint ['P']
- [PASS] age_gate: stint starts 1912; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'South Africa'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1918
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

