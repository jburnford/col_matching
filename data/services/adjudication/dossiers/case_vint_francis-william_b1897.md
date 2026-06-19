<!-- {"case_id": "case_vint_francis-william_b1897", "bio_ids": ["vint_francis-william_b1897"], "stint_ids": ["Vint, F.W___Kenya___1939"]} -->
# Dossier case_vint_francis-william_b1897

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `vint_francis-william_b1897`

- Printed name: **VINT, Francis William**
- Birth year: 1897 (attested in editions [1948])
- Honours: M.D
- Appears in editions: [1948]

### Verbatim printed entry text (OCR)

**Version `col1948-L36591.v` — printed in editions [1948]:**

> VINT, Francis William, M.D., B.Sc. (Belfast) (1st cl. hons.).—b. 1897; ed. Acad., Ballymena, Queen's Univ., Belfast; on mil. serv., 1915–19, lieut.; med. offr., Ken., 1927; senr. pathologist, 1936; publications:—The Brain of the Kenya Native, Malignant Melanoma in the Africas, The Measurement of red blood corpuscles. Malignant Disease in the Natives of Kenya, Post-Mortem Findings in the Natives of Kenya, Some recent researches on the Spleen and their possible relationship to Blackwater Fever, Cirrhosis of the Liver in the E.A. Native.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1927 | med. offr. | Kenya | [1948] |
| 1 | 1936 | senr. pathologist | Kenya *(inherited from previous clause)* | [1948] |

## Candidate stint `Vint, F.W___Kenya___1939`

- Staff-list name: **Vint, F.W** | colony: **Kenya** | listed 1939–1940 | editions [1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | F.W. Vint | Senior Pathologist | Medical Department | — | — |
| 1940 | F. W. Vint | Senior Pathologist | Medical Department | — | — |

### Deterministic checks: `vint_francis-william_b1897` vs `Vint, F.W___Kenya___1939`

- [PASS] surname_gate: bio 'VINT' vs stint 'Vint, F.W' (exact)
- [PASS] initials: bio ['F', 'W'] ~ stint ['F', 'W']
- [PASS] age_gate: stint starts 1939, birth 1897 (age 42)
- [PASS] colony: 2 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1939-1940
- [PASS] position_sim: best 94 vs bar 60: 'senr. pathologist' ~ 'Senior Pathologist'
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

