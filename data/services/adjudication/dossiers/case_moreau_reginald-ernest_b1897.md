<!-- {"case_id": "case_moreau_reginald-ernest_b1897", "bio_ids": ["moreau_reginald-ernest_b1897"], "stint_ids": ["Moreau, R. E___Tanganyika___1933"]} -->
# Dossier case_moreau_reginald-ernest_b1897

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `moreau_reginald-ernest_b1897`

- Printed name: **MOREAU, REGINALD ERNEST**
- Birth year: 1897 (attested in editions [1936, 1939, 1940])
- Honours: C.M.Z.S., M.B.O.U.
- Appears in editions: [1936, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1936-L63174.v` — printed in editions [1936, 1939, 1940]:**

> MOREAU, REGINALD ERNEST, C.M.Z.S., M.B.O.U.—B. 1897; 2nd div. clk., W.O., 1914; exec. offr. gr. II, army audit office, H.Q., B.T.E., Cairo, 1920; sec. & librarian, E. African agril. research station, Amami, Tanganyika Territory, 1928, also in ch. ornithological research.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914 | 2nd div. clk., W.O. | — | [1936, 1939, 1940] |
| 1 | 1920 | exec. offr. gr. II, army audit office, H.Q., B.T.E., Cairo | — | [1936, 1939, 1940] |
| 2 | 1928 | sec. & librarian, E. African agril. research station, Amami, also in ch. ornithological research | Tanganyika Territory | [1936, 1939, 1940] |

## Candidate stint `Moreau, R. E___Tanganyika___1933`

- Staff-list name: **Moreau, R. E** | colony: **Tanganyika** | listed 1933–1934 | editions [1933, 1934]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | R. E. Moreau | Secretary and Librarian | East African Agricultural Research Station | — | — |
| 1934 | R. E. Moreau | Secretary and Librarian | Customs | — | — |

### Deterministic checks: `moreau_reginald-ernest_b1897` vs `Moreau, R. E___Tanganyika___1933`

- [PASS] surname_gate: bio 'MOREAU' vs stint 'Moreau, R. E' (exact)
- [PASS] initials: bio ['R', 'E'] ~ stint ['R', 'E']
- [PASS] age_gate: stint starts 1933, birth 1897 (age 36)
- [FAIL] colony: no placed event resolves to 'Tanganyika'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1933-1934
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

