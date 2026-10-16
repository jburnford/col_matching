#!/usr/bin/env python3
"""Offline, place-only WHG preparation. Outputs candidates, never implicit approval.

Only source-specific, explicit place/year spans corroborated in raw text become
direct evidence. Inherited places and merged career dates stay separate. No
person fields, career roles, or atlas seat coordinates enter the output.
"""
import argparse
import collections
import csv
import hashlib
import json
from pathlib import Path
import re
import unicodedata

from col_match.kg.place_canon import is_institution

ROOT = Path(__file__).resolve().parent
VERSION = 1
STATUSES = {"british_empire", "outside_british_empire", "mixed_or_contested", "unknown"}


def rows(path):
    with path.open(encoding="utf-8") as handle:
        for number, line in enumerate(handle, 1):
            if line.strip():
                yield number, json.loads(line)


def norm(text):
    return " ".join(re.findall(r"\w+", unicodedata.normalize("NFKC", text or "").casefold()))


def contains(text, phrase):
    needle = norm(phrase)
    return bool(needle) and f" {needle} " in f" {norm(text)} "


class NameMatcher:
    """Token trie with failure links: scan each source once, not once per name.

    Occurrences are retrieval candidates only: e.g. Victoria can name a person.
    """
    def __init__(self, names):
        self.edges, self.fail, self.hits = [{}], [0], [[]]
        for name, qids in sorted(names.items()):
            if len(qids) != 1 or len(name.replace(" ", "")) < 3:
                continue
            state = 0
            parts = name.split()
            for token in parts:
                if token not in self.edges[state]:
                    self.edges[state][token] = len(self.edges)
                    self.edges.append({})
                    self.fail.append(0)
                    self.hits.append([])
                state = self.edges[state][token]
            self.hits[state].append((next(iter(qids)), len(parts)))
        queue = collections.deque(self.edges[0].values())
        while queue:
            state = queue.popleft()
            for token, child in self.edges[state].items():
                queue.append(child)
                failure = self.fail[state]
                while failure and token not in self.edges[failure]:
                    failure = self.fail[failure]
                self.fail[child] = self.edges[failure].get(token, 0)
                self.hits[child].extend(self.hits[self.fail[child]])

    def find(self, raw):
        tokens = list(re.finditer(r"\w+", raw))
        state, seen = 0, set()
        for index, token in enumerate(tokens):
            word = unicodedata.normalize("NFKC", token.group()).casefold()
            while state and word not in self.edges[state]:
                state = self.fail[state]
            state = self.edges[state].get(word, 0)
            for qid, size in self.hits[state]:
                start, end = tokens[index - size + 1].start(), token.end()
                printed = raw[start:end]
                # Preserve case in evidence; lowercase common words are too noisy.
                if not printed[0].isupper() or (qid, norm(printed)) in seen:
                    continue
                seen.add((qid, norm(printed)))
                yield qid, printed, start, end


def valid_year(value):
    return value if type(value) is int and 1500 <= value <= 1966 else None


def exportable_name(name):
    """Hold obvious delimiters/OCR furniture; preserve originals in evidence."""
    if not name or any(ch in name for ch in ';\t\r\n"“”@'):
        return False
    if name[0] in "([{" or name[-1] in ")]}" or name != name.strip():
        return False
    return name.count("(") == name.count(")") and name.count("[") == name.count("]")


def source_check(event, raw, edition):
    """Return a reason, not a confidence score masquerading as validation."""
    place, span = event.get("place"), event.get("text_span") or ""
    year = valid_year(event.get("year_start"))
    if event.get("place_inherited"):
        return "inherited_place"
    if not place or is_institution(place)[0]:
        return "missing_or_institution_place"
    if len(norm(place).replace(" ", "")) < 3:
        return "short_ambiguous_name"
    if year is None or valid_year(edition) is None or year > edition:
        return "missing_or_future_year"
    if not span or not norm(span) or not contains(raw, span):
        return "span_not_in_raw_text"
    if not contains(span, place):
        return "place_not_in_span"
    if not re.search(rf"(?<!\d){year}(?!\d)", span):
        return "year_not_explicit_in_span"
    return "direct_source_candidate"


