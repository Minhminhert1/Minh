from agents.base import call_agent, save_memory, load_memory, MODEL_SONNET
from pathlib import Path
from datetime import datetime

ROLE = "journalist"
JOURNAL_DIR = Path(__file__).parent / "journal"


def run(user_query: str, research: str, analysis: str, strategy: str, review: str, final_report: str) -> str:
    context = f"""## User query: {user_query}

## RESEARCH:
{research}

## ANALYSIS:
{analysis}

## STRATEGY:
{strategy}

## REVIEWER:
{review}

## FINAL REPORT:
{final_report}"""

    message = "Ghi chép toàn bộ session này theo format journal của bạn."
    journal_entry = call_agent(ROLE, MODEL_SONNET, message, context=context)

    # Lưu journal ra file
    JOURNAL_DIR.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    journal_path = JOURNAL_DIR / f"{timestamp}.md"
    journal_path.write_text(journal_entry, encoding="utf-8")
    print(f"[JOURNALIST] Journal saved → {journal_path.name}")

    return journal_entry
