"""Known-careers regression: the hand-verified false-positive gate.

`known_careers.json` (sibling repo, read-only) holds 543 hand-verified
careers. Per career, `officials[]` are stints belonging to ONE person
(positives) and `different_persons[]` are same-surname stints belonging to
OTHER people (hard negatives). The pipeline's prime directive is no false
merges, so the gate is:

    FALSE POSITIVE = one bio_id linked to BOTH a positive stint and a
    hard-negative stint of the same career — i.e. the pipeline silently
    merged two different people.

The FP count must be 0 after ANY matching change, at both linking levels
(stint matches and record attachments). Everything else reported here
(career coverage, splits) is informational.
"""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

KNOWN_CAREERS_PATH = Path(
    "~/textasdatacolonialofficelist/ml_data/known_careers.json").expanduser()

# Ground-truth errors verified by hand — never counted as FP or as recall.
# Q6264790: the 1961 Bermuda stint is actually J. G. Woodall, mis-named
# upstream (reported to col_pipeline).
EXPECTED_MISMATCHES: set[tuple[str, str]] = {
    ("Q6264790", "Woodall, John___Bermuda___1961"),
}

# Stints that known_careers.json labels a `different_person` (hard negative)
# but which are demonstrably the SAME person as the career's biography — a
# mislabel in the upstream (Gemini-generated) split. Keyed (career_id,
# official_id); reclassified from negative to positive in the calibration
# scorer. Each entry must be backed by record-level evidence, not judgment.
#
# gemini_malta_0251 / "Zammit, Carmelo___Malta___1936": the bio is C. Gr.
# Zammit (asst. custodian of archaeology 1930 -> custodian 1934 -> director
# of museum 1955). This stint's own 1939-1940 records print "C. G. Zammit,
# Curator of the Archaeological Section" — the exact man and career stage,
# the continuous predecessor of the 1956 "Director of Museums" stint that
# the same career labels a positive. Gemini split one career in two because
# the 1936-1937 rows abbreviate to "C. Zammit". (Surfaced by the calibration
# gate 2026-06-13; flagged for upstream correction.)
EXPECTED_FALSE_NEGATIVES: set[tuple[str, str]] = {
    ("gemini_malta_0251", "Zammit, Carmelo___Malta___1936"),
}


def load_known_careers(path: Path = KNOWN_CAREERS_PATH) -> list[dict]:
    return json.loads(path.read_text())


def score_links(
    careers: list[dict], links_by_bio: dict[str, set[str]], level: str
) -> dict:
    """`links_by_bio`: bio_id -> set of official_ids the bio is linked to at
    this level. Returns a report dict; report["false_positives"] is the gate."""
    stint_to_bios: dict[str, set[str]] = defaultdict(set)
    for bio_id, stints in links_by_bio.items():
        for s in stints:
            stint_to_bios[s].add(bio_id)

    fps: list[dict] = []
    careers_touched = 0
    positives_total = positives_linked = 0
    splits = 0
    for c in careers:
        cid = c.get("career_id", "?")
        pos = {o["official_id"] for o in c.get("officials", [])
               if (cid, o["official_id"]) not in EXPECTED_MISMATCHES}
        neg = {o["official_id"] for o in c.get("different_persons", [])}
        positives_total += len(pos)
        pos_bios: set[str] = set()
        for s in pos:
            if stint_to_bios.get(s):
                positives_linked += 1
                pos_bios.update(stint_to_bios[s])
        if pos_bios:
            careers_touched += 1
        if len(pos_bios) > 1:
            splits += 1  # one career claimed by several bios — recoverable
        for bio_id in pos_bios:
            wrong = links_by_bio[bio_id] & neg
            if wrong:
                fps.append({
                    "career_id": cid,
                    "bio_id": bio_id,
                    "positives_claimed": sorted(links_by_bio[bio_id] & pos),
                    "negatives_claimed": sorted(wrong),
                })
    return {
        "level": level,
        "careers": len(careers),
        "careers_touched": careers_touched,
        "positive_stints": positives_total,
        "positive_stints_linked": positives_linked,
        "career_splits": splits,
        "false_positives": len(fps),
        "fp_details": fps,
    }


