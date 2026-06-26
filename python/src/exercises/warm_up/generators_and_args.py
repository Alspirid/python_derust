from collections.abc import Iterator


def running_total(nums: list[int]) -> Iterator[int]:
    current = 0
    for val in nums:
        current += val
        yield current


def average(*nums) -> float:
    if not nums:
        return 0.0
    return sum(nums) / len(nums)


def make_user(**params) -> dict[str, str | int]:
    return {"role": "user", **params}


def add_tag(tag: str, tags: list[str] | None = None) -> list[str]:
    if tags is None:
        tags = []
    tags.append(tag)
    return tags


def common(a: list[int], b: list[int]) -> set[int]:
    return set(a) & set(b)
