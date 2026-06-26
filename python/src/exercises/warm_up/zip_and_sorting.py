def combine(words: list[str], nums: list[int]) -> dict[str, int]:
    zipped = zip(words, nums, strict=True)
    return {k: v for k, v in zipped}


def top_scorers(score_tuple: list[tuple[str, int]]) -> list[tuple[str, int]]:
    return sorted(score_tuple, key=lambda x: x[1], reverse=True)
