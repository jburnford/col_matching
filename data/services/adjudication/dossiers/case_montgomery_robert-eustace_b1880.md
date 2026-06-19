<!-- {"case_id": "case_montgomery_robert-eustace_b1880", "bio_ids": ["montgomery_robert-eustace_b1880"], "stint_ids": ["Montgomery, R. E___Uganda___1921"]} -->
# Dossier case_montgomery_robert-eustace_b1880

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 27 official(s) with this surname in the graph's staff lists; 11 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Montgomery, R. E___Uganda___1921` is also gate-compatible with biography(ies) outside this case: ['montgomery_r-e_e1909'] (already linked elsewhere or filtered).

## Biography `montgomery_robert-eustace_b1880`

- Printed name: **MONTGOMERY, ROBERT EUSTACE**
- Birth year: 1880 (attested in editions [1932])
- Honours: M.R.C.V.S
- Appears in editions: [1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1932]

### Verbatim printed entry text (OCR)

**Version `col1932-L62613.v` — printed in editions [1932]:**

> MONTGOMERY, ROBERT EUSTACE, M.R.C.V.S., Fellow Soc. Trop. Med.; Fellow Royal Socy. Med.—B. 1880; ed. Royal "Dick" Vet. Coll., Edinburgh; asst. Imp. bacteriologist, Indian civ. vety. dept., 1904; sp. duty on camels, 1905; mem. sleeping sickness expdn., Liverpool Schl. Trop. Med., to Zambesi, 1906-08; vety. pathologist, E.A.P., 1909; E. African Vety. Corps, 1914-1917, (ment. in despa.); dir., vety. research, Union S. Africa, 1917; vety. adviser, Kenya, Uganda, Tanganyika and Zanzibar, 1920-26; adviser on animal health to S. of S., 1930; co-edr. Jnl. Trop. Vety. Science; numerous publications "Trypanosomiasis," and other trop. diseases of animals.

**Version `col1918-L52903.v` — printed in editions [1918, 1919, 1920, 1921, 1922, 1923, 1924]:**

> MONTGOMERY, R. E.—Veterinary pathologist, E.A.P., Aug., 1909; dir. of veterinary research, Union of S. Africa, Dec., 1917.

**Version `col1925-L58007.v` — printed in editions [1925]:**

> MONTGOMERY, R. E.—VETERINARY PATHOLOGIST, E.A.P., AUG., 1909; DIR. OF VETERINARY RESEARCH, UNION OF S. AFRICA, DEC., 1917.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1904 | asst. Imp. bacteriologist, Indian civ. vety. dept | — | [1932] |
| 1 | 1905 | sp. duty on camels | — | [1932] |
| 2 | 1906–1908 | mem. sleeping sickness expdn., Liverpool Schl. Trop. Med., to Zambesi | — | [1932] |
| 3 | 1909 | vety. pathologist | East Africa Protectorate | [1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1932] |
| 4 | 1914–1917 | E. African Vety. Corps | East Africa Protectorate *(inherited from previous clause)* | [1932] |
| 5 | 1917 | dir., vety. research, Union S. Africa | East Africa Protectorate *(inherited from previous clause)* | [1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1932] |
| 6 | 1920–1926 | vety. adviser, Kenya, Uganda, Tanganyika and Zanzibar | Tanganyika | [1932] |
| 7 | 1930 | adviser on animal health to S. of S | Tanganyika *(inherited from previous clause)* | [1932] |

## Candidate stint `Montgomery, R. E___Uganda___1921`

- Staff-list name: **Montgomery, R. E** | colony: **Uganda** | listed 1921–1925 | editions [1921, 1922, 1923, 1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1921 | R. E. Montgomery | Veterinary Adviser | Veterinary Department | — | — |
| 1922 | R. E. Montgomery | Veterinary Adviser | Veterinary Department | — | — |
| 1923 | R. E. Montgomery | Veterinary Adviser | Veterinary Department | — | — |
| 1924 | R. E. Montgomery | Veterinary Adviser | Veterinary Department | — | — |
| 1925 | R. E. Montgomery | Veterinary Adviser | Veterinary Department | — | — |

### Deterministic checks: `montgomery_robert-eustace_b1880` vs `Montgomery, R. E___Uganda___1921`

- [PASS] surname_gate: bio 'MONTGOMERY' vs stint 'Montgomery, R. E' (exact)
- [PASS] initials: bio ['R', 'E'] ~ stint ['R', 'E']
- [PASS] age_gate: stint starts 1921, birth 1880 (age 41)
- [FAIL] colony: no placed event resolves to 'Uganda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1921-1925
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

