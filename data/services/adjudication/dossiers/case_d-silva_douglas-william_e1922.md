<!-- {"case_id": "case_d-silva_douglas-william_e1922", "bio_ids": ["d-silva_douglas-william_e1922"], "stint_ids": ["D\u2019Zilva, D___Fiji___1914"]} -->
# Dossier case_d-silva_douglas-william_e1922

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `d-silva_douglas-william_e1922`

- Printed name: **D’SILVA, Douglas William**
- Birth year: not printed
- Honours: M.B.E
- Appears in editions: [1951]

### Verbatim printed entry text (OCR)

**Version `col1951-L37708.v` — printed in editions [1951]:**

> D’SILVA, Douglas William, M.B.E., M.C. Dip. for.—ed. European High Sch., Final, and Imp. Forest Res. Inst. & Coll., Dehra Dun, India; on mil. serv., 1942-46, maj.; extra asst. consvr., forests, Burma, 1922; dep. consvr., 1946; asst. consvr., B. Hond., 1948.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1922 | extra asst. consvr., forests, Burma | — | [1951] |
| 1 | 1946 | dep. consvr | — | [1951] |
| 2 | 1948 | asst. consvr. | British Honduras | [1951] |

## Candidate stint `D’Zilva, D___Fiji___1914`

- Staff-list name: **D’Zilva, D** | colony: **Fiji** | listed 1914–1915 | editions [1914, 1915]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1914 | D. D’Zilva | Surveyors | Lands Department | — | — |
| 1915 | D. D’Zilva | Surveyors | Lands Department | — | — |

### Deterministic checks: `d-silva_douglas-william_e1922` vs `D’Zilva, D___Fiji___1914`

- [PASS] surname_gate: bio 'D’SILVA' vs stint 'D’Zilva, D' (fuzzy:1)
- [PASS] initials: bio ['D', 'W'] ~ stint ['D']
- [PASS] age_gate: stint starts 1914; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Fiji'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1914-1915
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

