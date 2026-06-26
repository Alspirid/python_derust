# collections
from collections import Counter, defaultdict, deque

d = defaultdict(list)
d[k].append(v)  # no KeyError
Counter(words).most_common(3)  # frequency
dq = deque(maxlen=100)
dq.append(x)  # O(1) both ends, auto-evict

# heapq — min-heap by default; negate or use tuples for priority/max
import heapq

heapq.heappush(h, (score, item))
heapq.heappop(h)
heapq.nlargest(k, items, key=lambda x: x.score)
# top-k over a huge stream: keep a min-heap of size k (bounded memory)

# bisect — sorted structures, versioning lookups
import bisect

bisect.insort(arr, x)
i = bisect.bisect_right(timestamps, t)

# dataclasses + pydantic (schema validation — know both)
from dataclasses import dataclass, field


@dataclass
class Doc:
    id: str
    score: float = 0.0


from pydantic import BaseModel, ValidationError


class ToolArgs(BaseModel):
    query: str
    k: int = 5


try:
    args = ToolArgs.model_validate(raw)  # raises on bad input
except ValidationError as e:
    ...


# generators — streaming, memory efficiency, resumable iteration
def batches(it, n):
    buf = []
    for x in it:
        buf.append(x)
        if len(buf) == n:
            yield buf
            buf = []
    if buf:
        yield buf


# async — parallel tool calls + concurrency limits
import asyncio

results = await asyncio.gather(*[call(t) for t in tools])  # parallel
sem = asyncio.Semaphore(5)  # cap concurrency

# functools — memoization / "prompt caching" analog
from functools import lru_cache, cache, partial

# timing for rate limiters (monotonic, not wall clock)
import time

now = time.monotonic()

# type hints interviewers expect
from typing import Callable, Literal, Optional, TypedDict


def rank(q: list[float], docs: list[Doc], k: int = 5) -> list[Doc]: ...
