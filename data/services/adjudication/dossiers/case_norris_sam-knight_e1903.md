<!-- {"case_id": "case_norris_sam-knight_e1903", "bio_ids": ["norris_sam-knight_e1903"], "stint_ids": ["Norris, S. K___British Central Africa___1905"]} -->
# Dossier case_norris_sam-knight_e1903

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 23 official(s) with this surname in the graph's staff lists; 17 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `norris_sam-knight_e1903`

- Printed name: **NORRIS, SAM KNIGHT**
- Birth year: not printed
- Honours: M.B
- Appears in editions: [1910, 1911]

### Verbatim printed entry text (OCR)

**Version `col1910-L47812.v` — printed in editions [1910, 1911]:**

> NORRIS, SAM KNIGHT., M.B., C.M. (Edin.), 1897.—Med. offr., Nyasaland Prot., Oct., 1903.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1903 | Med. offr. | Nyasaland | [1910, 1911] |

## Candidate stint `Norris, S. K___British Central Africa___1905`

- Staff-list name: **Norris, S. K** | colony: **British Central Africa** | listed 1905–1907 | editions [1905, 1906, 1907]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | S. K. Norris | Medical Officer | Medical Department | — | — |
| 1906 | S. K. Norris | Medical Officer | Medical Department | — | — |
| 1907 | S. K. Norris | Medical Officer | Medical Department | — | — |

### Deterministic checks: `norris_sam-knight_e1903` vs `Norris, S. K___British Central Africa___1905`

- [PASS] surname_gate: bio 'NORRIS' vs stint 'Norris, S. K' (exact)
- [PASS] initials: bio ['S', 'K'] ~ stint ['S', 'K']
- [PASS] age_gate: stint starts 1905; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'British Central Africa'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1907
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

