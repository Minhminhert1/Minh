from agents.base import call_agent, MODEL_OPUS  # Opus 4.8 — tầng trí tuệ cốt lõi

ROLE = "analysis"


def run(research_output: str) -> str:
    message = "Phân tích data từ Research và đưa ra nhận định theo framework của bạn."
    return call_agent(ROLE, MODEL_OPUS, message, context=research_output)
