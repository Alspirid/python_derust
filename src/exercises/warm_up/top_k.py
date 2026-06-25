import heapq
from collections.abc import Iterable


def top_k[T: (int, float, str)](iterable: Iterable[T], k: int) -> list[T]:
    h = []
    for value in iterable:
        heapq.heappush(
            h,
            value,
        )
        if len(h) > k:
            heapq.heappop(h)
    return h


top_k(range(1000), 3)  # → [997, 998, 999]   (any order ok)
top_k([5, 1, 9, 3, 7, 2], 2)  # → [7, 9]            (any order ok)
