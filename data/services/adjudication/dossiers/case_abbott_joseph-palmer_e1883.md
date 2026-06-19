<!-- {"case_id": "case_abbott_joseph-palmer_e1883", "bio_ids": ["abbott_joseph-palmer_e1883"], "stint_ids": ["Abbott, J___South Australia___1879"]} -->
# Dossier case_abbott_joseph-palmer_e1883

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 38 official(s) with this surname in the graph's staff lists; 16 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Abbott, J___South Australia___1879` is also gate-compatible with biography(ies) outside this case: ['abbott_wm-jackson_e1901'] (already linked elsewhere or filtered).

## Biography `abbott_joseph-palmer_e1883`

- Printed name: **ABBOTT, JOSEPH PALMER**
- Birth year: not printed
- Honours: KT., BART. (1892)
- Terminal: resigned 1885 — “resigned December, 1885”
- Appears in editions: [1886, 1888, 1889, 1890, 1894, 1896, 1898, 1899, 1900]

### Verbatim printed entry text (OCR)

**Version `col1894-L29938.v` — printed in editions [1894, 1896, 1898, 1899, 1900]:**

> ABBOTT, SIR JOSEPH PALMER, KT., BART. (1892).—Secretary for mines, New South Wales, 5 Jan., 1883, to Oct., 1885, when appointed Secretary for Lands; resigned Dec., 1885; speaker of the Legislative Assembly, 1892.

**Version `col1886-L31818.v` — printed in editions [1886, 1888, 1889, 1890]:**

> ABBOTT, Hon. J. P.—Secretary for mines, New South Wales, 5 Jan., 1883 to Oct., 1885, when appointed Secretary for Lands, resigned December, 1885.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1883–1885 | Secretary for mines | New South Wales | [1886, 1888, 1889, 1890, 1894, 1896, 1898, 1899, 1900] |
| 1 | 1885–1885 | Secretary for Lands | — | [1886, 1888, 1889, 1890, 1894, 1896, 1898, 1899, 1900] |
| 2 | 1892–1892 | speaker of the Legislative Assembly | — | [1894, 1896, 1898, 1899, 1900] |

## Candidate stint `Abbott, J___South Australia___1879`

- Staff-list name: **Abbott, J** | colony: **South Australia** | listed 1879–1880 | editions [1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1879 | J. Abbott | Draughtsmen | Survey Department | — | — |
| 1880 | J. Abbott | Draughtsmen | Photo-Lithographer | — | — |

### Deterministic checks: `abbott_joseph-palmer_e1883` vs `Abbott, J___South Australia___1879`

- [PASS] surname_gate: bio 'ABBOTT' vs stint 'Abbott, J' (exact)
- [PASS] initials: bio ['J', 'P'] ~ stint ['J']
- [PASS] age_gate: stint starts 1879; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'South Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1879-1880
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

