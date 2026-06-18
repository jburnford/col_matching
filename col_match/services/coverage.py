"""Coverage report: how much of the graph's matching problem do the
services-section biographies cover?

Reports stint coverage (overall / by colony / by decade) and, for the
POSSIBLE_MATCH candidate components, how many are directly adjudicable
(>= 2 member stints matched to the SAME biography).
"""

from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

from .schema import StintMatch


def _components(edges: list[tuple[str, str]]) -> list[set[str]]:
    parent: dict[str, str] = {}

    def find(x: str) -> str:
        while parent.setdefault(x, x) != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for a, b in edges:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb
    groups: dict[str, set[str]] = defaultdict(set)
    for node in parent:
        groups[find(node)].add(node)
    return list(groups.values())


def coverage_report(
    officials: list[dict],
    matches: list[StintMatch],
    edges: list[tuple[str, str]],
    out_dir: str | Path,
) -> dict:
    matched_stints = {m.official_id for m in matches}
    bios_of_stint: dict[str, set[str]] = defaultdict(set)
    for m in matches:
        bios_of_stint[m.official_id].add(m.bio_id)

    total = len(officials)
    by_colony_total: Counter = Counter()
    by_colony_hit: Counter = Counter()
    by_decade_total: Counter = Counter()
    by_decade_hit: Counter = Counter()
    for o in officials:
        decade = (o["first_year"] // 10) * 10 if o["first_year"] else 0
        by_colony_total[o["colony"]] += 1
        by_decade_total[decade] += 1
        if o["id"] in matched_stints:
            by_colony_hit[o["colony"]] += 1
            by_decade_hit[decade] += 1

    comps = _components(edges)
    adjudicable = partial = uncovered = 0
    for comp in comps:
        bio_hits: Counter = Counter()
        for stint in comp:
            for bio in bios_of_stint.get(stint, ()):
                bio_hits[bio] += 1
        if bio_hits and bio_hits.most_common(1)[0][1] >= 2:
            adjudicable += 1
        elif any(s in matched_stints for s in comp):
            partial += 1
        else:
            uncovered += 1

    report = {
        "stints_total": total,
        "stints_matched": len(matched_stints),
        "stint_coverage_pct": round(100 * len(matched_stints) / max(total, 1), 1),
        "components_total": len(comps),
        "components_adjudicable_same_bio": adjudicable,
        "components_partial": partial,
        "components_uncovered": uncovered,
        "by_decade": {
            str(d): {"total": by_decade_total[d], "matched": by_decade_hit[d]}
            for d in sorted(by_decade_total)
        },
        "top_colonies": {
            c: {"total": by_colony_total[c], "matched": by_colony_hit[c]}
            for c, _ in by_colony_total.most_common(25)
        },
    }

    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    (out / "coverage.json").write_text(json.dumps(report, indent=2))

    lines = [
        "# Services-section coverage report\n",
        f"- Stints matched to a biography: **{report['stints_matched']:,} / "
        f"{report['stints_total']:,} ({report['stint_coverage_pct']}%)**",
        f"- POSSIBLE_MATCH components: {report['components_total']:,}",
        f"  - directly adjudicable (≥2 stints, same biography): "
        f"**{adjudicable:,}**",
        f"  - partially covered (≥1 stint matched): {partial:,}",
        f"  - uncovered: {uncovered:,}",
        "\n## By decade (stint first_year)\n",
        "| decade | stints | matched | % |",
        "|---|---|---|---|",
    ]
    for d in sorted(by_decade_total):
        t, h = by_decade_total[d], by_decade_hit[d]
        lines.append(f"| {d}s | {t:,} | {h:,} | {100 * h / max(t, 1):.0f}% |")
    lines += ["\n## Top colonies\n", "| colony | stints | matched | % |", "|---|---|---|---|"]
    for c, _ in by_colony_total.most_common(25):
        t, h = by_colony_total[c], by_colony_hit[c]
        lines.append(f"| {c} | {t:,} | {h:,} | {100 * h / max(t, 1):.0f}% |")
    (out / "coverage.md").write_text("\n".join(lines) + "\n")
    return report