def suggested_class(labels):
    """Proposals only: mixed classes require review, not a precedence rule."""
    mapping = {
        "P": r"\b(city|town|village|settlement|hamlet)\b",
        "A": r"\b(colony|protectorate|province|district|presidency|country|state|territory|county|dominion)\b",
        "H": r"\b(river|lake|bay|sea|strait)\b",
        "T": r"\b(mountain|hill|cape)\b",
        "L": r"\b(island|archipelago|region)\b",
    }
    text = " ".join(labels).lower()
    found = {code for code, pattern in mapping.items() if re.search(pattern, text)}
    return next(iter(found)) if len(found) == 1 else ""


def relationship(qid, year, rules):
    matches = [r for r in rules if r["qid"] == qid and year is not None
               and r["start"] <= year <= r["end"]]
    if not matches:
        return {"status": "unknown", "sources": []}
    statuses = {r["status"] for r in matches}
    return {"status": next(iter(statuses)) if len(statuses) == 1 else "mixed_or_contested",
            "sources": sorted({r["source"] for r in matches})}


def validate_rules(config):
    if config.get("version") != 1:
        raise ValueError("Unsupported rules version")
    for rule in config.get("imperial_relationships", []):
        if (rule.get("status") not in STATUSES or not rule.get("source")
                or type(rule.get("start")) is not int or type(rule.get("end")) is not int
                or rule["start"] > rule["end"] or not re.fullmatch(r"Q\d+", rule.get("qid", ""))):
            raise ValueError(f"Invalid status rule: {rule}")
    for qid, decision in config.get("place_decisions", {}).items():
        if not re.fullmatch(r"Q\d+", qid):
            raise ValueError("Invalid decision QID")
        if decision.get("approved") and (not decision.get("evidence")
                or decision.get("fclass") not in set("AHLP RSTUV".replace(" ", ""))):
            raise ValueError("Approval needs identity evidence and an explicit feature class")


