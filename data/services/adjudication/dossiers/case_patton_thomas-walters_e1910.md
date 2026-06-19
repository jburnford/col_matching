<!-- {"case_id": "case_patton_thomas-walters_e1910", "bio_ids": ["patton_thomas-walters_e1910"], "stint_ids": ["Patton, T. W___Federated Malay States___1918"]} -->
# Dossier case_patton_thomas-walters_e1910

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `patton_thomas-walters_e1910`

- Printed name: **PATTON, THOMAS WALTERS**
- Birth year: not printed
- Appears in editions: [1920, 1921]

### Verbatim printed entry text (OCR)

**Version `col1920-L56275.v` — printed in editions [1920, 1921]:**

> PATTON, THOMAS WALTERS.—B.A. (Dublin); cadet, F.M.S., Nov., 1910; ag. 2nd A.D.O., Tapah, June, 1911; ag. A.D.O., Larut, Oct., 1912; ditto, Gopeng, Jan., 1913; ditto, Larut, Feb., 1913; ditto, Lands, Kinta, July, 1913; passed final exam. in Malay, Dec., 1913; ag. mag., Seremban, Dec., 1913; ag. A.D.O., Raub, Oct., 1914; 2nd lieut., 5th R. Irish Fus., Aug., 1915; attached censor's office, Singapore, May, 1917; ag. D.O., N. Tebal, July, 1917; ag. D.O.B.M., May, 1919.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1910 | cadet | Federated Malay States | [1920, 1921] |
| 1 | 1911 | ag. 2nd A.D.O., Tapah | Dominions Office | [1920, 1921] |
| 2 | 1912 | ag. A.D.O., Larut | Dominions Office | [1920, 1921] |
| 3 | 1913 | ditto, Gopeng | Dominions Office *(inherited from previous clause)* | [1920, 1921] |
| 4 | 1914 | ag. A.D.O., Raub | Dominions Office | [1920, 1921] |
| 5 | 1915 | 2nd lieut., 5th R. Irish Fus | Dominions Office *(inherited from previous clause)* | [1920, 1921] |
| 6 | 1917 | attached censor's office | Singapore | [1920, 1921] |
| 7 | 1917 | ag. D.O., N. Tebal | Dominions Office | [1920, 1921] |
| 8 | 1919 | ag. D.O.B.M | Dominions Office *(inherited from previous clause)* | [1920, 1921] |

## Candidate stint `Patton, T. W___Federated Malay States___1918`

- Staff-list name: **Patton, T. W** | colony: **Federated Malay States** | listed 1918–1919 | editions [1918, 1919]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1918 | T. W. Patton | Officer, Cadet Service | Cadet Service | — | — |
| 1919 | T. W. Patton | Cadet (Class V) | Cadet Service | — | — |

### Deterministic checks: `patton_thomas-walters_e1910` vs `Patton, T. W___Federated Malay States___1918`

- [PASS] surname_gate: bio 'PATTON' vs stint 'Patton, T. W' (exact)
- [PASS] initials: bio ['T', 'W'] ~ stint ['T', 'W']
- [PASS] age_gate: stint starts 1918; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Federated Malay States'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1918-1919
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

