import time
from contextlib import contextmanager

# class Timer:
#     elapsed: float
#     _start: float

#     def __enter__(self):
#         self._start = time.perf_counter()
#         return self

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.elapsed = time.perf_counter() - self._start


# with Timer() as t:
#     sum(range(10_000_000))
# print(t.elapsed)  # → a small positive float, e.g. 0.18


@contextmanager
def timer(operation: str):
    start = time.perf_counter()
    yield
    end = time.perf_counter()
    print(f"{operation}: {end - start}")


with timer("sum"):
    sum(range(10_000_000))
# → prints something like:  sum: 0.123s
