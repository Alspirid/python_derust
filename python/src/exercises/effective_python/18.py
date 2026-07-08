# zip

names = ["Cecilia", "Lise", "Marie"]


def get_longest_name(names: list[str]) -> tuple[str, int]:
    counts = [len(n) for n in names]
    max_count: int = 0
    longest_name: str = ""
    for name, count in zip(names, counts, strict=True):
        if count > max_count:
            longest_name = name
            max_count = count
    return (longest_name, max_count)


print(get_longest_name(names))
