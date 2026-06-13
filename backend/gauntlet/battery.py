"""Run a generated battery through the contestants and report tail risk.

Each curated case is Monte-Carlo'd with small structural jitter so the headline
numbers are stable, not a single lucky draw. Per agent we report pass-rate
(share of runs recovering at least TAU of the recoverable loss), the worst-case
P10 score (tail risk: the bad days behind the average), and the single hardest
case, the day that breaks that agent.

Deterministic: mock contestants plus seeded jitter, no API. Real-LLM rows would
be precomputed separately, like the leaderboard.
"""

import dataclasses
import json
from pathlib import Path

import numpy as np

from .agents.llm import MockLLM
from .agents.noop import DoNothingAgent
from .agents.rules import RuleAgent
from .fitness import TAU
from .oracle import oracle_cost
from .scenarios import build_from_genome
from .scoring import score
from .sim import run_episode

CONTESTANTS = ("noop", "rules", "llm")
MC_N = 16
SEED0 = 5000
REPO_ROOT = Path(__file__).resolve().parents[2]


def _agent(name: str):
    return {"noop": DoNothingAgent, "rules": RuleAgent, "llm": MockLLM}[name]()


def run_battery(battery: list, contestants=CONTESTANTS, mc_n: int = MC_N, seed0: int = SEED0) -> dict:
    cases_out = []
    # per agent: flat list of all (case x seed) scores, and per-case mean scores
    all_scores = {a: [] for a in contestants}
    per_case_mean = {a: [] for a in contestants}

    for ci, case in enumerate(battery):
        base = case["genome"]
        case_scores = {a: [] for a in contestants}
        for s in range(mc_n):
            seed = seed0 + ci * 1000 + s
            g = base.jitter(np.random.default_rng(seed))
            sc = build_from_genome(g, seed=seed)
            floor = float(run_episode(sc, DoNothingAgent())["_cum_cost"][-1])
            oracle = oracle_cost(sc)
            for a in contestants:
                cost = run_episode(sc, _agent(a))["totals"]["cost_eur"]
                case_scores[a].append(score(cost, floor, oracle))
        agents_block = {}
        for a in contestants:
            arr = np.array(case_scores[a])
            all_scores[a].extend(case_scores[a])
            per_case_mean[a].append(float(arr.mean()))
            agents_block[a] = {
                "mean": round(float(arr.mean()), 4),
                "pass_rate": round(float((arr >= TAU).mean()), 4),
                "p10": round(float(np.percentile(arr, 10)), 4),
            }
        cases_out.append({
            "name": case["name"], "label": case["label"],
            "stake": case["eval"]["stake"], "floor": case["eval"]["floor"],
            "oracle": case["eval"]["oracle"], "fitness": case["eval"]["fitness"],
            "genome": dataclasses.asdict(base), "agents": agents_block,
        })

    report = {}
    for a in contestants:
        arr = np.array(all_scores[a])
        means = per_case_mean[a]
        hardest_i = int(np.argmin(means))
        report[a] = {
            "pass_rate": round(float((arr >= TAU).mean()), 4),
            "p10": round(float(np.percentile(arr, 10)), 4),
            "mean": round(float(arr.mean()), 4),
            "hardest": {"name": cases_out[hardest_i]["name"],
                        "label": cases_out[hardest_i]["label"],
                        "mean": round(means[hardest_i], 4)},
        }
    return {"mc_n": mc_n, "k": len(battery), "cases": cases_out, "report": report,
            "contestants": list(contestants)}


def save(payload: dict, mode: str, out: Path) -> Path:
    out.mkdir(parents=True, exist_ok=True)
    f = out / f"{mode.replace(':', '_')}.json"
    f.write_text(json.dumps(payload))
    return f
