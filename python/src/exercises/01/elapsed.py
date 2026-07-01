import time
from types import TracebackType


class Stopwatch:
    elapsed: float
    _start: float

    def __enter__(self) -> "Stopwatch":
        self._start = time.monotonic()
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        self.elapsed = time.monotonic() - self._start
        return None


def do_work() -> int:
    res = 0
    for _ in range(100000):
        res += 10
    return res


with Stopwatch() as sw:
    do_work()
print(sw.elapsed)
