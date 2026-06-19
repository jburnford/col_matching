<!-- {"case_id": "case_boldero_a-h_e1896", "bio_ids": ["boldero_a-h_e1896"], "stint_ids": ["Boldero, A. H___Straits Settlements___1896"]} -->
# Dossier case_boldero_a-h_e1896

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Boldero, A. H___Straits Settlements___1896` is also gate-compatible with biography(ies) outside this case: ['boldero_a-h_e1896-2'] (already linked elsewhere or filtered).

## Biography `boldero_a-h_e1896`

- Printed name: **BOLDERO, A. H.**
- Birth year: not printed
- Appears in editions: [1898, 1899, 1900]

### Verbatim printed entry text (OCR)

**Version `col1898-L32262.v` — printed in editions [1898, 1899, 1900]:**

> BOLDERO, CAPT. A. H.—Ret. R.N.; dep. master attendant, marine dept., Singapore, May, 1896, ag. master attendant, S. Sttlmts., Dec. to July, 1897.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1896 | dep. master attendant, marine dept. | Singapore | [1898, 1899, 1900] |
| 1 | ?–1897 | ag. master attendant | Straits Settlements | [1898, 1899, 1900] |

## Candidate stint `Boldero, A. H___Straits Settlements___1896`

- Staff-list name: **Boldero, A. H** | colony: **Straits Settlements** | listed 1896–1905 | editions [1896, 1897, 1898, 1899, 1905]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1896 | A. H. Boldero | Deputy Master Attendant | Marine Department | — | — |
| 1897 | A. H. Boldero | Deputy Master Attendant | Marine Department | — | — |
| 1898 | A. H. Boldero | Deputy Master Attendant | Marine Department | — | — |
| 1899 | A. H. Boldero | Deputy Master Attendant | Marine Department | — | — |
| 1905 | Captain A. H. Boldero, R.N. | Master Attendant | Marine Department | — | Captain |

### Deterministic checks: `boldero_a-h_e1896` vs `Boldero, A. H___Straits Settlements___1896`

- [PASS] surname_gate: bio 'BOLDERO' vs stint 'Boldero, A. H' (exact)
- [PASS] initials: bio ['A', 'H'] ~ stint ['A', 'H']
- [PASS] age_gate: stint starts 1896; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1896-1905
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

