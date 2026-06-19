<!-- {"case_id": "case_fulkner_s-n_e1909", "bio_ids": ["fulkner_s-n_e1909"], "stint_ids": ["Faulkner, S. N___Kenya___1910"]} -->
# Dossier case_fulkner_s-n_e1909

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- Phase 1 found `fulkner_s-n_e1909` ↔ `Faulkner, S. N___Kenya___1910` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Faulkner, S. N___Kenya___1910` is also gate-compatible with biography(ies) outside this case: ['faulkner_s-n_e1909'] (already linked elsewhere or filtered).

## Biography `fulkner_s-n_e1909`

- Printed name: **FULKNER, S.N**
- Birth year: not printed
- Honours: O.B.E (1918)
- Appears in editions: [1922]

### Verbatim printed entry text (OCR)

**Version `col1922-L52236.v` — printed in editions [1922]:**

> FULKNER, S.N., O.B.E. (1918)—Ast. auditor, E.A.P., 8th Jan., 1909; senr. ast. auditor, Apr., 1915; dep. ch. acctnt., Uganda Rly., 1917.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1909 | Ast. auditor | East Africa Protectorate | [1922] |
| 1 | 1915 | senr. ast. auditor | East Africa Protectorate *(inherited from previous clause)* | [1922] |
| 2 | 1917 | dep. ch. acctnt., Uganda Rly | Uganda | [1922] |

## Candidate stint `Faulkner, S. N___Kenya___1910`

- Staff-list name: **Faulkner, S. N** | colony: **Kenya** | listed 1910–1927 | editions [1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1922, 1923, 1924, 1925, 1927]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1910 | S. N. Faulkner | Assistant Auditors | Audit | — | — |
| 1911 | S. N. Faulkner | Assistant Auditors | Audit | — | — |
| 1912 | S. N. Faulkner | Assistant Auditors | Audit | — | — |
| 1913 | S. N. Faulkner | Assistant Auditors | Audit | — | — |
| 1914 | S. N. Faulkner | Assistant Auditors | Audit | — | — |
| 1915 | S. N. Faulkner | Assistant Auditors | Audit | — | — |
| 1917 | S. N. Faulkner | Assistant Auditors | Audit | — | — |
| 1918 | S. N. Faulkner | Deputy Chief Accountant | Accounts | — | — |
| 1919 | S. N. Faulkner | Deputy Chief Accountant | Accounts | — | — |
| 1922 | S. N. Faulkner | Deputy Chief Accountant | Accounts | — | — |
| 1923 | S. N. Faulkner | Deputy Chief Accountant | Accounts | O.B.E. | — |
| 1924 | S. N. Faulkner | Deputy Chief Accountant | Accounts | — | — |
| 1925 | S. N. Faulkner | Deputy Chief Accountant | Accounts | — | — |
| 1927 | S. N. Faulkner | Deputy Chief Accountant | Accounts | O.B.E. | — |

### Deterministic checks: `fulkner_s-n_e1909` vs `Faulkner, S. N___Kenya___1910`

- [PASS] surname_gate: bio 'FULKNER' vs stint 'Faulkner, S. N' (fuzzy:1)
- [PASS] initials: bio ['S', 'N'] ~ stint ['S', 'N']
- [PASS] age_gate: stint starts 1910; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1910-1927
- [PASS] position_sim: best 76 vs bar 60: 'Ast. auditor' ~ 'Assistant Auditors'
- [PASS] honour: shared: O.B.E
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

