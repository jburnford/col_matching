#!/usr/bin/env python3
"""Fold the consolidated Nibi adjudication batch (job 17521812) into the
ledgers (docs/ADJUDICATION_BATCH.md apply plan). Append-only, idempotent:
rows already present are skipped.

  merge_decisions.jsonl      A6 res_dedup same -> add; the deterministic
                             honour-fingerprint override (same name +
                             birth + award-year refuted on a jurisdiction
                             label) -> add; the multi-member a7-same
                             cluster -> review marker
  exit_link_overrides.jsonl  a7 different -> suppress (namesake death
                             link); exitamb events with exactly ONE
                             same-verdict candidate -> promote
  person_overlays.jsonl      birth repairs (94 judged + single-candidate
                             A2 rows), honour dates (safe roll date_fills
                             + judged conflict adoptions), death dates
                             (deaths from exit_links minus suppressions,
                             plus promoted ambiguous deaths)

After this, run (in order):
  python3 iol_merge_apply.py                    # audited map from ledger
  COL_PROV=... kg_dedup_stage3_apply.py --overlay ...   # rebuild + overlays
  COL_KG_OUT=data/iol kg_emit_stage3.py ...     # re-emit KG
  python3 iol_link_exits.py                     # override-aware rerun
  python3 iol_identity_screens.py && python3 iol_identity_check.py
"""

from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path("data/iol")
IDD = ROOT / "identity"
ADJ = IDD / "adjudicate"
SOURCE = "nibi-17521812"


def jload(path: Path):
    if not path.exists():
        return
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            yield json.loads(line)


def append_new(path: Path, rows: list[dict], keyf) -> int:
    existing = {keyf(r) for r in jload(path)}
    added = 0
    with open(path, "a", encoding="utf-8") as fh:
        for r in rows:
            if keyf(r) in existing:
                continue
            existing.add(keyf(r))
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
            added += 1
    return added


