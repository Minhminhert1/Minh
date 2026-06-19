import anthropic
import json
import os
from pathlib import Path

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

MODEL_OPUS = "claude-opus-4-8"
MODEL_SONNET = "claude-sonnet-4-6"

SWAP_DIR = Path(__file__).parent
SHARED_DIR = SWAP_DIR.parent / "shared"


def _load_prompt(agent_dir: Path) -> str:
    return (agent_dir / "prompt.md").read_text(encoding="utf-8")


def _load_memory(agent_dir: Path) -> str:
    p = agent_dir / "memory.md"
    return p.read_text(encoding="utf-8") if p.exists() else ""


def call(agent_name: str, model: str, user_message: str, context: str = "") -> str:
    # Resolve agent directory
    if agent_name in ("global_macro_scout", "micro_calendar_scout"):
        agent_dir = SHARED_DIR / agent_name
    else:
        agent_dir = SWAP_DIR / agent_name

    system = _load_prompt(agent_dir)
    memory = _load_memory(agent_dir)
    if memory.strip():
        system += f"\n\n---\n## Memory\n{memory}"

    content = f"{context}\n\n---\n\n{user_message}" if context else user_message

    label = agent_name.upper().replace("_", " ")
    print(f"\n[{label}] đang xử lý...")

    kwargs = dict(
        model=model,
        max_tokens=3000,
        system=system,
        messages=[{"role": "user", "content": content}],
    )
    # Adaptive thinking chỉ cho Opus
    if model == MODEL_OPUS:
        kwargs["thinking"] = {"type": "adaptive"}
        kwargs["max_tokens"] = 5000

    with client.messages.stream(**kwargs) as s:
        msg = s.get_final_message()

    return "".join(b.text for b in msg.content if b.type == "text").strip()
