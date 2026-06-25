from collections import Counter

calls = ["search", "search", "fetch", "search", "fetch", "calc"]


def top_tools(calls: list[str], k: int) -> list[tuple[str, int]]:
    return Counter(calls).most_common(k)


top_tools(calls, 2)  # → [("search", 3), ("fetch", 2)]
