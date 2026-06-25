from collections.abc import Iterable, Iterator


def batched[T](items: Iterable[T], size: int) -> Iterator[list[T]]:
    buffer: list[T] = []
    for item in items:
        buffer.append(item)
        if len(buffer) == size:
            yield buffer
            buffer = []
    if buffer:
        yield buffer


print(list(batched([], 3)))  # → []
print(list(batched(range(6), 2)))  # → [[0, 1], [2, 3], [4, 5]]
print(list(batched(range(7), 3)))  # → [[0, 1, 2], [3, 4, 5], [6]]
