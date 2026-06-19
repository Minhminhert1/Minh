#!/usr/bin/env python3
"""
SWAP DESK — Multi-Agent System
Chỉ kích hoạt agents cần thiết dựa trên loại request.

Usage:
    python swap_desk.py
    → nhập request khi được hỏi, paste bảng rate nếu có

Task types tự động detect:
    CURVE_ONLY    → chỉ phân tích curve (paste bảng rate)
    MACRO_GLOBAL  → macro thế giới (Fed, DXY, yields)
    MICRO_CAL     → thanh khoản nội địa (OMO, cuối quý, T-bill)
    MORNING_BRIEF → briefing sáng (macro + micro + curve)
    TRADE_IDEA    → đề xuất trade (full pipeline)
    RISK_CHECK    → review rủi ro position đang hold
    PATTERN       → hỏi về seasonal / lịch sử
    CONTEXT_ONLY  → macro + micro, không có bảng rate
"""

import sys
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent))

from agents.swap_desk.base import call, MODEL_OPUS, MODEL_SONNET
from agents.swap_desk.orchestrator.agent import route, ROUTES

# Model mapping cho từng agent
AGENT_MODELS = {
    "curve_analyst":       MODEL_OPUS,
    "trade_architect":     MODEL_SONNET,
    "risk_sentinel":       MODEL_SONNET,
    "pattern_keeper":      MODEL_SONNET,
    "global_macro_scout":  MODEL_SONNET,
    "micro_calendar_scout": MODEL_SONNET,
}

# Thứ tự chạy (dependency order)
EXECUTION_ORDER = [
    "global_macro_scout",
    "micro_calendar_scout",
    "curve_analyst",
    "trade_architect",
    "risk_sentinel",
    "pattern_keeper",
]


def run(user_request: str) -> str:
    print(f"\n{'='*60}")
    print(f"SWAP DESK — {datetime.now().strftime('%d/%m/%Y %H:%M')}")
    print(f"{'='*60}")
    print(f"Request: {user_request[:100]}...")

    # Bước 1: Route — chỉ 1 call nhỏ để phân loại
    routing = route(user_request)
    agents_to_run = routing["agents"]

    # Bước 2: Chạy agents theo thứ tự, pass context dần
    outputs = {}
    context_chain = ""

    for agent in EXECUTION_ORDER:
        if agent not in agents_to_run:
            continue

        model = AGENT_MODELS[agent]
        result = call(agent, model, user_request, context=context_chain)
        outputs[agent] = result

        # Thêm output vào context cho agent tiếp theo
        context_chain += f"\n\n## {agent.upper().replace('_', ' ')} OUTPUT:\n{result}"

    # Bước 3: Tổng hợp báo cáo cuối
    print(f"\n{'='*60}")
    print("BÁO CÁO CUỐI")
    print(f"{'='*60}\n")

    final = _synthesize(outputs, routing["task_type"])
    print(final)
    return final


def _synthesize(outputs: dict, task_type: str) -> str:
    """Ghép output các agents thành báo cáo cuối có cấu trúc."""
    if len(outputs) == 1:
        # Chỉ 1 agent → trả về thẳng, không cần synthesize
        return list(outputs.values())[0]

    sections = []
    order_labels = {
        "global_macro_scout":   "🌍 GLOBAL MACRO",
        "micro_calendar_scout": "📅 MICRO CALENDAR",
        "curve_analyst":        "📈 CURVE ANALYSIS",
        "trade_architect":      "💡 TRADE IDEA",
        "risk_sentinel":        "🛡️ RISK REVIEW",
        "pattern_keeper":       "📚 PATTERN LOG",
    }
    for agent in EXECUTION_ORDER:
        if agent in outputs:
            label = order_labels.get(agent, agent.upper())
            sections.append(f"## {label}\n\n{outputs[agent]}")

    return "\n\n---\n\n".join(sections)


if __name__ == "__main__":
    print("\nSWAP DESK — Multi-Agent System")
    print("Nhập request (hoặc paste bảng rate). Gõ 'exit' để thoát.\n")

    while True:
        print("\n" + "-"*40)
        lines = []
        print("Nhập request (Enter 2 lần để gửi):")
        while True:
            line = input()
            if line == "exit":
                sys.exit(0)
            if line == "" and lines and lines[-1] == "":
                break
            lines.append(line)

        user_input = "\n".join(lines).strip()
        if user_input:
            run(user_input)
