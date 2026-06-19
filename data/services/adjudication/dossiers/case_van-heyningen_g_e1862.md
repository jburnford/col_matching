<!-- {"case_id": "case_van-heyningen_g_e1862", "bio_ids": ["van-heyningen_g_e1862"], "stint_ids": ["Van Heyningen, G___St Vincent___1879"]} -->
# Dossier case_van-heyningen_g_e1862

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['van-heyningen_g_e1862'] carry a single initial only — the namesake trap applies.

## Biography `van-heyningen_g_e1862`

- Printed name: **VAN HEYNINGEN, G**
- Birth year: not printed
- Appears in editions: [1890, 1894]

### Verbatim printed entry text (OCR)

**Version `col1890-L37171.v` — printed in editions [1890, 1894]:**

> VAN HEYNINGEN, G.—Postmaster, St. Vincent, May, 1862; chief of police, May, 1872; pol. and stip. mag., Calliaqua dist., Sept., 1879; ditto, Kingston dist., Jan., 1887.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1862 | Postmaster | St. Vincent | [1890, 1894] |
| 1 | 1872 | chief of police | St. Vincent *(inherited from previous clause)* | [1890, 1894] |
| 2 | 1879 | pol. and stip. mag., Calliaqua dist | St. Vincent *(inherited from previous clause)* | [1890, 1894] |
| 3 | 1887 | ditto, Kingston dist | St. Vincent *(inherited from previous clause)* | [1890, 1894] |

## Candidate stint `Van Heyningen, G___St Vincent___1879`

- Staff-list name: **Van Heyningen, G** | colony: **St Vincent** | listed 1879–1888 | editions [1879, 1888]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1879 | G. Van Heyningen | Chief of Police | Civil Establishment | — | — |
| 1888 | G. Van Heyningen | Police Magistrates, Kingstown District | Judicial Establishment | — | — |

### Deterministic checks: `van-heyningen_g_e1862` vs `Van Heyningen, G___St Vincent___1879`

- [PASS] surname_gate: bio 'VAN HEYNINGEN' vs stint 'Van Heyningen, G' (exact)
- [PASS] initials: bio ['G'] ~ stint ['G']
- [PASS] age_gate: stint starts 1879; no printed birth year — UNCHECKED
- [PASS] colony: 4 placed event(s) resolve to 'St Vincent'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1879-1888
- [PASS] position_sim: best 100 vs bar 60: 'chief of police' ~ 'Chief of Police'
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

