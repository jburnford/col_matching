<!-- {"case_id": "case_rowan_albertus-nicolaas_e1902", "bio_ids": ["rowan_albertus-nicolaas_e1902"], "stint_ids": ["Rowan, A. N___Cape of Good Hope___1877"]} -->
# Dossier case_rowan_albertus-nicolaas_e1902

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `rowan_albertus-nicolaas_e1902`

- Printed name: **ROWAN, ALBERTUS NICOLAAS**
- Birth year: not printed
- Appears in editions: [1927, 1928]

### Verbatim printed entry text (OCR)

**Version `col1927-L62460.v` — printed in editions [1927, 1928]:**

> ROWAN, ALBERTUS NICOLAAS.—Examr., deeds office, Transvaal, May, 1902; ch. examr., ditto, Oct., 1906; asst. regnr., deeds, Transvaal, Dec., 1918; regnr., deeds, mining rights, companies, patents, trade marks, designs and copyrights, S.W. Africa, Apr., 1922; regnr., deeds, Transvaal and Swaziland, Mar., 1925; mem., townships bd., Mar., 1925.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1902 | Examr., deeds office | Transvaal | [1927, 1928] |
| 1 | 1906 | ch. examr., ditto | Transvaal *(inherited from previous clause)* | [1927, 1928] |
| 2 | 1918 | asst. regnr., deeds | Transvaal | [1927, 1928] |
| 3 | 1922 | regnr., deeds, mining rights, companies, patents, trade marks, designs and copyrights, S.W. Africa | Transvaal *(inherited from previous clause)* | [1927, 1928] |
| 4 | 1925 | regnr., deeds, Transvaal and Swaziland | Transvaal | [1927, 1928] |

## Candidate stint `Rowan, A. N___Cape of Good Hope___1877`

- Staff-list name: **Rowan, A. N** | colony: **Cape of Good Hope** | listed 1877–1890 | editions [1877, 1878, 1879, 1880, 1883, 1888, 1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | A. N. Rowan | Deputy-Inspectors of Schools | Educational Department | — | — |
| 1878 | A. N. Rowan | Deputy-Inspectors of Schools | Educational Department | — | — |
| 1879 | A. N. Rowan | Deputy-Inspectors of Schools | Educational Department | — | — |
| 1880 | A. N. Rowan | Deputy Inspectors of Schools | Educational Department | — | — |
| 1883 | A. N. Rowan | Deputy-Inspector of Schools | Educational Department | — | — |
| 1888 | A. N. Rowan | Deputy-Inspectors of Schools | Educational Department | — | — |
| 1889 | A. N. Rowan | Deputy-Inspectors of Schools | Educational Department | — | — |
| 1890 | A. N. Rowan | Deputy-Inspector of Schools | Educational Department | — | — |

### Deterministic checks: `rowan_albertus-nicolaas_e1902` vs `Rowan, A. N___Cape of Good Hope___1877`

- [PASS] surname_gate: bio 'ROWAN' vs stint 'Rowan, A. N' (exact)
- [PASS] initials: bio ['A', 'N'] ~ stint ['A', 'N']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Cape of Good Hope'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1890
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

