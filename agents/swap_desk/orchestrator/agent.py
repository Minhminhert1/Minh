import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from base import call, MODEL_SONNET

# Agent được phép kích hoạt theo task type
ROUTES = {
    "CURVE_ONLY":    ["curve_analyst"],
    "MACRO_GLOBAL":  ["global_macro_scout"],
    "MICRO_CAL":     ["micro_calendar_scout"],
    "CONTEXT_ONLY":  ["global_macro_scout", "micro_calendar_scout"],
    "MORNING_BRIEF": ["global_macro_scout", "micro_calendar_scout", "curve_analyst"],
    "TRADE_IDEA":    ["curve_analyst", "global_macro_scout", "micro_calendar_scout",
                      "trade_architect", "risk_sentinel"],
    "RISK_CHECK":    ["risk_sentinel"],
    "PATTERN":       ["pattern_keeper"],
    "FULL":          ["global_macro_scout", "micro_calendar_scout", "curve_analyst",
                      "trade_architect", "risk_sentinel", "pattern_keeper"],
}


def route(user_request: str) -> dict:
    """Gọi 1 call nhỏ để classify task, trả về danh sách agents cần chạy."""
    prompt = _load_routing_prompt()
    result = call("orchestrator", MODEL_SONNET, user_request)

    # Parse JSON từ output
    try:
        start = result.find("{")
        end = result.rfind("}") + 1
        parsed = json.loads(result[start:end])
        task_type = parsed.get("task_type", "CURVE_ONLY")
    except Exception:
        task_type = "CURVE_ONLY"

    agents = ROUTES.get(task_type, ["curve_analyst"])
    print(f"\n[ORCHESTRATOR] Task: {task_type} → Agents: {agents}")
    return {"task_type": task_type, "agents": agents}


def _load_routing_prompt():
    pass  # prompt.md đã được load trong base.call()
