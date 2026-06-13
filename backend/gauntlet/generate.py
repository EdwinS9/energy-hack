"""CLI: generate an intelligent test-case battery and report tail risk per agent.

    python -m gauntlet.generate                         # discrimination battery
    python -m gauntlet.generate --mode adversarial --target rules
    python -m gauntlet.generate --k 40 --seed 1 --redteam   # LLM-seeded (needs a key)
"""

import argparse
from pathlib import Path

from . import battery as battery_mod
from .battery import REPO_ROOT
from .generator import GENS, K, POP, generate_battery

DEFAULT_OUT = REPO_ROOT / "traces" / "battery"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["discrimination", "adversarial"], default="discrimination")
    ap.add_argument("--target", choices=["rules", "llm"], default="rules",
                    help="agent to break in adversarial mode")
    ap.add_argument("--k", type=int, default=K)
    ap.add_argument("--pop", type=int, default=POP)
    ap.add_argument("--gens", type=int, default=GENS)
    ap.add_argument("--mc", type=int, default=battery_mod.MC_N)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--redteam", action="store_true", help="seed search with LLM-proposed cases")
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = ap.parse_args()

    mode = f"adversarial:{args.target}" if args.mode == "adversarial" else "discrimination"

    llm_seeds = None
    if args.redteam:
        from .redteam import propose_genomes
        llm_seeds = propose_genomes(n=12, seed=args.seed)
        print(f"red-team author proposed {len(llm_seeds)} valid genomes as search seeds")

    print(f"generating {args.k} cases | mode={mode} pop={args.pop} gens={args.gens} seed={args.seed} ...")
    cases = generate_battery(mode=mode, k=args.k, pop=args.pop, gens=args.gens,
                             seed=args.seed, llm_seeds=llm_seeds)
    payload = battery_mod.run_battery(cases, mc_n=args.mc)
    payload["mode"] = mode
    payload["seed"] = args.seed
    f = battery_mod.save(payload, mode, args.out)

    print(f"\nbattery -> {f}")
    print(f"\n{'agent':8s} {'pass-rate':>10s} {'worst-P10':>10s} {'mean':>7s}   hardest case")
    for a, r in payload["report"].items():
        print(f"{a:8s} {r['pass_rate']*100:9.0f}% {r['p10']*100:9.0f}% {r['mean']*100:6.0f}%   "
              f"{r['hardest']['label'][:54]} ({r['hardest']['mean']*100:.0f}%)")


if __name__ == "__main__":
    main()
