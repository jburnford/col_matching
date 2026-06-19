<!-- {"case_id": "case_hathorn_john-walton_e1861", "bio_ids": ["hathorn_john-walton_e1861"], "stint_ids": ["Hathorn, J. W___Natal___1879"]} -->
# Dossier case_hathorn_john-walton_e1861

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hathorn_john-walton_e1861`

- Printed name: **HATHORN, JOHN WALTON**
- Birth year: not printed
- Appears in editions: [1886]

### Verbatim printed entry text (OCR)

**Version `col1886-L33948.v` — printed in editions [1886]:**

> HATHORN, JOHN WALTON.—2nd clerk in the colonial engineers' office, Natal, March, 1861; 3rd clerk in the audit office, May, 1864; 1st clerk in the general post office, Sep., 1865; 1st clerk in the treasury, June, 1874; 1st clerk and clerk of the court to the resident magistrate, Pietermaritzburg; and sub-distributor of stamps, Pietermaritzburg, March, 1876; acted as controller of arms and ammunition for eight months, from August, 1877; has acted frequently as resident magistrate and administrator of native law, both of the city of Pietermaritzburg and of Umgeni Division of Pietermaritzburg County, and as post-master-general, and clerk of the peace; resident magistrate, Ixopo division, 1881; justice of peace for the colony, June, 1881.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1861 | 2nd clerk in the colonial engineers' office | Natal | [1886] |
| 1 | 1864 | 3rd clerk in the audit office | Natal *(inherited from previous clause)* | [1886] |
| 2 | 1865 | 1st clerk in the general post office | Natal *(inherited from previous clause)* | [1886] |
| 3 | 1874 | 1st clerk in the treasury | Natal *(inherited from previous clause)* | [1886] |
| 4 | 1876 | and sub-distributor of stamps, Pietermaritzburg | Natal *(inherited from previous clause)* | [1886] |
| 5 | 1877 | acted as controller of arms and ammunition for eight months, from | Natal *(inherited from previous clause)* | [1886] |
| 6 | 1881 | resident magistrate, Ixopo division | Natal *(inherited from previous clause)* | [1886] |

## Candidate stint `Hathorn, J. W___Natal___1879`

- Staff-list name: **Hathorn, J. W** | colony: **Natal** | listed 1879–1886 | editions [1879, 1880, 1886]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1879 | J. W. Hathorn | 1st Clerk | Magisterial Department and Staff | — | — |
| 1880 | J. W. Hathorn | 1st Clerk | Magisterial Department and Staff | — | — |
| 1886 | J. W. Hathorn | — | Resident Magistrates | — | — |

### Deterministic checks: `hathorn_john-walton_e1861` vs `Hathorn, J. W___Natal___1879`

- [PASS] surname_gate: bio 'HATHORN' vs stint 'Hathorn, J. W' (exact)
- [PASS] initials: bio ['J', 'W'] ~ stint ['J', 'W']
- [PASS] age_gate: stint starts 1879; no printed birth year — UNCHECKED
- [PASS] colony: 7 placed event(s) resolve to 'Natal'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1879-1886
- [FAIL] position_sim: best 19 vs bar 60: 'resident magistrate, Ixopo division' ~ '1st Clerk'
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

