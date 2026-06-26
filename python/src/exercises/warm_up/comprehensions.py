def sum_evens(numbers: list[int]) -> int:
    return sum(x for x in numbers if not x % 2)


def square_odds(numbers: list[int]) -> list[int]:
    return [x**2 for x in numbers if x % 2]


def word_lengths(words: list[str]) -> dict[str, int]:
    return {w: len(w) for w in words}
