<!-- {"case_id": "case_lingham_arthur_e1882", "bio_ids": ["lingham_arthur_e1882"], "stint_ids": ["Lingham, A___Grenada___1894"]} -->
# Dossier case_lingham_arthur_e1882

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['lingham_arthur_e1882'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Lingham, A___Grenada___1894` is also gate-compatible with biography(ies) outside this case: ['lingham_arthur_e1888'] (already linked elsewhere or filtered).

## Biography `lingham_arthur_e1882`

- Printed name: **LINGHAM, ARTHUR**
- Birth year: not printed
- Appears in editions: [1898, 1899, 1900]

### Verbatim printed entry text (OCR)

**Version `col1898-L34475.v` — printed in editions [1898, 1899, 1900]:**

> LINGHAM, ARTHUR.—Lieut. R.N. (retd.); served in Egypt 1882 (medal and star); barbrmr., Br. Guiana, 1888; ch. of pol., Grenada, 1892.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1882 | served in Egypt | — | [1898, 1899, 1900] |
| 1 | 1888 | barbrmr. | British Guiana | [1898, 1899, 1900] |
| 2 | 1892 | ch. of pol. | Grenada | [1898, 1899, 1900] |

## Candidate stint `Lingham, A___Grenada___1894`

- Staff-list name: **Lingham, A** | colony: **Grenada** | listed 1894–1897 | editions [1894, 1897]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1894 | A. Lingham | Chief of Police and Sanitary Inspector | Medical Officers | — | — |
| 1897 | A. Lingham | Chief of Police and Sanitary Inspector | Police and Prisons | — | — |

### Deterministic checks: `lingham_arthur_e1882` vs `Lingham, A___Grenada___1894`

- [PASS] surname_gate: bio 'LINGHAM' vs stint 'Lingham, A' (exact)
- [PASS] initials: bio ['A'] ~ stint ['A']
- [PASS] age_gate: stint starts 1894; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Grenada'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1894-1897
- [FAIL] position_sim: best 38 vs bar 60: 'ch. of pol.' ~ 'Chief of Police and Sanitary Inspector'
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

