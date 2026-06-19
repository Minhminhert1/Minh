import anthropic
import os
from pathlib import Path

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

MODEL_OPUS = "claude-opus-4-8"
MODEL_SONNET = "claude-sonnet-4-6"

AGENTS_DIR = Path(__file__).parent


def load_prompt(role: str) -> str:
    path = AGENTS_DIR / role / "prompt.md"
    return path.read_text(encoding="utf-8")


def load_memory(role: str) -> str:
    path = AGENTS_DIR / role / "memory.md"
    if path.exists():
        return path.read_text(encoding="utf-8")
    return ""


def save_memory(role: str, content: str):
    path = AGENTS_DIR / role / "memory.md"
    path.write_text(content, encoding="utf-8")


def call_agent(role: str, model: str, user_message: str, context: str = "") -> str:
    system_prompt = load_prompt(role)
    memory = load_memory(role)

    if memory.strip():
        system_prompt = f"{system_prompt}\n\n---\n## Memory của agent này\n{memory}"

    messages = []
    if context:
        messages.append({
            "role": "user",
            "content": f"## Context từ các agent trước\n{context}\n\n---\n\n{user_message}"
        })
    else:
        messages.append({"role": "user", "content": user_message})

    print(f"\n[{role.upper()}] ({model.split('-')[1].upper()}) đang xử lý...")

    with client.messages.stream(
        model=model,
        max_tokens=4096,
        system=system_prompt,
        messages=messages,
        thinking={"type": "adaptive"},
    ) as stream:
        response = stream.get_final_message()

    # Extract text content only
    result = ""
    for block in response.content:
        if block.type == "text":
            result += block.text

    return result.strip()
