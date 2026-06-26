from typing import Literal

type Level = Literal["debug", "info", "error"]


def log(level: Level, message: str) -> str:
    return f"[{level}] {message}"


log("info", "starting")
