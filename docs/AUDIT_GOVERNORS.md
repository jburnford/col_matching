# Governors-table year audit

A systematic cross-check for the error class Guggisberg exposed: a person's
career-event **years** come from one free-text anchor bio (OCR'd), so a
copy-forward typo (his "Br. Guiana, 1923" for 1928) rides straight through.
But every colony entry also prints a **"Governors since …" table** — name +
exact appointment date — which is structured, independent of the bio, and
repeated across ~66 editions. Where bio and table disagree, the table wins.

## Run

```bash
python3 audit_governors.py      # pass 1: parse governor tables -> data/kg/governors_table_rows.jsonl
python3 reconcile_governors.py  # pass 2: flag bio/table conflicts -> data/kg/governor_year_flags.jsonl
```

Flagged conflicts are **candidates for review**, not auto-applied. Confirmed
ones go into `data/kg/career_event_corrections.json` (applied in
`build_static_atlas.py::_facts()`), then rebuild.

## How it decides (precision controls)

- match a bio **governorship** to a table governor by `(colony_qid, surname)`,
  filtered by given-name initial to defeat same-surname collisions;
- the bio role must be a *substantive* governorship (grounded `role_label`
  anchored to governor/lieut-gov/administrator; never "secretary **to** the
  governor", which only mentions one — this was the main false-positive source);
- acting/administrator **table** rows are excluded (they add spurious years);
- flag only when the table has a real consensus year (≥2 editions, ≥60%
  plurality) and the gap is ≥2 years (±1 is appointed-vs-assumed-office noise).

## Current result

Across the **12 colonies** whose governor history is published as a parseable
HTML table (Barbados, British Guiana, Mauritius, Tasmania, Seychelles, Jamaica,
Victoria, St Vincent, Bahamas, Nova Scotia, Antigua, Basutoland), the audit
finds exactly **one** clean conflict — Guggisberg, British Guiana, bio 1923 vs
table 1928 (9/9 editions) — already corrected. Zero false positives at the
"high" tier.

## Expanding recall

The big African/Asian colonies (Nigeria, Gold Coast, Ceylon, Hong Kong, Kenya)
print only the *current* governor as a "Governor." title + text block, not a
history table, so they aren't covered yet. To extend: (a) parse those
current-governor text blocks across editions into (colony, name, year) — each
edition is a fresh attestation, so the first edition naming a governor gives
the appointment year; (b) optionally detect governor tables by content (rows of
name+date) rather than by the title regex. Either turns this from "12 colonies"
into near-empire coverage.
