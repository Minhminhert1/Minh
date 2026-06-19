from agents.base import call_agent, MODEL_SONNET

ROLE = "reviewer"


def run(analysis_output: str, strategy_output: str) -> str:
    context = f"""## ANALYSIS:
{analysis_output}

## STRATEGY:
{strategy_output}"""

    message = "Phản biện setup của Strategy. Chạy đầy đủ checklist và đưa ra đánh giá APPROVE / CAUTION / REJECT."
    return call_agent(ROLE, MODEL_SONNET, message, context=context)
