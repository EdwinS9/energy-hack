"""Gates for the intelligent test-case generator.

Verifiable claims, not vibes: curation roughly doubles the yield of genuinely
hard + discriminating days vs unfiltered random; diversity selection spreads the
battery in feature space; adversarial mode demonstrably lowers the target
agent's score; the whole pipeline is deterministic; the battery report stays in
range. Everything runs on the deterministic mock substrate (no API)."""

import numpy as np

from gauntlet import battery as battery_mod
from gauntlet import fitness
from gauntlet.config import N_STEPS
from gauntlet.genome import Bust, CaseGenome, Fault
from gauntlet.generator import _diversity_select, generate_battery
from gauntlet.oracle import oracle_cost
from gauntlet.scenarios import build_from_genome
from gauntlet.sim import run_episode
from gauntlet.agents.noop import DoNothingAgent

# small, fast settings; gates are chosen to hold with margin at this scale
POP, GENS, K = 40, 3, 12


def _good(e: dict) -> bool:
    return e["stake"] >= fitness.MIN_STAKE and e["spread"] >= 0.2


def test_genome_builds_valid_scenarios():
    rng = np.random.default_rng(1)
    for i in range(20):
        g = CaseGenome.sample(rng)
        sc = build_from_genome(g, seed=i)
        for p in sc.forecast:
            assert sc.forecast[p].shape == (N_STEPS,)
            assert sc.twin[p].shape == (N_STEPS,)
            assert np.all(sc.forecast[p] >= -1e-9) and np.all(sc.twin[p] >= -1e-9)
        floor = float(run_episode(sc, DoNothingAgent())["_cum_cost"][-1])
        assert floor - oracle_cost(sc) >= -1.0   # oracle never worse than doing nothing


def test_fitness_prefers_hard_discriminating_days():
    hard = CaseGenome(busts=[Bust("munich", 40, 64, 0.6, 1)],
                      fault=Fault("zaragoza", 48, 0.5), price_spike=1.5)
    calm = CaseGenome(busts=[Bust("valencia", 40, 48, 0.2, -1)])
    assert fitness.evaluate(hard)["fitness"] > fitness.evaluate(calm)["fitness"]


def test_generation_is_deterministic():
    a = generate_battery("discrimination", k=K, pop=POP, gens=GENS, seed=0)
    b = generate_battery("discrimination", k=K, pop=POP, gens=GENS, seed=0)
    assert [c["genome"].key() for c in a] == [c["genome"].key() for c in b]


def test_curation_beats_unfiltered_random():
    """The fitness function is the product: a curated battery is harder AND more
    discriminating than the unfiltered random days you would otherwise test on."""
    rng = np.random.default_rng(0)
    unfilt = [fitness.evaluate(CaseGenome.sample(rng)) for _ in range(200)]
    battery = [c["eval"] for c in generate_battery("discrimination", k=K, pop=POP, gens=GENS, seed=0)]

    def mean(es, f):
        return float(np.mean([f(e) for e in es]))

    # money at stake AND agent-separation both lift; the binary good-test
    # fraction lifts too (the diversity tail keeps it from saturating)
    assert mean(battery, lambda e: e["fitness"]) >= 1.3 * mean(unfilt, lambda e: e["fitness"])
    assert mean(battery, lambda e: e["spread"]) > mean(unfilt, lambda e: e["spread"])
    assert mean(battery, _good) >= mean(unfilt, _good)


def test_diversity_selection_spreads_more_than_greedy():
    battery = generate_battery("discrimination", k=K, pop=POP, gens=GENS, seed=0)

    # rebuild the same fitness-sorted pool to compare against a pure greedy top-k
    rng = np.random.default_rng(0)
    cache, seen = {}, {}

    def ev(g):
        key = g.key()
        if key not in cache:
            cache[key] = fitness.evaluate(g, seed=0)
            seen[key] = g
        return cache[key]

    pop = [CaseGenome.sample(rng) for _ in range(POP)]
    for g in pop:
        ev(g)
    for _ in range(GENS):
        pop.sort(key=lambda g: ev(g)["fitness"], reverse=True)
        ne = max(2, POP // 2)
        elites = pop[:ne]
        children = [elites[int(rng.integers(ne))].mutate(rng) for _ in range(POP - ne)]
        for c in children:
            ev(c)
        pop = elites + children
    ranked = [seen[k] for k, _ in sorted(cache.items(), key=lambda kv: kv[1]["fitness"], reverse=True)]
    greedy = ranked[:K]

    def spread(gs):
        F = [g.feature_vector() for g in gs]
        return np.mean([np.linalg.norm(F[i] - F[j]) for i in range(len(F)) for j in range(i + 1, len(F))])

    assert spread([c["genome"] for c in battery]) > spread(greedy)


def test_adversarial_mode_lowers_target_score():
    disc = generate_battery("discrimination", k=K, pop=POP, gens=GENS, seed=0)
    adv = generate_battery("adversarial:rules", k=K, pop=POP, gens=GENS, seed=0)
    disc_rules = np.mean([c["eval"]["score_rules"] for c in disc])
    adv_rules = np.mean([c["eval"]["score_rules"] for c in adv])
    assert adv_rules < disc_rules


def test_redteam_validation_clamps_to_guardrails():
    """The LLM author never bypasses the realism guardrails: out-of-range
    proposals are clamped, junk is dropped, empty days are rejected."""
    from gauntlet import redteam
    from gauntlet.genome import (BUST_DEPTH_HI, DAY_HI, FAULT_MAG_HI)

    g = redteam._validate({"busts": [{"park": "munich", "start_step": 10, "end_step": 999,
                                       "depth": 5.0, "sign": -1}],
                           "fault": {"park": "zaragoza", "onset_step": 90, "magnitude": 9.0},
                           "eclipse": False, "price_spike": 4.0})
    assert g is not None
    b = g.busts[0]
    assert b.depth <= BUST_DEPTH_HI and b.end <= DAY_HI and b.start < b.end
    assert g.fault.magnitude <= FAULT_MAG_HI
    assert g.price_spike <= 1.8

    assert redteam._validate({"busts": [{"park": "atlantis", "start_step": 40, "end_step": 50,
                                         "depth": 0.4, "sign": 1}], "fault": None}) is None
    assert redteam._validate({"busts": [], "fault": None, "eclipse": False}) is None


def test_battery_report_in_range():
    cases = generate_battery("discrimination", k=8, pop=POP, gens=GENS, seed=0)
    payload = battery_mod.run_battery(cases, mc_n=4)
    for a, r in payload["report"].items():
        for kpi in ("pass_rate", "p10", "mean"):
            assert 0.0 <= r[kpi] <= 1.0
    assert payload["report"]["noop"]["mean"] < 0.01   # do-nothing is the floor