def build_calibration_cases(
    careers: list[dict],
    bios: list,
    officials: list[dict],
    data_dir: str,
    stint_links: dict[str, set[str]],
) -> tuple[list, list, dict[str, dict], dict]:
    """Blind adjudication cases from the known careers.

    For each career resolvable to exactly ONE bio via accepted phase-1 stint
    links, build a case holding that bio plus ALL the career's stints —
    ground-truth positives and `different_persons` hard negatives mixed,
    annotated through the production `_annotate` path. The dossier carries no
    labels; the answer key is returned separately and written next to (never
    inside) the dossiers.

    Returns (candidates, cases, labels, stats). Pairs that fail the hard
    gates (age, initials) are dropped exactly as production would drop them;
    they are recorded in the labels as `gated_out` since the system can never
    link them regardless of adjudicator behaviour.
    """
    from collections import defaultdict as _dd

    from .candidates import _annotate
    from .match import _norm as _n, _surname_of_official as _surn
    from .schema import Case

    bios_by_id = {b.bio_id: b for b in bios}
    officials_by_id = {o["id"]: o for o in officials}
    by_surname: dict[str, list[dict]] = _dd(list)
    for o in officials:
        by_surname[_surn(o["name"])].append(o)
    bio_surname_counts: dict[str, int] = _dd(int)
    for b in bios:
        bio_surname_counts[_n(b.surname)] += 1

    stint_to_bios: dict[str, set[str]] = _dd(set)
    for bio_id, stints in stint_links.items():
        for s in stints:
            stint_to_bios[s].add(bio_id)

    all_cands: list = []
    cases: list[Case] = []
    labels: dict[str, dict] = {}
    n_unresolved = n_multi_bio = 0
    for c in careers:
        cid = c.get("career_id", "?")
        pos = [o["official_id"] for o in c.get("officials", [])
               if (cid, o["official_id"]) not in EXPECTED_MISMATCHES]
        neg = [o["official_id"] for o in c.get("different_persons", [])
               if (cid, o["official_id"]) not in EXPECTED_FALSE_NEGATIVES]
        # documented mislabels: the "different person" is actually this bio
        pos += [o["official_id"] for o in c.get("different_persons", [])
                if (cid, o["official_id"]) in EXPECTED_FALSE_NEGATIVES]
        holder_bios: set[str] = set()
        for s in pos:
            holder_bios.update(stint_to_bios.get(s, ()))
        if not holder_bios:
            n_unresolved += 1
            continue
        if len(holder_bios) > 1:
            n_multi_bio += 1
            continue
        bio = bios_by_id.get(next(iter(holder_bios)))
        if bio is None:
            n_unresolved += 1
            continue

        case_cands: list = []
        gated_out: list[str] = []
        for sid in dict.fromkeys(pos + neg):  # de-dup, stable order
            official = officials_by_id.get(sid)
            if official is None:
                gated_out.append(sid)
                continue
            fuzzy = _surn(official["name"]) != _n(bio.surname)
            cand = _annotate(bio, official, fuzzy, data_dir,
                             bio_surname_counts, by_surname)
            if cand is None:
                gated_out.append(sid)
                continue
            cand.phase1_dropped_ambiguous = False
            cand.competing_bio_ids = []
            case_cands.append(cand)
        if not case_cands:
            n_unresolved += 1
            continue

        case_id = f"calib_{cid}"
        stint_ids = sorted({x.official_id for x in case_cands})
        cases.append(Case(
            case_id=case_id, bio_ids=[bio.bio_id], stint_ids=stint_ids,
            n_candidates=len(case_cands), route="adjudicate"))
        labels[case_id] = {
            "career_id": cid,
            "bio_id": bio.bio_id,
            "positives": sorted(set(pos) & set(stint_ids)),
            "negatives": sorted(set(neg) & set(stint_ids)),
            "gated_out": gated_out,
        }
        all_cands.extend(case_cands)

    stats = {
        "careers": len(careers),
        "cases_built": len(cases),
        "careers_unresolved": n_unresolved,
        "careers_multi_bio_skipped": n_multi_bio,
        "candidate_pairs": len(all_cands),
        "positive_pairs": sum(len(l["positives"]) for l in labels.values()),
        "negative_pairs": sum(len(l["negatives"]) for l in labels.values()),
        "gated_out_pairs": sum(len(l["gated_out"]) for l in labels.values()),
    }
    return all_cands, cases, labels, stats


