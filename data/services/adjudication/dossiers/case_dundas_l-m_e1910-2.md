<!-- {"case_id": "case_dundas_l-m_e1910-2", "bio_ids": ["dundas_l-m_e1910-2"], "stint_ids": ["Dundas, L. M___Kenya___1911"]} -->
# Dossier case_dundas_l-m_e1910-2

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 14 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `dundas_l-m_e1910-2`

- Printed name: **DUNDAS, L. M**
- Birth year: not printed
- Appears in editions: [1923, 1924]

### Verbatim printed entry text (OCR)

**Version `col1923-L54069.v` — printed in editions [1923, 1924]:**

> DUNDAS, L. M.—Land ranger, E. Africa Prot., June, 1910; asst. dist. comanr., Kenya, Apr., 1920.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1910 | Land ranger, E. Africa Prot | — | [1923, 1924] |
| 1 | 1920 | asst. dist. comanr. | Kenya | [1923, 1924] |

## Candidate stint `Dundas, L. M___Kenya___1911`

- Staff-list name: **Dundas, L. M** | colony: **Kenya** | listed 1911–1919 | editions [1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1911 | L. M. Dundas | Land Rangers | Lands Department | — | — |
| 1912 | L. M. Dundas | Land Rangers | Land Department | — | — |
| 1913 | L. M. Dundas | Land Rangers | Land Department | — | — |
| 1914 | L. M. Dundas | Land Rangers | Land Department | — | — |
| 1915 | L. M. Dundas | Land Rangers | Land Department | — | — |
| 1917 | L. M. Dundas | Land Rangers | Land Department | — | — |
| 1918 | L. M. Dundas | Land Rangers | Land Department | — | — |
| 1919 | L. M. Dundas | Land Rangers | Land Department | — | — |

### Deterministic checks: `dundas_l-m_e1910-2` vs `Dundas, L. M___Kenya___1911`

- [PASS] surname_gate: bio 'DUNDAS' vs stint 'Dundas, L. M' (exact)
- [PASS] initials: bio ['L', 'M'] ~ stint ['L', 'M']
- [PASS] age_gate: stint starts 1911; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1911-1919
- [FAIL] position_sim: best 43 vs bar 60: 'asst. dist. comanr.' ~ 'Land Rangers'
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

