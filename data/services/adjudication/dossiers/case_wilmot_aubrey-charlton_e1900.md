<!-- {"case_id": "case_wilmot_aubrey-charlton_e1900", "bio_ids": ["wilmot_aubrey-charlton_e1900"], "stint_ids": ["Wilmot, A. C___Uganda___1910"]} -->
# Dossier case_wilmot_aubrey-charlton_e1900

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 13 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `wilmot_aubrey-charlton_e1900`

- Printed name: **WILMOT, AUBREY CHARLTON**
- Birth year: not printed
- Appears in editions: [1933, 1934, 1935, 1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1933-L64541.v` — printed in editions [1933, 1934, 1935, 1936, 1937, 1939, 1940]:**

> WILMOT, AUBREY CHARLTON.—Cape civ. serv., 1900; transf., Transvaal, 1902; ch. clk., mast. sup. ct., 1910; ch. clk., land bank, 1912; ass't. gen. man., 1921; gen. man., 1924; man. dir., 1930; chmn., farmers' spec. relief bd., 1931; chmn., farmers' assistance bd., 1935; chmn., immigrts. selection bd., 1935; chmn., cent. bd., land and agrl. bank of S. Africa, 1937.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1900 | Cape civ. serv | Cape of Good Hope | [1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 1 | 1902 | transf. | Transvaal | [1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 2 | 1910 | ch. clk., mast. sup. ct | Transvaal *(inherited from previous clause)* | [1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 3 | 1912 | ch. clk., land bank | Transvaal *(inherited from previous clause)* | [1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 4 | 1921 | ass't. gen. man | Transvaal *(inherited from previous clause)* | [1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 5 | 1924 | gen. man | Transvaal *(inherited from previous clause)* | [1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 6 | 1930 | man. dir | Transvaal *(inherited from previous clause)* | [1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 7 | 1931 | chmn., farmers' spec. relief bd | Transvaal *(inherited from previous clause)* | [1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 8 | 1935 | chmn., farmers' assistance bd | Transvaal *(inherited from previous clause)* | [1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 9 | 1937 | chmn., cent. bd., land and agrl. bank of S. Africa | Transvaal *(inherited from previous clause)* | [1933, 1934, 1935, 1936, 1937, 1939, 1940] |

## Candidate stint `Wilmot, A. C___Uganda___1910`

- Staff-list name: **Wilmot, A. C** | colony: **Uganda** | listed 1910–1913 | editions [1910, 1912, 1913]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1910 | A. C. Wilmot | District Engineer | Public Works | — | — |
| 1912 | A. C. Wilmot | District Engineer | Public Works | — | — |
| 1913 | A. C. Wilmot | District Engineer | Public Works | — | — |

### Deterministic checks: `wilmot_aubrey-charlton_e1900` vs `Wilmot, A. C___Uganda___1910`

- [PASS] surname_gate: bio 'WILMOT' vs stint 'Wilmot, A. C' (exact)
- [PASS] initials: bio ['A', 'C'] ~ stint ['A', 'C']
- [PASS] age_gate: stint starts 1910; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Uganda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1910-1913
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

