from agents.base import call_agent, MODEL_SONNET

ROLE = "orchestrator"


def run(user_query: str, context: str = "") -> str:
    message = f"""Người dùng hỏi: {user_query}

Nhiệm vụ của bạn lúc này:
1. Phân tích intent của câu hỏi
2. Xác định data nào cần thu thập
3. Viết task brief rõ ràng cho RESEARCH agent

Trả về task brief ngắn gọn cho RESEARCH."""

    return call_agent(ROLE, MODEL_SONNET, message, context)


def synthesize(user_query: str, research: str, analysis: str, strategy: str, review: str) -> str:
    context = f"""
## RESEARCH output:
{research}

## ANALYSIS output:
{analysis}

## STRATEGY output:
{strategy}

## REVIEWER output:
{review}
"""
    message = f"""Câu hỏi gốc của user: {user_query}

Tổng hợp output từ tất cả agent thành báo cáo cuối theo format chuẩn trong prompt của bạn."""

    return call_agent(ROLE, MODEL_SONNET, message, context)
