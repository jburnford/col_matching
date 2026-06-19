<!-- {"case_id": "case_cracknell_e-c_e1861", "bio_ids": ["cracknell_e-c_e1861"], "stint_ids": ["Cracknell, E. C___New South Wales___1877"]} -->
# Dossier case_cracknell_e-c_e1861

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `cracknell_e-c_e1861`

- Printed name: **CRACKNELL, E. C**
- Birth year: not printed
- Appears in editions: [1886, 1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1886-L32849.v` — printed in editions [1886, 1888, 1889, 1890]:**

> CRACKNELL, E. C.—Superintendent of telegraphs, New South Wales, 15th Jan., 1861.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1861 | Superintendent of telegraphs | New South Wales | [1886, 1888, 1889, 1890] |

## Candidate stint `Cracknell, E. C___New South Wales___1877`

- Staff-list name: **Cracknell, E. C** | colony: **New South Wales** | listed 1877–1889 | editions [1877, 1878, 1879, 1880, 1886, 1888, 1889]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | E. C. Cracknell | Superintendent of Electric Telegraphs | Roads and Bridges | — | — |
| 1878 | E. C. Cracknell | Superintendent of Electric Telegraphs | Roads and Bridges | — | — |
| 1879 | E. C. Cracknell | Superintendent of Electric Telegraphs | Roads and Bridges | — | — |
| 1880 | E. C. Cracknell | Superintendent of Electric Telegraphs | Roads and Bridges | — | — |
| 1886 | E. C. Cracknell | Superintendent of Electric Telegraphs | Electric Telegraph Department | — | — |
| 1886 | E. C. Cracknell | Major Commanding | Torpedo and Signalling Corps | — | Major |
| 1888 | E. C. Cracknell | Superintendent of Electric Telegraphs | Electric Telegraph Department | — | — |
| 1889 | E. C. Cracknell | Superintendent of Electric Telegraphs | Electric Telegraph Department | — | — |
| 1889 | E. C. Cracknell | Torpedo and Signalling Corps, Major Commanding | Colonial Defence | — | Major |

### Deterministic checks: `cracknell_e-c_e1861` vs `Cracknell, E. C___New South Wales___1877`

- [PASS] surname_gate: bio 'CRACKNELL' vs stint 'Cracknell, E. C' (exact)
- [PASS] initials: bio ['E', 'C'] ~ stint ['E', 'C']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'New South Wales'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1889
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

