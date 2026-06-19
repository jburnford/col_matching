<!-- {"case_id": "case_assumpcao_emile-marcolino-de_e1891", "bio_ids": ["assumpcao_emile-marcolino-de_e1891"], "stint_ids": ["Assump\u00e7\u00e3o, E. M___Lagos___1898"]} -->
# Dossier case_assumpcao_emile-marcolino-de_e1891

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `assumpcao_emile-marcolino-de_e1891`

- Printed name: **ASSUMPCAO, EMILE MARCOLINO DE**
- Birth year: not printed
- Appears in editions: [1913]

### Verbatim printed entry text (OCR)

**Version `col1913-L43479.v` — printed in editions [1913]:**

> ASSUMPCAO, EMILE MARCOLINO DE.—Kntl. Lagos corp. serv. as 2nd apprentice, printing dept., Apr., 1891; head printer, Lagos Weekly Record, June, 1894, to Dec., 1895; astt. mail agent's clk., Queen's warehouse, Jan. to Apr., 1896; astt. clk. med. dept. Lagos, Apr., 1896; warden and storekr., med. dept., Jan., 1897; clk. corresp. branch and storekr. col. sec.'s office, Jan., 1900; regis. of corresp. off. gen. man. Lagos govt. rly., May, 1901; acted as 1st clk., Mar., 1902, to Mar., 1904; performed duties of chief and 1st clk. concurrently from Mar. to Aug., 1903; apptd. head clk., 1st Apr., 1904; supervisor, govt. rlyw. printing dept., 15th July, 1907.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1891 | 2nd apprentice, printing dept. | Lagos | [1913] |
| 1 | 1894–1895 | head printer | Lagos | [1913] |
| 2 | 1896–1896 | astt. mail agent's clk. | — | [1913] |
| 3 | 1896 | astt. clk. med. dept. | Lagos | [1913] |
| 4 | 1897 | warden and storekr. | — | [1913] |
| 5 | 1900 | clk. corresp. branch and storekr. | — | [1913] |
| 6 | 1901 | regis. of corresp. off. gen. man. | Lagos | [1913] |
| 7 | 1902–1904 | acted as 1st clk. | — | [1913] |
| 8 | 1903–1903 | performed duties of chief and 1st clk. concurrently | — | [1913] |
| 9 | 1904 | head clk. | — | [1913] |
| 10 | 1907 | supervisor, govt. rlyw. printing dept. | — | [1913] |

## Candidate stint `Assumpção, E. M___Lagos___1898`

- Staff-list name: **Assumpção, E. M** | colony: **Lagos** | listed 1898–1899 | editions [1898, 1899]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1898 | E. M. Assumpção | Clerk | Medical | — | — |
| 1899 | E. M. Assumpção | Clerk | Medical | — | — |

### Deterministic checks: `assumpcao_emile-marcolino-de_e1891` vs `Assumpção, E. M___Lagos___1898`

- [PASS] surname_gate: bio 'ASSUMPCAO' vs stint 'Assumpção, E. M' (fuzzy:2)
- [PASS] initials: bio ['E', 'M', 'D'] ~ stint ['E', 'M']
- [PASS] age_gate: stint starts 1898; no printed birth year — UNCHECKED
- [PASS] colony: 4 placed event(s) resolve to 'Lagos'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1898-1899
- [FAIL] position_sim: best 27 vs bar 60: 'astt. clk. med. dept.' ~ 'Clerk'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

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

