"""How good is a test case? A case is valuable only if it DISCRIMINATES.

The product already brackets every scenario between a perfect-foresight oracle
and do-nothing, so floor - oracle is the recoverable euros at stake, for free. A
case with nothing recoverable teaches nothing; a case where competent agents
recover wildly different amounts teaches a lot. Fitness rewards both:

    discrimination mode : norm_stake * (DISC_FLOOR + |score_llm - score_rules|)
    adversarial mode    : norm_stake * (DISC_FLOOR + (1 - score_target))

Discrimination is agent-agnostic (find days that separate good from bad).
Adversarial points the same machine at one agent (find the day that breaks it).
Everything here is deterministic: mock agents plus the analytic oracle, no API.
"""

import numpy as np

from .agents.llm import MockLLM
from .agents.noop import DoNothingAgent
from .agents.rules import RuleAgent
from .oracle import oracle_cost
from .scenarios import build_from_genome
from .scoring import score
from .sim import run_episode

STAKE_REF = 4000.0   # euros at which norm_stake saturates (tanh)
MIN_STAKE = 300.0    # below this, the day recovers too little to test anything
DISC_FLOOR = 0.25    # keeps stake meaningful when the score spread is small
TAU = 0.5            # "pass" threshold on the recovered-share score

# the competent panel whose disagreement defines discrimination (noop is the
# floor by construction, so it carries no signal and is excluded here)
_PANEL = ("rules", "llm")


def _make(name: str):
    return {"rules": RuleAgent, "llm": MockLLM}[name]()


def evaluate(genome, target: str | None = None, seed: int = 0) -> dict:
    """Return stake, panel scores, discrimination and the fitness for this genome."""
    sc = build_from_genome(genome, seed=seed)
    floor = float(run_episode(sc, DoNothingAgent())["_cum_cost"][-1])
    oracle = oracle_cost(sc)
    stake = floor - oracle

    scores, false_dispatches = {}, {}
    for a in _PANEL:
        t = run_episode(sc, _make(a))
        scores[a] = score(t["totals"]["cost_eur"], floor, oracle)
        false_dispatches[a] = t["totals"]["false_dispatches"]
    spread = abs(scores["llm"] - scores["rules"])
    norm_stake = float(np.tanh(stake / STAKE_REF)) if stake > 0 else 0.0

    if stake < MIN_STAKE:
        fitness = 0.0
    elif target in _PANEL:
        fitness = norm_stake * (DISC_FLOOR + (1.0 - scores[target]))
    else:
        fitness = norm_stake * (DISC_FLOOR + spread)

    return {
        "fitness": round(fitness, 4),
        "stake": round(stake, 1),
        "floor": round(floor, 1),
        "oracle": round(oracle, 1),
        "norm_stake": round(norm_stake, 4),
        "spread": round(spread, 4),
        "score_rules": round(scores["rules"], 4),
        "score_llm": round(scores["llm"], 4),
        "false_dispatches": false_dispatches,
    }
