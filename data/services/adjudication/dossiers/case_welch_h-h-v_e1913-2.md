<!-- {"case_id": "case_welch_h-h-v_e1913-2", "bio_ids": ["welch_h-h-v_e1913-2"], "stint_ids": ["Welch, H. H. V___Kenya___1922"]} -->
# Dossier case_welch_h-h-v_e1913-2

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Welch, H. H. V___Kenya___1922` is also gate-compatible with biography(ies) outside this case: ['welch_h-h-v_e1913'] (already linked elsewhere or filtered).

## Biography `welch_h-h-v_e1913-2`

- Printed name: **WELCH, H. H. V**
- Birth year: not printed
- Appears in editions: [1923, 1924, 1925, 1927]

### Verbatim printed entry text (OCR)

**Version `col1923-L58967.v` — printed in editions [1923, 1924, 1925, 1927]:**

> WELCH, H. H. V.—M.R.C.S., L.C.R.P., med. offr., E.A.P., Oct., 1913; res. surg., European Hosp., Nairobi, Kenya, Aug., 1920.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1913 | M.R.C.S., L.C.R.P., med. offr. | East Africa Protectorate | [1923, 1924, 1925, 1927] |
| 1 | 1920 | res. surg., European Hosp., Nairobi | Kenya | [1923, 1924, 1925, 1927] |

## Candidate stint `Welch, H. H. V___Kenya___1922`

- Staff-list name: **Welch, H. H. V** | colony: **Kenya** | listed 1922–1925 | editions [1922, 1923, 1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | H. H. V. Welch | Resident Surgical Officer | Medical | — | — |
| 1923 | H. H. V. Welch | Resident Surgical Officer | Medical | — | — |
| 1924 | H. H. V. Welch | Resident Surgical Officer | Medical | — | — |
| 1925 | H. H. V. Welch | Resident Surgical Officer | Medical Department | — | — |

### Deterministic checks: `welch_h-h-v_e1913-2` vs `Welch, H. H. V___Kenya___1922`

- [PASS] surname_gate: bio 'WELCH' vs stint 'Welch, H. H. V' (exact)
- [PASS] initials: bio ['H', 'H', 'V'] ~ stint ['H', 'H', 'V']
- [PASS] age_gate: stint starts 1922; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1922-1925
- [FAIL] position_sim: best 44 vs bar 60: 'res. surg., European Hosp., Nairobi' ~ 'Resident Surgical Officer'
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

