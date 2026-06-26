from typing import TypedDict


class ToolCall(TypedDict):
    name: str
    arguments: dict[str, str]


def run(call: ToolCall) -> str:
    return f"calling {call['name']}"


run({"name": "search", "arguments": {"q": "hello"}})  # ✓
