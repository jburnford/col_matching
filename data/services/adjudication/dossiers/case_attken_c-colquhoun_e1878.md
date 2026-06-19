<!-- {"case_id": "case_attken_c-colquhoun_e1878", "bio_ids": ["attken_c-colquhoun_e1878"], "stint_ids": ["Aitken, C. C___Jamaica___1883"]} -->
# Dossier case_attken_c-colquhoun_e1878

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 24 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Aitken, C. C___Jamaica___1883` is also gate-compatible with biography(ies) outside this case: ['aitken_c-colquhoun_e1878'] (already linked elsewhere or filtered).

## Biography `attken_c-colquhoun_e1878`

- Printed name: **ATTKEN, C. Colquhoun**
- Birth year: not printed
- Appears in editions: [1898]

### Verbatim printed entry text (OCR)

**Version `col1898-L31881.v` — printed in editions [1898]:**

> ATTKEN, C. Colquhoun.—3rd class ck., col. sec. office, Jamaica, Feb., 1878; 2nd class ck., gen. register office, 1878; 1st class ck., 1880.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1878 | 3rd class ck., col. sec. office | Jamaica | [1898] |
| 1 | 1880 | 1st class ck | Jamaica *(inherited from previous clause)* | [1898] |

## Candidate stint `Aitken, C. C___Jamaica___1883`

- Staff-list name: **Aitken, C. C** | colony: **Jamaica** | listed 1883–1913 | editions [1883, 1886, 1888, 1889, 1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907, 1909, 1910, 1911, 1912, 1913]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1883 | C. C. Aitken | First Clerk | Registrar General's Department | — | — |
| 1886 | C. C. Aitken | First Clerk | Registrar General's Department | — | — |
| 1888 | C. C. Aitken | First Clerk | Registrar General's Department | — | — |
| 1889 | C. C. Aitken | First Clerk | Registrar General's Department | — | — |
| 1894 | C. C. Aitken | First Clerk | Registrar-General's Department | — | — |
| 1896 | C. C. Aitken | First Clerk | Registrar-General's Department | — | — |
| 1897 | C. C. Aitken | First Clerk | Registrar-General's Department | — | — |
| 1898 | C. C. Aitken | First Clerk | Registrar-General's Department | — | — |
| 1899 | C. C. Aitken | First Clerk | Registrar-General's Department | — | — |
| 1900 | C. C. Aitken | First Clerk | Registrar-General's Department | — | — |
| 1905 | C. C. Aitken | First Clerk | Registrar-General's Department | — | — |
| 1906 | C. C. Aitken | First Clerk | Registrar-General's Department | — | — |
| 1907 | C. C. Aitken | First Clerk | Registrar-General's Department | — | — |
| 1909 | C. C. Aitken | First Clerk | Registrar-General's Department | — | — |
| 1910 | C. C. Aitken | First Clerk | Registrar-General's Department | — | — |
| 1911 | C. C. Aitken | Assistant Deputy Keeper of Records | Island Record Office | — | — |
| 1911 | C. C. Aitken | First Clerk | Registrar-General's Department | — | — |
| 1912 | C. C. Aitken | First Clerk | Registrar-General's Department | — | — |
| 1912 | C. C. Aitken | Assistant Deputy Keeper of Records | Island Record Office | — | — |
| 1913 | C. C. Aitken | Assistant Deputy Keeper of Records | Island Record Office | — | — |
| 1913 | C. C. Aitken | Assistant Registrar-General | Registrar-General's Department | — | — |

### Deterministic checks: `attken_c-colquhoun_e1878` vs `Aitken, C. C___Jamaica___1883`

- [PASS] surname_gate: bio 'ATTKEN' vs stint 'Aitken, C. C' (fuzzy:1)
- [PASS] initials: bio ['C', 'C'] ~ stint ['C', 'C']
- [PASS] age_gate: stint starts 1883; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Jamaica'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1883-1913
- [FAIL] position_sim: best 35 vs bar 60: '1st class ck' ~ 'First Clerk'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

