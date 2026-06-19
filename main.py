#!/usr/bin/env python3
"""
FX Research Multi-Agent System
Model tiering: ANALYSIS → Opus 4.8 | Others → Sonnet 4.6
"""

import sys
from pathlib import Path

# Cho phép import từ root
sys.path.insert(0, str(Path(__file__).parent))

from agents.orchestrator import agent as orchestrator
from agents.research import agent as research
from agents.analysis import agent as analysis
from agents.strategy import agent as strategy
from agents.reviewer import agent as reviewer
from agents.journalist import agent as journalist


def run_pipeline(user_query: str) -> str:
    print(f"\n{'='*60}")
    print(f"QUERY: {user_query}")
    print(f"{'='*60}")

    # 1. Orchestrator phân tích intent
    task_brief = orchestrator.run(user_query)
    print(f"\n[ORCHESTRATOR] Task brief:\n{task_brief[:300]}...")

    # 2. Research thu thập data
    research_output = research.run(task_brief)

    # 3. Analysis phân tích (Opus 4.8)
    analysis_output = analysis.run(research_output)

    # 4. Strategy đề xuất setup
    strategy_output = strategy.run(analysis_output)

    # 5. Reviewer phản biện
    review_output = reviewer.run(analysis_output, strategy_output)

    # 6. Orchestrator tổng hợp báo cáo cuối
    final_report = orchestrator.synthesize(
        user_query, research_output, analysis_output, strategy_output, review_output
    )

    # 7. Journalist ghi chép (chạy cuối, không block kết quả)
    journalist.run(
        user_query, research_output, analysis_output,
        strategy_output, review_output, final_report
    )

    print(f"\n{'='*60}")
    print("BÁO CÁO CUỐI")
    print(f"{'='*60}\n")
    print(final_report)

    return final_report


if __name__ == "__main__":
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
    else:
        query = input("Nhập câu hỏi: ").strip()

    if not query:
        print("Vui lòng nhập câu hỏi.")
        sys.exit(1)

    run_pipeline(query)
