from pydantic import BaseModel, ValidationError


class ToolArgs(BaseModel):
    query: str
    k: int = 5


def parse_args(params: dict) -> ToolArgs | None:
    try:
        return ToolArgs.model_validate(params)
    except ValidationError as e:
        print(e.errors())


parse_args({"query": "hello", "k": 3})  # → ToolArgs(query="hello", k=3)
parse_args({"query": "hello"})  # → ToolArgs(query="hello", k=5)   (default)
parse_args({"query": "hello", "k": "abc"})  # → raises ValidationError
