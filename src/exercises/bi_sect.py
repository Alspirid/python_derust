import bisect

scores = [0.1, 0.3, 0.3, 0.5, 0.7, 0.9]


def count_below[T: (int, float)](items: list[T], t: T) -> int:
    return bisect.bisect_left(items, t)


print(count_below(scores, 0.5))  # → 3   (0.1, 0.3, 0.3)
print(count_below(scores, 0.3))  # → 1   (just 0.1 — the 0.3s are not "below")