def _wilson_lower(successes: int, n: int, z: float = 1.96) -> float:
    if n == 0:
        return 0.0
    p = successes / n
    denom = 1 + z * z / n
    centre = p + z * z / (2 * n)
    margin = z * ((p * (1 - p) + z * z / (4 * n)) / n) ** 0.5
    return (centre - margin) / denom


def score_verdicts(verdict_rows: list[dict], labels: dict[str, dict]) -> dict:
    """Score compiled (post-guard) verdicts against the calibration answer
    key. The gate: confirm-tier assignments must contain ZERO hard negatives,
    and confirm-tier precision on labelled stints must be >= 0.995."""
    from collections import defaultdict as _dd

    tiers: dict[str, dict] = {t: {"tp": 0, "fp": 0, "fp_details": []}
                              for t in ("confirm", "review")}
    positives_total = sum(len(l["positives"]) for l in labels.values())
    positives_confirmed = 0
    guard_counts: dict[str, int] = _dd(int)
    for row in verdict_rows:
        lab = labels.get(row["case_id"])
        if lab is None or row["tier"] not in tiers or not row["bio_id"]:
            continue
        for t in row.get("guard_trace", []):
            guard_counts[t.split(":")[0]] += 1
        bucket = tiers[row["tier"]]
        for sid in row["stint_ids"]:
            if sid in lab["negatives"]:
                bucket["fp"] += 1
                bucket["fp_details"].append(
                    {"case_id": row["case_id"], "bio_id": row["bio_id"],
                     "stint_id": sid, "tier": row["tier"]})
            elif sid in lab["positives"]:
                bucket["tp"] += 1
                if row["tier"] == "confirm":
                    positives_confirmed += 1

    conf = tiers["confirm"]
    n_conf = conf["tp"] + conf["fp"]
    precision = conf["tp"] / n_conf if n_conf else None
    report = {
        "cases_scored": len({r["case_id"] for r in verdict_rows
                             if r["case_id"] in labels}),
        "confirm_assignments": n_conf,
        "confirm_fp": conf["fp"],
        "confirm_precision": round(precision, 4) if precision is not None else None,
        "confirm_precision_wilson_lower": round(
            _wilson_lower(conf["tp"], n_conf), 4) if n_conf else None,
        "recall_confirm_tier": round(positives_confirmed / positives_total, 4)
            if positives_total else None,
        "review_tp": tiers["review"]["tp"],
        "review_fp": tiers["review"]["fp"],
        "guard_triggers": dict(sorted(guard_counts.items())),
        "fp_details": conf["fp_details"] + tiers["review"]["fp_details"],
        "gate_passed": conf["fp"] == 0
            and (precision is None or precision >= 0.995),
    }
    return report


def load_phase1_links(data_dir: str) -> tuple[dict[str, set[str]], dict[str, set[str]]]:
    """(stint-level, record-level) bio_id -> linked official_ids from the
    accepted phase-1 artifacts."""
    matches = Path(data_dir) / "matches"
    stint: dict[str, set[str]] = defaultdict(set)
    with (matches / "stint_matches.jsonl").open(encoding="utf-8") as fh:
        for line in fh:
            m = json.loads(line)
            stint[m["bio_id"]].add(m["official_id"])
    record: dict[str, set[str]] = defaultdict(set)
    with (matches / "record_attachments.jsonl").open(encoding="utf-8") as fh:
        for line in fh:
            a = json.loads(line)
            record[a["bio_id"]].add(a["stint_id"])
    return stint, record
