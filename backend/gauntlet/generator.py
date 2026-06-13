"""Intelligent test-case generator: seeded evolutionary search for hard, diverse days.

Random sampling spends most of its budget on unremarkable days. This searches
instead: sample a population, keep the fittest, mutate them toward higher
discrimination (or higher regret against a target agent), repeat, then greedily
pick a diverse battery by farthest-point selection in genome-feature space so
the result is hard AND spread across failure modes, not K copies of one idea.

Fully deterministic given a seed: same seed yields the same battery. The
optional LLM red-team author injects proposed genomes as extra seeds; it never
replaces the search and is off unless seeds are passed in.
"""

import numpy as np

from . import fitness
from .genome import CaseGenome

POP = 96
GENS = 5
K = 30
ELITE_FRAC = 0.5
TOP_POOL_MULT = 6   # diversity-select from the TOP_POOL_MULT*K fittest candidates


def generate_battery(mode: str = "discrimination", k: int = K, pop: int = POP,
                     gens: int = GENS, seed: int = 0, llm_seeds: list | None = None) -> list:
    """Evolve a population, then diversity-select k cases.

    mode: "discrimination" | "adversarial:rules" | "adversarial:llm".
    Returns a list of {name, label, genome, eval}, fittest-first within diversity.
    """
    target = mode.split(":", 1)[1] if mode.startswith("adversarial") else None
    rng = np.random.default_rng(seed)
    cache: dict[tuple, dict] = {}
    seen: dict[tuple, CaseGenome] = {}

    def ev(g: CaseGenome) -> dict:
        key = g.key()
        if key not in cache:
            cache[key] = fitness.evaluate(g, target=target, seed=seed)
            seen[key] = g
        return cache[key]

    population = [CaseGenome.sample(rng) for _ in range(pop)]
    for g in (llm_seeds or []):
        population.append(g)
    for g in population:
        ev(g)

    for _ in range(gens):
        population.sort(key=lambda g: ev(g)["fitness"], reverse=True)
        n_elite = max(2, int(pop * ELITE_FRAC))
        elites = population[:n_elite]
        children = []
        for _ in range(pop - n_elite):
            parent = elites[int(rng.integers(n_elite))]
            child = parent.mutate(rng)
            ev(child)
            children.append(child)
        population = elites + children

    pool = [seen[key] for key in seen if cache[key]["fitness"] > 0.0]
    pool.sort(key=lambda g: ev(g)["fitness"], reverse=True)
    chosen = _diversity_select(pool[: max(k, TOP_POOL_MULT * k)], k, ev)
    return [
        {"name": f"G{seed:02d}-{i:03d}", "label": g.label(), "genome": g, "eval": ev(g)}
        for i, g in enumerate(chosen)
    ]


def _diversity_select(candidates: list, k: int, ev) -> list:
    """Greedy farthest-point sampling in feature space, seeded by the fittest case.

    All candidates are already high-fitness (top pool), so spreading them out in
    feature space buys diversity without sacrificing much difficulty."""
    if not candidates:
        return []
    feats = [g.feature_vector() for g in candidates]
    chosen_idx = [0]   # candidates are fitness-sorted, so index 0 is the fittest
    while len(chosen_idx) < min(k, len(candidates)):
        best_i, best_d = None, -1.0
        for i in range(len(candidates)):
            if i in chosen_idx:
                continue
            d = min(float(np.linalg.norm(feats[i] - feats[j])) for j in chosen_idx)
            if d > best_d:
                best_i, best_d = i, d
        chosen_idx.append(best_i)
    chosen = [candidates[i] for i in chosen_idx]
    chosen.sort(key=lambda g: ev(g)["fitness"], reverse=True)
    return chosen


def random_battery_fitness(k: int, pop: int, gens: int, seed: int) -> float:
    """Baseline: mean fitness of the top k from pure random sampling (no search).

    Used to prove the search earns its keep: same total evaluation budget."""
    rng = np.random.default_rng(seed + 7919)
    budget = pop * (gens + 1)
    genomes = [CaseGenome.sample(rng) for _ in range(budget)]
    fits = sorted((fitness.evaluate(g, seed=seed)["fitness"] for g in genomes), reverse=True)
    return float(np.mean(fits[:k])) if fits else 0.0
