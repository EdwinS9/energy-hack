"""Optional LLM red-team author: an LLM proposes novel hard days as search seeds.

This is the 'opt-in' half of the generator. The deterministic search runs fine
without it; when enabled, an LLM (DeepSeek by default, via the same provider
wiring as the worker) proposes scenario genomes that get clamped to the realism
guardrails and dropped into the population as starting points the evolutionary
search then refines. The LLM never has the last word on what ships: anything it
proposes still has to survive the fitness function like every other candidate.

Kept out of any live request path; this runs offline at battery-build time.
"""

import json
import os

from .config import PARK_IDS
from .genome import (BUST_DEPTH_HI, BUST_DEPTH_LO, BUST_DUR_LO, CaseGenome,
                     DAY_HI, DAY_LO, FAULT_MAG_HI, FAULT_MAG_LO, FAULT_ONSET_HI,
                     FAULT_ONSET_LO, MAX_BUSTS, SPIKE_HI, SPIKE_LO, Bust, Fault)

PROMPT = """You design hard, realistic stress-test days for an AI agent that manages a
portfolio of three solar parks (zaragoza 50MW, valencia 40MW, munich 30MW) in a day-ahead
electricity market. A good test day has real money at stake and SEPARATES good agents from bad
ones: it should reward an agent that correctly tells a weather forecast bust (trade, no crew)
from a silent hardware fault (dispatch a crew) and punish one that confuses them.

Steps are 15-minute indices 0..95 (step 48 = noon). Propose DIVERSE days, not variations of one.
Return JSON: {"cases": [{"busts": [{"park": str, "start_step": int, "end_step": int,
"depth": float, "sign": 1 or -1}], "fault": {"park": str, "onset_step": int, "magnitude": float}
or null, "eclipse": bool, "price_spike": float, "rationale": str}]}
Where: depth is the fraction of output lost at the cloud trough (0.2-0.7); sign +1 is a shortfall
(realized worse than forecast), -1 is surprise extra sun; fault magnitude is 0.15-0.55 of capacity;
price_spike multiplies the evening peak (1.0-1.8). Use at most two busts per day."""


def _client_and_model():
    provider = os.environ.get("GAUNTLET_PROVIDER", "")
    if not provider and os.environ.get("GAUNTLET_USE_ANTHROPIC"):
        provider = "anthropic"
    if provider == "anthropic" and os.environ.get("ANTHROPIC_API_KEY"):
        from anthropic import Anthropic
        return "anthropic", Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"]), \
            os.environ.get("GAUNTLET_MODEL", "claude-sonnet-4-6")
    if provider == "deepseek" and os.environ.get("DEEPSEEK_API_KEY"):
        from openai import OpenAI
        return "deepseek", OpenAI(api_key=os.environ["DEEPSEEK_API_KEY"],
                                  base_url="https://api.deepseek.com"), \
            os.environ.get("GAUNTLET_MODEL", "deepseek-chat")
    raise RuntimeError("red-team author needs GAUNTLET_PROVIDER plus the matching API key in the env")


def propose_genomes(n: int = 12, seed: int = 0) -> list:
    """Ask the LLM for n hard days; return the validated, guardrail-clamped genomes."""
    provider, client, model = _client_and_model()
    user = f"Propose {n} diverse hard test days. Vary the failure mode across them."
    if provider == "anthropic":
        msg = client.messages.create(model=model, max_tokens=2000, temperature=0.7,
                                      system=PROMPT, messages=[{"role": "user", "content": user}])
        text = msg.content[0].text
    else:
        resp = client.chat.completions.create(
            model=model, max_tokens=2000, temperature=0.7,
            response_format={"type": "json_object"},
            messages=[{"role": "system", "content": PROMPT}, {"role": "user", "content": user}])
        text = resp.choices[0].message.content
    return _parse(text)


def _parse(text: str) -> list:
    data = json.loads(text[text.index("{"): text.rindex("}") + 1])
    out = []
    for raw in data.get("cases", []):
        g = _validate(raw)
        if g is not None:
            out.append(g)
    return out


def _clip(v, lo, hi):
    return max(lo, min(hi, v))


def _validate(raw: dict) -> CaseGenome | None:
    """Clamp a proposed case into the realism guardrails; drop it if unusable."""
    try:
        busts = []
        for b in (raw.get("busts") or [])[:MAX_BUSTS]:
            if b.get("park") not in PARK_IDS:
                continue
            start = int(_clip(int(b["start_step"]), DAY_LO, DAY_HI - BUST_DUR_LO))
            end = int(_clip(int(b["end_step"]), start + BUST_DUR_LO, DAY_HI))
            depth = float(_clip(float(b["depth"]), BUST_DEPTH_LO, BUST_DEPTH_HI))
            sign = 1 if int(b.get("sign", 1)) >= 0 else -1
            busts.append(Bust(b["park"], start, end, depth, sign))
        fault = None
        fr = raw.get("fault")
        if isinstance(fr, dict) and fr.get("park") in PARK_IDS:
            fault = Fault(fr["park"],
                          int(_clip(int(fr["onset_step"]), FAULT_ONSET_LO, FAULT_ONSET_HI)),
                          float(_clip(float(fr["magnitude"]), FAULT_MAG_LO, FAULT_MAG_HI)))
        spike = float(_clip(float(raw.get("price_spike", 1.0)), SPIKE_LO, SPIKE_HI))
        if not busts and fault is None and not raw.get("eclipse"):
            return None   # an empty day tests nothing
        return CaseGenome(busts=busts, fault=fault, eclipse=bool(raw.get("eclipse", False)),
                          price_spike=spike)
    except (KeyError, ValueError, TypeError):
        return None
