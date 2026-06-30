# archive/ — one-off analysis & diagnostic scripts

These are exploratory scripts from the **matching / measurement** phase of the
project — used to size a problem, diagnose unmatched records, or A/B a model,
then kept for provenance. They are **not part of the core knowledge-graph
pipeline** and nothing imports them.

They still run unchanged from the repo root, e.g.:

```bash
python3 archive/diagnose_unmatched.py
```

(Their data paths are relative to the working directory, so run them from the
repository root just like before — only their location moved, not their
behaviour.)

Grouping:
- `measure_*.py` — quantify a lever or error class (ambiguity, OCR quality,
  dedup signal, truncation, …) before building around it.
- `diagnose_*.py`, `probe_*.py`, `triage_*.py`, `decompose_gaps.py`,
  `classify_unmatched.py` — inspect why specific records didn't match.
- `gen_*_verdicts.py` — generate adjudication verdicts for calibration/pilot
  slices.
- `deepseek_dedup_ab.py` — model A/B for the dedup experiments.
- `size_co_london.py`, `check_brooke_wiring.py` — small one-off checks.
