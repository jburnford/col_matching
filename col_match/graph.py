"""Read-only accessor for the COL_Official seam.

Implements docs/data_contract.md: pull candidate clusters (connected
components of POSSIBLE_MATCH) and each stint's quarantine-filtered evidence.
There is deliberately no write path in this module.

Usage:

    from col_match.config import Config
    from col_match.graph import connect, fetch_cluster

    cfg = Config.from_env()
    with connect(cfg) as driver:
        cluster = fetch_cluster(driver, seed_uri="col:official/sierra_leone/cardew_f", cfg=cfg)
        for stint in cluster:
            print(stint["official"]["canonical_name"], len(stint["records"]))
"""

from __future__ import annotations

from contextlib import contextmanager
from typing import Any, Iterator

from neo4j import GraphDatabase

# Colony/year pairs quarantined upstream but not removed from the graph.
# See docs/data_contract.md → Quarantine filters.
_QUARANTINED_COLONY_YEARS = {
    ("Aden", 1922),
    ("Lagos", 1879),
    ("Lagos", 1883),
}


@contextmanager
def connect(cfg) -> Iterator[Any]:
    """Yield a Neo4j driver. Read-only by convention — do not write through it."""
    driver = GraphDatabase.driver(cfg.neo4j_uri, auth=(cfg.neo4j_user, cfg.neo4j_password))
    try:
        yield driver
    finally:
        driver.close()


def _keep_record(rec: dict) -> bool:
    """Apply the mandatory quarantine filters from the data contract."""
    if rec.get("quarantined"):
        return False
    if (rec.get("colony"), rec.get("year")) in _QUARANTINED_COLONY_YEARS:
        return False
    return True


def _evidence_for(tx, official_uri: str) -> list[dict]:
    """Return non-quarantined COL_PersonRecord evidence for one official."""
    rows = tx.run(
        """
        MATCH (pr:COL_PersonRecord)-[:RECORD_OF]->(o:COL_Official {uri: $uri})
        RETURN pr {
          .name_raw, .canonical_name, .surname, .given_names,
          .position_raw, .department_raw,
          .salary_min, .salary_max, .salary_currency,
          .honors, .qualifications, .military_rank, .location,
          .colony, .year, .quarantined, .quarantine_reason
        } AS pr
        ORDER BY pr.year
        """,
        uri=official_uri,
    )
    return [r["pr"] for r in rows if _keep_record(r["pr"])]


def fetch_cluster(driver, *, seed_uri: str, cfg) -> list[dict]:
    """Return the candidate cluster containing `seed_uri`.

    A cluster is the connected component of COL_Official nodes reachable from
    the seed via POSSIBLE_MATCH edges whose uncertainty is <= cfg.max_uncertainty
    (in either direction). Each entry is {official, records}, with records
    quarantine-filtered. Officials with no surviving evidence are dropped.
    """
    with driver.session(database=cfg.neo4j_database) as session:
        officials = session.execute_read(_cluster_officials, seed_uri, cfg.max_uncertainty)
        result = []
        for off in officials:
            records = session.execute_read(_evidence_for, off["uri"])
            if records:
                result.append({"official": off, "records": records})
        return result


def _cluster_officials(tx, seed_uri: str, max_uncertainty: float) -> list[dict]:
    rows = tx.run(
        """
        MATCH (seed:COL_Official {uri: $uri})
        OPTIONAL MATCH path = (seed)-[:POSSIBLE_MATCH*1..6]-(other:COL_Official)
          WHERE all(r IN relationships(path) WHERE r.uncertainty <= $thr)
        WITH seed, collect(DISTINCT other) AS others
        WITH [seed] + others AS members
        UNWIND members AS m
        RETURN DISTINCT m {
          .uri, .canonical_name, .surname, .colony,
          .first_year, .last_year, .editions, .domain
        } AS official
        """,
        uri=seed_uri,
        thr=max_uncertainty,
    )
    return [r["official"] for r in rows]
