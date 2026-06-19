<!-- {"case_id": "case_gyde_charlie-john_e1897", "bio_ids": ["gyde_charlie-john_e1897"], "stint_ids": ["Gyde, C. J___South Africa___1912"]} -->
# Dossier case_gyde_charlie-john_e1897

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `gyde_charlie-john_e1897`

- Printed name: **GYDE, CHARLIE JOHN**
- Birth year: not printed
- Honours: M.I.C.E
- Appears in editions: [1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927]

### Verbatim printed entry text (OCR)

**Version `col1919-L52800.v` — printed in editions [1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927]:**

> GYDE, CHARLIE JOHN, M.I.C.E.—Indian govt. service, 1897-1902; asst. engnr. P.W.D., Transvaal, June, 1902; inspr. of wks., July, 1904; dist. engnr., Mar., 1907; inspecting engnr., Sept., 1917; ch. engnr., Jan., 1925.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1897–1902 | Indian govt. service | — | [1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927] |
| 1 | 1902 | asst. engnr. P.W.D. | Transvaal | [1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927] |
| 2 | 1904 | inspr. of wks | Transvaal *(inherited from previous clause)* | [1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927] |
| 3 | 1907 | dist. engnr | Transvaal *(inherited from previous clause)* | [1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927] |
| 4 | 1917 | inspecting engnr | Transvaal *(inherited from previous clause)* | [1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927] |
| 5 | 1925 | ch. engnr | Transvaal *(inherited from previous clause)* | [1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927] |

## Candidate stint `Gyde, C. J___South Africa___1912`

- Staff-list name: **Gyde, C. J** | colony: **South Africa** | listed 1912–1918 | editions [1912, 1914, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | C. J. Gyde | District Engineer | Province of the Cape of Good Hope | — | — |
| 1914 | C. J. Gyde | District Engineer | Public Works Department | — | — |
| 1918 | C. J. Gyde | Inspecting Engineer | Public Works Department | — | — |

### Deterministic checks: `gyde_charlie-john_e1897` vs `Gyde, C. J___South Africa___1912`

- [PASS] surname_gate: bio 'GYDE' vs stint 'Gyde, C. J' (exact)
- [PASS] initials: bio ['C', 'J'] ~ stint ['C', 'J']
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

