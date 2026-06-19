<!-- {"case_id": "calib_gemini_natal_0264", "bio_ids": ["plant_robert_e1888"], "stint_ids": ["Plant, R___Natal___1894"]} -->
# Dossier calib_gemini_natal_0264

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 14 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['plant_robert_e1888'] carry a single initial only — the namesake trap applies.

## Biography `plant_robert_e1888`

- Printed name: **PLANT, ROBERT**
- Birth year: not printed
- Appears in editions: [1907, 1908, 1909, 1910, 1911, 1912, 1913]

### Verbatim printed entry text (OCR)

**Version `col1907-L46319.v` — printed in editions [1907, 1908, 1909, 1910, 1911, 1912, 1913]:**

> PLANT, ROBERT.—Inspr. of native educa., Natal, 18th Oct., 1888; senr. inspir. of native schls., 1st July, 1904.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1888 | Inspr. of native educa. | Natal | [1907, 1908, 1909, 1910, 1911, 1912, 1913] |
| 1 | 1904 | senr. inspir. of native schls | Natal *(inherited from previous clause)* | [1907, 1908, 1909, 1910, 1911, 1912, 1913] |

## Candidate stint `Plant, R___Natal___1894`

- Staff-list name: **Plant, R** | colony: **Natal** | listed 1894–1910 | editions [1894, 1896, 1898, 1900, 1905, 1906, 1907, 1910]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1894 | R. Plant | Inspector, Native Education | Education Department | — | — |
| 1896 | R. Plant | Inspector, Native Education | Education Department | — | — |
| 1898 | R. Plant | Inspector, Native Education | Education Department | — | — |
| 1900 | R. Plant | Inspector, Native Education | Education Department | — | — |
| 1905 | R. Plant | Senior Inspector, Native Education | Education Department | — | — |
| 1906 | R. Plant | Senior Inspector, Native Education | Education Department | — | — |
| 1907 | R. Plant | Senior Inspector, Native Education | Education Department | — | — |
| 1910 | R. Plant | Senior Inspector, Native Education | Education Department | — | — |

### Deterministic checks: `plant_robert_e1888` vs `Plant, R___Natal___1894`

- [PASS] surname_gate: bio 'PLANT' vs stint 'Plant, R' (exact)
- [PASS] initials: bio ['R'] ~ stint ['R']
- [PASS] age_gate: stint starts 1894; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Natal'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1894-1910
- [PASS] position_sim: best 90 vs bar 60: 'Inspr. of native educa.' ~ 'Inspector, Native Education'
- [FAIL] honour: no shared honour
- [PASS] edition_cooccurrence: 2 agreeing edition-year(s) [1907, 1910] pos~62 (bar: >=2)
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