def main() -> None:
    stats = Counter()

    # ---- 1. merge decisions (A6 unions + override + review marker) -----
    rows = []
    for r in jload(ADJ / "res_dedup.jsonl"):
        if r.get("verdict") not in ("same", "different"):
            continue
        # 'split' records a judged refutation so the A6 screen stops
        # re-flagging the pair (no map effect — only drop/add build it)
        rows.append({"person_a": r["person_a"],
                     "person_b": r["person_b"],
                     "action": "add" if r["verdict"] == "same" else "split",
                     "verdict": r["verdict"],
                     "confidence": r.get("confidence"),
                     "reason": (r.get("reason") or "")[:250],
                     "source": SOURCE})
    # deterministic honour fingerprint outranks the judge: identical name,
    # identical birth year, same award+year, editions disjoint — refuted
    # only on 'Cent. Provs vs Nagpur' (Nagpur IS the Cent. Provs capital)
    for r in jload(IDD / "a6_honour_duplicates.jsonl"):
        if r.get("birth_agree") and r.get("editions_disjoint"):
            rows.append({"person_a": r["person_a"],
                         "person_b": r["person_b"], "action": "add",
                         "verdict": "override",
                         "confidence": None,
                         "reason": f"a6-honour-override: same name+birth "
                                   f"{r['birth_a']}+{r['award']} "
                                   f"{r['award_year']}; fingerprint "
                                   "outranks judged refutation",
                         "source": f"a6-honour-override-{SOURCE}"})
    # multi-member cluster with a confirmed post-death attestation: park
    # for hand review (no surgery on this evidence)
    rows.append({"person_a": "kgp_iol1889_supp-c1431316",
                 "person_b": "kgp_iol1889_supp-c1431316",
                 "action": "review", "verdict": "unsure",
                 "confidence": None,
                 "reason": "a7-same on 2-member cluster: death 3.3.1910 "
                           "but attested to 1916 — possible fusion, "
                           "hand-review",
                 "source": f"{SOURCE}-a7"})
    stats["merge_decisions"] = append_new(
        IDD / "merge_decisions.jsonl", rows,
        lambda r: (r["person_a"], r["person_b"]))

    # ---- 2. exit-link overrides ----------------------------------------
    ex_rows = []
    amb_verdicts: dict[str, list[dict]] = defaultdict(list)
    for r in jload(ADJ / "res_exit.jsonl"):
        if r["id"].startswith("a7::"):
            if r.get("verdict") == "different":
                ex_rows.append({"event_id": r["event_id"],
                                "person_id": r["person_id"],
                                "action": "suppress",
                                "reason": (r.get("reason") or "")[:200],
                                "source": SOURCE})
        else:
            amb_verdicts[r["event_id"]].append(r)
    for ev, rs in sorted(amb_verdicts.items()):
        same = [r for r in rs if r.get("verdict") == "same"]
        if len(same) == 1:
            ex_rows.append({"event_id": ev,
                            "person_id": same[0]["person_id"],
                            "action": "promote",
                            "reason": (same[0].get("reason") or "")[:200],
                            "source": SOURCE})
    stats["exit_overrides"] = append_new(
        IDD / "exit_link_overrides.jsonl", ex_rows,
        lambda r: (r["event_id"], r["person_id"], r["action"]))

    # ---- 3. person overlays --------------------------------------------
    ov_rows = []
    # birth: judged repairs + unambiguous single-candidate A2 rows
    for r in jload(ADJ / "res_birth.jsonl"):
        if r.get("verdict") == "repair" and r.get("birth_year"):
            ov_rows.append({"person_id": r["person_id"],
                            "field": "birth_year",
                            "value": r["birth_year"],
                            "reason": (r.get("reason") or "")[:200],
                            "source": SOURCE})
    for r in jload(IDD / "a2_age_invariants.jsonl"):
        cands = r.get("suggested_birth_years") or []
        if len(cands) == 1:
            ov_rows.append({"person_id": r["person_id"],
                            "field": "birth_year", "value": cands[0],
                            "reason": "a2 single-candidate digit repair "
                                      f"({r['birth_year']} -> {cands[0]})",
                            "source": "a2-deterministic"})
    # honours: safe roll date fills + judged conflict adoptions
    adopted = {r["person_id"] for r in jload(ADJ / "res_roll.jsonl")
               if r.get("verdict") == "same"}
    for r in jload(IDD / "roll_links.jsonl"):
        fill = r["status"] == "date_fill" and r["n_bio_claimants"] == 1
        adopt = r["status"] == "conflict" and r["person_id"] in adopted
        if not (fill or adopt):
            continue
        ov_rows.append({"person_id": r["person_id"],
                        "field": "honour_year",
                        "award_key": r["grade"],
                        "value": r["roll_year"],
                        "month": r.get("roll_month"),
                        "day": r.get("roll_day"),
                        "replace": bool(adopt),
                        "reason": ("roll date fill" if fill else
                                   f"roll date adopted over bio "
                                   f"{r['bio_year']}"),
                        "source": f"honours-roll ({r['roll_name']})"})
    # deaths: linked deaths minus suppressions, plus promoted ambiguous
    suppressed = {(r["event_id"], r["person_id"])
                  for r in jload(IDD / "exit_link_overrides.jsonl")
                  if r["action"] == "suppress"}
    promoted = {(r["event_id"], r["person_id"])
                for r in jload(IDD / "exit_link_overrides.jsonl")
                if r["action"] == "promote"}
    review = {"kgp_iol1889_supp-c1431316"}   # fused-cluster candidate
    ev_full = {}
    for f in sorted((ROOT / "casualties").glob("casualties_*.jsonl")):
        for i, line in enumerate(open(f, encoding="utf-8")):
            rr = json.loads(line)
            ev_full[f"{rr['edition_tag']}:{i}"] = rr

    def death_row(event_id, person_id, day, month, year, src):
        return {"person_id": person_id, "field": "death_date",
                "value": year, "month": month, "day": day,
                "event_id": event_id, "reason": "casualty-table death",
                "source": src}

    for r in jload(IDD / "exit_links.jsonl"):
        if r["event"] != "death":
            continue
        if (r["event_id"], r["person_id"]) in suppressed \
                or r["person_id"] in review:
            continue
        ov_rows.append(death_row(r["event_id"], r["person_id"],
                                 r.get("day"), r.get("month"), r["year"],
                                 "exit-links"))
    for ev_id, pid in sorted(promoted):
        ev = ev_full.get(ev_id) or {}
        if ev.get("event") == "death" and ev.get("year"):
            ov_rows.append(death_row(ev_id, pid, ev.get("day"),
                                     ev.get("month"), ev["year"],
                                     "exit-ambiguous-promoted"))
    stats["person_overlays"] = append_new(
        IDD / "person_overlays.jsonl", ov_rows,
        lambda r: (r["person_id"], r["field"], r.get("award_key"),
                   r.get("event_id")))

    print("appended:", dict(stats))
    ov = Counter(r["field"] for r in jload(IDD / "person_overlays.jsonl"))
    print("overlay ledger now:", dict(ov))
    dec = Counter(r["action"] for r in jload(IDD / "merge_decisions.jsonl"))
    print("merge ledger now:", dict(dec))


if __name__ == "__main__":
    main()
