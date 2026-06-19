from agents.base import call_agent, MODEL_SONNET

ROLE = "research"


def run(task_brief: str) -> str:
    message = f"""Task từ Orchestrator:
{task_brief}

Thu thập và tổng hợp data theo checklist trong prompt của bạn. Ghi rõ nguồn và thời gian."""

    return call_agent(ROLE, MODEL_SONNET, message)
