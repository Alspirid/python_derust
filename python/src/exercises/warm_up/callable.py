from collections.abc import Callable

type Func = Callable[[int], int]


def apply_twice(fn: Func, value: int) -> int:
    return fn(fn(value))


print(apply_twice(lambda x: x + 1, 10))  # → 12
print(apply_twice(lambda x: x * 2, 3))  # → 12
