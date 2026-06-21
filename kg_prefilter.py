#!/usr/bin/env python3
"""Deterministic pre-filter for the flagged-drop review (flag-don't-drop).

Auto-confirms the *mechanical* flagged drops that the LLM reviewers would only
rubber-stamp anyway, so the LLM phase reads far fewer bios. Two high-precision,
dictionary-free rules, each emitting an EXACT source substring as evidence (the
same 0-FP gate kg_review_flags._confirmed enforces at merge time):

  * year   : chained ranges the validator's single-pair expander misses
             ("1896-7-8" -> {1896,1897,1898}); confirm a flagged year if it is
             produced by expanding a chained range present verbatim in source.
  * place  : a dotted acronym (>=2 letter-dot pairs: E.A.P., S. S., G.W.) from
             the flagged value that appears dot-bounded in source. Gated by a
             denylist of OCR-misread tokens the LLM tends to *correct*
             (colonial/minister/...) so we never auto-keep a correction case.

Everything not confirmed is written back out as residue batches for the LLM.
Only processes batches whose verdicts_NNN.jsonl does not yet exist (resumable;
already-reviewed batches are left untouched).

Usage:
  python3 kg_prefilter.py            # process all not-yet-reviewed batches
"""
from __future__ import annotations
import json, glob, re
from pathlib import Path

REVIEW = Path("data/kg/review")
BATCHES = REVIEW / "batches"
VERDICTS = REVIEW / "verdicts"
RESIDUE = REVIEW / "residue"


def _nws(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "")).strip().lower()


# ---- year rule: expand chained ranges ("1896-7-8", "1904-5-6-7") ----
_CHAIN = re.compile(r"\b1[789]\d\d(?:\s*[-–—]\s*\d{1,2})+\b")


def confirm_year(year: int, src: str):
    for m in _CHAIN.finditer(src):
        sub = m.group(0)
        parts = re.split(r"\s*[-–—]\s*", sub)
        base = parts[0]
        years = {int(base)}
        for p in parts[1:]:
            years.add(int(base[: 4 - len(p)] + p) if len(p) < 4 else int(p))
        if year in years:
            return _nws(sub)
    return None


# ---- place rule: dotted acronym, dot-bounded in source ----
_ACR = re.compile(r"(?:[A-Za-z]\.\s*){2,}")
# OCR-misread tokens the LLM reviewers corrected rather than kept; never
# auto-confirm a value containing one (route it to the LLM instead).
_DENY = {"colonial", "minister", "ministry", "marine"}


def confirm_place(val: str, src: str):
    low = val.lower()
    if any(d in low for d in _DENY):
        return None
    nsrc = _nws(src)
    for m in _ACR.finditer(val):
        letters = [c for c in m.group(0).lower() if c.isalpha()]
        if len(letters) < 2:
            continue
        pat = r"(?<![a-z])" + r"\.\s*".join(letters) + r"\."
        mm = re.search(pat, nsrc)
        if mm:
            return _nws(mm.group(0))
    return None


def confirm(packet: dict, src: str):
    """Return (source_evidence, rule) if deterministically confirmable, else None."""
    reason = packet.get("reason", "")
    fv = packet.get("flagged_value")
    if "place" in reason:
        if isinstance(fv, str):
            ev = confirm_place(fv, src)
            if ev:
                return ev, "acronym"
    elif "year" in reason:
        yr = fv if isinstance(fv, int) else (fv.get("year_start") if isinstance(fv, dict) else None)
        if yr:
            ev = confirm_year(yr, src)
            if ev:
                return ev, "chained-range"
    return None


def main() -> None:
    RESIDUE.mkdir(parents=True, exist_ok=True)
    VERDICTS.mkdir(parents=True, exist_ok=True)

    prefilter_path = VERDICTS / "verdicts_prefilter.jsonl"
    n_conf = n_res_pk = 0
    persons_total = persons_cleared = persons_residue = 0
    residue_batches = []

    with prefilter_path.open("w", encoding="utf-8") as vf:
        for bf in sorted(BATCHES.glob("batch_*.jsonl")):
            nnn = bf.stem.split("_")[1]
            if (VERDICTS / f"verdicts_{nnn}.jsonl").exists():
                continue  # already reviewed by an LLM agent — leave it
            residue_lines = []
            for line in bf.open(encoding="utf-8"):
                line = line.strip()
                if not line:
                    continue
                o = json.loads(line)
                persons_total += 1
                src = o.get("source_text", "")
                pid = o["person_id"]
                residue_pk = []
                for pk in o.get("packets", []):
                    hit = confirm(pk, src)
                    if hit:
                        ev, rule = hit
                        vf.write(json.dumps({
                            "person_id": pid,
                            "field_path": pk["field_path"],
                            "flagged_value": pk["flagged_value"],
                            "reason": pk["reason"],
                            "verdict": "keep",
                            "corrected_value": None,
                            "source_evidence": ev,
                            "confidence": 0.98,
                            "rationale": f"deterministic: {rule}",
                        }, ensure_ascii=False) + "\n")
                        n_conf += 1
                    else:
                        residue_pk.append(pk)
                if residue_pk:
                    persons_residue += 1
                    n_res_pk += len(residue_pk)
                    residue_lines.append(json.dumps(
                        {**o, "packets": residue_pk}, ensure_ascii=False))
                else:
                    persons_cleared += 1
            if residue_lines:
                rp = RESIDUE / f"batch_{nnn}.jsonl"
                rp.write_text("\n".join(residue_lines) + "\n", encoding="utf-8")
                residue_batches.append((nnn, len(residue_lines)))

    print(f"prefilter: confirmed {n_conf} packets -> {prefilter_path}")
    print(f"persons: {persons_total} total | {persons_cleared} cleared "
          f"({100*persons_cleared//max(persons_total,1)}%) | {persons_residue} -> LLM")
    print(f"residue: {n_res_pk} packets across {len(residue_batches)} batches")
    for nnn, n in residue_batches:
        print(f"  residue/batch_{nnn}.jsonl  {n} persons")


if __name__ == "__main__":
    main()
