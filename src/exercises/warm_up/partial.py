from functools import partial


def log(level: str, message: str) -> str:
    return f"[{level}] {message}"


# build `error` with partial so that:
error = partial(log, "ERROR")

print(error("disk full"))  # → "[ERROR] disk full"
