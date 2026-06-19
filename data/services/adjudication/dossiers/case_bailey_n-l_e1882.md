<!-- {"case_id": "case_bailey_n-l_e1882", "bio_ids": ["bailey_n-l_e1882"], "stint_ids": ["Bailey, L___Fiji___1928"]} -->
# Dossier case_bailey_n-l_e1882

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 69 official(s) with this surname in the graph's staff lists; 29 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Bailey, L___Fiji___1928` is also gate-compatible with biography(ies) outside this case: ['bailey_alfred-lisle_b1885'] (already linked elsewhere or filtered).

## Biography `bailey_n-l_e1882`

- Printed name: **BAILEY, N. L**
- Birth year: not printed
- Appears in editions: [1883, 1886]

### Verbatim printed entry text (OCR)

**Version `col1883-L26287.v` — printed in editions [1883, 1886]:**

> BAILEY, N. L.—Chief Justice, Gold Coast, Oct., 1882.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1882 | Chief Justice | Gold Coast | [1883, 1886] |

## Candidate stint `Bailey, L___Fiji___1928`

- Staff-list name: **Bailey, L** | colony: **Fiji** | listed 1928–1930 | editions [1928, 1929, 1930]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1928 | L. Bailey | Assistant Mistress | Education Department | — | — |
| 1929 | Mrs. L. Bailey | Assistant Mistress, Girls' Grammar School | Education Department | — | — |
| 1930 | Mrs. L. Bailey | Assistant Mistresses, Girls' Grammar School | Education Department | — | — |

### Deterministic checks: `bailey_n-l_e1882` vs `Bailey, L___Fiji___1928`

- [PASS] surname_gate: bio 'BAILEY' vs stint 'Bailey, L' (exact)
- [PASS] initials: bio ['N', 'L'] ~ stint ['L']
- [PASS] age_gate: stint starts 1928; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Fiji'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1928-1930
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