def digest(path):
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def run(root, output, config_path, force=False):
    config = json.loads(config_path.read_text(encoding="utf-8"))
    validate_rules(config)
    inputs = [config_path, Path(__file__)]
    for corpus in ("kg", "iol"):
        graph = root / f"data/{corpus}/graph_stage3"
        inputs += [graph / "places.jsonl", graph / "career_events.jsonl"]
        inputs += sorted((root / f"data/{corpus}/bios").glob("*.jsonl"))
    inputs += [root / "col_match/kg/place_canon.py"]
    temporal_path = root / "research/geography-2026-10-07/current-temporal-review.tsv"
    if temporal_path.exists():
        inputs.append(temporal_path)
    manifest = {str(p.relative_to(root)) if p.is_relative_to(root) else str(p): digest(p)
                for p in inputs}
    output.mkdir(parents=True, exist_ok=True)
    outputs = ["places.jsonl", "evidence.jsonl", "review.tsv", "unresolved-names.json",
               "review-groups.json", "whg-preview.tsv", "whg-ready.tsv", "report.json"]
    previous = output / "manifest.json"
    if not force and previous.exists():
        old = json.loads(previous.read_text())
        if old.get("inputs") == manifest and all(
                (output / name).exists() and digest(output / name) == old.get("outputs", {}).get(name)
                for name in outputs):
            print("Unchanged inputs and outputs; reused", output)
            return json.loads((output / "report.json").read_text())

    places, lookup, counts = {}, {}, collections.Counter()
    unresolved, review_groups = {}, collections.defaultdict(list)
    temporal = collections.Counter()
    if temporal_path.exists():
        with temporal_path.open(encoding="utf-8") as handle:
            temporal.update(row["qid"] for row in csv.DictReader(handle, delimiter="\t"))
    def ensure(qid, label=None):
        if qid not in places:
            places[qid] = {"qid": qid, "labels": set(), "variants": set(), "types": set(),
                           "corpora": set(), "event_years": set(), "source_years": set(),
                           "direct_years": set(), "direct_variants": collections.Counter(),
                           "variant_sources": collections.defaultdict(set),
                           "direct_count": 0, "event_count": 0, "source_examples": [],
                           "name_occurrence_count": 0, "occurrence_years": set(),
                           "occurrence_examples": [],
                           "grounding_methods": set(), "temporal_flags": 0}
        if label:
            places[qid]["labels"].add(label)
        return places[qid]

    for corpus in ("kg", "iol"):
        lookup[corpus] = collections.defaultdict(set)
        graph = root / f"data/{corpus}/graph_stage3"
        for _, row in rows(graph / "places.jsonl"):
            qid = row.get("qid")
            if not qid or not re.fullmatch(r"Q\d+", qid):
                counts["invalid_place_identifiers"] += 1
                continue
            p = ensure(qid, row.get("label"))
            p["corpora"].add(corpus)
            p["variants"].add(row["place"])
            p["types"].update(str(x) for x in row.get("instance_of", []))
            p["grounding_methods"].add(row.get("match_type") or "unknown")
            lookup[corpus][norm(row["place"])].add(qid)
        for _, event in rows(graph / "career_events.jsonl"):
            counts[f"{corpus}_events"] += 1
            # Explicit place identity only. The colony field can be inferred or wrong.
            qid = event.get("place_qid")
            if not qid:
                counts[f"{corpus}_events_without_explicit_place_qid"] += 1
                continue
            p = ensure(qid, event.get("place_label"))
            p["corpora"].add(corpus)
            p["event_count"] += 1
            y = valid_year(event.get("year_start"))
            if y is not None:
                p["event_years"].add(y)
            if event.get("date_uncertain"):
                counts["uncertain_event_years"] += 1
            if event.get("location_note") or event.get("historical_corrections"):
                p["temporal_flags"] += 1

    # Stream raw sources. No graph person join: a merged biography's editions
    # cannot establish that every place occurs in every edition.
    with (output / "evidence.jsonl").open("w", encoding="utf-8") as evidence:
        for corpus in ("kg", "iol"):
            matcher = NameMatcher(lookup[corpus])
            files = sorted((root / f"data/{corpus}/bios").glob("*.jsonl"))
            counts[f"{corpus}_source_files"] = len(files)
            for path in files:
                for line, bio in rows(path):
                    raw, edition = bio.get("raw_text") or "", bio.get("edition_year")
                    if valid_year(edition) is not None:
                        for qid, printed, start, end in matcher.find(raw):
                            p = places[qid]
                            p["name_occurrence_count"] += 1
                            p["occurrence_years"].add(edition)
                            locator = {"path": str(path.relative_to(root)), "line": line,
                                       "char_start": start, "char_end": end}
                            if len(p["occurrence_examples"]) < 3:
                                p["occurrence_examples"].append(locator)
                            record = {"place_id": "imperial-places:" + qid, "qid": qid,
                                      "printed_name": printed, "publication_year": edition,
                                      "historical_year": None, "corpus": corpus,
                                      "source": locator, "evidence_tier": "name_occurrence_only",
                                      "identity_basis": "lexicon_candidate_not_disambiguated"}
                            evidence.write(json.dumps(record, ensure_ascii=False) + "\n")
                            counts["name_occurrence_records"] += 1
                    for index, event in enumerate(bio.get("events") or []):
                        reason = source_check(event, raw, edition)
                        counts[reason] += 1
                        if reason != "direct_source_candidate":
                            continue
                        candidates = lookup[corpus].get(norm(event["place"]), set())
                        if len(candidates) != 1:
                            issue = "source_identity_ambiguous" if candidates else "source_identity_unmapped"
                            counts[issue] += 1
                            key = corpus + ":" + norm(event["place"])
                            item = unresolved.setdefault(key, {"name": event["place"], "corpus": corpus,
                                                               "reason": issue, "candidate_qids": sorted(candidates),
                                                               "count": 0, "source_examples": []})
                            item["count"] += 1
                            if len(item["source_examples"]) < 3:
                                item["source_examples"].append({"path": str(path.relative_to(root)),
                                                                "line": line, "event_index": index})
                            continue
                        qid = next(iter(candidates))
                        p = places[qid]
                        year = event["year_start"]
                        p["source_years"].add(edition)
                        p["direct_years"].add(year)
                        p["direct_variants"][event["place"]] += 1
                        p["variant_sources"][event["place"]].add((edition, corpus))
                        p["direct_count"] += 1
                        locator = {"path": str(path.relative_to(root)), "line": line,
                                   "event_index": index}
                        if len(p["source_examples"]) < 3:
                            p["source_examples"].append(locator)
                        # Citation metadata only; deliberately exclude name, role,
                        # personal identifiers, and full biographical passages.
                        record = {"place_id": "imperial-places:" + qid, "qid": qid,
                                  "evidence_tier": "explicit_place_and_year_span",
                                  "printed_name": event["place"], "historical_year": year,
                                  "publication_year": edition, "corpus": corpus,
                                  "source": locator, "identity_basis": "existing_grounding_candidate",
                                  "imperial_relationship": relationship(qid, year, config.get("imperial_relationships", []))}
                        record["page_locators"] = [{k: v[k] for k in ("doc", "page", "block", "bbox") if k in v}
                                                   for v in bio.get("provenance", [])]
                        evidence.write(json.dumps(record, ensure_ascii=False) + "\n")
                        counts["direct_evidence_records"] += 1

    fields = ["id", "title", "title_source", "attestation_year", "fclasses", "matches", "variants"]
    with ((output / "places.jsonl").open("w", encoding="utf-8") as place_file,
          (output / "review.tsv").open("w", encoding="utf-8", newline="") as review_file,
          (output / "whg-preview.tsv").open("w", encoding="utf-8", newline="") as preview_file,
          (output / "whg-ready.tsv").open("w", encoding="utf-8", newline="") as ready_file):
        review = csv.DictWriter(review_file, fieldnames=["qid", "label", "direct_evidence", "name_occurrences", "event_references", "priority", "issues"], delimiter="\t", lineterminator="\n")
        preview = csv.DictWriter(preview_file, fieldnames=fields, delimiter="\t", lineterminator="\n", quoting=csv.QUOTE_NONE)
        ready = csv.DictWriter(ready_file, fieldnames=fields, delimiter="\t", lineterminator="\n", quoting=csv.QUOTE_NONE)
        for writer in (review, preview, ready):
            writer.writeheader()
        for qid, p in sorted(places.items()):
            decision = config.get("place_decisions", {}).get(qid, {})
            labels = sorted(p["labels"])
            title = decision.get("title") or (p["direct_variants"].most_common(1)[0][0] if p["direct_variants"] else (labels[0] if labels else qid))
            fclass = decision.get("fclass") or suggested_class(p["types"])
            issues = []
            if not p["direct_count"]:
                issues.append("no_direct_source_evidence")
            if len(labels) > 1:
                issues.append("multiple_grounded_labels")
            if not fclass:
                issues.append("place_type_unresolved")
            if p["temporal_flags"]:
                issues.append("historical_corrections_or_location_notes")
            if temporal[qid]:
                issues.append("temporal_screen_candidate_not_confirmed_error")
            if not decision.get("approved"):
                issues.append("identity_not_independently_approved")
            if title not in p["direct_variants"]:
                issues.append("title_not_directly_attested")
            held_names = sorted(v for v in p["direct_variants"] if not exportable_name(v))
            if held_names:
                issues.append("name_variants_need_punctuation_review")
            statuses = {str(y): relationship(qid, y, config.get("imperial_relationships", [])) for y in sorted(p["direct_years"])}
            if not statuses or any(v["status"] == "unknown" for v in statuses.values()):
                issues.append("imperial_relationship_unknown")
            approved = (decision.get("approved") is True and p["direct_count"] > 0
                        and bool(fclass) and title in p["direct_variants"] and exportable_name(title))
            result = {
                "id": "imperial-places:" + qid, "qid": qid, "title": title,
                "grounded_labels": labels, "candidate_variants": sorted(p["variants"]),
                "directly_attested_variants": sorted(p["direct_variants"]),
                "name_variants_held_from_export": held_names,
                "candidate_place_types": sorted(p["types"]), "proposed_fclass": fclass,
                "corpora": sorted(p["corpora"]),
                "candidate_event_years": sorted(p["event_years"]),
                "direct_historical_years": sorted(p["direct_years"]),
                "source_publication_years": sorted(p["source_years"]),
                "candidate_name_occurrence_publication_years": sorted(p["occurrence_years"]),
                "name_occurrence_count": p["name_occurrence_count"],
                "name_occurrence_examples": p["occurrence_examples"],
                "imperial_relationships_by_historical_year": statuses,
                "candidate_imperial_relationships_by_year": {str(y): relationship(qid, y, config.get("imperial_relationships", [])) for y in sorted(p["event_years"])},
                "direct_evidence_count": p["direct_count"], "source_examples": p["source_examples"],
                "grounding_methods": sorted(p["grounding_methods"]),
                "temporal_screen_event_count": temporal[qid],
                "ready": approved, "review_issues": issues,
                "geometry": None,
            }
            place_file.write(json.dumps(result, ensure_ascii=False) + "\n")
            priority = p["direct_count"] + p["event_count"]
            review.writerow({"qid": qid, "label": title, "direct_evidence": p["direct_count"],
                             "name_occurrences": p["name_occurrence_count"],
                             "event_references": p["event_count"], "priority": priority,
                             "issues": ";".join(issues)})
            for issue in issues:
                review_groups[issue].append({"qid": qid, "title": title, "priority": priority,
                                             "direct_evidence": p["direct_count"],
                                             "name_occurrences": p["name_occurrence_count"]})
            counts["place_candidates"] += 1
            counts["places_with_direct_evidence"] += bool(p["direct_count"])
            counts["places_with_name_occurrences"] += bool(p["name_occurrence_count"])
            counts["ready_places"] += bool(approved)
            counts["name_variants_held_from_export"] += len(held_names)
            if p["direct_count"] and fclass and title in p["direct_variants"] and exportable_name(title):
                variants = [v for v in sorted(p["direct_variants"]) if v != title and exportable_name(v)]
                # Simple preview uses one real publication year; the JSONL ledger
                # preserves all discrete years. Never stretch them into a lifespan.
                publication_year, title_corpus = min(p["variant_sources"][title])
                source_title = "Colonial Office List" if title_corpus == "kg" else "India Office List"
                row = {"id": result["id"], "title": title,
                       "title_source": f"{source_title} ({publication_year}); locators in evidence.jsonl",
                       "attestation_year": publication_year, "fclasses": fclass,
                       "matches": "wd:" + qid, "variants": ";".join(v + "@und" for v in variants)}
                preview.writerow(row)
                counts["preview_places"] += 1
                if approved:
                    ready.writerow(row)

    write_json(output / "unresolved-names.json", sorted(unresolved.values(), key=lambda r: (-r["count"], r["name"])))
    write_json(output / "review-groups.json", {issue: sorted(items, key=lambda r: (-r["priority"], r["qid"]))
                                             for issue, items in sorted(review_groups.items())})
    counts["unresolved_name_groups"] = len(unresolved)
    counts["temporal_screen_place_groups"] = sum(bool(temporal[qid]) for qid in places)
    report = {"pipeline_version": VERSION, "counts": dict(sorted(counts.items())),
              "scope": "Place and year candidates only; no people or career networks.",
              "limitations": [
                  "Existing Wikidata mappings are candidates, not independent verification.",
                  "Only explicit source spans with full historical years are included as direct evidence.",
                  "Source date/name co-occurrence corroborates extraction, not historical identity.",
                  "Absent source files, inherited places and abbreviated years are held back.",
                  "No atlas coordinates, modern-country status inheritance, or inferred lifespans.",
                  "LP-TSV is a preview; rich evidence and imperial status remain in JSONL sidecars.",
                  "No network calls, WHG upload, or publication performed."
              ]}
    write_json(output / "report.json", report)
    write_json(previous, {"inputs": manifest, "outputs": {name: digest(output / name) for name in outputs}})
    print(json.dumps(report, indent=2))
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--out", type=Path, default=ROOT / "out/whg")
    parser.add_argument("--rules", type=Path, default=ROOT / "config/whg_rules.json")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    run(args.root.resolve(), args.out.resolve(), args.rules.resolve(), args.force)


if __name__ == "__main__":
    main()
