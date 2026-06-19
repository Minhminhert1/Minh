from agents.base import call_agent, MODEL_SONNET

ROLE = "strategy"


def run(analysis_output: str) -> str:
    message = "Dựa vào nhận định của Analysis, đề xuất setup giao dịch cụ thể theo format chuẩn."
    return call_agent(ROLE, MODEL_SONNET, message, context=analysis_output)
