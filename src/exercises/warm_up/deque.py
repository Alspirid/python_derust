from collections import deque
from collections.abc import Iterable


def recent[T](stream: Iterable[T], n: int) -> list[T]:
    return list(deque(stream, maxlen=n))


print(recent(range(1000), 3))  # → [997, 998, 999]
print(recent(["a", "b", "c", "d"], 2))  # → ["c", "d"]
    